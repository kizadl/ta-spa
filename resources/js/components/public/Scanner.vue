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
              
              <div class="flex flex-wrap items-center gap-3">
                <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/20">
                  <div :class="['w-2 h-2 rounded-full bg-emerald-500', isLoading ? 'animate-ping' : 'animate-pulse']"></div>
                  <span class="text-[10px] font-bold text-emerald-500 uppercase tracking-wider">
                    {{ isLoading ? 'Processing...' : 'AI Model Ready' }}
                  </span>
                </div>
                
                <button 
                  @click="showGuideModal = true" 
                  class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-zinc-800/80 border border-zinc-700 hover:border-emerald-500/50 hover:bg-zinc-800 transition-all group"
                >
                  <Info class="w-3.5 h-3.5 text-zinc-400 group-hover:text-emerald-400 transition-colors" />
                  <span class="text-[10px] font-bold text-zinc-400 group-hover:text-emerald-400 uppercase tracking-wider transition-colors">
                    Panduan Foto
                  </span>
                </button>
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
                  <img :src="imagePreview" class="absolute inset-0 w-full h-full object-cover" loading="lazy" />
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
          <div 
            v-if="predictionResult" 
            class="mt-8 p-8 rounded-3xl text-center relative overflow-hidden transition-colors duration-500 shadow-lg"
            :class="statusInfo?.cardClass"
          >
            <div class="relative z-10">
              <div :class="predictionResult.status === 'DITOLAK' ? 'flex flex-col md:flex-row items-center justify-center gap-8' : ''">
                
                <!-- KIRI: CONTOH FOTO JIKA DITOLAK -->
                <div v-if="predictionResult.status === 'DITOLAK'" class="flex-1 w-full max-w-sm mx-auto bg-black/20 p-6 rounded-2xl border border-white/10 text-left">
                  <p class="text-sm text-white font-bold mb-3 text-center">Contoh Foto yang Benar:</p>
                  <img src="/pict_example.jpg" alt="Contoh Foto Biji Kopi" class="w-full rounded-xl shadow-sm border border-white/20" loading="lazy" />
                </div>

                <!-- KANAN / TENGAH: HASIL PREDIKSI -->
                <div class="flex-1 w-full max-w-sm mx-auto flex flex-col justify-center">
                  <p class="text-xs font-black text-white/70 uppercase tracking-[0.3em] mb-2">Hasil Klasifikasi AI</p>
                  <h4 class="text-5xl font-black text-white mb-4 tracking-tighter">{{ predictionResult.label }}</h4>
                  
                  <div class="flex flex-wrap justify-center gap-3">
                    <div class="px-4 py-1.5 bg-black/20 rounded-full backdrop-blur-md border border-white/10">
                      <span class="text-white font-bold text-xs uppercase tracking-widest">Confidence: {{ predictionResult.confidence }}</span>
                    </div>
                    
                    <div 
                      class="px-4 py-1.5 rounded-full backdrop-blur-md border flex items-center gap-2"
                      :class="statusInfo?.badgeClass"
                    >
                      <div :class="['w-1.5 h-1.5 rounded-full', statusInfo?.dotClass]"></div>
                      <span class="font-bold text-xs uppercase tracking-widest">
                        {{ statusInfo?.text }}
                      </span>
                    </div>
                  </div>

                  <!-- Menampilkan Probabilitas -->
                  <div v-if="predictionResult.details" class="mt-6 text-sm text-white/80 whitespace-pre-line text-left bg-black/20 p-4 rounded-xl border border-white/10 w-full">
                    {{ predictionResult.details }}
                  </div>
                </div>

              </div>
            </div>
            <Bean class="absolute -right-10 -bottom-10 w-40 h-40 text-white/10 rotate-12" />
          </div>
        </transition>

      </div>
    </div>

    <!-- Modal Panduan -->
    <transition 
      enter-active-class="transition duration-300 ease-out" 
      enter-from-class="opacity-0" 
      enter-to-class="opacity-100" 
      leave-active-class="transition duration-200 ease-in" 
      leave-from-class="opacity-100" 
      leave-to-class="opacity-0"
    >
      <div v-if="showGuideModal" class="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm" @click="showGuideModal = false">
        <div class="bg-zinc-900 border border-zinc-800 rounded-3xl max-w-3xl w-full p-6 sm:p-8 relative overflow-hidden shadow-2xl" @click.stop>
          <button @click="showGuideModal = false" class="absolute top-4 right-4 text-zinc-400 hover:text-white bg-zinc-800 hover:bg-zinc-700 p-2 rounded-full transition-colors z-10">
            <X class="w-5 h-5" />
          </button>
          
          <div class="flex items-center gap-3 mb-8 pr-8">
            <div class="p-2.5 rounded-xl bg-emerald-500/10">
              <Info class="w-6 h-6 text-emerald-500" />
            </div>
            <h3 class="text-2xl font-bold text-white font-display">Panduan Pengambilan Foto</h3>
          </div>
          
          <div class="grid md:grid-cols-2 gap-8 items-center">
            <div class="space-y-4">
              <div class="bg-black/50 rounded-2xl overflow-hidden border border-zinc-800 relative group">
                <img src="/pict_example.jpg" alt="Contoh Foto Benar" class="w-full h-auto aspect-video object-cover" />
                <div class="absolute inset-0 border-2 border-emerald-500/0 group-hover:border-emerald-500/50 rounded-2xl transition-colors pointer-events-none"></div>
              </div>
              <div class="flex items-center gap-2 text-emerald-400 text-sm font-medium">
                <div class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></div>
                Contoh Foto yang Benar
              </div>
            </div>
            
            <div class="flex flex-col justify-center space-y-6">
              <div>
                <h4 class="text-lg font-bold text-white mb-3 flex items-center gap-2">
                  <span class="text-emerald-500">Tips</span> agar hasil akurat:
                </h4>
                <ul class="space-y-3">
                  <li class="flex items-start gap-3">
                    <div class="min-w-[24px] h-6 rounded-full bg-emerald-500/10 text-emerald-500 flex items-center justify-center text-xs font-bold mt-0.5 border border-emerald-500/20">1</div>
                    <p class="text-zinc-300 text-sm leading-relaxed">Pastikan objek biji kopi <strong>fokus</strong> dan tidak buram (blur).</p>
                  </li>
                  <li class="flex items-start gap-3">
                    <div class="min-w-[24px] h-6 rounded-full bg-emerald-500/10 text-emerald-500 flex items-center justify-center text-xs font-bold mt-0.5 border border-emerald-500/20">2</div>
                    <p class="text-zinc-300 text-sm leading-relaxed">Gunakan <strong>pencahayaan yang cukup</strong> (cahaya matahari/lampu terang) agar tekstur dan warna jelas.</p>
                  </li>
                  <li class="flex items-start gap-3">
                    <div class="min-w-[24px] h-6 rounded-full bg-emerald-500/10 text-emerald-500 flex items-center justify-center text-xs font-bold mt-0.5 border border-emerald-500/20">3</div>
                    <p class="text-zinc-300 text-sm leading-relaxed">Hindari <strong>bayangan yang terlalu gelap</strong> atau pantulan cahaya yang menyilaukan.</p>
                  </li>
                  <li class="flex items-start gap-3">
                    <div class="min-w-[24px] h-6 rounded-full bg-emerald-500/10 text-emerald-500 flex items-center justify-center text-xs font-bold mt-0.5 border border-emerald-500/20">4</div>
                    <p class="text-zinc-300 text-sm leading-relaxed">Ambil foto dari <strong>jarak yang pas</strong>. Biji kopi harus terlihat jelas secara keseluruhan.</p>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          
          <div class="mt-8 pt-6 border-t border-zinc-800 flex justify-end">
            <button @click="showGuideModal = false" class="px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl transition-colors">
              Mengerti
            </button>
          </div>
        </div>
      </div>
    </transition>

  </section>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { router } from '@inertiajs/vue3'
