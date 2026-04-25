<script setup lang="ts">
import AppLayout from '@/layouts/app/AppSidebarLayout.vue';
import Notification from './Notification.vue';
import type { BreadcrumbItem } from '@/types';
import { usePage } from '@inertiajs/vue3';
import { computed } from 'vue';

const { breadcrumbs = [] } = defineProps<{
    breadcrumbs?: BreadcrumbItem[];
}>();

// Mengambil data user untuk keperluan pengecekan role jika dibutuhkan di level ini
const page = usePage();
const user = computed(() => page.props.auth.user);
</script>

<template>
    <AppLayout :breadcrumbs="breadcrumbs">
        <slot />
        <Notification />
    </AppLayout>
</template>