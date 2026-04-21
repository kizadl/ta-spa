<script setup lang="ts">
import { Head } from '@inertiajs/vue3';
import { route } from 'ziggy-js';
import PlaceholderPattern from '@/components/PlaceholderPattern.vue';
import UserCreate from './UserCreate.vue';
import UserEdit from './UserEdit.vue';
import UserDelete from './UserDelete.vue';

defineOptions({
    layout: {
        breadcrumbs: [
            {
                title: 'User',
                href: route('admin.users.index'),
            },
        ],
    },
});

const props = defineProps({
    users: Object,
});

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
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { ref } from 'vue';
import { router } from '@inertiajs/vue3';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import { KeyIcon } from 'lucide-vue-next';
// Note: UserCreate, UserEdit, UserDelete are not imported yet. Add them if you have them.

const search = ref('');
const sortField = ref('id');
const sortOrder = ref('asc');

const sortBy = (field: string) => {
    if (sortField.value === field) {
        sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc';
    } else {
        sortField.value = field;
        sortOrder.value = 'asc';
    }
    // Implement sort logic/router visit here
};

const changePage = (page: number) => {
    // Implement change page logic/router visit here
};

</script>

<template>
    <Head title="Dashboard" />

    <div
        class="flex h-full flex-1 flex-col gap-4 overflow-x-auto rounded-xl p-4"
    >
        <!-- Header Section -->
            <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
                <div>
                    <h1 class="text-2xl font-bold tracking-tight">User Management</h1>
                    <p class="text-muted-foreground">Kelola data pengguna sistem</p>
                </div>
                <div class="flex gap-2">
                    <UserCreate />
                </div>
            </div>

            <!-- Search and Filter Section -->
            <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
                <div class="flex flex-1 gap-2">
                    <Input v-model="search" placeholder="Cari nama atau email pengguna..." class="max-w-sm" />
                </div>
            </div>

            <!-- Table Section -->
            <div class="rounded-md border">
                <Table>
                    <TableHeader>
                        <TableRow>
                            <TableHead class="cursor-pointer" @click="sortBy('id')">
                                ID
                                <span v-if="sortField === 'id'" class="ml-1">
                                    {{ sortOrder === 'asc' ? '↑' : '↓' }}
                                </span>
                            </TableHead>
                            <TableHead class="cursor-pointer" @click="sortBy('name')">
                                Nama
                                <span v-if="sortField === 'name'" class="ml-1">
                                    {{ sortOrder === 'asc' ? '↑' : '↓' }}
                                </span>
                            </TableHead>
                            <TableHead class="cursor-pointer" @click="sortBy('email')">
                                Email
                                <span v-if="sortField === 'email'" class="ml-1">
                                    {{ sortOrder === 'asc' ? '↑' : '↓' }}
                                </span>
                            </TableHead>
                            <TableHead class="text-center">Aksi</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        <TableRow v-if="!props.users?.data?.length">
                            <TableCell colspan="8" class="h-24 text-center"> Tidak ada data pengguna. </TableCell>
                        </TableRow>
                        <TableRow v-for="user in props.users?.data" :key="user.id" class="hover:bg-muted/50">
                            <TableCell class="font-medium">{{ user.id }}</TableCell>
                            <TableCell>
                                <div class="font-medium">{{ user.name }}</div>
                            </TableCell>
                            <TableCell>{{ user.email }}</TableCell>
                            <TableCell>
                                <div class="flex items-center justify-center gap-2">
                                    <UserEdit :user="user" />
                                    <UserDelete :user-id="user.id" :user-name="user.name" />
                                </div>
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>
            </div>

            <!-- Pagination Section -->
            <div v-if="users && users.last_page > 1" class="flex justify-center">
                <Pagination v-slot="{ page }" :items-per-page="users.per_page" :total="users.total" :default-page="users.current_page">
                    <PaginationContent v-slot="{ items }" class="flex items-center gap-1">
                        <PaginationFirst @click="changePage(1)" />
                        <PaginationPrevious @click="changePage(users.current_page - 1)" />

                        <template v-for="(item, index) in items">
                            <PaginationItem v-if="item.type === 'page'" :key="index" :value="item.value" as-child>
                                <Button
                                    class="h-9 w-9 p-0"
                                    :variant="item.value === users.current_page ? 'default' : 'outline'"
                                    @click="changePage(item.value)"
                                >
                                    {{ item.value }}
                                </Button>
                            </PaginationItem>
                            <PaginationEllipsis v-else :key="item.type" :index="index" />
                        </template>

                        <PaginationNext @click="changePage(users.current_page + 1)" />
                        <PaginationLast @click="changePage(users.last_page)" />
                    </PaginationContent>
                </Pagination>
            </div>
    </div>
</template>
