<?php

namespace App\Http\Controllers\Public;

use App\Http\Controllers\Controller;
use App\Models\Classification;
use Illuminate\Http\Request;

use Illuminate\Support\Facades\Http;

class ClassificationController extends Controller
{
    public function index()
    {
        $classifications = Classification::where('user_id', auth()->id())->get();
        return inertia('user/classification/ClassificationIndex', [
            'classifications' => $classifications,
        ]);
    }


    public function predict(Request $request)
    {
        $request->validate([
            'image' => 'required|image|max:2048',
        ]);

        $image = $request->file('image');

        try {
            // 1. Kirim ke AI Server (Flask)
            $response = Http::attach(
                'image',
                file_get_contents($image),
                $image->getClientOriginalName()
            )->post('http://127.0.0.1:5001/predict');

            if ($response->failed()) {
                return response()->json(['error' => 'Gagal terhubung ke AI server'], 500);
            }

            $data = $response->json();

            // 2. SIMPAN KE DB (BAIK BERHASIL MAUPUN DITOLAK)
            $path = $image->store('classifications', 'public');
            $confidence = (float) filter_var($data['confidence'] ?? 0, FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION);
            
            // Tentukan status untuk Database
            $dbStatus = ($data['status'] === 'BERHASIL') ? 'Berhasil' : 'Ditolak';

            Classification::create([
                'user_id' => auth()->id() ?? null,
                'image_path' => $path,
                'result' => $data['label'] ?? 'Unknown',
                'confidence' => $confidence,
                'status' => $dbStatus,
            ]);

            // 3. KEMBALIKAN KE VUE (Bawa serta 'status' asli dari Flask)
            return response()->json([
                'label' => $data['label'] ?? 'Unknown',
                'confidence' => $data['confidence'] ?? '0',
                'message' => $data['pesan'] ?? 'Hasil klasifikasi selesai.',
                'status' => $data['status'] // INI PENTING UNTUK SINKRONISASI
            ]);

        } catch (\Exception $e) {
            return response()->json(['error' => 'Terjadi kesalahan internal: ' . $e->getMessage()], 500);
        }
    }
    public function destroy(Classification $classification)
    {
        if ($classification->user_id !== auth()->id()) {
            abort(403);
        }

        // Hapus file dari storage jika ada
        if ($classification->image_path && \Storage::disk('public')->exists($classification->image_path)) {
            \Storage::disk('public')->delete($classification->image_path);
        }

        $classification->delete();

        return back()->with('success', 'Klasifikasi berhasil dihapus');
    }
}