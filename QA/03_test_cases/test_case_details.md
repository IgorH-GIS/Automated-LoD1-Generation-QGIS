# Detailed Test Cases – Automated LoD1 Building Height Extraction

## General Execution Information

| Field | Value |
|---|---|
| Test object | `lod1_extractor_baseline_v1_0.py` |
| Application version | Baseline v1.0 |
| Test environment | QGIS 3.44.8-Solothurn / Windows |
| Tester | Igor Hajducki |
| Execution status | Not Started |

> Important: The baseline script modifies the input building layer by adding zonal statistics fields. Every test must therefore use a backup or a separate copy of the building layer.

---

# TC-001 – Process valid building, DSM and DTM layers

**Related requirements:** FR-001, FR-002, FR-003  
**Type:** Smoke / Functional  
**Priority:** Critical  
**Test data:** TD-01

## Preconditions

- QGIS is running.
- A test project is open.
- A polygon layer named `Polygons` is loaded.
- A DSM raster named `dsm` is loaded.
- A DTM raster named `dtm_prudnik_clean` is loaded.
- All layers cover the same test area.
- The GeoPackage destination directory exists.
- A backup of the building layer has been created.

## Steps

1. Open the QGIS Python Console.
2. Open `lod1_extractor_baseline_v1_0.py`.
3. Verify that the destination GeoPackage path exists.
4. Execute the script.
5. Observe messages displayed in the Python Console.
6. Open the attribute table of the building layer.
7. Verify that roof and ground statistics fields were added.
8. Open the destination GeoPackage in QGIS.
9. Verify that the layer `buildings_lod1_wynik` exists.

## Expected Result

- The script finishes without an unhandled exception.
- Median roof and ground values are calculated.
- The output fields are added to the building layer.
- The layer `buildings_lod1_wynik` is written to the GeoPackage.
- A success message is displayed only after a successful export.

## Actual Result

The script successfully loaded the three required input layers and completed both zonal statistics operations for DSM and DTM.

The operations modified the input `Polygons` layer and added the following fields:

- `ROOF_count`
- `ROOF_sum`
- `ROOF_mean`
- `GND_count`
- `GND_sum`
- `GND_mean`

The `ROOF_*` fields contained numeric values, while all `GND_*` fields contained `NULL`. The expected `ROOF_median` and `GND_median` fields were not created.

During the GeoPackage export stage, the script terminated with the following unhandled exception:

`ValueError: too many values to unpack (expected 2)`

The error occurred because the result returned by `QgsVectorFileWriter.writeAsVectorFormatV3()` contained more values than the two variables provided by the baseline implementation.

The final success or failure message was not executed. The expected file `lod1_test_output.gpkg` was not created, and the `buildings_lod1_wynik` layer was therefore unavailable.

In addition, the zonal statistics operations did not create the required `ROOF_median` and `GND_median` fields. Instead, count, sum and mean fields were added. This behaviour was registered as a separate defect.

All generated `GND_*` fields contained `NULL` during the original execution. Subsequent investigation confirmed that the DTM used during TC-001 contained internal NoData areas under the selected polygons. After correcting the TD-01 dataset, manual zonal median calculation returned numeric values for both final polygons. This observation was classified as a test data issue and not as an additional baseline defect.



**Status:** Fail  
**Evidence:** `12_tc001_input_before_execution.png`, `13_tc001_console_result.png`, `13a_tc001_input_modified_after_failure.png`, `14_tc001_output_missing.png`  
**Defect ID:** KAN-7, KAN-9

## Retest – Baseline Fix v1.1

**Date:** 2026-08-08  
**Build:** v1.1

### Actual Result

The corrected script successfully completed both zonal statistics operations and exported the processed layer to `lod1_test_output.gpkg`.

The output layer `buildings_lod1_wynik` contained 2 records.

The following required fields were created:

- `ROOF_median`
- `GND_median`

Both fields contained numeric values for both records. No `NULL` values were observed.

The QGIS Python Console displayed:

`SUKCES! Dane zapisane do GeoPackage.`

**Status:** Pass  
**Verified Defects:** KAN-7, KAN-9  
**Evidence:** `21_tc001_retest_console.png`, `22_tc001_retest_output.png`
---

# TC-002 – Execute script without the building layer

**Related requirements:** FR-001, NFR-001, NFR-004  
**Type:** Negative  
**Priority:** High  
**Test data:** TD-02

## Preconditions

- The DSM layer `dsm` is loaded.
- The DTM layer `dtm_prudnik_clean` is loaded.
- No layer named `Polygons` is present in the QGIS project.

## Steps

