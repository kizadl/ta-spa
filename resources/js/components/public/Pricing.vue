<template>
  <section id="pricing" class="py-24 px-4">
    <div class="max-w-6xl mx-auto">
      <div class="text-center mb-12">
        <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4 font-display">Simple, transparent pricing</h2>
        <p class="text-zinc-400 max-w-2xl mx-auto mb-8">Start free, scale as you grow. No hidden fees, no surprises.</p>

        <!-- Billing Toggle -->
        <div class="inline-flex items-center p-1 rounded-full bg-zinc-900 border border-zinc-800">
          <button
            @click="billingCycle = 'monthly'"
            :class="[
              'relative px-4 py-2 text-sm font-medium rounded-full transition-colors',
              billingCycle === 'monthly' ? 'text-white' : 'text-zinc-400',
            ]"
          >
            <div
              v-if="billingCycle === 'monthly'"
              class="absolute inset-0 bg-zinc-800 rounded-full"
            />
            <span class="relative z-10">Monthly</span>
          </button>
          <button
            @click="billingCycle = 'yearly'"
            :class="[
              'relative px-4 py-2 text-sm font-medium rounded-full transition-colors',
              billingCycle === 'yearly' ? 'text-white' : 'text-zinc-400',
            ]"
          >
            <div
              v-if="billingCycle === 'yearly'"
              class="absolute inset-0 bg-zinc-800 rounded-full"
            />
            <span class="relative z-10">Yearly</span>
            <span class="relative z-10 ml-2 px-2 py-0.5 text-xs bg-emerald-500/20 text-emerald-400 rounded-full">
              -20%
            </span>
          </button>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div
          v-for="(plan, index) in plans"
          :key="plan.name"
          :class="[
            'relative p-6 rounded-2xl border transition-all duration-300 hover:scale-[1.02]',
            plan.highlighted
              ? 'bg-zinc-900 border-zinc-700'
              : 'bg-zinc-900/50 border-zinc-800 hover:border-zinc-600',
          ]"
        >
          <div
            v-if="plan.highlighted"
            class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1 bg-white text-zinc-950 text-xs font-medium rounded-full"
          >
            Most Popular
          </div>

          <div class="mb-6">
            <h3 class="text-xl font-semibold text-white mb-2">{{ plan.name }}</h3>
            <p class="text-zinc-400 text-sm">{{ plan.description }}</p>
          </div>

          <div class="mb-6">
            <div class="flex items-baseline gap-1">
              <span class="text-4xl font-bold text-white">${{ plan.price[billingCycle] }}</span>
              <span v-if="plan.price.monthly > 0" class="text-zinc-400 text-sm">/month</span>
            </div>
            <p v-if="billingCycle === 'yearly' && plan.price.yearly > 0" class="text-xs text-zinc-500 mt-1">
              Billed annually (${{ plan.price.yearly * 12 }}/year)
            </p>
          </div>

          <ul class="space-y-3 mb-8">
            <li v-for="feature in plan.features" :key="feature" class="flex items-center gap-3 text-sm text-zinc-300">
              <Check class="w-4 h-4 text-emerald-500 shrink-0" :stroke-width="1.5" />
              {{ feature }}
            </li>
          </ul>

          <button
            :class="[
              'w-full rounded-full py-2 font-medium transition-colors',
              plan.highlighted
                ? 'shimmer-btn bg-white text-zinc-950 hover:bg-zinc-200'
                : 'bg-zinc-800 text-white hover:bg-zinc-700 border border-zinc-700',
            ]"
          >
            {{ plan.cta }}
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Check } from 'lucide-vue-next'

type BillingCycle = 'monthly' | 'yearly'

const billingCycle = ref<BillingCycle>('monthly')

const plans = [
  {
    name: 'Starter',
    description: 'Perfect for side projects and small teams',
    price: { monthly: 0, yearly: 0 },
    features: ['3 team members', '10 projects', 'Basic analytics', 'Community support', '1GB storage'],
    cta: 'Get Started',
    highlighted: false,
  },
  {
    name: 'Pro',
    description: 'For growing teams that need more power',
    price: { monthly: 29, yearly: 24 },
    features: [
      'Unlimited team members',
      'Unlimited projects',
      'Advanced analytics',
      'Priority support',
      '100GB storage',
      'Custom domains',
      'API access',
    ],
    cta: 'Start Free Trial',
    highlighted: true,
  },
  {
    name: 'Enterprise',
    description: 'For organizations with advanced needs',
    price: { monthly: 99, yearly: 79 },
    features: [
      'Everything in Pro',
      'SSO & SAML',
      'Dedicated support',
      'SLA guarantee',
      'Unlimited storage',
      'Custom integrations',
      'Audit logs',
    ],
    cta: 'Contact Sales',
    highlighted: false,
  },
]
</script>
