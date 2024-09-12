-- List bands with Glam rock style ranked by their longevity
-- Select the database where you imported the data
USE your_database_name;
SELECT 
    band_name, 
    CASE 
        WHEN split IS NULL OR split = 0 THEN YEAR(CURDATE()) - formed 
        ELSE split - formed
    END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
