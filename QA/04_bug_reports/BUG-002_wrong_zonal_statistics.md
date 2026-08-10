# BUG-002 – Incorrect zonal statistics generated instead of median

**Jira ID:** KAN-9  
**Severity:** Critical  
**Priority:** High  
**Related Test Case:** TC-001  
**Status:** Fixed and retested

## Summary

The baseline script generates count, sum and mean fields instead of the
required median roof and ground elevations.

## Preconditions

- Valid TD-01 dataset is loaded.
- Building layer contains no existing `ROOF_*` or `GND_*` fields.

## Steps to Reproduce

1. Execute baseline v1.0.
2. Open the building attribute table.
3. Inspect fields created by the zonal statistics operations.

## Expected Result

The application creates:

- `ROOF_median`
- `GND_median`

## Actual Result

The baseline creates:

- `ROOF_count`
- `ROOF_sum`
- `ROOF_mean`
- `GND_count`
- `GND_sum`
- `GND_mean`

The required median fields are not created.

## Fix

Build v1.1 was updated to use the feature-based zonal statistics algorithm
with the median statistic explicitly selected.

## Retest

The corrected build generated valid:

- `ROOF_median`
- `GND_median`

Independent QGIS validation confirmed the calculated values.

**Result:** PASS