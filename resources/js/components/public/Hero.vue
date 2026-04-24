<template>
  <section
    class="relative min-h-screen flex flex-col items-center justify-center px-4 pt-24 pb-16 overflow-hidden"
  >
    <!-- Background gradient -->
    <div
      class="absolute inset-0 bg-gradient-to-b from-zinc-950 via-zinc-950 to-zinc-900 pointer-events-none"
    />

    <!-- Subtle radial glow -->
    <div
      class="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[600px] bg-zinc-800/20 rounded-full blur-3xl pointer-events-none"
    />

    <div class="relative z-10 max-w-5xl mx-auto text-center">
      <!-- Badge -->
      <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-zinc-900 border border-zinc-800 mb-8">
        <span class="w-2 h-2 rounded-full bg-emerald-500 pulse-glow" />
        <span class="text-sm text-zinc-400">GREENS</span>
      </div>

      <!-- Headline -->
      <h1 class="text-5xl sm:text-6xl lg:text-7xl font-bold tracking-tight text-white mb-6 font-display">
        <span class="block">Klasifikasi</span>
        <span class="block text-zinc-500">Biji Hijau Kopi</span>
      </h1>

      <!-- Subheadline -->
      <p class="text-lg sm:text-xl text-zinc-400 max-w-2xl mx-auto mb-10 leading-relaxed">
        Klasifikasi Biji Hijau Kopi adalah sebuah sistem yang menggunakan Kecerdasan Buatan (AI) untuk mengklasifikasikan biji hijau kopi berdasarkan Proses Pasca Panennya
      </p>

      <!-- CTAs -->
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4 mb-16">
        <button
          class="shimmer-btn bg-white text-zinc-950 hover:bg-zinc-200 rounded-full px-8 py-3 text-base font-medium shadow-lg shadow-white/10 flex items-center gap-2"
        >
          Mulai Klasifikasi
          <ArrowRight :size="16" />
        </button>
        <!-- <button
          class="rounded-full px-8 py-3 text-base font-medium border border-zinc-800 text-zinc-300 hover:bg-zinc-900 hover:text-white hover:border-zinc-700 bg-transparent"
        >
          View Demo
        </button> -->
      </div>

      <!-- Social Proof -->
      <div class="flex flex-col items-center gap-4">
        <div class="flex items-center -space-x-3">
          <img
            v-for="(avatar, index) in avatars"
            :key="index"
            :src="avatar"
            :alt="`Avatar ${index + 1}`"
            class="w-10 h-10 rounded-full border-2 border-zinc-950 object-cover"
          />
        </div>
        <p class="text-sm text-zinc-500">
          Telah digunakan oleh <span class="text-zinc-300 font-medium">2,000+</span> orang
        </p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ArrowRight } from 'lucide-vue-next'

const avatars = [
  '/professional-headshot-1.png',
  '/professional-headshot-2.png',
  '/professional-headshot-3.png',
  '/professional-headshot-4.png',
  '/professional-headshot-5.png',
]
</script>
