<?php
/**
 * Mass Rebranding Script
 * Mengubah semua referensi "Warta Jabar" / "Warta Janten" menjadi "BantenStream"
 * di semua file HTML
 */

// Set direktori yang akan diproses
$baseDir = __DIR__;

// Pattern yang akan diganti
$replacements = array(
    // Dalam title tags
    array(
        'find' => '- Warta Janten</title>',
        'replace' => '- BantenStream</title>'
    ),
    array(
        'find' => '- Warta Jabar</title>',
        'replace' => '- BantenStream</title>'
    ),
    // Dalam logo HTML (dari image ke text)
    array(
        'find' => '<img src="img/warta jabar.png" alt="Warta Jabar">',
        'replace' => 'BantenStream'
    ),
    // Dalam copyright
    array(
        'find' => 'Copyright © 2026 <strong>Warta Janten</strong>',
        'replace' => 'Copyright © 2026 <strong>BantenStream</strong>'
    ),
    array(
        'find' => 'Copyright © 2026 <strong>Warta Jabar</strong>',
        'replace' => 'Copyright © 2026 <strong>BantenStream</strong>'
    ),
);

// Exclude files
$excludeFiles = array('mass_rebrand.php', 'template.html');

// Fungsi untuk rekursif scan directory
function processDirectory($dir, $replacements, $excludeFiles) {
    $files = array_diff(scandir($dir), array('.', '..', '.git'));
    $processedCount = 0;
    $totalCount = 0;
    
    foreach ($files as $file) {
        $filePath = $dir . DIRECTORY_SEPARATOR . $file;
        
        if (is_dir($filePath)) {
            // Rekursi ke subfolder
            $processedCount += processDirectory($filePath, $replacements, $excludeFiles);
        } elseif (is_file($filePath) && pathinfo($filePath, PATHINFO_EXTENSION) === 'html') {
            // Skip excluded files
            if (in_array(basename($filePath), $excludeFiles)) {
                echo "SKIP: {$filePath}\n";
                continue;
            }
            
            $totalCount++;
            $originalContent = file_get_contents($filePath);
            $newContent = $originalContent;
            $changed = false;
            
            foreach ($replacements as $replacement) {
                if (strpos($newContent, $replacement['find']) !== false) {
                    $newContent = str_replace($replacement['find'], $replacement['replace'], $newContent);
                    $changed = true;
                }
            }
            
            if ($changed) {
                file_put_contents($filePath, $newContent);
                echo "✓ UPDATED: {$filePath}\n";
                $processedCount++;
            } else {
                echo "- UNCHANGED: {$filePath}\n";
            }
        }
    }
    
    return $processedCount;
}

echo "========================================\n";
echo "MASS REBRANDING SCRIPT - Warta Jabar → BantenStream\n";
echo "========================================\n\n";

$processedCount = processDirectory($baseDir, $replacements, $excludeFiles);

echo "\n========================================\n";
echo "Rebranding Selesai!\n";
echo "Total file yang diperbarui: {$processedCount}\n";
echo "========================================\n";
?>
