<script setup lang="ts">
import { Link } from '@inertiajs/vue3';
import { route } from 'ziggy-js';

defineProps<{
    title?: string;
    description?: string;
}>();
</script>

<template>
    <div
        class="flex min-h-svh flex-col items-center justify-center gap-6 bg-black p-6 md:p-10 text-white"
    >
        <div class="w-full max-w-sm">
            <div class="flex flex-col gap-8">
                <div class="flex flex-col items-center gap-4">
                    <Link
                        :href="route('home')"
                        class="flex flex-col items-center gap-2 font-medium"
                    >
                        <div
                            class="mb-1 flex h-12 w-12 items-center justify-center rounded-xl bg-emerald-500 shadow-lg shadow-emerald-500/20"
                        >
                            <span class="text-zinc-950 font-bold text-xl">GB</span>
                        </div>
                        <span class="font-semibold text-white text-xl tracking-wider">GREENS</span>
                        <span class="sr-only">{{ title }}</span>
                    </Link>
                    <div class="space-y-2 text-center mt-4">
                        <h1 class="text-2xl font-bold">{{ title }}</h1>
                        <p class="text-center text-sm text-zinc-400">
                            {{ description }}
                        </p>
                    </div>
                </div>
                <div class="bg-zinc-900 border border-zinc-800 p-8 rounded-3xl shadow-2xl">
                    <slot />
                </div>
            </div>
        </div>
    </div>
</template>
