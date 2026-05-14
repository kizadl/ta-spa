<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Models\Classification; // Import model Classification
use Illuminate\Support\Facades\DB;
use App\Models\User;

class DashboardController extends Controller
{
    public function index()
    {
        $user = Auth::user();

        // Mulai Query Dasar
        $query = Classification::query();

        // LOGIKA ROLE: Jika yang login adalah 'user', kunci hanya data miliknya
        if ($user->role === 'user') {
            $query->where('user_id', $user->id);
        }
        // Jika admin, biarkan query mengambil semua data (tanpa where)

        // Ambil data Chart (sudah terfilter role)
        $chartData = (clone $query)->select('result', DB::raw('count(*) as total'))
            ->groupBy('result')
            ->get();

        // Ambil History Terbaru (sudah terfilter role)
        $recentHistory = (clone $query)->latest()->limit(10)->get();

        // Hitung Total Scan (sudah terfilter role)
        $totalScan = (clone $query)->count();

        // Rata-rata akurasi dari yang berhasil
        $avgAccuracy = (clone $query)->where('status', 'Berhasil')->avg('confidence') ?? 0;

        // Tingkat keberhasilan (Total Berhasil / Total Scan)
        $totalBerhasil = (clone $query)->where('status', 'Berhasil')->count();
        $successRate = $totalScan > 0 ? ($totalBerhasil / $totalScan) * 100 : 0;

        $totalUser = User::where('role', 'user')->count();

        return inertia('admin/Dashboard', [
            'user' => $user,
            'chartData' => $chartData,
            'recentHistory' => $recentHistory,
            'totalScan' => $totalScan,
            'avgAccuracy' => round($avgAccuracy, 2),
            'successRate' => round($successRate, 2),
            'totalUser' => $totalUser,
        ]);
    }
}