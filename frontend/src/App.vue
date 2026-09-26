<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">污水处理工艺调度管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">覆盖进水、生化池、二沉池、深度处理、污泥脱水及排放监测的全流程污水处理工艺调度后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "进水监控", path: "/inflow" }, { label: "生化池曝气", path: "/aeration" }, { label: "二沉池管理", path: "/sediment" }, { label: "深度处理", path: "/advanced_treat" }, { label: "消毒工艺", path: "/disinfection" }, { label: "出水排放", path: "/effluent" }, { label: "污泥脱水", path: "/sludge" }, { label: "药剂管理", path: "/chemical" }, { label: "除臭系统", path: "/odor" }, { label: "在线监测", path: "/online_monitor" }, { label: "能耗管理", path: "/energy" }, { label: "设备台账", path: "/equipment" }, { label: "班组交班", path: "/shift" }, { label: "异常处置", path: "/abnormal" }, { label: "水质化验", path: "/water_quality" }, { label: "维保计划", path: "/maintain_plan" }, { label: "试剂耗材", path: "/reagent_stock" }, { label: "工艺日志", path: "/process_log" }]
</script>
