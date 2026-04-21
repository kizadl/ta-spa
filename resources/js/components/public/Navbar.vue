<template>
  <header class="fixed top-4 left-1/2 -translate-x-1/2 z-50 w-[calc(100%-2rem)] max-w-3xl">
    <nav
      class="relative flex items-center justify-between px-4 py-3 rounded-full bg-zinc-900/40 backdrop-blur-md border border-zinc-800"
    >
      <!-- Logo -->
      <a href="#" class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-white flex items-center justify-center">
          <span class="text-zinc-950 font-bold text-sm">A</span>
        </div>
        <span class="font-semibold text-white hidden sm:block">Apex</span>
      </a>

      <!-- Desktop Nav Items -->
      <div class="hidden md:flex items-center gap-1 relative">
        <a
          v-for="(item, index) in navItems"
          :key="item.label"
          :href="item.href"
          class="relative px-4 py-2 text-sm text-zinc-400 hover:text-white transition-colors"
          @mouseenter="hoveredIndex = index"
          @mouseleave="hoveredIndex = null"
        >
          <div
            v-if="hoveredIndex === index"
            class="absolute inset-0 bg-zinc-800 rounded-full"
          />
          <span class="relative z-10">{{ item.label }}</span>
        </a>
      </div>

      <!-- CTA Buttons -->
      <div class="hidden md:flex items-center gap-3">
        <button
          class="px-4 py-2 text-sm text-zinc-400 hover:text-white hover:bg-zinc-800 rounded-lg transition-colors"
        >
          Sign In
        </button>
        <button
          class="shimmer-btn bg-white text-zinc-950 hover:bg-zinc-200 rounded-full px-4 py-2 text-sm font-medium"
        >
          Get Started
        </button>
      </div>

      <!-- Mobile Menu Button -->
      <button
        class="md:hidden p-2 text-zinc-400 hover:text-white"
        @click="mobileMenuOpen = !mobileMenuOpen"
        :aria-label="mobileMenuOpen ? 'Close menu' : 'Open menu'"
      >
        <Menu v-if="!mobileMenuOpen" :size="20" />
        <X v-else :size="20" />
      </button>

      <!-- Mobile Menu -->
      <div
        v-if="mobileMenuOpen"
        class="absolute top-full left-0 right-0 mt-2 p-4 rounded-2xl bg-zinc-900/95 backdrop-blur-md border border-zinc-800"
      >
        <div class="flex flex-col gap-2">
          <a
            v-for="item in navItems"
            :key="item.label"
            :href="item.href"
            class="px-4 py-3 text-sm text-zinc-400 hover:text-white hover:bg-zinc-800 rounded-lg transition-colors"
            @click="mobileMenuOpen = false"
          >
            {{ item.label }}
          </a>
          <hr class="border-zinc-800 my-2" />
          <button class="px-4 py-3 text-sm text-zinc-400 hover:text-white hover:bg-zinc-800 rounded-lg transition-colors text-left">
            Sign In
          </button>
          <button
            class="shimmer-btn bg-white text-zinc-950 hover:bg-zinc-200 rounded-full px-4 py-2 text-sm font-medium w-full"
          >
            Get Started
          </button>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Menu, X } from 'lucide-vue-next'

const navItems = [
  { label: 'Features', href: '#features' },
  { label: 'Pricing', href: '#pricing' },
  { label: 'Docs', href: '#docs' },
  { label: 'Blog', href: '#blog' },
]

const hoveredIndex = ref<number | null>(null)
const mobileMenuOpen = ref(false)
</script>
