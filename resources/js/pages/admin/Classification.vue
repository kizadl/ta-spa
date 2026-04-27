<script setup lang="ts">
import { Head } from '@inertiajs/vue3';
import { route } from 'ziggy-js';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import {
    Pagination,
    PaginationEllipsis,
    PaginationFirst,
    PaginationLast,
    PaginationContent,
    PaginationItem,
    PaginationNext,
    PaginationPrevious,
} from '@/components/ui/pagination';
import { Button } from '@/components/ui/button';
import { router } from '@inertiajs/vue3';
import { Trash2, Eye } from 'lucide-vue-next';
import { ref } from 'vue';
import {
    Dialog,
    DialogContent,
    DialogHeader,
    DialogTitle,
} from '@/components/ui/dialog';

defineOptions({
    layout: {
        breadcrumbs: [
            {
                title: 'History Klasifikasi',
                href: route('admin.classifications.index'),
            },
        ],
    },
});

const props = defineProps({
    classifications: Object,
});

const isViewDialogOpen = ref(false);
const selectedImage = ref('');

const viewImage = (path: string) => {
    selectedImage.value = '/storage/' + path;
    isViewDialogOpen.value = true;
};

const changePage = (page: number) => {
    router.visit(route('admin.classifications.index', { page }), {
        preserveScroll: true,
    });
};

const deleteClassification = (id: number) => {
    if (confirm('Apakah Anda yakin ingin menghapus history ini?')) {
        router.delete(route('admin.classifications.destroy', id), {
            preserveScroll: true,
        });
    }
};

const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleString('id-ID', {
        day: '2-digit',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
    });
};

const getResultColor = (result: string) => {
    switch (result?.toLowerCase()) {
        case 'honey':
            return 'bg-amber-100 text-amber-800 border-amber-200';
        case 'washed':
            return 'bg-blue-100 text-blue-800 border-blue-200';
        case 'natural':
            return 'bg-emerald-100 text-emerald-800 border-emerald-200';
        default:
            return 'bg-primary/10 text-primary border-primary/20';
    }
};
</script>

<template>
    <Head title="History Klasifikasi" />

    <div class="flex h-full flex-1 flex-col gap-4 overflow-x-auto rounded-xl p-4">
        <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
            <div>
                <h1 class="text-2xl font-bold tracking-tight">History Klasifikasi</h1>
                <p class="text-muted-foreground">Daftar semua hasil klasifikasi yang dilakukan oleh pengguna maupun tamu.</p>
            </div>
        </div>

        <div class="rounded-md border">
            <Table>
                <TableHeader>
                    <TableRow>
                        <TableHead>Waktu</TableHead>
                        <TableHead>User Pembuat</TableHead>
                        <TableHead>Hasil</TableHead>
                        <TableHead>Confidence</TableHead>
                        <TableHead>Status</TableHead>
                        <TableHead class="text-center">Aksi</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    <TableRow v-if="!props.classifications?.data?.length">
                        <TableCell colspan="6" class="h-24 text-center">Tidak ada data klasifikasi.</TableCell>
                    </TableRow>
                    <TableRow v-for="item in props.classifications?.data" :key="item.id" class="hover:bg-muted/50">
                        <TableCell>{{ formatDate(item.created_at) }}</TableCell>
                        <TableCell>
                            <div class="font-medium">
                                {{ item.user ? item.user.name : 'Guess' }}
                            </div>
                            <div v-if="item.user" class="text-xs text-muted-foreground">
                                {{ item.user.email }}
                            </div>
                        </TableCell>
                        <TableCell>
                            <span :class="[
                                'inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium border',
                                getResultColor(item.result)
                            ]">
                                {{ item.result }}
                            </span>
                        </TableCell>
                        <TableCell>{{ item.confidence }}%</TableCell>
                        <TableCell>
                            <span :class="[
                                'inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium',
                                item.status === 'Berhasil' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                            ]">
                                {{ item.status }}
                            </span>
                        </TableCell>
                        <TableCell>
                            <div class="flex items-center justify-center gap-2">
                                <Button variant="ghost" size="icon" @click="viewImage(item.image_path)" v-if="item.image_path" title="Lihat Foto">
                                    <Eye class="h-4 w-4 text-blue-500" />
                                </Button>
                                <Button variant="ghost" size="icon" @click="deleteClassification(item.id)" title="Hapus">
                                    <Trash2 class="h-4 w-4 text-red-500" />
                                </Button>
                            </div>
                        </TableCell>
                    </TableRow>
                </TableBody>
            </Table>
        </div>

        <!-- Pagination -->
        <div v-if="classifications && classifications.last_page > 1" class="flex justify-center mt-4">
            <Pagination v-slot="{ page }" :items-per-page="classifications.per_page" :total="classifications.total" :default-page="classifications.current_page">
                <PaginationContent v-slot="{ items }" class="flex items-center gap-1">
                    <PaginationFirst @click="changePage(1)" />
                    <PaginationPrevious @click="changePage(classifications.current_page - 1)" />

                    <template v-for="(item, index) in items">
                        <PaginationItem v-if="item.type === 'page'" :key="index" :value="item.value" as-child>
                            <Button
                                class="h-9 w-9 p-0"
                                :variant="item.value === classifications.current_page ? 'default' : 'outline'"
                                @click="changePage(item.value)"
                            >
                                {{ item.value }}
                            </Button>
                        </PaginationItem>
                        <PaginationEllipsis v-else :key="item.type" :index="index" />
                    </template>

                    <PaginationNext @click="changePage(classifications.current_page + 1)" />
                    <PaginationLast @click="changePage(classifications.last_page)" />
                </PaginationContent>
            </Pagination>
        </div>

        <!-- View Photo Dialog -->
        <Dialog :open="isViewDialogOpen" @update:open="isViewDialogOpen = $event">
            <DialogContent class="max-w-3xl rounded-3xl overflow-hidden p-0">
                <DialogHeader class="p-6 pb-0">
                    <DialogTitle>Detail Foto Klasifikasi</DialogTitle>
                </DialogHeader>
                <div class="p-6">
                    <div class="aspect-video rounded-2xl overflow-hidden bg-muted flex items-center justify-center border">
                        <img :src="selectedImage" class="w-full h-full object-contain" alt="Classification result" loading="lazy" />
                    </div>
                </div>
            </DialogContent>
        </Dialog>
    </div>
</template>
