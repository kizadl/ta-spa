<template>
  <header class="fixed top-4 left-1/2 -translate-x-1/2 z-50 w-[calc(100%-2rem)] max-w-3xl">
    <nav
      class="relative flex items-center justify-between px-4 py-3 rounded-full bg-zinc-900/40 backdrop-blur-md border border-zinc-800"
    >
      <!-- Logo -->
      <a href="#" class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-emerald-500 flex items-center justify-center">
          <span class="text-zinc-950 font-bold text-sm">GB</span>
        </div>
        <span class="font-semibold text-white hidden sm:block">GREENS</span>
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
        <div v-if="user">
          <Link
            href="/dashboard"
            class="px-4 py-2 text-sm text-zinc-400 hover:text-white hover:bg-zinc-800 rounded-lg transition-colors"
          >
            Dashboard
          </Link>
          <Link
            class="shimmer-btn bg-red-500 text-zinc-950 hover:bg-red-400 rounded-full px-4 py-2 text-sm font-bold shadow-lg shadow-emerald-500/20 transition-all active:scale-95 inline-flex items-center"
            :href="route('logout')"
            method="post"
            @click="handleLogout"
          >
            <LogOut class="mr-2 h-4 w-4" />
            Log out
          </Link>
        </div>
        <div v-else>
          <Link
            href="/login"
            class="px-4 py-2 text-sm text-zinc-400 hover:text-white hover:bg-zinc-800 rounded-lg transition-colors"
          >
            Masuk
          </Link>
          <Link
            href="/register"
            class="shimmer-btn bg-emerald-500 text-zinc-950 hover:bg-emerald-400 rounded-full px-4 py-2 text-sm font-bold shadow-lg shadow-emerald-500/20 transition-all active:scale-95"
          >
            Daftar
          </Link>
        </div>
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
          <Link href="/login" class="px-4 py-3 text-sm text-zinc-400 hover:text-white hover:bg-zinc-800 rounded-lg transition-colors text-left" @click="mobileMenuOpen = false">
            Masuk
          </Link>
          <Link
            href="/register"
            class="shimmer-btn bg-emerald-500 text-zinc-950 hover:bg-emerald-400 rounded-full px-4 py-3 text-sm font-bold text-center shadow-lg shadow-emerald-500/20"
            @click="mobileMenuOpen = false"
          >
            Daftar
          </Link>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { Link, usePage, router } from '@inertiajs/vue3'
import { LogOut, Menu, X } from 'lucide-vue-next'
import { route } from 'ziggy-js';

const page = usePage()
const user = computed(() => page.props.auth?.user)

const navItems = [
  { label: 'Klasifikasi', href: '#klasifikasi' },
  { label: 'Keunggulan', href: '#keunggulan' },
  { label: 'Teknologi', href: '#technology' },
  { label: 'F.A.Q', href: '#faq' },
]

const handleLogout = () => {
  router.flushAll();
};

const hoveredIndex = ref<number | null>(null)
const mobileMenuOpen = ref(false)
</script>
