<template>
  <section id="klasifikasi" class="py-24 px-4 bg-black">
    <div class="max-w-6xl mx-auto">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4 font-display ">COFFEE <span class="text-emerald-500">SCANNER</span></h2>
        <p class="text-zinc-400 max-w-2xl mx-auto">
          Identifikasi proses pasca-panen biji kopi Anda (Natural, Honey, Wash) menggunakan teknologi Artificial Intelligence.
        </p>
      </div>

      <div class="max-w-5xl mx-auto">
        <div class="group relative p-8 rounded-3xl bg-zinc-900 border border-zinc-800 hover:border-emerald-500/50 transition-all duration-500 overflow-hidden">
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
                  <div :class="['w-2 h-2 rounded-full bg-emerald-500', isLoading ? 'animate-ping' : 'animate-pulse']"></div>
                  <span class="text-[10px] font-bold text-emerald-500 uppercase tracking-wider">
                    {{ isLoading ? 'Processing...' : 'AI Model Ready' }}
                  </span>
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
                @click="startClassification"
                :disabled="!imagePreview || isLoading"
                class="w-full py-4 rounded-xl font-bold text-base transition-all border-2 border-emerald-600 text-emerald-500 hover:bg-emerald-600 hover:text-white active:scale-95 disabled:opacity-50 disabled:border-zinc-700 disabled:text-zinc-500 disabled:cursor-not-allowed flex items-center justify-center gap-2"
              >
                <Loader2 v-if="isLoading" class="w-5 h-5 animate-spin" />
                {{ isLoading ? 'Sedang Menganalisis...' : 'Analisis Sekarang' }}
              </button>
            </div>
          </div>
        </div>

        <transition enter-active-class="transition duration-500 ease-out" enter-from-class="transform scale-95 opacity-0" enter-to-class="transform scale-100 opacity-100">
          <div v-if="predictionResult" class="mt-8 p-8 rounded-3xl bg-emerald-600 shadow-[0_0_50px_-12px_rgba(16,185,129,0.5)] text-center relative overflow-hidden">
            <div class="relative z-10">
              <p class="text-xs font-black text-emerald-100 uppercase tracking-[0.3em] mb-2">Hasil Klasifikasi AI</p>
              <h4 class="text-5xl font-black text-white italic mb-2 tracking-tighter">{{ predictionResult.label }}</h4>
              <div class="inline-block px-4 py-1.5 bg-black/20 rounded-full backdrop-blur-md">
                <span class="text-emerald-500 font-bold text-sm uppercase tracking-widest">Confidence: {{ predictionResult.confidence }}</span>
              </div>
            </div>
            <Bean class="absolute -right-10 -bottom-10 w-40 h-40 text-white/10 rotate-12" />
          </div>
        </transition>

      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Upload, Plus, X, Loader2, Bean } from 'lucide-vue-next'

const imagePreview = ref<string | null>(null)
const selectedFile = ref<File | null>(null)
const predictionResult = ref<{ label: string, confidence: string } | null>(null)
const isLoading = ref(false)

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  
  if (file) {
    selectedFile.value = file
    predictionResult.value = null // Reset hasil jika ganti gambar
    const reader = new FileReader()
    reader.onload = (e) => {
      imagePreview.value = e.target?.result as string
    }
    reader.readAsDataURL(file)
  }
}

const startClassification = async () => {
  if (!selectedFile.value) return
  
  isLoading.value = true
  const formData = new FormData()
  formData.append('image', selectedFile.value)

  try {
    const response = await fetch('http://127.0.0.1:5001/predict', {
      method: 'POST',
      body: formData
    })
    
    if (!response.ok) throw new Error("Gagal terhubung ke AI server")
    
    const data = await response.json()
    // Pastikan data yang dikirim Flask sesuai (label & confidence)
    predictionResult.value = {
      label: data.label,
      confidence: data.confidence
    }
  } catch (error) {
    alert("Error: Pastikan backend-ai sudah dijalankan (python app.py)")
    console.error(error)
  } finally {
    isLoading.value = false
  }
}

const clearImage = () => {
  imagePreview.value = null
  selectedFile.value = null
  predictionResult.value = null
}
</script>