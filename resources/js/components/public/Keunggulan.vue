<template>
  <section id="features" class="py-24 px-4">
    <div class="max-w-6xl mx-auto">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4 font-display">Keunggulan Sistem Kami</h2>
        <p class="text-zinc-400 max-w-2xl mx-auto">
          Didukung oleh teknologi kecerdasan buatan terkini untuk memberikan klasifikasi biji kopi yang cepat, presisi, dan andal.
        </p>
      </div>

      

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <!-- Large card - AI Architecture -->
        <div
          class="md:col-span-2 group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-emerald-500/50 hover:scale-[1.02] transition-all duration-300 overflow-hidden"
        >
          <div class="flex items-start justify-between mb-8">
            <div>
              <div class="p-2 rounded-lg bg-emerald-500/10 w-fit mb-4">
                <Activity class="w-5 h-5 text-emerald-500" :stroke-width="1.5" />
              </div>
              <h3 class="text-xl font-semibold text-white mb-2">Arsitektur EfficientNetB0</h3>
              <p class="text-zinc-400 text-sm">
                Model klasifikasi kami menggunakan EfficientNetB0, menghadirkan keseimbangan optimal antara akurasi tinggi dan efisiensi komputasi untuk mendeteksi proses pasca-panen (Natural, Honey, Wash).
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
            <div v-for="(metric, idx) in metrics" :key="metric" class="text-center">
              <div class="text-2xl font-bold text-white mb-1">{{ metricValues[idx] }}%</div>
              <div class="text-xs text-zinc-500">{{ metric }}</div>
            </div>
          </div>
        </div>
        <!-- Security -->
        <div
          class="group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-emerald-500/50 hover:scale-[1.02] transition-all duration-300">
          <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4 group-hover:bg-emerald-500/10 transition-colors">
            <Bean 
              class="w-5 h-5 text-zinc-400 group-hover:text-emerald-500 transition-colors -rotate-15 group-hover:rotate-0 transition-transform duration-500" 
              :stroke-width="1.5" 
            />
          </div>
          <h3 class="text-lg font-semibold text-white mb-2">Target Klasifikasi</h3>
          <p class="text-zinc-400 text-sm mb-4">
            Model ini dilatih khusus untuk membedakan tiga metode pemrosesan pasca-panen utama:
          </p>
          <div class="flex flex-wrap gap-2">
            <span class="px-2 py-1 text-[10px] font-black bg-zinc-800 rounded text-emerald-500 border border-emerald-500/20 tracking-widest uppercase">Natural</span>
            <span class="px-2 py-1 text-[10px] font-black bg-zinc-800 rounded text-emerald-500 border border-emerald-500/20 tracking-widest uppercase">Honey</span>
            <span class="px-2 py-1 text-[10px] font-black bg-zinc-800 rounded text-emerald-500 border border-emerald-500/20 tracking-widest uppercase">Wash</span>
          </div>
        </div>
        
        <!-- Analytics -->
        <div
        class="group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-emerald-500/50 hover:scale-[1.02] transition-all duration-300"
        >
        <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4 group-hover:bg-emerald-500/10 transition-colors">
          <BarChart3 class="w-5 h-5 text-zinc-400 group-hover:text-emerald-500 transition-colors" :stroke-width="1.5" />
        </div>
        <h3 class="text-lg font-semibold text-white mb-2">Performa Stabil</h3>
        <p class="text-zinc-400 text-sm mb-4">Grafik akurasi klasifikasi berdasarkan dataset pelatihan yang komprehensif.</p>
        <div class="flex items-end gap-1 h-12">
          <div class="flex-1 bg-emerald-500/20 h-[80%] rounded-t-sm"></div>
          <div class="flex-1 bg-emerald-500/40 h-[60%] rounded-t-sm"></div>
          <div class="flex-1 bg-emerald-500 h-[95%] rounded-t-sm"></div>
          <div class="flex-1 bg-emerald-500/60 h-[40%] rounded-t-sm"></div>
        </div>
      </div>
      
      <!-- Performance -->
      <div
      class="group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-emerald-500/50 hover:scale-[1.02] transition-all duration-300"
      >
      <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4 group-hover:bg-emerald-500/10 transition-colors">
        <Zap class="w-5 h-5 text-zinc-400 group-hover:text-emerald-500 transition-colors" :stroke-width="1.5" />
      </div>
      <h3 class="text-lg font-semibold text-white mb-2">Proses Instan</h3>
      <p class="text-zinc-400 text-sm mb-4">
            Infrastruktur yang dioptimalkan untuk memberikan hasil prediksi klasifikasi secara instan.
          </p>
          <div class="flex items-center gap-2 text-emerald-500 text-sm">
            <span class="font-mono">~150ms</span>
            <span class="text-zinc-500 italic">inference time</span>
          </div>
        </div>
        
      <!-- Command Palette -->
      <div
        class="group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-emerald-500/50 hover:scale-[1.02] transition-all duration-300"
      >
        <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4 group-hover:bg-emerald-500/10 transition-colors">
          <Command class="w-5 h-5 text-zinc-400 group-hover:text-emerald-500 transition-colors" :stroke-width="1.5" />
        </div>
        <h3 class="text-lg font-semibold text-white mb-2">Panduan Cepat</h3>
        <p class="text-zinc-400 text-sm mb-6">Gunakan pintasan keyboard untuk berpindah antarmuka dan memulai analisis dengan cepat.</p>
        <div class="flex items-center gap-1">
          <kbd class="px-2 py-1 text-xs bg-zinc-800 border border-zinc-700 rounded text-zinc-300 font-mono italic">
            Alt + S
          </kbd>
          <span class="text-xs text-zinc-600 ml-1">untuk Scan</span>
        </div>
      </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { Activity, Command, BarChart3, Zap, Shield } from 'lucide-vue-next'
import { Bean, Upload, FolderOpen, X } from 'lucide-vue-next'

const dots = ref([true, true, true, false, true])
const metrics = ['Akurasi', 'Presisi', 'Recall', 'F1-Score']
const metricValues = [96, 95, 96, 95]

let interval: ReturnType<typeof setInterval>

  onMounted(() => {
    interval = setInterval(() => {
    dots.value = dots.value.map(() => Math.random() > 0.2)
  }, 2000)
})

onBeforeUnmount(() => {
  clearInterval(interval)
})
</script>
