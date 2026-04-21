<template>
    <Dialog :open="open" @update:open="open = $event">
        <DialogTrigger as-child>
            <Button @click="open = true">
                <UserPlus class="mr-2 h-4 w-4" />
                Tambah User
            </Button>
        </DialogTrigger>

        <DialogContent class="max-h-[90vh] overflow-y-auto">
            <DialogHeader>
                <DialogTitle>Tambah User Baru</DialogTitle>
                <DialogDescription> Masukkan data user yang ingin ditambahkan. </DialogDescription>
            </DialogHeader>

            <form @submit.prevent="submit" class="grid gap-4 py-4">
                <div class="flex flex-col gap-2">
                    <Label for="name">Nama Lengkap</Label>
                    <Input id="name" v-model="form.name" placeholder="Masukkan nama lengkap" />
                    <p v-if="form.errors.name" class="mt-1 text-sm text-red-500">
                        {{ form.errors.name }}
                    </p>
                </div>

                <div class="flex flex-col gap-2">
                    <Label for="email">Email</Label>
                    <Input id="email" v-model="form.email" type="email" placeholder="Masukkan email" />
                    <p v-if="form.errors.email" class="mt-1 text-sm text-red-500">
                        {{ form.errors.email }}
                    </p>
                </div>

                <div class="flex flex-col gap-2">
                    <Label for="password">Password</Label>
                    <div class="relative">
                        <Input id="password" :type="showPassword ? 'text' : 'password'" v-model="form.password" placeholder="Masukkan password" />
                        <Button
                            type="button"
                            variant="ghost"
                            class="absolute right-2 top-1/2 h-auto -translate-y-1/2 p-1"
                            @click="showPassword = !showPassword"
                        >
                            <Eye v-if="!showPassword" class="h-4 w-4" />
                            <EyeOff v-else class="h-4 w-4" />
                        </Button>
                    </div>
                    <p v-if="form.errors.password" class="mt-1 text-sm text-red-500">
                        {{ form.errors.password }}
                    </p>
                </div>

                <div class="flex flex-col gap-2">
                    <Label for="password_confirmation">Konfirmasi Password</Label>
                    <div class="relative">
                        <Input
                            id="password_confirmation"
                            :type="showPasswordConfirmation ? 'text' : 'password'"
                            v-model="form.password_confirmation"
                            placeholder="Konfirmasi password"
                        />
                        <Button
                            type="button"
                            variant="ghost"
                            class="absolute right-2 top-1/2 h-auto -translate-y-1/2 p-1"
                            @click="showPasswordConfirmation = !showPasswordConfirmation"
                        >
                            <Eye v-if="!showPasswordConfirmation" class="h-4 w-4" />
                            <EyeOff v-else class="h-4 w-4" />
                        </Button>
                    </div>
                    <p v-if="form.errors.password_confirmation" class="mt-1 text-sm text-red-500">
                        {{ form.errors.password_confirmation }}
                    </p>
                </div>

                <div class="mt-6 flex justify-end space-x-2">
                    <Button type="button" variant="outline" @click="open = false">Batal</Button>
                    <Button type="submit" :disabled="form.processing">
                        {{ form.processing ? 'Menyimpan...' : 'Simpan User' }}
                    </Button>
                </div>
            </form>
        </DialogContent>
    </Dialog>
</template>

<script setup lang="ts">
import { Button } from '@/components/ui/button';
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from '@/components/ui/dialog';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { MultipleSelect } from '@/components/ui/multiple-select';
import { SelectSearch } from '@/components/ui/select-search';
import { useForm } from '@inertiajs/vue3';
import { Eye, EyeOff, UserPlus } from 'lucide-vue-next';
import { computed, ref } from 'vue';

const open = ref(false);
const showPassword = ref(false);
const showPasswordConfirmation = ref(false);

const form = useForm({
    name: '',
    email: '',
    password: '',
    password_confirmation: '',
});

const submit = () => {
    form.post(route('users.store'), {
        preserveScroll: true,
        onSuccess: () => {
            form.reset();
            open.value = false;
        },
    });
};
</script>