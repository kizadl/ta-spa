<template>
  <section id="features" class="py-24 px-4">
    <div class="max-w-6xl mx-auto">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4 font-display">Everything you need to ship</h2>
        <p class="text-zinc-400 max-w-2xl mx-auto">
          Built for modern teams. Powerful features that help you build, deploy, and scale faster than ever.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <!-- Large card - System Status -->
        <div
          class="md:col-span-2 group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-zinc-600 hover:scale-[1.02] transition-all duration-300 overflow-hidden"
        >
          <div class="flex items-start justify-between mb-8">
            <div>
              <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4">
                <Activity class="w-5 h-5 text-zinc-400" :stroke-width="1.5" />
              </div>
              <h3 class="text-xl font-semibold text-white mb-2">Real-time Monitoring</h3>
              <p class="text-zinc-400 text-sm">
                Track system health, performance metrics, and alerts in real-time across all your deployments.
              </p>
            </div>
            <div class="flex items-center gap-2">
              <div
                v-for="(active, i) in dots"
                :key="i"
                :class="[
                  'w-2 h-2 rounded-full',
                  active ? 'bg-emerald-500 animate-pulse' : 'bg-zinc-700',
                ]"
              />
            </div>
          </div>
          <div class="grid grid-cols-4 gap-4">
            <div v-for="metric in metrics" :key="metric" class="text-center">
              <div class="text-2xl font-bold text-white mb-1">{{ Math.floor(Math.random() * 40 + 60) }}%</div>
              <div class="text-xs text-zinc-500">{{ metric }}</div>
            </div>
          </div>
        </div>

        <!-- Command Palette -->
        <div
          class="group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-zinc-600 hover:scale-[1.02] transition-all duration-300"
        >
          <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4">
            <Command class="w-5 h-5 text-zinc-400" :stroke-width="1.5" />
          </div>
          <h3 class="text-lg font-semibold text-white mb-2">Command Palette</h3>
          <p class="text-zinc-400 text-sm mb-6">Navigate anywhere instantly with powerful keyboard shortcuts.</p>
          <div class="flex items-center gap-1">
            <kbd class="px-2 py-1 text-xs bg-zinc-800 border border-zinc-700 rounded text-zinc-300 font-mono">
              ⌘
            </kbd>
            <kbd class="px-2 py-1 text-xs bg-zinc-800 border border-zinc-700 rounded text-zinc-300 font-mono">
              K
            </kbd>
          </div>
        </div>

        <!-- Analytics -->
        <div
          class="group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-zinc-600 hover:scale-[1.02] transition-all duration-300"
        >
          <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4">
            <BarChart3 class="w-5 h-5 text-zinc-400" :stroke-width="1.5" />
          </div>
          <h3 class="text-lg font-semibold text-white mb-2">Analytics</h3>
          <p class="text-zinc-400 text-sm mb-4">Deep insights into your application performance.</p>
          <svg viewBox="0 0 100 70" class="w-full h-24">
            <defs>
              <linearGradient id="chartGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="rgb(255,255,255)" stop-opacity="0.2" />
                <stop offset="100%" stop-color="rgb(255,255,255)" stop-opacity="0" />
              </linearGradient>
            </defs>
            <path
              d="M 0 60 L 20 45 L 40 55 L 60 30 L 80 40 L 100 15 L 100 70 L 0 70 Z"
              fill="url(#chartGradient)"
              class="opacity-50"
            />
            <path
              d="M 0 60 L 20 45 L 40 55 L 60 30 L 80 40 L 100 15"
              fill="none"
              stroke="white"
              stroke-width="2"
              stroke-linecap="round"
            />
          </svg>
        </div>

        <!-- Performance -->
        <div
          class="group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-zinc-600 hover:scale-[1.02] transition-all duration-300"
        >
          <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4">
            <Zap class="w-5 h-5 text-zinc-400" :stroke-width="1.5" />
          </div>
          <h3 class="text-lg font-semibold text-white mb-2">Blazing Fast</h3>
          <p class="text-zinc-400 text-sm mb-4">
            Edge-optimized infrastructure for sub-50ms response times globally.
          </p>
          <div class="flex items-center gap-2 text-emerald-500 text-sm">
            <span class="font-mono">~32ms</span>
            <span class="text-zinc-500">avg response</span>
          </div>
        </div>

        <!-- Security -->
        <div
          class="group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-zinc-600 hover:scale-[1.02] transition-all duration-300"
        >
          <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4">
            <Shield class="w-5 h-5 text-zinc-400" :stroke-width="1.5" />
          </div>
          <h3 class="text-lg font-semibold text-white mb-2">Enterprise Security</h3>
          <p class="text-zinc-400 text-sm mb-4">SOC2 compliant with end-to-end encryption and SSO support.</p>
          <div class="flex items-center gap-2">
            <span class="px-2 py-1 text-xs bg-zinc-800 rounded text-zinc-400">SOC2</span>
            <span class="px-2 py-1 text-xs bg-zinc-800 rounded text-zinc-400">GDPR</span>
            <span class="px-2 py-1 text-xs bg-zinc-800 rounded text-zinc-400">HIPAA</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { Activity, Command, BarChart3, Zap, Shield } from 'lucide-vue-next'

const dots = ref([true, true, true, false, true])
const metrics = ['CPU', 'Memory', 'Network', 'Storage']

let interval: NodeJS.Timeout

onMounted(() => {
  interval = setInterval(() => {
    dots.value = dots.value.map(() => Math.random() > 0.2)
  }, 2000)
})

onBeforeUnmount(() => {
  clearInterval(interval)
})
</script>
