# SQL Validation Results

## Environment

- Database: GeoPackage / SQLite
- Tool: DBeaver
- Output layer: `buildings_lod1_wynik`
- Tested build: v1.1

## Results

| ID | Validation | Expected | Actual | Status |
|---|---|---|---|---|
| SQL-01 | Exported record count | 2 records | 2 records | Pass |
| SQL-02 | NULL roof/ground medians | 0 records | 0 records | Pass |
| SQL-03 | Roof elevation <= ground elevation | 0 records | 0 records | Pass |
| SQL-04 | Calculated building height | Positive numeric values | 5.20 m, 6.68 m | Pass |
| SQL-05 | GeoPackage metadata registration | Output layer registered | To be completed | Pending |

## Conclusion

Database validation confirmed that build v1.1 exported the expected number of records and produced complete numeric roof and ground median values.

No NULL elevation values were found.

The calculated relative building heights were:

- FID 10: 5.20 m
- FID 13: 6.68 m