1. Remove or rename the `Polygons` layer.
2. Confirm that `dsm` and `dtm_prudnik_clean` remain loaded.
3. Execute `lod1_extractor_v1_1.py`.
4. Observe the Python Console.
5. Verify whether an output GeoPackage layer was created.

## Expected Result

- The application does not terminate with an unclear Python exception.
- The user receives a clear message that the required building layer was not found.
- Zonal statistics are not started.
- No misleading success message is displayed.
- No incomplete output layer is created.

## Actual Result

The test project contained the required `dsm` and `dtm_prudnik_clean`
layers, but no layer named `Polygons`.

After executing build v1.1, the script terminated immediately with the
following unhandled exception:

`IndexError: list index out of range`

The exception occurred while accessing the first result returned by:

`QgsProject.instance().mapLayersByName('Polygons')[0]`

The application did not display a clear message explaining that the
required building layer was missing. No processing operations were
started and no new output was produced.

**Status:** Fail  
**Evidence:** `28_td02_missing_building_project.png`, `29_tc002_console_result.png`  
**Defect ID:** KAN-10

## Retest – Build v1.2

**Build:** v1.2

### Actual Result

The script detected that the required `Polygons` layer was missing before
starting spatial processing.

Instead of the previous unclear:

`IndexError: list index out of range`

the application returned:

`Required building layer 'Polygons' was not found in the current QGIS project.`

No zonal statistics operations were started and no output GeoPackage was
created.

**Status:** Pass  
**Verified Defect:** KAN-10  
**Evidence:** `32_tc002_retest_console.png`
---

# TC-003 – Execute script without the DSM layer

**Related requirements:** FR-002, NFR-001, NFR-004  
**Type:** Negative  
**Priority:** High  
**Test data:** TD-03

## Preconditions

- The building layer `Polygons` is loaded.
- The DTM layer `dtm_prudnik_clean` is loaded.
- No layer named `dsm` is present.

## Steps

1. Remove the `dsm` layer from the project.
2. Execute the baseline script.
3. Observe the Python Console.
4. Check whether the building attribute table was modified.
5. Check whether an output layer was created.

## Expected Result

- The user receives a clear message that the DSM layer is missing.
- Processing does not start.
- The input building layer remains unchanged.
- No incomplete output is written.
- No misleading success message is displayed.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-004 – Execute script without the DTM layer

**Related requirements:** FR-003, NFR-001, NFR-004  
**Type:** Negative  
**Priority:** High  
**Test data:** TD-04

## Preconditions

- The building layer `Polygons` is loaded.
- The DSM layer `dsm` is loaded.
- No layer named `dtm_prudnik_clean` is present.

## Steps

1. Remove the `dtm_prudnik_clean` layer.
2. Execute the baseline script.
3. Observe the Python Console.
4. Check whether roof statistics were added before the failure.
5. Check whether an output layer was created.

## Expected Result

- The application detects the missing DTM before modifying the input layer.
- The user receives a clear message identifying the missing layer.
- Partial processing is not performed.
- No incomplete output is written.
- No misleading success message is displayed.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-005 – Execute script when the building layer has a different name

**Related requirements:** FR-001, NFR-001, NFR-004  
**Type:** Negative  
**Priority:** High  
**Test data:** TD-09

## Preconditions

- A valid building polygon layer is loaded under the name `building`.
- No layer named `Polygons` is present.
- DSM and DTM layers are loaded under the expected names.

## Steps

1. Rename the valid building layer from `Polygons` to `building`.
2. Execute the baseline script.
3. Observe the Python Console.
4. Check whether processing starts.
5. Check whether an output layer is created.

## Expected Result

- The application does not crash with an unclear exception.
- The user receives a clear message explaining the expected building layer name.
- The script does not modify an unintended layer.
- No misleading success message is displayed.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-006 – Calculate median roof elevation

**Related requirements:** FR-004, FR-006  
**Type:** Functional  
**Priority:** Critical  
**Test data:** TD-01

## Preconditions

- All valid input layers are loaded.
- The building layer contains polygons covered by the DSM.
- A clean copy of the building layer is used.

## Steps

1. Record the number of building features.
2. Execute the corrected script build v1.1.
3. Open the building attribute table.
4. Locate the field created with the `ROOF_` prefix.
5. Confirm that values exist for buildings covered by the DSM.
6. Use both buildings available in TD-01.
7. Independently calculate DSM median values using the QGIS Zonal Statistics tool.
8. Compare the independent values with the script results.

## Expected Result

- A roof median field is created.
- Covered buildings contain numeric median values.
- Values match the independently calculated DSM medians.
- No unrelated attributes are removed.

