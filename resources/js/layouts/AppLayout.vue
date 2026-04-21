<script setup lang="ts">
import AppLayout from '@/layouts/app/AppSidebarLayout.vue';
import Notification from './Notification.vue';
import type { BreadcrumbItem } from '@/types';

const { breadcrumbs = [] } = defineProps<{
    breadcrumbs?: BreadcrumbItem[];
}>();
</script>

<template>
    <AppLayout :breadcrumbs="breadcrumbs">
        <slot />
        <Notification />
    </AppLayout>
</template>
