Software Requirements Specification (SRS)
1. Purpose

The purpose of this application is to automate the extraction of roof and ground elevation values from UAV-derived DSM and DTM raster datasets and assign them to building polygons. The resulting dataset is exported to a GeoPackage for further acoustic analysis in external software such as CadnaA.

2. Business Goal

The application reduces manual GIS processing by automating the preparation of LoD1 building datasets required for acoustic simulations.

3. Input Data

The application requires:

Building polygon layer
DSM raster
DTM raster
Destination GeoPackage path

4. Output

The application creates a GeoPackage layer containing:

Building geometry
Roof median elevation
Ground median elevation

5. User

GIS Analyst

6. Environment
QGIS 3.x
Python
PyQGIS
GeoPackage

7. Workflow
Load Layers

↓

Calculate Roof Median

↓

Calculate Ground Median

↓

Save GeoPackage

↓

Ready for Acoustic Analysis

## 8. Functional Requirements (FR)

* **FR-001:** The application shall load the building polygon layer from the currently opened QGIS project.  
  *Priority:* High

* **FR-002:** The application shall load the DSM raster layer.  
  *Priority:* High

* **FR-003:** The application shall load the DTM raster layer.  
  *Priority:* High

* **FR-004:** The application shall calculate the median roof elevation for each building polygon.  
  *Priority:* High

* **FR-005:** The application shall calculate the median ground elevation for each building polygon.  
  *Priority:* High

* **FR-006:** The calculated values shall be written into the building attribute table.  
  *Priority:* High

* **FR-007:** The application shall export processed data into a GeoPackage database.  
  *Priority:* Critical

* **FR-008:** The application shall overwrite the destination layer if it already exists.  
  *Priority:* Medium

* **FR-009:** The application shall display a success or failure message after the export operation.  
  *Priority:* Medium

* **FR-010:** The exported GeoPackage shall preserve valid geometries.  
  *Priority:* Critical

* **FR-011:** The application shall preserve all original building geometries.  
  *Priority:* Critical

* **FR-012:** The application shall process every building polygon available in the input layer.  
  *Priority:* High

---

## 9. Non-Functional Requirements (NFR)

* **NFR-001:** The application shall complete processing without unexpected termination (crashes).
* **NFR-002:** The application shall preserve spatial data integrity throughout the process.
* **NFR-003:** The application shall generate a GeoPackage compatible with standard QGIS/GDAL drivers.
* **NFR-004:** The application shall report processing errors clearly to the user.
* **NFR-005:** The application shall produce repeatable results for identical input datasets.
* **NFR-006:** The application shall either process input layers with different CRS correctly or stop processing and clearly report an unsupported CRS configuration.