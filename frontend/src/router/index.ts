import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Inflow = () => import('@/views/inflow/index.vue')
const Aeration = () => import('@/views/aeration/index.vue')
const Sediment = () => import('@/views/sediment/index.vue')
const AdvancedTreat = () => import('@/views/advanced_treat/index.vue')
const Disinfection = () => import('@/views/disinfection/index.vue')
const Effluent = () => import('@/views/effluent/index.vue')
const Sludge = () => import('@/views/sludge/index.vue')
const Chemical = () => import('@/views/chemical/index.vue')
const Odor = () => import('@/views/odor/index.vue')
const OnlineMonitor = () => import('@/views/online_monitor/index.vue')
const Energy = () => import('@/views/energy/index.vue')
const Equipment = () => import('@/views/equipment/index.vue')
const Shift = () => import('@/views/shift/index.vue')
const Abnormal = () => import('@/views/abnormal/index.vue')
const WaterQuality = () => import('@/views/water_quality/index.vue')
const MaintainPlan = () => import('@/views/maintain_plan/index.vue')
const ReagentStock = () => import('@/views/reagent_stock/index.vue')
const ProcessLog = () => import('@/views/process_log/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/inflow', name: 'inflow', component: Inflow },
    { path: '/aeration', name: 'aeration', component: Aeration },
    { path: '/sediment', name: 'sediment', component: Sediment },
    { path: '/advanced_treat', name: 'advanced_treat', component: AdvancedTreat },
    { path: '/disinfection', name: 'disinfection', component: Disinfection },
    { path: '/effluent', name: 'effluent', component: Effluent },
    { path: '/sludge', name: 'sludge', component: Sludge },
    { path: '/chemical', name: 'chemical', component: Chemical },
    { path: '/odor', name: 'odor', component: Odor },
    { path: '/online_monitor', name: 'online_monitor', component: OnlineMonitor },
    { path: '/energy', name: 'energy', component: Energy },
    { path: '/equipment', name: 'equipment', component: Equipment },
    { path: '/shift', name: 'shift', component: Shift },
    { path: '/abnormal', name: 'abnormal', component: Abnormal },
    { path: '/water_quality', name: 'water_quality', component: WaterQuality },
    { path: '/maintain_plan', name: 'maintain_plan', component: MaintainPlan },
    { path: '/reagent_stock', name: 'reagent_stock', component: ReagentStock },
    { path: '/process_log', name: 'process_log', component: ProcessLog },
  ],
})

export default router
