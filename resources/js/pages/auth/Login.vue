<script setup lang="ts">
import { Form, Head } from '@inertiajs/vue3';
import { route } from 'ziggy-js';
import InputError from '@/components/InputError.vue';
import PasswordInput from '@/components/PasswordInput.vue';
import TextLink from '@/components/TextLink.vue';
import { Button } from '@/components/ui/button';
import { Checkbox } from '@/components/ui/checkbox';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Spinner } from '@/components/ui/spinner';

defineOptions({
    layout: {
        title: 'Masuk ke Akun Anda',
        description: 'Masukkan email dan kata sandi Anda di bawah ini',
    },
});

defineProps<{
    status?: string;
    canResetPassword: boolean;
    canRegister: boolean;
}>();
</script>

<template>
    <Head title="Masuk" />

    <div
        v-if="status"
        class="mb-4 text-center text-sm font-medium text-emerald-500"
    >
        {{ status }}
    </div>

    <Form
        :action="route('login')" method="post"
        :reset-on-success="['password']"
        v-slot="{ errors, processing }"
        class="flex flex-col gap-6"
    >
        <div class="grid gap-6">
            <div class="grid gap-2">
                <Label for="email" class="text-zinc-300">Alamat Email</Label>
                <Input
                    id="email"
                    type="email"
                    name="email"
                    required
                    autofocus
                    :tabindex="1"
                    autocomplete="email"
                    placeholder="email@contoh.com"
                    class="bg-zinc-950 border-zinc-800 text-white placeholder:text-zinc-600 focus-visible:ring-emerald-500"
                />
                <InputError :message="errors.email" />
            </div>

            <div class="grid gap-2">
                <div class="flex items-center justify-between">
                    <Label for="password" class="text-zinc-300">Kata Sandi</Label>
                    <TextLink
                        v-if="canResetPassword"
                        :href="route('password.request')"
                        class="text-sm text-emerald-500 hover:text-emerald-400"
                        :tabindex="5"
                    >
                        Lupa kata sandi?
                    </TextLink>
                </div>
                <PasswordInput
                    id="password"
                    name="password"
                    required
                    :tabindex="2"
                    autocomplete="current-password"
                    placeholder="Kata Sandi"
                    class="bg-zinc-950 border-zinc-800 text-white placeholder:text-zinc-600 focus-visible:ring-emerald-500"
                />
                <InputError :message="errors.password" />
            </div>

            <div class="flex items-center justify-between">
                <Label for="remember" class="flex items-center space-x-3 text-zinc-300 cursor-pointer">
                    <Checkbox id="remember" name="remember" :tabindex="3" class="border-zinc-600 data-[state=checked]:bg-emerald-500 data-[state=checked]:border-emerald-500 data-[state=checked]:text-zinc-950" />
                    <span class="text-sm">Ingat saya</span>
                </Label>
            </div>

            <Button
                type="submit"
                class="mt-4 w-full bg-emerald-500 text-zinc-950 hover:bg-emerald-400 font-bold transition-all"
                :tabindex="4"
                :disabled="processing"
                data-test="login-button"
            >
                <Spinner v-if="processing" class="mr-2" />
                Masuk
            </Button>
        </div>

        <div
            class="text-center text-sm text-zinc-400"
            v-if="canRegister"
        >
            Belum punya akun?
            <TextLink :href="route('register')" :tabindex="5" class="text-emerald-500 hover:text-emerald-400 font-medium ml-1">Daftar sekarang</TextLink>
        </div>
    </Form>
</template>
