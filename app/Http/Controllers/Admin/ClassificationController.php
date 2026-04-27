<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Classification;
use Illuminate\Http\Request;
use Inertia\Inertia;

class ClassificationController extends Controller
{
    public function index()
    {
        $classifications = Classification::with('user')
            ->latest()
            ->paginate(10);

        return Inertia::render('admin/Classification', [
            'classifications' => $classifications
        ]);
    }

    public function destroy(Classification $classification)
    {
        $classification->delete();
        return redirect()->back()->with('success', 'History classification deleted successfully.');
    }
}
