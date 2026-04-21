export interface User {
    id: number;
    name: string;
    email: string;
    avatar?: string;
    email_verified_at: string | null;
    created_at: string;
    updated_at: string;
}

export interface BreadcrumbItem {
    title: string;
    href: string;
}

export interface NavItem {
    title: string;
    href: string;
    icon?: any;
    current?: boolean;
}

export type AppVariant = 'default' | 'sidebar' | 'topbar' | 'header';

export type Appearance = 'light' | 'dark' | 'system';
export type ResolvedAppearance = 'light' | 'dark';

export interface TwoFactorConfigContent {
    enabled?: boolean;
    recoveryCodes?: string[];
    qrCode?: string;
    secretKey?: string;
    title?: string;
    description?: string;
    buttonText?: string;
}

export interface FlashToast {
    message: string;
    type: 'success' | 'error' | 'info' | 'warning';
}

export interface PageProps {
    auth: {
        user: User;
    };
    [key: string]: any;
}

// Extend inertia vue 3 page props
declare module '@inertiajs/core' {
    interface PageProps {
        auth: {
            user: User;
        };
        [key: string]: any;
    }
}
