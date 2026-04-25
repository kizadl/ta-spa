<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('classifications', function (Blueprint $table) {
        $table->id();
        // user_id boleh kosong (untuk guest)
        $table->foreignId('user_id')->nullable()->constrained()->onDelete('cascade');
        $table->string('image_path');
        $table->string('result'); 
        $table->float('confidence');
        $table->timestamps(); 
    });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('classifications');
    }
};
