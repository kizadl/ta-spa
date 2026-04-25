<template>
  <section class="py-16 overflow-hidden">
    <div class="text-center mb-10">
      <p class="text-sm text-zinc-500 uppercase tracking-wider font-medium">Trusted by industry leaders</p>
    </div>

    <div class="relative">
      <!-- Fade masks -->
      <div
        class="absolute left-0 top-0 bottom-0 w-32 bg-gradient-to-r from-zinc-950 to-transparent z-10 pointer-events-none"
      />
      <div
        class="absolute right-0 top-0 bottom-0 w-32 bg-gradient-to-l from-zinc-950 to-transparent z-10 pointer-events-none"
      />

      <!-- Marquee container -->
      <div class="flex animate-marquee">
        <div v-for="logo in [...logos, ...logos]" :key="`${logo.name}-marquee`" class="flex items-center justify-center min-w-[160px] h-16 mx-8 grayscale opacity-50 hover:grayscale-0 hover:opacity-100 transition-all duration-300">
          <div class="flex items-center gap-2 text-zinc-400">
            <div class="w-8 h-8 rounded-lg bg-zinc-800 flex items-center justify-center">
              <span class="text-xs font-bold">{{ logo.name[0] }}</span>
            </div>
            <span class="font-medium">{{ logo.name }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const logos = [
  { name: 'Vercel', width: 100 },
  { name: 'Stripe', width: 80 },
  { name: 'Linear', width: 90 },
  { name: 'Notion', width: 100 },
  { name: 'Figma', width: 70 },
  { name: 'Slack', width: 90 },
  { name: 'Discord', width: 100 },
  { name: 'GitHub', width: 90 },
]
</script>
