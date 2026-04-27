<script setup lang="ts">
import { Head, router } from '@inertiajs/vue3';
import { Button } from '@/components/ui/button';
import { Trash2, Plus, History, ScanSearch, Calendar, AlertCircle } from 'lucide-vue-next';
import Scanner from '@/components/public/Scanner.vue';
import { ref } from 'vue';
import { route } from 'ziggy-js';
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
} from '@/components/ui/dialog';

defineOptions({
    layout: {
        breadcrumbs: [
            {
                title: 'Klasifikasi',
                href: route('classifications.index'),
            },
        ],
    },
});

const props = defineProps<{
    classifications: any[];
}>();

const showScanner = ref(false);
const isDeleteDialogOpen = ref(false);
const itemToDelete = ref<number | null>(null);
const isDeleting = ref(false);

const confirmDelete = (id: number) => {
    itemToDelete.value = id;
    isDeleteDialogOpen.value = true;
};

const deleteClassification = () => {
    if (!itemToDelete.value) return;
    
    isDeleting.value = true;
    router.delete(route('classifications.destroy', itemToDelete.value), {
        preserveScroll: true,
        onSuccess: () => {
            isDeleteDialogOpen.value = false;
            itemToDelete.value = null;
        },
        onFinish: () => {
            isDeleting.value = false;
        }
    });
};


const toggleScanner = () => {
    showScanner.value = !showScanner.value;
    if (!showScanner.value) {
        // Refresh data saat menutup scanner jika ada data baru
        router.reload({ only: ['classifications'] });
    }
};

</script>

