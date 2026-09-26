"""深度处理接口：维护深度处理单元，覆盖开始反冲洗、调整投药量、停运维护等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.advanced_treat import AdvancedTreatService

router = APIRouter(prefix="/api/advanced_treat", tags=["深度处理"])

service = AdvancedTreatService()

LIST_FIELDS = ["单元编号", "处理工艺", "进水浊度", "出水浊度", "药剂投加量", "滤池水头损失", "反冲洗周期", "运行状态"]
STATUSES = ["运行", "反冲洗", "堵塞", "停运"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按单元编号检索"),
    status: str | None = Query(default=None, description="运行、反冲洗、堵塞、停运"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按单元编号与状态过滤深度处理列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条深度处理单元明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"深度处理单元 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条深度处理单元，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="深度处理单元已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条深度处理单元执行开始反冲洗、调整投药量、停运维护；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出深度处理清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "advanced_treat", "total": total, "items": items}
