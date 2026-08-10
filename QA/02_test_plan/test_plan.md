# Test Plan – Automated LoD1 Building Height Extraction

## 1. Document Control

| Field | Value |
|---|---|
| Project | Automated LoD1 Building Height Extraction |
| Test object | PyQGIS script for DSM/DTM zonal statistics and GeoPackage export |
| Application version | Baseline v1.0 |
| Document version | 1.0 |
| Author | Igor Hajducki |
| Status | Draft |
| Date | 2026-08-03 |

---

## 2. Test Objective

The objective of testing is to verify that the PyQGIS script correctly:

- loads the required building, DSM and DTM layers,
- calculates median roof and ground elevation values,
- writes calculated attributes to the building layer,
- exports the processed layer to a GeoPackage,
- preserves building geometries and record count,
- reports processing and export errors clearly,
- produces repeatable results for identical input datasets.

The testing process also aims to identify risks related to missing layers, invalid input data, hard-coded paths, NULL values and GeoPackage export failures.

---

## 3. Scope of Testing

### 3.1 Functional Testing

The following functions are included in the test scope:

- loading the building polygon layer,
- loading the DSM raster layer,
- loading the DTM raster layer,
- calculation of median roof elevation,
- calculation of median ground elevation,
- creation of output attribute fields,
- GeoPackage export,
- overwriting an existing output layer,
- display of success and error messages.

### 3.2 Negative Testing

The following error conditions will be tested:

- missing building layer,
- missing DSM layer,
- missing DTM layer,
- incorrect layer name,
- empty building layer,
- building polygons outside raster coverage,
- invalid GeoPackage output path,
- unavailable destination directory,
- existing output layer,
- NULL values produced during zonal statistics.

### 3.3 Data Integrity Testing

The exported data will be verified for:

- correct number of records,
- valid building geometries,
- preservation of original geometries,
- presence of roof and ground elevation fields,
- NULL elevation values,
- logical consistency between roof and ground elevation,
- repeatability of results.

### 3.4 Regression Testing

Regression tests will be executed after corrections are introduced to confirm that:

- reported defects have been fixed,
- previously working functions still operate correctly,
- GeoPackage export remains valid after code changes.

---

## 4. Out of Scope

The following areas are not included in this test cycle:

- accuracy of UAV photogrammetric reconstruction,
- CloudCompare point-cloud classification,
- accuracy of QuickOSM building footprints,
- full integration testing with CadnaA or SoundPLAN,
- performance testing on enterprise-scale datasets,
- testing of QGIS itself,
- API testing, because the current application does not expose an API,
- graphical user interface testing, because the script is executed from the QGIS Python console.

---

## 5. Test Environment

| Component | Configuration |
|---|---|
| Operating system | Windows 10 |
| GIS software | QGIS 3.44.8-Solothurn |
| Programming environment | Python / PyQGIS |
| Input vector format | QGIS vector layer / GeoPackage |
| Input raster format | DSM and DTM raster layers |
| Output format | GeoPackage |
| Database validation | DBeaver and SQLite SQL |
| Defect management | Jira |
| Source control | GitHub |


---

## 6. Test Types

The following test types will be used:

- smoke testing,
- functional testing,
- negative testing,
- data integrity testing,
- database validation,
- regression testing,
- manual exploratory testing.

---

## 7. Entry Criteria

Testing can begin when:

- the baseline v1.0 script is available,
- the expected application behaviour is documented,
- the QGIS test project is prepared,
- DSM, DTM and building test layers are available,
- a backup copy of the original input data has been created,
- the destination GeoPackage location is defined.

---

## 8. Exit Criteria

Testing can be completed when:

- all Critical and High priority test cases have been executed,
- no unresolved Critical defects remain,
- reported fixes have been retested,
- the output GeoPackage has been validated using SQL,
- test evidence has been collected,
- the Test Summary Report has been prepared.

Medium and Low severity defects may remain open if they are documented and do not prevent the main workflow from completing.

---

## 9. Test Data

The test process will use several datasets and configurations:

| Dataset | Purpose |
|---|---|
| TD-00 | Original layers with mixed CRS: EPSG:4326, EPSG:32633 and EPSG:2180 |
| TD-01 | Valid layers reprojected to a common CRS |
| TD-02 | Project without the building polygon layer |
| TD-03 | Project without the DSM layer |
| TD-04 | Project without the DTM layer |
| TD-05 | Building polygons outside DSM coverage |
| TD-06 | Empty building layer |
| TD-07 | Invalid or unavailable GeoPackage path |
| TD-08 | GeoPackage containing an existing destination layer |
| TD-09 | Building polygon layer present under a different name |
| TD-10 | Building layer containing existing ROOF_median and GND_median fields |
| TD-11 | Read-only or unavailable GeoPackage destination |

The original production-like dataset will not be modified without creating a backup.

---

## 10. Defect Management

Defects will be registered in Jira.

Each defect report should contain:

- clear title,
- related requirement,
- environment,
- preconditions,
- steps to reproduce,
- expected result,
- actual result,
- severity,
- priority,
- screenshots or logs,
- retest result.

### Severity Levels

| Severity | Meaning |
|---|---|
| Critical | The main workflow cannot be completed or output data is unusable |
| High | Important functionality fails, but a workaround may exist |
| Medium | Functionality works partially or produces misleading behaviour |
| Low | Minor issue without significant influence on processing |

---

## 11. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Hard-coded layer names | Script may terminate when names differ | Test missing and renamed layers |
| Hard-coded output path | Export may fail on another workstation | Test invalid and unavailable paths |
| Input layer modified in place | Original data may be changed | Create a backup before testing |
| GeoPackage layer overwrite | Existing results may be lost | Use dedicated test output files |
| Missing raster coverage | NULL elevation values may be created | Validate attributes using SQL |
| QGIS version differences | Processing algorithms may behave differently | Record the exact QGIS version |
| Lack of exception handling | User may receive an unclear Python error | Document and test failure scenarios |

---

## 12. Test Deliverables

The testing process will produce:

- Software Requirements Specification,
- Test Plan,
- Test Cases,
- Jira defect reports,
- SQL validation queries,
- screenshots and logs,
- regression test results,
- Test Summary Report.