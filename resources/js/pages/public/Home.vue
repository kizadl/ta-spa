<template>
  <div class="bg-background text-foreground min-h-screen">
    <Navbar />
    <Hero :total-classifications="totalClassifications" />
    <Logo />
    <Scanner  />
    <Keunggulan />
    <Teknologi />
    <FAQ />
    <FinalCta />
    <Footer/>
  </div>
</template>

<script setup lang="ts">
import Navbar from '@/components/public/Navbar.vue'
import Hero from '@/components/public/Hero.vue'
import Logo from '@/components/public/Logo.vue'
import Keunggulan from '@/components/public/Keunggulan.vue' 
import Scanner from '@/components/public/Scanner.vue'
import Teknologi from '@/components/public/Teknologi.vue' 
import FAQ from '@/components/public/FAQ.vue'
import FinalCta from '@/components/public/FinalCta.vue'

defineProps<{
  totalClassifications?: number
}>()
</script>