## Actual Result

Manual DSM zonal median validation was performed independently using QGIS.

The manually calculated values were approximately:

- FID 10: 239.4506 m
- FID 13: 241.8607 m

Build v1.1 produced:

- FID 10: 239.4506072998 m
- FID 13: 241.8606567383 m

The script output matches the independently calculated median values.

**Status:** Pass
**Evidence:** `27_manual_dsm_median_validation.png`, `25_sql_output_validation.png`
**Defect ID:** —

---

# TC-007 – Calculate median ground elevation

**Related requirements:** FR-005, FR-006  
**Type:** Functional  
**Priority:** Critical  
**Test data:** TD-01

## Preconditions

- All valid input layers are loaded.
- Building polygons are covered by the DTM.
- A clean copy of the building layer is used.

## Steps

1. Execute the corrected script build v1.1.
2. Open the building attribute table.
3. Locate the field created with the `GND_` prefix.
4. Confirm that values exist for buildings covered by the DTM.
5. Select both test buildings.
6. Independently calculate DTM median values using the QGIS Zonal Statistics tool.
7. Compare the independent values with the script results.

## Expected Result

- A ground median field is created.
- Covered buildings contain numeric median values.
- Values match the independently calculated DTM medians.
- Existing attributes remain available.

## Actual Result

Manual DTM zonal median validation was performed independently using QGIS.

The manually calculated values were approximately:

- FID 10: 234.2485 m
- FID 13: 235.1835 m

Build v1.1 produced:

- FID 10: 234.2485198975 m
- FID 13: 235.1835479736 m

The script output matches the independently calculated median values.

**Status:** Pass  
**Evidence:** `18_manual_dtm_median_result.png`, `25_sql_output_validation.png`  
**Defect ID:** —

---

# TC-008 – Process every building record from the input layer

**Related requirements:** FR-012  
**Type:** Data Integrity  
**Priority:** High  
**Test data:** TD-01

## Preconditions

- A valid building layer containing at least several features is loaded.
- All required rasters are available.
- The original feature count is known.

## Steps

1. Record the feature count of the input building layer.
2. Execute the baseline script.
3. Record the feature count after zonal statistics.
4. Open `buildings_lod1_wynik`.
5. Record the feature count of the exported layer.
6. Compare all three values.

## Expected Result

- The number of features remains unchanged.
- Every input building is present in the exported layer.
- No feature is duplicated.
- No feature is unintentionally removed.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-009 – Process a building outside raster coverage

**Related requirements:** NFR-001, NFR-002, NFR-004  
**Type:** Edge Case  
**Priority:** High  
**Test data:** TD-05

## Preconditions

- The building layer contains at least one polygon outside DSM or DTM coverage.
- Other polygons are inside raster coverage.
- Required layers are loaded.

## Steps

1. Identify the building polygon located outside raster coverage.
2. Execute the baseline script.
3. Observe the Python Console.
4. Open the building attribute table.
5. Inspect roof and ground values for the outside polygon.
6. Verify whether the polygon is preserved in the output.
7. Check whether the user receives any warning.

## Expected Result

- The application does not crash.
- The polygon remains in the output layer.
- Missing raster statistics are represented consistently, for example as `NULL`.
- The user is informed that incomplete elevation data was produced.
- Valid buildings are still processed correctly.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-010 – Process an empty building layer

**Related requirements:** FR-012, NFR-001  
**Type:** Negative  
**Priority:** Medium  
**Test data:** TD-06

## Preconditions

- An empty polygon layer named `Polygons` is loaded.
- DSM and DTM layers are loaded.

## Steps

1. Confirm that the building layer contains zero features.
2. Execute the baseline script.
3. Observe the Python Console.
4. Check whether output fields were created.
5. Check whether an output GeoPackage layer was created.

## Expected Result

- The application does not crash.
- The user receives information that the input layer contains zero features.
- The application does not report a normal successful processing result without mentioning the empty input.
- No invalid records are created.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-011 – Export the processed layer to GeoPackage

**Related requirements:** FR-007, NFR-003  
**Type:** Functional  
**Priority:** Critical  
**Test data:** TD-01

## Preconditions

- Valid processing has completed.
- The destination directory exists.
- The user has write permission.
- The destination file is not read-only.

## Steps

1. Execute the baseline script.
2. Observe the export result message.
3. Navigate to the destination directory.
4. Confirm that the GeoPackage file exists.
5. Add the GeoPackage to QGIS.
6. Confirm that `buildings_lod1_wynik` exists.
7. Open its attribute table.
8. Confirm that geometry and calculated fields are present.

## Expected Result

