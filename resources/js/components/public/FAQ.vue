<template>
  <section id="faq" class="py-24 px-4 bg-zinc-950 border-t border-zinc-900">
    <div class="max-w-4xl mx-auto">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4 font-display">Pertanyaan yang Sering Diajukan</h2>
        <p class="text-zinc-400">Temukan jawaban untuk pertanyaan umum seputar klasifikasi AI GREENS CoffeeScan.</p>
      </div>

      <div class="space-y-4">
        <div 
          v-for="(faq, index) in faqs" 
          :key="index"
          class="border border-zinc-800 bg-zinc-900/50 rounded-2xl overflow-hidden transition-all duration-300 hover:border-emerald-500/30"
        >
          <button 
            @click="toggle(index)"
            class="w-full flex items-center justify-between p-6 text-left focus:outline-none"
          >
            <span class="font-semibold text-white pr-8">{{ faq.question }}</span>
            <div class="flex-shrink-0 w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center">
              <ChevronDown 
                class="w-5 h-5 text-emerald-500 transition-transform duration-300" 
                :class="activeIndex === index ? 'rotate-180' : ''"
              />
            </div>
          </button>
          
          <div 
            class="transition-all duration-300 ease-in-out overflow-hidden"
            :class="activeIndex === index ? 'max-h-48 opacity-100' : 'max-h-0 opacity-0'"
          >
            <div class="px-6 pb-6 text-zinc-400 text-sm leading-relaxed">
              {{ faq.answer }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ChevronDown } from 'lucide-vue-next'

const activeIndex = ref<number | null>(0)

const toggle = (index: number) => {
  activeIndex.value = activeIndex.value === index ? null : index
}

const faqs = [
  {
    question: 'Apa itu GREENS CoffeeScan?',
    answer: 'GREENS CoffeeScan adalah platform berbasis kecerdasan buatan (AI) yang dirancang khusus untuk mendeteksi dan mengklasifikasikan proses pasca-panen pada biji kopi Arabika (Natural, Honey, Wash).'
  },
  {
    question: 'Seberapa akurat model AI ini?',
    answer: 'Kami menggunakan arsitektur EfficientNetB0 canggih yang memberikan tingkat akurasi tinggi. Meskipun begitu, hasil prediksi AI sebaiknya digunakan sebagai asisten verifikasi dan referensi sekunder Anda.'
  },
  {
    question: 'Bagaimana cara mendapatkan hasil klasifikasi yang maksimal?',
    answer: 'Untuk hasil terbaik, pastikan foto biji kopi Anda jelas dan fokus. Ambil gambar dari jarak dekat dengan pencahayaan putih yang merata, dan pastikan tekstur serta warna biji kopi terlihat dengan baik.'
  },
  {
    question: 'Apakah layanan ini berbayar?',
    answer: 'Tidak, layanan analisis pemindaian dasar ini sepenuhnya gratis. Kami membangun platform ini untuk membantu produktivitas komunitas petani, prosesor, dan pecinta kopi.'
  },
  {
    question: 'Apakah foto yang saya unggah aman?',
    answer: 'Tentu saja. Privasi data Anda terjamin. Jika Anda memutuskan untuk membuat akun, foto tersebut hanya akan disimpan dalam database privat sebagai riwayat pribadi Anda dan tidak akan disebarluaskan.'
  }
]
</script>
