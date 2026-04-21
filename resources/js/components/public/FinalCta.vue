<template>
  <section class="py-24 px-4">
    <div class="max-w-4xl mx-auto text-center">
      <h2 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-white mb-6 tracking-tight font-display">
        Ready to ship faster?
      </h2>
      <p class="text-lg sm:text-xl text-zinc-400 mb-10 max-w-2xl mx-auto">
        Join thousands of teams already building with Apex. Start free, no credit card required.
      </p>

      <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <button
          class="shimmer-btn bg-white text-zinc-950 hover:bg-zinc-200 rounded-full px-8 py-3 text-base font-medium shadow-lg shadow-white/20 flex items-center gap-2"
        >
          Get Started for Free
          <ArrowRight :size="20" />
        </button>
        <button
          class="rounded-full px-8 py-3 text-base font-medium border border-zinc-800 text-zinc-300 hover:bg-zinc-900 hover:text-white hover:border-zinc-700 bg-transparent"
        >
          Talk to Sales
        </button>
      </div>

      <p class="mt-8 text-sm text-zinc-500">Free forever for individuals. Team plans start at $29/month.</p>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ArrowRight } from 'lucide-vue-next'
</script>
