<template>
  <section id="klasifikasi" class="py-24 px-4 bg-black">
    <div class="max-w-6xl mx-auto">


      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4 font-display">COFFEE SCAN</h2>
        <p class="text-zinc-400 max-w-2xl mx-auto">
          Identifikasi proses pasca-panen biji kopi Anda (Natural, Honey, Wash) menggunakan teknologi Artificial Intelligence.
        </p>
      </div>

      <div class="max-w-5xl mx-auto">
        <div
          class="group relative p-8 rounded-3xl bg-zinc-900 border border-zinc-800 hover:border-emerald-500/50 transition-all duration-500 overflow-hidden"
        >
          <div class="flex flex-col md:flex-row items-stretch justify-between gap-8">
            <div class="flex-1 flex flex-col justify-center">
              <div class="p-3 rounded-xl bg-emerald-500/10 w-fit mb-6">
                <Upload class="w-6 h-6 text-emerald-500" :stroke-width="2" />
              </div>
              <h3 class="text-2xl font-bold text-white mb-3">Klasifikasi Foto</h3>
              <p class="text-zinc-400 text-sm mb-8 leading-relaxed max-w-xs">
                Unggah foto biji kopi Arabika Anda. Pastikan gambar jelas dan mendapatkan pencahayaan yang cukup untuk hasil terbaik.
              </p>
              
              <div class="flex items-center gap-3">
                <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/20">
                  <div class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
                  <span class="text-[10px] font-bold text-emerald-500 uppercase tracking-wider">AI Model Ready</span>
                </div>
              </div>
            </div>

            <div class="w-full md:w-1/2 flex flex-col justify-center gap-4">
              <label 
                for="coffee-upload"
                class="relative group/upload w-full aspect-[4/3] cursor-pointer flex flex-col items-center justify-center border-2 border-dashed border-zinc-800 rounded-2xl bg-zinc-950/50 p-6 hover:border-emerald-500/40 hover:bg-zinc-900/50 transition-all duration-300 overflow-hidden"
              >
                <input 
                  type="file" 
                  id="coffee-upload" 
                  class="hidden" 
                  accept="image/*"
                  @change="handleFileChange" 
                />
                
                <template v-if="!imagePreview">
                  <div class="w-16 h-16 bg-zinc-800 rounded-full flex items-center justify-center mb-6 group-hover/upload:scale-110 transition-transform duration-300">
                    <Plus class="w-8 h-8 text-zinc-400 group-hover/upload:text-emerald-500 transition-colors" />
                  </div>
                  <p class="text-base font-semibold text-zinc-300">Pilih Gambar Biji Kopi</p>
                  <p class="text-sm text-zinc-500 mt-2">Format PNG, JPG (Maks 5MB)</p>
                </template>

                <template v-else>
                  <img :src="imagePreview" class="absolute inset-0 w-full h-full object-cover" />
                  <div class="absolute inset-0 bg-black/40 opacity-0 group-hover/upload:opacity-100 transition-opacity duration-300 flex items-center justify-center backdrop-blur-[2px]">
                    <span class="bg-black/60 text-white px-4 py-2 rounded-full text-sm font-medium">Klik untuk mengganti</span>
                  </div>
                  <button 
                    @click.stop.prevent="clearImage" 
                    class="absolute top-4 right-4 bg-red-500 text-white p-1.5 rounded-full hover:bg-red-600 transition-all hover:scale-110 z-10 shadow-xl"
                  >
                    <X class="w-4 h-4" />
                  </button>
                </template>
              </label>
              
              <button 
                :disabled="!imagePreview"
                class="w-full py-4 rounded-xl font-bold text-base transition-all border-2 border-emerald-600 text-emerald-500 hover:bg-emerald-600/10 active:scale-95 disabled:opacity-50 disabled:border-zinc-700 disabled:text-zinc-500 disabled:hover:bg-transparent disabled:active:scale-100 disabled:cursor-not-allowed flex-none"
              >
                Analisis Sekarang
              </button>
            </div>
          </div>
        </div>

        <!-- <div
          class="group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-zinc-600 hover:scale-[1.02] transition-all duration-300"
        >
          <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4">
            <Command class="w-5 h-5 text-zinc-400" :stroke-width="1.5" />
          </div>
          <h3 class="text-lg font-semibold text-white mb-2">Panduan Cepat</h3>
          <p class="text-zinc-400 text-sm mb-6">Gunakan shortcut untuk berpindah antar mode klasifikasi.</p>
          <div class="flex items-center gap-1">
            <kbd class="px-2 py-1 text-xs bg-zinc-800 border border-zinc-700 rounded text-zinc-300 font-mono italic">Alt + S</kbd>
            <span class="text-xs text-zinc-600 ml-1">untuk Scan</span>
          </div>
        </div> -->

        <!-- <div
          class="group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-zinc-600 hover:scale-[1.02] transition-all duration-300"
        >
          <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4">
            <BarChart3 class="w-5 h-5 text-zinc-400" :stroke-width="1.5" />
          </div>
          <h3 class="text-lg font-semibold text-white mb-2">Akurasi Model</h3>
          <p class="text-zinc-400 text-sm mb-4">Performa klasifikasi berdasarkan dataset saat ini.</p>
          <div class="flex items-end gap-1 h-12">
            <div class="flex-1 bg-orange-500/20 h-[80%] rounded-t-sm"></div>
            <div class="flex-1 bg-orange-500/40 h-[60%] rounded-t-sm"></div>
            <div class="flex-1 bg-orange-500 h-[95%] rounded-t-sm"></div>
            <div class="flex-1 bg-orange-500/60 h-[40%] rounded-t-sm"></div>
          </div>
        </div> -->

        <!-- <div
          class="group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-zinc-600 hover:scale-[1.02] transition-all duration-300"
        >
          <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4">
            <Zap class="w-5 h-5 text-zinc-400" :stroke-width="1.5" />
          </div>
          <h3 class="text-lg font-semibold text-white mb-2">Proses Cepat</h3>
          <p class="text-zinc-400 text-sm mb-4">
            Prediksi instan menggunakan akselerasi GPU via TensorFlow.js.
          </p>
          <div class="flex items-center gap-2 text-orange-500 text-sm">
            <span class="font-mono">~150ms</span>
            <span class="text-zinc-500 italic">inference time</span>
          </div>
        </div> -->

        <!-- <div
          class="group relative p-6 rounded-2xl bg-zinc-900 border border-zinc-800 hover:border-zinc-600 hover:scale-[1.02] transition-all duration-300"
        >
          <div class="p-2 rounded-lg bg-zinc-800 w-fit mb-4">
            <Shield class="w-5 h-5 text-zinc-400" :stroke-width="1.5" />
          </div>
          <h3 class="text-lg font-semibold text-white mb-2">Privasi Terjamin</h3>
          <p class="text-zinc-400 text-sm mb-4">Foto Anda diproses langsung di browser tanpa disimpan di server kami.</p>
          <div class="flex items-center gap-2">
            <span class="px-2 py-1 text-[10px] font-bold bg-zinc-800 rounded text-zinc-400">CLIENT-SIDE</span>
            <span class="px-2 py-1 text-[10px] font-bold bg-zinc-800 rounded text-zinc-400">ENCRYPTED</span>
          </div>
        </div> -->
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { 
  Upload, 
  Plus, 
  X, 
  Command, 
  BarChart3, 
  Zap, 
  Shield 
} from 'lucide-vue-next'

const imagePreview = ref<string | null>(null)

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      imagePreview.value = e.target?.result as string
    }
    reader.readAsDataURL(file)
  }
}

const clearImage = () => {
  imagePreview.value = null
}
</script>