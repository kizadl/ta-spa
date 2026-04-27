<template>
  <section class="py-24 px-4 bg-black">
    <div class="max-w-4xl mx-auto text-center">
      <h2 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-white mb-6 tracking-tight font-display">
        Pantau Riwayat Klasifikasi
      </h2>
      <p v-if="!user" class="text-lg sm:text-xl text-zinc-400 mb-10 max-w-2xl mx-auto">
        Masuk ke akun Anda sekarang untuk menyimpan hasil dan melihat kembali seluruh riwayat klasifikasi biji kopi yang pernah Anda lakukan.
      </p>
      <p v-else class="text-lg sm:text-xl text-zinc-400 mb-10 max-w-2xl mx-auto">
        Pantau riwayat klasifikasi biji kopi Anda sekarang.
      </p>

      <div v-if="!user" class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <Link
          href="/login"
          class="shimmer-btn bg-emerald-500 text-zinc-950 hover:bg-emerald-400 rounded-full px-8 py-3 text-base font-bold shadow-lg shadow-emerald-500/20 flex items-center gap-2 transition-all active:scale-95"
        >
          Masuk ke Akun
          <ArrowRight :size="20" />
        </Link>
        <Link
          href="/register"
          class="rounded-full px-8 py-3 text-base font-medium border border-zinc-800 text-zinc-300 hover:bg-zinc-900 hover:text-white hover:border-zinc-700 bg-transparent transition-all active:scale-95"
        >
          Daftar Baru
        </Link>
      </div>

      <div v-else class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <Link
          href="/dashboard"
          class="shimmer-btn bg-emerald-500 text-zinc-950 hover:bg-emerald-400 rounded-full px-8 py-3 text-base font-bold shadow-lg shadow-emerald-500/20 flex items-center gap-2 transition-all active:scale-95"
        >
          Dashboard
        </Link>
      </div>

      <p class="mt-8 text-sm text-zinc-500">Gratis sepenuhnya. Jangan biarkan riwayat klasifikasi Anda hilang.</p>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ArrowRight } from 'lucide-vue-next'
import { Link, usePage } from '@inertiajs/vue3'
import { computed } from 'vue'

const page = usePage()
const user = computed(() => page.props.auth?.user)
</script>
