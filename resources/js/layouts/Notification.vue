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
import { ref, watch, computed } from 'vue'
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

watch(
    flash,
    () => {
        if (flash.value.success) {
            message.value = flash.value.success
            type.value = 'success'
            isOpen.value = true
        } else if (flash.value.error) {
            message.value = flash.value.error
            type.value = 'error'
            isOpen.value = true
        }

        if (message.value) {
            setTimeout(() => {
                isOpen.value = false
                setTimeout(() => {
                    message.value = null
                    type.value = null
                }, 300)
            }, 2500)
        }
    },
    { immediate: true }
)
</script>