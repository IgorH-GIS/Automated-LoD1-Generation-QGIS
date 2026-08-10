-- QA SQL Validation
-- Automated LoD1 Building Height Extraction
-- Build: v1.1


-- SQL-01
-- Verify that the expected number of records was exported.

SELECT COUNT(*) AS record_count
FROM buildings_lod1_wynik;


-- SQL-02
-- Verify that roof and ground median values are not NULL.

SELECT
    fid,
    ROOF_median,
    GND_median
FROM buildings_lod1_wynik
WHERE ROOF_median IS NULL
   OR GND_median IS NULL;


-- SQL-03
-- Verify logical consistency:
-- roof elevation should be higher than ground elevation.

SELECT
    fid,
    ROOF_median,
    GND_median
FROM buildings_lod1_wynik
WHERE ROOF_median <= GND_median;


-- SQL-04
-- Inspect calculated elevations for all exported buildings.

SELECT
    fid,
    ROOF_median,
    GND_median,
    ROUND(ROOF_median - GND_median, 2) AS calculated_height
FROM buildings_lod1_wynik;


-- SQL-05
-- Verify that the output layer is registered in the GeoPackage metadata.

SELECT
    table_name,
    data_type,
    srs_id
FROM gpkg_contents
WHERE table_name = 'buildings_lod1_wynik';