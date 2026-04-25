<?php

namespace App\Http\Controllers\Public;

use App\Http\Controllers\Controller;
use App\Models\Classification;
use Illuminate\Http\Request;

class ClassificationController extends Controller
{
    public function store(Request $request)
    {
        $request->validate([
            'image' => 'required|image|max:2048',
            'result' => 'required|string',
            'confidence' => 'required',
        ]);

        // Simpan gambar ke storage public
        $path = $request->file('image')->store('classifications', 'public');

        // Simpan ke Database
        Classification::create([
            'user_id' => auth()->id(), // null jika guest, id jika login
            'image_path' => $path,
            'result' => $request->result,
            'confidence' => (float) filter_var($request->confidence, FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION),
        ]);

        return response()->json(['message' => 'Data tersimpan ke history']);
    }
}