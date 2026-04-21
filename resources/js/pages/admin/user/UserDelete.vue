<template>
    <Dialog :open="open" @update:open="open = $event">
        <DialogTrigger as-child>
            <Button variant="default" size="sm" @click="open = true" class="bg-red-600 hover:bg-red-700 text-white">
                <Trash2 class="mr-2 h-4 w-4" />
                Hapus
            </Button>
        </DialogTrigger>

        <DialogContent>
            <DialogHeader>
                <DialogTitle>Konfirmasi Hapus</DialogTitle>
                <DialogDescription> Apakah Anda yakin ingin menghapus user "{{ userName }}"? Tindakan ini tidak dapat dibatalkan. </DialogDescription>
            </DialogHeader>

            <DialogFooter>
                <Button variant="outline" @click="open = false">Batal</Button>
                <Button variant="default" @click="deleteUser" :disabled="isDeleting" class="bg-red-600 hover:bg-red-700 text-white">
                    {{ isDeleting ? 'Menghapus...' : 'Hapus' }}
                </Button>
            </DialogFooter>
        </DialogContent>
    </Dialog>
</template>

<script setup lang="ts">
import { Button } from '@/components/ui/button';
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from '@/components/ui/dialog';
import { router } from '@inertiajs/vue3';
import { Trash2 } from 'lucide-vue-next';
import { ref } from 'vue';

const open = ref(false);
const isDeleting = ref(false);

const props = defineProps<{
    userId: number;
    userName: string;
}>();

const deleteUser = () => {
    isDeleting.value = true;

    router.delete(route('admin.users.destroy', props.userId), {
        preserveScroll: true,
        onSuccess: () => {
            open.value = false;
            isDeleting.value = false;
        },
        onError: () => {
            isDeleting.value = false;
        },
    });
};
</script>