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
    totalScan: number
}>();

// Konfigurasi Warna & Data untuk Pie Chart
const chartConfig = computed(() => ({
    labels: props.chartData.map(item => item.result),
    datasets: [{
        backgroundColor: ['#eab308', '#22c55e', '#3b82f6'], // Honey (Yellow), Natural (Green), Washed (Blue)
        data: props.chartData.map(item => item.total),
        borderWidth: 1
    }]
}));

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

        <div class="grid gap-4 md:grid-cols-3">
            <Card>
                <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle class="text-sm font-medium">Total Scan</CardTitle>
                </CardHeader>
                <CardContent>
                    <div class="text-2xl font-bold">{{ totalScan }}</div>
                    <p class="text-xs text-muted-foreground">Akumulasi seluruh pemindaian</p>
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
                                    <td class="p-4 align-middle">
                                        {{ new Date(item.created_at).toLocaleDateString('id-ID') }}
                                    </td>
                                    <td class="p-4 align-middle font-medium uppercase">{{ item.result }}</td>
                                    <td class="p-4 align-middle">{{ item.confidence }}%</td>
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