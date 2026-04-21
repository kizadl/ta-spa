<template>
  <div class="bg-background text-foreground min-h-screen">
    <Navbar />
    <Hero />
    <LogoMarquee />
    <BentoGrid />
    <Pricing />
    <FinalCta />
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Navbar from '@/components/public/Navbar.vue'
import Hero from '@/components/public/Hero.vue'
import LogoMarquee from '@/components/public/LogoMarquee.vue'
import BentoGrid from '@/components/public/BentoGrid.vue'
import Pricing from '@/components/public/Pricing.vue'
import FinalCta from '@/components/public/FinalCta.vue'
import Footer from '@/components/public/Footer.vue'
</script>
