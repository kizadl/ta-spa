<?php

use Illuminate\Support\Facades\Route;
use Laravel\Fortify\Features;
use App\Http\Controllers\Admin\UserController;
use App\Http\Controllers\Admin\DashboardController;
use App\Http\Controllers\Public\ClassificationController; // Import Controller

Route::redirect('dashboard', 'admin/dashboard')->name('dashboard');

Route::get('/', function () {
    return inertia('public/Home', [
        'canRegister' => Features::enabled(Features::registration()),
    ]);
})->name('home');

Route::post('/classifications', [ClassificationController::class, 'store'])->name('public.classifications.store');

Route::prefix('admin')->name('admin.')->middleware(['auth', 'verified'])->group(function () {
    Route::get('dashboard', [DashboardController::class, 'index'])->name('dashboard');
    Route::resource('users', UserController::class)->names('users');

    // Route tambahan untuk Admin jika ingin melihat history klasifikasi secara global
    // Route::get('history', [DashboardController::class, 'history'])->name('history');
});



require __DIR__ . '/settings.php';
