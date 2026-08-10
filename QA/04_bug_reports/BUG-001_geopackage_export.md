# BUG-001 – GeoPackage export terminates with ValueError

**Jira ID:** KAN-7  
**Severity:** Critical  
**Priority:** High  
**Related Test Case:** TC-001  
**Status:** Fixed and retested

## Summary

The baseline script terminates during GeoPackage export because the return
value of `QgsVectorFileWriter.writeAsVectorFormatV3()` is assigned to only
two variables.

## Preconditions

- Valid `Polygons`, `dsm` and `dtm_prudnik_clean` layers are loaded.
- All test layers use EPSG:2180.
- Output directory exists and is writable.

## Steps to Reproduce

1. Open the valid TD-01 QGIS project.
2. Execute baseline v1.0.
3. Observe the GeoPackage export stage.

## Expected Result

The processed building layer is exported successfully and a clear success
message is displayed.

## Actual Result

The script terminates with:

`ValueError: too many values to unpack (expected 2)`

No valid output GeoPackage is produced.

## Fix

Build v1.1 was updated to handle all values returned by
`writeAsVectorFormatV3()`.

## Retest

TC-001 was repeated using build v1.1.

**Result:** PASS