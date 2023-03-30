-- Lists all bands with Glam rock as their main style, ranked by theri longevity.

SELECT band_name, (IFNULL(split, YEAR(CURDATE())) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';