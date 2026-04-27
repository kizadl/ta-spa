<template>
    <Dialog v-model:open="isOpen">
        <DialogContent class="sm:max-w-sm rounded-xl text-center pt-8 pb-6 px-6">
            <!-- Icon -->
            <div class="flex justify-center mb-4">
                <component :is="type === 'success' ? CheckCircle : XCircle" :class="[
                    'w-8 h-8',
                    type === 'success' ? 'text-green-500' : 'text-red-500'
                ]" />
            </div>

            <!-- Title & Description -->
            <DialogHeader>
                <DialogTitle class="text-center text-xl font-semibold">
                    {{ type === 'success' ? 'Success!' : 'Error!' }}
                </DialogTitle>
                <DialogDescription class="text-center mt-1 text-gray-500">
                    {{ message }}
                </DialogDescription>
            </DialogHeader>
        </DialogContent>
    </Dialog>
</template>

<script setup>
import { ref, computed } from 'vue'
import { usePage } from '@inertiajs/vue3'
import {
    Dialog,
    DialogContent,
    DialogHeader,
    DialogTitle,
    DialogDescription,
} from '@/components/ui/dialog'

// Icons from lucide-vue
import { CheckCircle, XCircle } from 'lucide-vue-next'

const page = usePage()
const flash = computed(() => page.props.flash || {})

const message = ref(null)
const type = ref(null)
const isOpen = ref(false)
let activeTimeout = null

const trigger = (msg, t) => {
    if (activeTimeout) clearTimeout(activeTimeout)

    message.value = msg
    type.value = t
    isOpen.value = true

    activeTimeout = setTimeout(() => {
        isOpen.value = false
        setTimeout(() => {
            message.value = null
            type.value = null
            activeTimeout = null
        }, 300)
    }, 2500)
}

const showNotification = (msg, t) => {
    if (!msg) return

    // Jika sudah terbuka, kita reset agar animasinya terpicu ulang
    if (isOpen.value) {
        isOpen.value = false
        setTimeout(() => trigger(msg, t), 100)
    } else {
        trigger(msg, t)
    }
}

// Gunakan router event agar selalu terdeteksi setiap kali request selesai
import { router } from '@inertiajs/vue3'
import { onMounted, onUnmounted } from 'vue'

let unregisterFinishEvent = null

onMounted(() => {
    // Cek saat mount awal
    if (flash.value.success || flash.value.error) {
        showNotification(flash.value.success || flash.value.error, flash.value.success ? 'success' : 'error')
    }

    // Dengarkan setiap kali aksi Inertia selesai
    unregisterFinishEvent = router.on('finish', () => {
        const currentFlash = page.props.flash || {}
        if (currentFlash.success || currentFlash.error) {
            showNotification(currentFlash.success || currentFlash.error, currentFlash.success ? 'success' : 'error')
        }
    })
})

onUnmounted(() => {
    if (unregisterFinishEvent) unregisterFinishEvent()
})


</script>