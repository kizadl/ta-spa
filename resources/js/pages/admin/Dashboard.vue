<script setup lang="ts">
import { Head } from '@inertiajs/vue3';
import { route } from 'ziggy-js';
import PlaceholderPattern from '@/components/PlaceholderPattern.vue';
import { Card } from '@/components/ui/card';

defineOptions({
    layout: {
        breadcrumbs: [
            {
                title: 'Dashboard',
                href: route('admin.dashboard'),
            },
        ],
    },
});

const { user } = defineProps<{ user: User }>();
</script>

<template>
    <Head title="Dashboard" />

    <div
        class="flex h-full flex-1 flex-col gap-4 overflow-x-auto rounded-xl p-4"
    >
       <!-- card greetings -->
        <Card class="flex-1 border-border bg-card">
            <div class="flex flex-col">
                <div class="flex items-center justify-between">
                    <div>
                        <h3 class="text-base font-medium text-foreground">
                            Selamat Datang {{ user.name }} 
                        </h3>
                        <p class="text-sm text-muted-foreground">
                            ini adalah dashboard admin
                        </p>
                    </div>
                </div>
            </div>
        </Card>
    </div>
</template>
