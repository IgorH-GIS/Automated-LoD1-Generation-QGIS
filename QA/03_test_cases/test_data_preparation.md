# Test Data Preparation

## 1. Purpose

This document describes the datasets and QGIS project configurations prepared for testing the Automated LoD1 Building Height Extraction script.

Large raster and spatial datasets are stored locally and are not included in the public GitHub repository.

---

## 2. Local Test Workspace

`C:\Project\LoD1_QA_Test_Data`

Tests are executed only on working copies. Original source data is stored separately and is not modified during testing.

---

## 3. Test Data Register

| ID | Configuration | Purpose | Status |
|---|---|---|---|
| TD-00 | Original layers with mixed CRS: EPSG:4326, EPSG:32633 and EPSG:2180 | Baseline behaviour with data received by the tester | Prepared |
| TD-01 | Valid layers in EPSG:2180, corrected DTM coverage and 2 fully covered building polygons | Positive workflow and smoke tests | Prepared |
| TD-02 | Project without the building polygon layer | Missing mandatory vector layer | Prepared |
| TD-03 | Project without the DSM layer | Missing mandatory DSM raster | Not Prepared |
| TD-04 | Project without the DTM layer | Missing mandatory DTM raster | Not Prepared |
| TD-05 | Building polygons outside raster coverage | Missing zonal statistics coverage | Not Prepared |
| TD-06 | Empty building layer | Zero-feature input validation | Not Prepared |
| TD-07 | Invalid GeoPackage path | Export failure handling | Not Prepared |
| TD-08 | Existing destination layer | Overwrite behaviour | Not Prepared |
| TD-09 | Building layer under a different name | Hard-coded layer-name validation | Not Prepared |
| TD-10 | Existing ROOF and GND fields | Repeated execution behaviour | Not Prepared |
| TD-11 | Read-only destination | File permission failure handling | Not Prepared |

---

## 4. TD-01 Test Data Correction Log

During the initial execution of TC-001, all generated `GND_*` fields contained `NULL`.

Further investigation showed that the DTM used in the original TD-01 dataset contained internal NoData areas under the selected building polygons.

The issue was verified using the QGIS Identify tool and manual zonal statistics.

To create a valid positive test dataset:

- DTM NoData gaps in the controlled test area were filled using the QGIS/GDAL Fill NoData tool.
- CRS was confirmed as EPSG:2180.
- Building polygons were reduced to two features fully covered by both DSM and corrected DTM.
- The working `Polygons` layer was recreated without existing `ROOF_*` and `GND_*` fields.
- Manual DTM median calculation returned valid numeric results for both final test polygons.

The corrected TD-01 dataset is used only for QA testing. The operation does not modify the original source DTM.

### Validation Result

Manual DTM median values for the final test buildings:

- Building 1: approximately 234.25 m
- Building 2: approximately 235.18 m

### Conclusion

The `GND_* = NULL` result observed during the original TC-001 execution was caused by invalid test-data coverage and was not classified as an additional defect in baseline v1.0.