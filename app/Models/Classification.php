<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Classification extends Model
{
    //
    protected $fillable = [
        'user_id',
        'image_path',
        'result',
        'confidence',
        'status'
    ];

    // Relasi ke User (Satu klasifikasi dimiliki satu User)
    public function user()
    {
        return $this->belongsTo(User::class);
    }
}
