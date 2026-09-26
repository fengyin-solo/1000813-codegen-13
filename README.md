# 污水处理工艺调度管理平台

覆盖进水、生化池、二沉池、深度处理、污泥脱水及排放监测的全流程污水处理工艺调度后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 进水监控 | `inflow` | 进水记录 | 记录编号、进水流量、COD浓度 |
| 生化池曝气 | `aeration` | 曝气单元 | 单元编号、池体编号、溶解氧浓度 |
| 二沉池管理 | `sediment` | 沉淀单元 | 单元编号、进水SS、出水SS |
| 深度处理 | `advanced_treat` | 深度处理单元 | 单元编号、处理工艺、进水浊度 |
| 消毒工艺 | `disinfection` | 消毒单元 | 单元编号、消毒方式、投加浓度 |
| 出水排放 | `effluent` | 排放记录 | 记录编号、出水流量、COD浓度 |
| 污泥脱水 | `sludge` | 脱水机组 | 机组编号、进泥浓度、出泥含水率 |
| 药剂管理 | `chemical` | 药剂 | 药剂编号、药剂名称、药剂类型 |
| 除臭系统 | `odor` | 除臭单元 | 单元编号、除臭方式、收集风量 |
| 在线监测 | `online_monitor` | 监测仪表 | 仪表编号、监测指标、量程范围 |
| 能耗管理 | `energy` | 能耗记录 | 记录编号、电耗、药剂消耗 |
| 设备台账 | `equipment` | 工艺设备 | 设备编号、设备名称、设备类型 |
| 班组交班 | `shift` | 交班记录 | 交班编号、交班时间、交班人员 |
| 异常处置 | `abnormal` | 异常记录 | 异常编号、异常类型、发生时间 |
| 水质化验 | `water_quality` | 化验样本 | 样本编号、采样点位、采样时间 |
| 维保计划 | `maintain_plan` | 维保计划 | 计划编号、维保对象、维保内容 |
| 试剂耗材 | `reagent_stock` | 试剂耗材 | 耗材编号、耗材名称、耗材类别 |
| 工艺日志 | `process_log` | 工艺日志 | 日志编号、记录时段、记录人员 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
