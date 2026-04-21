<template>
  <footer class="border-t border-zinc-800 bg-zinc-950">
    <div class="max-w-6xl mx-auto px-4 py-16">
      <div class="grid grid-cols-2 md:grid-cols-5 gap-8">
        <!-- Brand -->
        <div class="col-span-2 md:col-span-1">
          <a href="#" class="flex items-center gap-2 mb-4">
            <div class="w-8 h-8 rounded-lg bg-white flex items-center justify-center">
              <span class="text-zinc-950 font-bold text-sm">A</span>
            </div>
            <span class="font-semibold text-white">Apex</span>
          </a>
          <p class="text-sm text-zinc-500 mb-4">The modern platform for teams who ship fast.</p>
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-zinc-900 border border-zinc-800">
            <span class="w-2 h-2 rounded-full bg-emerald-500 pulse-glow" />
            <span class="text-xs text-zinc-400">All Systems Operational</span>
          </div>
        </div>

        <!-- Links -->
        <div v-for="(links, title) in footerLinks" :key="title">
          <h4 class="text-sm font-semibold text-white mb-4">{{ title }}</h4>
          <ul class="space-y-3">
            <li v-for="link in links" :key="link">
              <a href="#" class="text-sm text-zinc-500 hover:text-white transition-colors">
                {{ link }}
              </a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Bottom -->
      <div
        class="mt-16 pt-8 border-t border-zinc-800 flex flex-col sm:flex-row items-center justify-between gap-4"
      >
        <p class="text-sm text-zinc-500">&copy; {{ new Date().getFullYear() }} Apex, Inc. All rights reserved.</p>
        <div class="flex items-center gap-6">
          <a href="#" class="text-sm text-zinc-500 hover:text-white transition-colors">Twitter</a>
          <a href="#" class="text-sm text-zinc-500 hover:text-white transition-colors">GitHub</a>
          <a href="#" class="text-sm text-zinc-500 hover:text-white transition-colors">Discord</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
const footerLinks: Record<string, string[]> = {
  Product: ['Features', 'Pricing', 'Changelog', 'Roadmap', 'API'],
  Resources: ['Documentation', 'Guides', 'Blog', 'Community', 'Templates'],
  Company: ['About', 'Careers', 'Press', 'Partners', 'Contact'],
  Legal: ['Privacy', 'Terms', 'Security', 'Cookies', 'Licenses'],
}
</script>