<template>
    <Head title="Klasifikasi Kopi" />

    <div class="flex h-full flex-1 flex-col gap-8 rounded-xl p-4 md:p-8 overflow-x-hidden">
        <!-- Header Section -->
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
            <div>
                <h1 class="text-3xl font-bold tracking-tight flex items-center gap-3">
                    <History class="w-8 h-8 text-emerald-500" />
                    Riwayat Klasifikasi
                </h1>
                <p class="text-muted-foreground mt-1">Kelola dan lihat hasil analisis biji kopi Anda.</p>
            </div>
            <Button 
                @click="toggleScanner" 
                :variant="showScanner ? 'outline' : 'default'"
                class="w-full sm:w-auto h-12 px-6 rounded-xl font-bold shadow-lg shadow-emerald-500/20 transition-all active:scale-95"
            >
                <template v-if="!showScanner">
                    <Plus class="mr-2 h-5 w-5" />
                    Klasifikasi Baru
                </template>
                <template v-else>
                    Tutup Scanner
                </template>
            </Button>
        </div>

        <!-- Scanner Section -->
        <transition
            enter-active-class="transition duration-300 ease-out"
            enter-from-class="transform -translate-y-4 opacity-0"
            enter-to-class="transform translate-y-0 opacity-100"
            leave-active-class="transition duration-200 ease-in"
            leave-from-class="transform translate-y-0 opacity-100"
            leave-to-class="transform -translate-y-4 opacity-0"
        >
            <div v-if="showScanner" class="mb-12 rounded-3xl overflow-hidden shadow-2xl border border-emerald-500/20">
                <Scanner />
            </div>
        </transition>

        <!-- History Grid -->
        <div v-if="classifications.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 pb-12">
            <div 
                v-for="item in classifications" 
                :key="item.id" 
                class="group relative bg-white dark:bg-zinc-900 rounded-[2rem] border border-zinc-200 dark:border-zinc-800 p-4 flex gap-5 items-center shadow-sm hover:shadow-xl hover:border-emerald-500/30 transition-all duration-300"
            >
                <!-- Small Photo Thumbnail -->
                <div class="w-24 h-24 sm:w-32 sm:h-32 rounded-2xl overflow-hidden bg-zinc-100 dark:bg-zinc-950 flex-shrink-0 relative">
                    <img 
                        :src="'/storage/' + item.image_path" 
                        class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" 
                    />
                </div>

                <!-- Info Section -->
                <div class="flex-1 min-w-0 flex flex-col justify-between py-1 pr-6">
                    <div class="flex justify-between items-start mb-2">
                        <div class="space-y-0.5">
                            <div class="flex items-center gap-2 text-[9px] font-bold text-zinc-400 uppercase tracking-widest mb-1">
                                <Calendar class="w-3 h-3" />
                                {{ new Date(item.created_at).toLocaleDateString('id-ID', { day: 'numeric', month: 'short' }) }}
                            </div>
                            <h3 class="text-xl font-black text-emerald-600 dark:text-emerald-500 italic truncate leading-none">{{ item.result }}</h3>
                            <div 
                                class="mt-2 inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider border"
                                :class="(item.status === 'Berhasil' || (!item.status && Number(item.confidence) >= 90)) 
                                    ? 'bg-emerald-50 text-emerald-600 border-emerald-200 dark:bg-emerald-950/30 dark:text-emerald-400 dark:border-emerald-800' 
                                    : 'bg-red-50 text-red-600 border-red-200 dark:bg-red-950/30 dark:text-red-400 dark:border-red-800'"
                            >
                                <div :class="['w-1.5 h-1.5 rounded-full mr-1.5', (item.status === 'Berhasil' || (!item.status && Number(item.confidence) >= 90)) ? 'bg-emerald-500' : 'bg-red-500']"></div>
                                {{ item.status || (Number(item.confidence) >= 90 ? 'Berhasil' : 'Gagal') }}
                            </div>
                        </div>
                        <div class="text-right">
                            <p class="text-[9px] font-bold text-zinc-400 uppercase tracking-widest">Confidence</p>
                            <p class="text-lg font-bold text-zinc-900 dark:text-zinc-100 leading-none mt-1">{{ Number(item.confidence).toFixed(2) }}%</p>
                        </div>
                    </div>
                    
                    <div class="space-y-2">
                        <div class="h-1.5 w-full bg-zinc-100 dark:bg-zinc-800 rounded-full overflow-hidden">
                            <div 
                                class="h-full rounded-full transition-all duration-1000"
                                :class="(item.status === 'Berhasil' || (!item.status && Number(item.confidence) >= 90)) ? 'bg-emerald-500' : 'bg-red-500'"
                                :style="{ width: item.confidence + '%' }"
                            ></div>
                        </div>
                    </div>
                </div>

                <!-- Tombol Hapus Pojok Kanan Bawah -->
                <Button 
                    variant="ghost" 
                    size="icon" 
                    @click="confirmDelete(item.id)"
                    class="absolute bottom-3 right-3 h-8 w-8 text-zinc-400 hover:text-red-500 hover:bg-red-50/50 dark:hover:bg-red-950/20 transition-colors"
                >
                    <Trash2 class="h-4 w-4" />
                </Button>
            </div>
        </div>

        <!-- Empty State -->
        <div v-else-if="!showScanner" class="text-center py-32 bg-white dark:bg-zinc-900 rounded-[2.5rem] border-2 border-dashed border-zinc-200 dark:border-zinc-800 shadow-sm mb-12">
            <div class="inline-flex p-6 rounded-3xl bg-zinc-50 dark:bg-zinc-950 mb-6">
                <ScanSearch class="w-12 h-12 text-zinc-400" />
            </div>
            <h3 class="text-xl font-bold text-zinc-900 dark:text-white mb-2">Belum ada riwayat</h3>
            <p class="text-zinc-500 dark:text-zinc-400 max-w-xs mx-auto mb-8">Anda belum pernah melakukan klasifikasi biji kopi. Mulai sekarang untuk melihat hasilnya di sini.</p>
            <Button @click="showScanner = true" class="h-12 px-8 rounded-xl font-bold">
                Mulai Klasifikasi Pertama
            </Button>
        </div>

        <!-- Delete Confirmation Dialog -->
        <Dialog :open="isDeleteDialogOpen" @update:open="isDeleteDialogOpen = $event">
            <DialogContent class="sm:max-w-[425px] rounded-3xl">
                <DialogHeader>
                    <div class="mx-auto w-12 h-12 rounded-full bg-red-100 dark:bg-red-900/30 flex items-center justify-center mb-4">
                        <AlertCircle class="w-6 h-6 text-red-600 dark:text-red-400" />
                    </div>
                    <DialogTitle class="text-center text-xl font-bold">Hapus Riwayat?</DialogTitle>
                    <DialogDescription class="text-center">
                        Tindakan ini tidak dapat dibatalkan. Riwayat klasifikasi dan foto akan dihapus secara permanen dari server kami.
                    </DialogDescription>
                </DialogHeader>
                <DialogFooter class="flex flex-col sm:flex-row gap-2 mt-4">
                    <Button variant="outline" @click="isDeleteDialogOpen = false" class="rounded-xl flex-1 h-12 font-bold">
                        Batal
                    </Button>
                    <Button 
                        variant="destructive" 
                        @click="deleteClassification" 
                        :disabled="isDeleting"
                        class="rounded-xl flex-1 h-12 font-bold"
                    >
                        {{ isDeleting ? 'Menghapus...' : 'Ya, Hapus' }}
                    </Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>
    </div>
</template>
