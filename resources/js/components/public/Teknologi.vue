<template>
  <section id="technology" class="py-24 px-4 bg-black">
    <div class="max-w-6xl mx-auto">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4 font-display">Teknologi di Balik Layar</h2>
        <p class="text-zinc-400 max-w-2xl mx-auto">
          Sistem klasifikasi kami dibangun di atas ekosistem kecerdasan buatan modern untuk memastikan hasil yang cepat, efisien, dan akurat.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8">
        <div
          v-for="tech in technologies"
          :key="tech.name"
          :class="[
            'relative p-8 rounded-3xl border transition-all duration-500 hover:scale-[1.02] flex flex-col',
            tech.highlighted
              ? 'bg-zinc-900 border-emerald-500/50 shadow-2xl shadow-emerald-900/20'
              : 'bg-zinc-950 border-zinc-800 hover:border-zinc-700',
          ]"
        >
          <div
            v-if="tech.badge"
            :class="[
              'absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1.5 text-xs font-bold rounded-full uppercase tracking-widest shadow-lg whitespace-nowrap',
              tech.highlighted
                ? 'bg-emerald-500 text-zinc-950'
                : 'bg-zinc-800 text-zinc-300 border border-zinc-700'
            ]"
          >
            {{ tech.badge }}
          </div>

          <div class="mb-8 flex-1">
            <h3 class="text-2xl font-bold text-white mb-4">{{ tech.name }}</h3>
            <p class="text-zinc-400 text-sm leading-relaxed">{{ tech.description }}</p>
          </div>

          <ul class="space-y-4 mb-4">
            <li v-for="feature in tech.features" :key="feature" class="flex items-start gap-3 text-sm text-zinc-300">
              <Check class="w-5 h-5 text-emerald-500 shrink-0 mt-0.5" :stroke-width="2" />
              <span class="leading-relaxed">{{ feature }}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { Check } from 'lucide-vue-next'

const technologies = [
  {
    name: 'Convolutional Neural Network',
    badge: 'Algoritma',
    description: 'Metode Deep Learning mutakhir yang secara khusus dirancang untuk memproses dan menganalisis data visual dengan meniru cara kerja korteks visual manusia.',
    features: [
      'Mampu mengenali pola spasial pada tekstur dan warna biji kopi',
      'Mengekstraksi fitur visual secara otomatis',
      'Tahan terhadap variasi pencahayaan dan sudut gambar',
      'Standar industri terdepan untuk klasifikasi citra'
    ],
    highlighted: false,
  },
  {
    name: 'EfficientNetB0',
    badge: 'Arsitektur Utama',
    description: 'Arsitektur CNN canggih yang menggunakan metode compound scaling, menyeimbangkan kedalaman, lebar, dan resolusi jaringan secara presisi.',
    features: [
      'Akurasi klasifikasi tinggi (State-of-the-art)',
      'Jumlah parameter jauh lebih efisien dari arsitektur lama (ResNet/VGG)',
      'Waktu prediksi instan yang tidak membebani perangkat',
      'Memanfaatkan Transfer Learning untuk dataset kopi'
    ],
    highlighted: true,
  },
  {
  name: 'TensorFlow.js & WebGL',
  badge: 'Deployment',
  description: 'Infrastruktur runtime yang memungkinkan model AI dijalankan secara native di sisi klien menggunakan akselerasi perangkat keras tanpa bergantung pada server backend.',
  features: [
    'Komputasi paralel menggunakan WebGL (GPU Acceleration)',
    'Zero-latency inference (Prediksi instan tanpa jeda jaringan)',
    'Data Privacy: Pemrosesan foto dilakukan 100% lokal di browser',
    'Konversi model format .keras ke format JSON teroptimasi'
  ],
  highlighted: false,
},
]
</script>