- The GeoPackage is created or updated.
- The expected output layer exists.
- The layer can be opened in QGIS.
- Attributes and geometries are readable.
- A success message is displayed after the export succeeds.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-012 – Overwrite an existing destination layer

**Related requirements:** FR-008  
**Type:** Functional  
**Priority:** High  
**Test data:** TD-08

## Preconditions

- The destination GeoPackage already contains `buildings_lod1_wynik`.
- The existing layer contains recognisable old or test data.
- Valid input layers are loaded.

## Steps

1. Record the feature count and sample values from the existing output layer.
2. Execute the baseline script.
3. Reopen or refresh the GeoPackage.
4. Open `buildings_lod1_wynik`.
5. Compare its contents with the previous version.
6. Check whether old records were appended or replaced.

## Expected Result

- The existing layer is replaced.
- Old records are not duplicated or appended.
- The new output contains the current processing results.
- Other layers in the same GeoPackage remain unchanged.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-013 – Export using an invalid GeoPackage path

**Related requirements:** FR-007, NFR-004  
**Type:** Negative  
**Priority:** High  
**Test data:** TD-07

## Preconditions

- A working copy of the baseline script has been created.
- The baseline file itself remains unchanged.
- Valid input layers are loaded.

## Steps

1. In the working copy, set the output path to a directory that does not exist.
2. Execute the script.
3. Observe the Python Console.
4. Verify whether any output file was created.
5. Verify whether a success message was displayed.

## Expected Result

- Export fails safely.
- A clear failure message is displayed.
- The message contains useful information about the invalid path.
- No success message is displayed.
- No corrupt or partial GeoPackage is created.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-014 – Export to a read-only destination

**Related requirements:** FR-007, NFR-004  
**Type:** Negative  
**Priority:** High  
**Test data:** TD-11

## Preconditions

- A test GeoPackage already exists.
- The GeoPackage file has been marked as read-only in Windows file properties.
- A working copy of the script points to that file.
- Valid input layers are loaded.

## Steps

1. Right-click the test GeoPackage file.
2. Open `Properties`.
3. Mark the file as `Read-only`.
4. Apply the change.
5. Execute the script.
6. Observe the Python Console.
7. Check whether the existing GeoPackage was modified.
8. Remove the read-only flag after the test.

## Expected Result

- The application does not overwrite the read-only file.
- A clear export failure message is displayed.
- The existing file remains readable and unchanged.
- No success message is displayed.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-015 – Display correct success and failure messages

**Related requirements:** FR-009, NFR-004  
**Type:** Functional  
**Priority:** High  
**Test data:** TD-01 and TD-07

## Preconditions

- A valid configuration is available.
- An invalid output-path configuration is available.

## Steps – Successful Run

1. Execute the script using valid layers and a valid output path.
2. Record the final console message.
3. Confirm that the output exists.

## Steps – Failed Run

1. Execute a working copy using an invalid output path.
2. Record the final console message.
3. Confirm that the output does not exist.

## Expected Result

- A success message appears only after a successful export.
- A failure message appears after an export error.
- The failure message is understandable and useful.
- Success and failure messages do not contradict the real result.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-016 – Validate exported geometries

**Related requirements:** FR-010, NFR-002  
**Type:** Data Integrity  
**Priority:** Critical  
**Test data:** TD-01

## Preconditions

- A valid output GeoPackage has been created.
- The layer `buildings_lod1_wynik` is loaded.

## Steps

1. Open the QGIS Processing Toolbox.
2. Search for `Check validity`.
3. Select `buildings_lod1_wynik` as the input layer.
4. Run the geometry validation.
5. Review valid, invalid and error outputs.
6. Record the number of invalid geometries.

## Expected Result

- All output geometries are valid.
- The invalid geometry count is zero.
- The layer can be opened and rendered correctly.
- The geometry type remains polygon or multipolygon.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-017 – Preserve original building geometries

**Related requirements:** FR-011, NFR-002  
**Type:** Regression / Data Integrity  
**Priority:** Critical  
**Test data:** TD-01

## Preconditions

- An untouched copy of the original building layer is available.
- The processed output layer is available.
- Both layers use the same CRS.

## Steps

1. Load the untouched original layer.
2. Load `buildings_lod1_wynik`.
3. Confirm that both layers contain the same number of features.
4. Use the QGIS `Symmetrical difference` algorithm with the original and output layers.
5. Review the resulting difference layer.
6. Check whether any geometry differences were generated.

## Expected Result

- The feature counts are identical.
- The symmetrical difference output is empty or contains no meaningful geometry.
- Building shapes, positions and boundaries remain unchanged.
- Only attributes are added or modified.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-018 – Produce identical results for identical input data

