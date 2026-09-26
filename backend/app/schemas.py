"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class InflowEntry(BaseModel):
    """进水记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 进水流量
    field_2: str | None = None  # COD浓度
    field_3: str | None = None  # 氨氮浓度
    field_4: str | None = None  # 总磷浓度
    field_5: str | None = None  # pH值
    field_6: str | None = None  # 采样时间
    field_7: str | None = None  # 进水状态

class AerationEntry(BaseModel):
    """曝气单元明细结构。"""

    field_0: str | None = None  # 单元编号
    field_1: str | None = None  # 池体编号
    field_2: str | None = None  # 溶解氧浓度
    field_3: str | None = None  # 曝气量
    field_4: str | None = None  # MLSS浓度
    field_5: str | None = None  # SV30值
    field_6: str | None = None  # 风机频率
    field_7: str | None = None  # 运行状态

class SedimentEntry(BaseModel):
    """沉淀单元明细结构。"""

    field_0: str | None = None  # 单元编号
    field_1: str | None = None  # 进水SS
    field_2: str | None = None  # 出水SS
    field_3: str | None = None  # 污泥回流比
    field_4: str | None = None  # 排泥频率
    field_5: str | None = None  # 刮泥机状态
    field_6: str | None = None  # 堰板液位
    field_7: str | None = None  # 运行状态

class AdvancedTreatEntry(BaseModel):
    """深度处理单元明细结构。"""

    field_0: str | None = None  # 单元编号
    field_1: str | None = None  # 处理工艺
    field_2: str | None = None  # 进水浊度
    field_3: str | None = None  # 出水浊度
    field_4: str | None = None  # 药剂投加量
    field_5: str | None = None  # 滤池水头损失
    field_6: str | None = None  # 反冲洗周期
    field_7: str | None = None  # 运行状态

class DisinfectionEntry(BaseModel):
    """消毒单元明细结构。"""

    field_0: str | None = None  # 单元编号
    field_1: str | None = None  # 消毒方式
    field_2: str | None = None  # 投加浓度
    field_3: str | None = None  # 接触时间
    field_4: str | None = None  # 余氯浓度
    field_5: str | None = None  # 紫外强度
    field_6: str | None = None  # 灯管使用时长
    field_7: str | None = None  # 运行状态

class EffluentEntry(BaseModel):
    """排放记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 出水流量
    field_2: str | None = None  # COD浓度
    field_3: str | None = None  # 氨氮浓度
    field_4: str | None = None  # 总磷浓度
    field_5: str | None = None  # 总氮浓度
    field_6: str | None = None  # 采样时间
    field_7: str | None = None  # 排放状态

class SludgeEntry(BaseModel):
    """脱水机组明细结构。"""

    field_0: str | None = None  # 机组编号
    field_1: str | None = None  # 进泥浓度
    field_2: str | None = None  # 出泥含水率
    field_3: str | None = None  # 絮凝剂投加量
    field_4: str | None = None  # 处理量
    field_5: str | None = None  # 滤布状态
    field_6: str | None = None  # 运行电流
    field_7: str | None = None  # 运行状态

class ChemicalEntry(BaseModel):
    """药剂明细结构。"""

    field_0: str | None = None  # 药剂编号
    field_1: str | None = None  # 药剂名称
    field_2: str | None = None  # 药剂类型
    field_3: str | None = None  # 有效成分
    field_4: str | None = None  # 包装规格
    field_5: str | None = None  # 供应商
    field_6: str | None = None  # 有效期至
    field_7: str | None = None  # 药剂状态

class OdorEntry(BaseModel):
    """除臭单元明细结构。"""

    field_0: str | None = None  # 单元编号
    field_1: str | None = None  # 除臭方式
    field_2: str | None = None  # 收集风量
    field_3: str | None = None  # 排放浓度
    field_4: str | None = None  # 填料状态
    field_5: str | None = None  # 喷淋流量
    field_6: str | None = None  # 压差
    field_7: str | None = None  # 运行状态

class OnlineMonitorEntry(BaseModel):
    """监测仪表明细结构。"""

    field_0: str | None = None  # 仪表编号
    field_1: str | None = None  # 监测指标
    field_2: str | None = None  # 量程范围
    field_3: str | None = None  # 校准周期
    field_4: str | None = None  # 最近校准
    field_5: str | None = None  # 数据偏差
    field_6: str | None = None  # 仪表位置
    field_7: str | None = None  # 仪表状态

class EnergyEntry(BaseModel):
    """能耗记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 电耗
    field_2: str | None = None  # 药剂消耗
    field_3: str | None = None  # 用水量
    field_4: str | None = None  # 设备编号
    field_5: str | None = None  # 统计时段
    field_6: str | None = None  # 能耗基准
    field_7: str | None = None  # 记录状态

class EquipmentEntry(BaseModel):
    """工艺设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备名称
    field_2: str | None = None  # 设备类型
    field_3: str | None = None  # 规格型号
    field_4: str | None = None  # 安装日期
    field_5: str | None = None  # 设计寿命
    field_6: str | None = None  # 所属工艺段
    field_7: str | None = None  # 设备状态

class ShiftEntry(BaseModel):
    """交班记录明细结构。"""

    field_0: str | None = None  # 交班编号
    field_1: str | None = None  # 交班时间
    field_2: str | None = None  # 交班人员
    field_3: str | None = None  # 接班人员
    field_4: str | None = None  # 运行概况
    field_5: str | None = None  # 遗留问题
    field_6: str | None = None  # 临时措施
    field_7: str | None = None  # 记录状态

class AbnormalEntry(BaseModel):
    """异常记录明细结构。"""

    field_0: str | None = None  # 异常编号
    field_1: str | None = None  # 异常类型
    field_2: str | None = None  # 发生时间
    field_3: str | None = None  # 影响工艺段
    field_4: str | None = None  # 处置措施
    field_5: str | None = None  # 处置人
    field_6: str | None = None  # 恢复时间
    field_7: str | None = None  # 异常状态

class WaterQualityEntry(BaseModel):
    """化验样本明细结构。"""

    field_0: str | None = None  # 样本编号
    field_1: str | None = None  # 采样点位
    field_2: str | None = None  # 采样时间
    field_3: str | None = None  # 化验项目
    field_4: str | None = None  # 化验结果
    field_5: str | None = None  # 标准限值
    field_6: str | None = None  # 化验人员
    field_7: str | None = None  # 样本状态

class MaintainPlanEntry(BaseModel):
    """维保计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 维保对象
    field_2: str | None = None  # 维保内容
    field_3: str | None = None  # 计划日期
    field_4: str | None = None  # 维保周期
    field_5: str | None = None  # 维保班组
    field_6: str | None = None  # 上次维保日
    field_7: str | None = None  # 计划状态

class ReagentStockEntry(BaseModel):
    """试剂耗材明细结构。"""

    field_0: str | None = None  # 耗材编号
    field_1: str | None = None  # 耗材名称
    field_2: str | None = None  # 耗材类别
    field_3: str | None = None  # 规格
    field_4: str | None = None  # 供应商
    field_5: str | None = None  # 存放条件
    field_6: str | None = None  # 有效期至
    field_7: str | None = None  # 耗材状态

class ProcessLogEntry(BaseModel):
    """工艺日志明细结构。"""

    field_0: str | None = None  # 日志编号
    field_1: str | None = None  # 记录时段
    field_2: str | None = None  # 记录人员
    field_3: str | None = None  # 关键参数
    field_4: str | None = None  # 调整内容
    field_5: str | None = None  # 调整原因
    field_6: str | None = None  # 效果评估
    field_7: str | None = None  # 日志状态
