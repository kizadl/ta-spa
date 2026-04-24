<template>
  <footer class="border-t border-zinc-800 bg-zinc-950">
    <div class="max-w-6xl mx-auto px-4 py-16">
      <div class="grid grid-cols-2 md:grid-cols-5 gap-8">
        <!-- Brand -->
        <div class="col-span-2 md:col-span-2">
          <a href="#" class="flex items-center gap-2 mb-4">
            <div class="w-8 h-8 rounded-lg bg-emerald-500 flex items-center justify-center">
              <span class="text-zinc-950 font-bold text-sm">GB</span>
            </div>
            <span class="font-semibold text-white">Greens</span>
          </a>
          <p class="text-sm text-zinc-500 mb-4 max-w-xs">Platform cerdas yang ditenagai oleh kecerdasan buatan untuk membantu Anda mengklasifikasikan proses pasca-panen biji kopi Arabika dengan akurat.</p>
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-zinc-900 border border-zinc-800">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            <span class="text-xs text-zinc-400">Model AI Aktif & Berjalan</span>
          </div>
        </div>

        <!-- Links -->
        <div v-for="(links, title) in footerLinks" :key="title">
          <h4 class="text-sm font-semibold text-white mb-4">{{ title }}</h4>
          <ul class="space-y-3">
            <li v-for="link in links" :key="link.label">
              <a :href="link.href" class="text-sm text-zinc-500 hover:text-white transition-colors">
                {{ link.label }}
              </a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Bottom -->
      <div
        class="mt-16 pt-8 border-t border-zinc-800 flex flex-col sm:flex-row items-center justify-between gap-4"
      >
        <p class="text-sm text-zinc-500">&copy; {{ new Date().getFullYear() }} Greens. Hak Cipta Dilindungi.</p>
        <div class="flex items-center gap-6">
          <a href="#" class="text-sm text-zinc-500 hover:text-white transition-colors">Instagram</a>
          <a href="#" class="text-sm text-zinc-500 hover:text-white transition-colors">GitHub</a>
          <a href="#" class="text-sm text-zinc-500 hover:text-white transition-colors">Youtube</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
const footerLinks = {
  Navigasi: [
    { label: 'Beranda', href: '#' },
    { label: 'Klasifikasi', href: '#klasifikasi' },
    { label: 'Keunggulan', href: '#keunggulan' },
    { label: 'Teknologi', href: '#technology' },
  ],
  Bantuan: [
    { label: 'Panduan Pengguna', href: '#' },
    { label: 'F.A.Q', href: '#faq' },
    { label: 'Hubungi Kami', href: '#' },
    { label: 'Komunitas', href: '#' },
  ],
  Legal: [
    { label: 'Kebijakan Privasi', href: '#' },
    { label: 'Syarat Ketentuan', href: '#' },
    { label: 'Keamanan', href: '#' },
    { label: 'Lisensi', href: '#' },
  ],
}
</script>
