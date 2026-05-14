<script setup lang="ts">
import { Head } from '@inertiajs/vue3';
import { route } from 'ziggy-js';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '@/components/ui/card';
import { User } from '@/types';
import { computed } from 'vue';

// Import untuk Chart
import { Pie } from 'vue-chartjs';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend);

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

// Terima Props dari Controller
const props = defineProps<{ 
    user: User,
    chartData: Array<{ result: string, total: number }>,
    recentHistory: Array<any>,
    totalScan: number,
    avgAccuracy: number,
    successRate: number,
    totalUser: number,
}>();

// Konfigurasi Warna & Data untuk Pie Chart
const chartConfig = computed(() => ({
    labels: props.chartData.map(item => item.result),
    datasets: [{
        backgroundColor: props.chartData.map(item => {
            switch (item.result?.toLowerCase()) {
                case 'honey': return '#f59e0b'; // Amber-500 
                case 'wash': return '#10b981'; // Blue-500 
                case 'natural': return '#713600'; // Emerald-500  
                default: return '#94a3b8'; // Slate-400
            }
        }),
        data: props.chartData.map(item => item.total),
        borderWidth: 1
    }]
}));

const getResultColorClass = (result: string) => {
    switch (result?.toLowerCase()) {
        case 'honey': return 'text-amber-600 dark:text-amber-500';
        case 'washed': return 'text-blue-600 dark:text-blue-500';
        case 'natural': return 'text-emerald-600 dark:text-emerald-500';
        default: return 'text-muted-foreground';
    }
};

const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'bottom' as const,
        }
    }
};

</script>

<template>
    <Head title="Dashboard" />

    <div class="flex h-full flex-1 flex-col gap-4 p-4 overflow-y-auto">
        
        <Card class="border-border bg-card">
            <CardHeader class="pb-3">
                <CardTitle class="text-lg font-semibold text-foreground">
                    Selamat Datang, {{ user.name }}! ☕
                </CardTitle>
                <CardDescription>
                    Anda masuk sebagai <span class="font-bold uppercase">{{ user.role }}</span>. Berikut ringkasan data klasifikasi kopi.
                </CardDescription>
            </CardHeader>
        </Card>

        <div class="grid gap-4 md:grid-cols-4">
            <Card>
                <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle class="text-sm font-medium">Total Pengguna</CardTitle>
                </CardHeader>
                <CardContent>
                    <div class="text-2xl font-bold">{{ totalUser }}</div>
                    <p class="text-xs text-muted-foreground">Akumulasi seluruh pengguna</p>
                </CardContent>
            </Card>
            
            <Card>
                <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle class="text-sm font-medium">Total Scan</CardTitle>
                </CardHeader>
                <CardContent>
                    <div class="text-2xl font-bold">{{ totalScan }}</div>
                    <p class="text-xs text-muted-foreground">Akumulasi seluruh pemindaian</p>
                </CardContent>
            </Card>

            <Card>
                <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle class="text-sm font-medium">Rata-rata Akurasi</CardTitle>
                </CardHeader>
                <CardContent>
                    <div class="text-2xl font-bold text-emerald-600">{{ avgAccuracy }}%</div>
                    <p class="text-xs text-muted-foreground">Dari klasifikasi berstatus berhasil</p>
                </CardContent>
            </Card>

            <Card>
                <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle class="text-sm font-medium">Tingkat Keberhasilan</CardTitle>
                </CardHeader>
                <CardContent>
                    <div class="text-2xl font-bold text-blue-600">{{ successRate }}%</div>
                    <p class="text-xs text-muted-foreground">Persentase status berhasil dari total scan</p>
                </CardContent>
            </Card>
        </div>

        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
            <Card class="col-span-1 lg:col-span-3">
                <CardHeader>
                    <CardTitle>Distribusi Pasca Panen</CardTitle>
                    <CardDescription>Persentase hasil klasifikasi</CardDescription>
                </CardHeader>
                <CardContent class="h-[300px]">
                    <Pie v-if="chartData.length > 0" :data="chartConfig" :options="chartOptions" />
                    <div v-else class="flex h-full items-center justify-center text-muted-foreground">
                        Belum ada data untuk ditampilkan
                    </div>
                </CardContent>
            </Card>

            <Card class="col-span-1 lg:col-span-4">
                <CardHeader>
                    <CardTitle>Riwayat Terakhir</CardTitle>
                    <CardDescription>10 pemindaian terbaru</CardDescription>
                </CardHeader>
                <CardContent>
                    <div class="relative w-full overflow-auto">
                        <table class="w-full caption-bottom text-sm">
                            <thead class="[&_tr]:border-b">
                                <tr class="border-b transition-colors hover:bg-muted/50">
                                    <th class="h-12 px-4 text-left align-middle font-medium">Tanggal</th>
                                    <th class="h-12 px-4 text-left align-middle font-medium">Hasil</th>
                                    <th class="h-12 px-4 text-left align-middle font-medium">Akurasi</th>
                                </tr>
                            </thead>
                            <tbody class="[&_tr:last-child]:border-0">
                                <tr v-for="item in recentHistory" :key="item.id" class="border-b transition-colors hover:bg-muted/50">
                                    <td class="p-4 align-middle text-muted-foreground">
                                        {{ new Date(item.created_at).toLocaleDateString('id-ID', { day: '2-digit', month: 'short' }) }}
                                    </td>
                                    <td class="p-4 align-middle font-black italic tracking-tight" :class="getResultColorClass(item.result)">
                                        {{ item.result }}
                                    </td>
                                    <td class="p-4 align-middle font-medium">{{ item.confidence }}%</td>
                                </tr>
                                <tr v-if="recentHistory.length === 0">
                                    <td colspan="3" class="p-4 text-center text-muted-foreground">Tidak ada data.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </CardContent>
            </Card>
        </div>
    </div>
</template>