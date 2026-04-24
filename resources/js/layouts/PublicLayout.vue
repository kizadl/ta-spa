<script setup lang="ts">
import Navbar from '@/components/public/Navbar.vue';
import Footer from '@/components/public/Footer.vue';
import Notification from '@/layouts/Notification.vue';
</script>

<template>
    <div class="min-h-screen bg-background flex flex-col font-sans">
        <Navbar />
        <main class="flex-grow">
            <slot />
        </main>
        <Footer />
        <Notification />
    </div>
</template>