**Related requirements:** NFR-005  
**Type:** Repeatability  
**Priority:** High  
**Test data:** TD-01

## Preconditions

- Two clean copies of the same building input layer are available.
- Identical DSM and DTM layers are used.
- Two separate output GeoPackages are available.

## Steps

1. Execute the script using the first clean building copy.
2. Save the result as output A.
3. Execute the script using the second clean building copy.
4. Save the result as output B.
5. Compare feature counts.
6. Compare roof and ground median fields.
7. Compare geometries.
8. Record any differences.

## Expected Result

- Output A and output B contain the same number of records.
- Calculated elevation values are identical.
- Geometries are identical.
- Repeated processing produces a reproducible result.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-019 – Execute script when output fields already exist

**Related requirements:** FR-006, NFR-005  
**Type:** Regression  
**Priority:** Medium  
**Test data:** TD-10

## Preconditions

- The building layer already contains fields created with the `ROOF_` and `GND_` prefixes.
- Valid DSM and DTM layers are loaded.

## Steps

1. Record the existing field names.
2. Execute the baseline script again.
3. Open the attribute table.
4. Inspect the field list.
5. Check for duplicated fields such as additional numbered suffixes.
6. Compare calculated values with the previous execution.
7. Observe console messages.

## Expected Result

- The script handles existing output fields predictably.
- Ambiguous duplicate fields are not created without warning.
- Existing results are updated or the user receives a clear message.
- The repeated run does not corrupt the attribute table.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —

---

# TC-020 – Validate logical consistency of roof and ground elevations

**Related requirements:** FR-004, FR-005, NFR-002  
**Type:** Data Integrity  
**Priority:** Critical  
**Test data:** TD-01

## Preconditions

- Valid roof and ground median fields have been generated.
- Buildings are covered by both DSM and DTM.

## Steps

1. Open the output attribute table.
2. Identify the exact roof and ground field names.
3. Apply a filter equivalent to:

   `"ROOF_median" < "GND_median"`

4. Record the number of matching records.
5. Apply a second filter for NULL roof or ground values.
6. Review any matching buildings on the map.
7. Record whether the results are caused by missing coverage, invalid input or processing errors.

## Expected Result

- For valid buildings, roof elevation is not lower than ground elevation.
- No unexpected NULL values exist within valid raster coverage.
- Invalid or suspicious records can be identified and explained.
- The exported data is suitable for further height calculation.

## Actual Result

Database validation was performed using DBeaver on the exported
`buildings_lod1_wynik` GeoPackage layer.

The following checks were executed:

1. NULL validation for `ROOF_median` and `GND_median` returned 0 records.
2. Logical consistency validation using:

   `ROOF_median <= GND_median`

   returned 0 records.
3. Both exported buildings contained numeric roof and ground median values.
4. Calculated relative building heights were positive:

   - FID 10: 5.20 m
   - FID 13: 6.68 m

No logically inconsistent roof/ground elevation records were detected.

**Status:** Pass  
**Evidence:** `25_sql_output_validation.png`, `26_sql_null_validation.png`  
**Defect ID:** —

---

# TC-021 – Execute the script with input layers using different CRS

**Related requirements:** NFR-002, NFR-004, NFR-006  
**Type:** Compatibility / Negative  
**Priority:** High  
**Test data:** TD-00

## Preconditions

- QGIS is running in a fresh session.
- The project `td00_as_received_project.qgz` is open.
- The following layers are loaded:
  - `Polygons` – EPSG:4326,
  - `dsm` – EPSG:32633,
  - `dtm_prudnik_clean` – EPSG:2180.
- The building layer is a clean working copy.
- The output path points to a dedicated test GeoPackage.

## Steps

1. Confirm the CRS of every input layer.
2. Confirm that the layers appear spatially aligned in the QGIS map canvas.
3. Execute the baseline script.
4. Observe all messages and exceptions in the Python Console.
5. Open the building attribute table.
6. Inspect the generated `ROOF_` and `GND_` fields.
7. Check for unexpected NULL values.
8. Open the exported GeoPackage layer.
9. Verify its feature count, geometries and calculated values.
10. Compare the result with the correctly prepared TD-01 dataset.

## Expected Result

- The application either processes the input layers correctly despite their different CRS, or stops processing before modifying the data and displays a clear CRS compatibility message.
- No silent NULL values are produced for otherwise valid buildings.
- No partial output is reported as successful.
- No misleading success message is displayed.

## Actual Result

_To be completed during execution._

**Status:** Not Run  
**Evidence:** —  
**Defect ID:** —