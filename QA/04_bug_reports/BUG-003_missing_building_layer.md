# BUG-003 – Missing building layer causes unhandled IndexError

**Jira ID:** KAN-10  
**Severity:** High  
**Priority:** High  
**Related Test Case:** TC-002  
**Status:** Fixed and retested

## Summary

When the required `Polygons` layer is missing, build v1.1 terminates with an
unclear Python exception.

## Preconditions

- `dsm` layer is loaded.
- `dtm_prudnik_clean` layer is loaded.
- No layer named `Polygons` is present.

## Steps to Reproduce

1. Open the TD-02 project.
2. Execute build v1.1.
3. Observe the Python Console.

## Expected Result

The application stops before processing and clearly informs the user that the
required building layer is missing.

## Actual Result

The script terminates with:

`IndexError: list index out of range`

No clear explanation is provided to the user.

## Fix

Build v1.2 introduced explicit validation of required input layers.

The application now reports:

`Required building layer 'Polygons' was not found in the current QGIS project.`

## Retest

TC-002 was repeated using build v1.2.

**Result:** PASS