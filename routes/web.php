<?php

use Illuminate\Support\Facades\Route;
use Laravel\Fortify\Features;
use App\Http\Controllers\Admin\UserController;
use App\Http\Controllers\Admin\DashboardController;
use App\Http\Controllers\Public\ClassificationController; // Import Controller

Route::get('dashboard', function () {
    if (auth()->user()->role === 'admin') {
        return redirect()->route('admin.dashboard');
    }
    return app(DashboardController::class)->index();
})->middleware(['auth', 'verified'])->name('dashboard');

Route::get('/', function () {
    return inertia('public/Home', [
        'canRegister' => Features::enabled(Features::registration()),
    ]);
})->name('home');

Route::post('/predict', [ClassificationController::class, 'predict'])->name('public.predict');

Route::middleware(['auth', 'verified'])->group(function () {
    Route::get('/classifications', [ClassificationController::class, 'index'])->name('classifications.index');
    Route::delete('/classifications/{classification}', [ClassificationController::class, 'destroy'])->name('classifications.destroy');
});


Route::prefix('admin')->name('admin.')->middleware(['auth', 'verified'])->group(function () {
    Route::get('dashboard', [DashboardController::class, 'index'])->name('dashboard');
    Route::resource('users', UserController::class)->names('users');

    // Route tambahan untuk Admin jika ingin melihat history klasifikasi secara global
    // Route::get('history', [DashboardController::class, 'history'])->name('history');
});



require __DIR__ . '/settings.php';
