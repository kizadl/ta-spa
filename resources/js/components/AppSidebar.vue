<script setup lang="ts">
import { Link, usePage } from '@inertiajs/vue3';
import { computed } from 'vue';
import { route } from 'ziggy-js';
import { BookOpen, FolderGit2, LayoutGrid, Users, ScanSearch } from 'lucide-vue-next';
import AppLogo from '@/components/AppLogo.vue';
import NavFooter from '@/components/NavFooter.vue';
import NavMain from '@/components/NavMain.vue';
import NavUser from '@/components/NavUser.vue';

import {
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarHeader,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
} from '@/components/ui/sidebar';
import type { NavItem } from '@/types';

const page = usePage();
// Ambil data user dari auth yang dikirim via HandleInertiaRequests
const user = computed(() => page.props.auth.user);

    const adminNavItems: NavItem[] = [
    {
        title: 'Dashboard',
        href: route('admin.dashboard'),
        icon: LayoutGrid,
    },
    {
        title: 'Users Management',
        href: route('admin.users.index'),
        icon: Users,
    },
    {
        title: 'History Klasifikasi',
        href: route('admin.classifications.index'),
        icon: ScanSearch,
    },
];

const userNavItems: NavItem[] = [
    {
        title: 'Dashboard',
        href: route('dashboard'),
        icon: LayoutGrid,
    },
    {
        title: 'Klasifikasi',
        href: route('classifications.index'),
        icon: ScanSearch,
    },
];


const navItems = computed(() => {
    if (user.value?.role === 'admin') {
        return adminNavItems;
    } else {
        return userNavItems;
    }
});

// 2. Filter menu berdasarkan role user yang sedang login
// const filteredNavItems = computed(() => {
//     return allNavItems.filter(item => {
//         // Jika menu tidak punya batasan role, tampilkan untuk semua
//         if (!item.role) return true;
//         // Jika ada batasan role, cek apakah role user cocok (admin === admin)
//         return item.role === user.value?.role;
//     });
// });

const footerNavItems: NavItem[] = [
    {
        title: 'Repository',
        href: 'https://github.com/laravel/vue-starter-kit',
        icon: FolderGit2,
    },
    {
        title: 'Documentation',
        href: 'https://laravel.com/docs/starter-kits#vue',
        icon: BookOpen,
    },
];
</script>

<template>
    <Sidebar collapsible="icon" variant="inset">
        <SidebarHeader>
            <SidebarMenu>
                <SidebarMenuItem>
                    <SidebarMenuButton size="lg" as-child>
                        <Link :href="route('admin.dashboard')">
                            <AppLogo />
                        </Link>
                    </SidebarMenuButton>
                </SidebarMenuItem>
            </SidebarMenu>
        </SidebarHeader>

        <SidebarContent>
            <NavMain :items="navItems" />
        </SidebarContent>

        <SidebarFooter>
            <NavFooter :items="footerNavItems" />
            <NavUser />
        </SidebarFooter>
    </Sidebar>
    <slot />
</template>