import { route } from 'ziggy-js'
import { Upload, Plus, X, Loader2, Bean, Info } from 'lucide-vue-next'

const imagePreview = ref<string | null>(null)
const selectedFile = ref<File | null>(null)
const predictionResult = ref<{ label: string, confidence: string, details?: string, status?: string } | null>(null)
const isLoading = ref(false)
const showGuideModal = ref(false)

const statusInfo = computed(() => {
  if (!predictionResult.value) return null
  
  // Membaca status langsung dari Backend!
  const statusAI = predictionResult.value.status 

  if (statusAI === 'BERHASIL') {
    return {
      text: 'Berhasil',
      cardClass: 'bg-emerald-600 shadow-[0_0_50px_-12px_rgba(16,185,129,0.5)]',
      badgeClass: 'bg-emerald-500/20 border-emerald-500/50 text-emerald-200',
      dotClass: 'bg-emerald-400'
    }
  } else {
    // Berlaku untuk 'DITOLAK'
    return {
      text: 'Ditolak',
      cardClass: 'bg-red-600 shadow-[0_0_50px_-12px_rgba(220,38,38,0.5)]',
      badgeClass: 'bg-red-500/20 border-red-500/50 text-red-200',
      dotClass: 'bg-red-400'
    }
  }
})

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
    const response = await fetch('/predict', {
      method: 'POST',
      body: formData,
      headers: {
        'X-CSRF-TOKEN': (document.querySelector('meta[name="csrf-token"]') as HTMLMetaElement)?.content || ''
      }
    })
    
    if (!response.ok) {
      const errorData = await response.json()
      throw new Error(errorData.error || "Gagal melakukan klasifikasi")
    }
    
    const data = await response.json()
    predictionResult.value = {
      label: data.label,
      confidence: data.confidence + '%', // Tambah % biar rapi di UI
      details: data.message,
      status: data.status // Simpan status dari Laravel/Flask
    }

    // Refresh data jika di Inertia context (dashboard)
    if (typeof route === 'function' && route().current('classifications.index')) {
      router.reload({ only: ['classifications'] })
    }
  } catch (error: any) {
    console.error(error)
    predictionResult.value = {
      label: 'Gagal',
      confidence: '0%',
      details: error.message || 'Terjadi kesalahan saat klasifikasi',
      status: 'DITOLAK' // Beri status DITOLAK agar UI langsung memerah
    }
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