"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import inflow as router_inflow
from app.routers import aeration as router_aeration
from app.routers import sediment as router_sediment
from app.routers import advanced_treat as router_advanced_treat
from app.routers import disinfection as router_disinfection
from app.routers import effluent as router_effluent
from app.routers import sludge as router_sludge
from app.routers import chemical as router_chemical
from app.routers import odor as router_odor
from app.routers import online_monitor as router_online_monitor
from app.routers import energy as router_energy
from app.routers import equipment as router_equipment
from app.routers import shift as router_shift
from app.routers import abnormal as router_abnormal
from app.routers import water_quality as router_water_quality
from app.routers import maintain_plan as router_maintain_plan
from app.routers import reagent_stock as router_reagent_stock
from app.routers import process_log as router_process_log

ROUTERS = [router_inflow, router_aeration, router_sediment, router_advanced_treat, router_disinfection, router_effluent, router_sludge, router_chemical, router_odor, router_online_monitor, router_energy, router_equipment, router_shift, router_abnormal, router_water_quality, router_maintain_plan, router_reagent_stock, router_process_log]
