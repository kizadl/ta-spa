<template>
  <div class="bg-background text-foreground min-h-screen">
    <Navbar />
    <Hero />
    <LogoMarquee />
    <BentoGrid />
    <Kelebihan />
    <Pricing />
    <FAQ />
    <FinalCta />
    <Footer/>
  </div>
</template>

<script setup lang="ts">
import Navbar from '@/components/public/Navbar.vue'
import Hero from '@/components/public/Hero.vue'
import LogoMarquee from '@/components/public/LogoMarquee.vue'
import Kelebihan from '@/components/public/kelebihan.vue'
import BentoGrid from '@/components/public/BentoGrid.vue'
import Pricing from '@/components/public/Pricing.vue'
import FAQ from '@/components/public/FAQ.vue'
import FinalCta from '@/components/public/FinalCta.vue'
</script>
