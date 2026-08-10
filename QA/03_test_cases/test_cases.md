# Test Cases – Automated LoD1 Building Height Extraction

## 1. Document Control

| Field | Value |
|---|---|
| Project | Automated LoD1 Building Height Extraction |
| Test object | PyQGIS baseline v1.0 and corrective builds v1.1–v1.2
| Document version | 1.0 |
| Author | Igor Hajducki |
| Status | Draft |
| Date | 2026-08-03 |

---

## 2. Test Status Definitions

| Status | Meaning |
|---|---|
| Not Run | Test has not been executed |
| Pass | Actual result matches the expected result |
| Fail | Actual result differs from the expected result |
| Blocked | Test cannot be executed because of another problem |

---

## 3. Test Case Inventory

| ID | Requirement | Test Case | Type | Priority | Test Data | Status |
|---|---|---|---|---|---|---|
| TC-001 | FR-001, FR-002, FR-003 | Process valid building, DSM and DTM layers | Smoke / Functional | Critical | TD-01 | Fail → Pass (Retest v1.1) |
| TC-002 | FR-001, NFR-001, NFR-004 | Execute script without the building layer | Negative | High | TD-02 |  Fail → Pass (Retest v1.2) |
| TC-003 | FR-002, NFR-001, NFR-004 | Execute script without the DSM layer | Negative | High | TD-03 | Not Run |
| TC-004 | FR-003, NFR-001, NFR-004 | Execute script without the DTM layer | Negative | High | TD-04 | Not Run |
| TC-005 | FR-001 | Execute script when the building layer has a different name | Negative | High | TD-09 | Not Run |
| TC-006 | FR-004, FR-006 | Calculate median roof elevation | Functional | Critical | TD-01 | Pass |
| TC-007 | FR-005, FR-006 | Calculate median ground elevation | Functional | Critical | TD-01 | Pass |
| TC-008 | FR-012 | Process every building record from the input layer | Data integrity | High | TD-01 | Not Run |
| TC-009 | NFR-001, NFR-002, NFR-004 | Process a building outside raster coverage | Edge case | High | TD-05 | Not Run |
| TC-010 | FR-012, NFR-001 | Process an empty building layer | Negative | Medium | TD-06 | Not Run |
| TC-011 | FR-007, NFR-003 | Export the processed layer to GeoPackage | Functional | Critical | TD-01 | Not Run |
| TC-012 | FR-008 | Overwrite an existing destination layer | Functional | High | TD-08 | Not Run |
| TC-013 | FR-007, NFR-004 | Export using an invalid GeoPackage path | Negative | High | TD-07 | Not Run |
| TC-014 | FR-007, NFR-004 | Export to an unavailable or read-only directory | Negative | High | TD-11 | Not Run |
| TC-015 | FR-009, NFR-004 | Display a correct success or failure message | Functional | High | TD-01 / TD-07 | Not Run |
| TC-016 | FR-010, NFR-002 | Validate exported geometries | Data integrity | Critical | TD-01 | Not Run |
| TC-017 | FR-011, NFR-002 | Preserve original building geometries | Regression / Data integrity | Critical | TD-01 | Not Run |
| TC-018 | NFR-005 | Produce identical results for identical input data | Repeatability | High | TD-01 | Not Run |
| TC-019 | FR-006, NFR-005 | Execute the script when output fields already exist | Regression | Medium | TD-10 | Not Run |
| TC-020 | FR-004, FR-005, NFR-002 | Validate logical consistency of roof and ground elevations | Data integrity | Critical | TD-01 | Pass |
| TC-021 | NFR-002, NFR-004, NFR-006 | Execute the script with input layers using different CRS | Compatibility / Negative | High | TD-00 | Not Run |