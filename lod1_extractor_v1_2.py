import processing

from qgis.core import (
    QgsProject,
    QgsVectorFileWriter
)

print("Rozpoczynamy wektorową ekstrakcję wysokości dla akustyka...")

# Pobranie i walidacja wymaganych warstw
building_layers = QgsProject.instance().mapLayersByName("Polygons")
dsm_layers = QgsProject.instance().mapLayersByName("dsm")
dtm_layers = QgsProject.instance().mapLayersByName("dtm_prudnik_clean")

if not building_layers:
    raise RuntimeError(
        "Required building layer 'Polygons' was not found in the current QGIS project."
    )

if not dsm_layers:
    raise RuntimeError(
        "Required DSM layer 'dsm' was not found in the current QGIS project."
    )

if not dtm_layers:
    raise RuntimeError(
        "Required DTM layer 'dtm_prudnik_clean' was not found in the current QGIS project."
    )

buildings = building_layers[0]
dsm = dsm_layers[0]
dtm = dtm_layers[0]

# 1. Mediana rzędnej dachu z DSM
print("1/2: Pobieram medianę wysokości dachów...")

roof_result = processing.run("native:zonalstatisticsfb", {
    'INPUT': buildings,
    'INPUT_RASTER': dsm,
    'RASTER_BAND': 1,
    'COLUMN_PREFIX': 'ROOF_',
    'STATISTICS': [3],
    'OUTPUT': 'TEMPORARY_OUTPUT'
})

buildings_with_roof = roof_result['OUTPUT']

# 2. Mediana rzędnej gruntu z DTM
print("2/2: Pobieram medianę rzędnych gruntu...")

ground_result = processing.run("native:zonalstatisticsfb", {
    'INPUT': buildings_with_roof,
    'INPUT_RASTER': dtm,
    'RASTER_BAND': 1,
    'COLUMN_PREFIX': 'GND_',
    'STATISTICS': [3],
    'OUTPUT': 'TEMPORARY_OUTPUT'
})

buildings_result = ground_result['OUTPUT']

# 3. Zapis wyniku do GeoPackage
sciezka_gpkg = r"C:\Project\LoD1_QA_Test_Data\outputs\lod1_test_output.gpkg"

opcje_zapisu = QgsVectorFileWriter.SaveVectorOptions()
opcje_zapisu.driverName = "GPKG"
opcje_zapisu.layerName = "buildings_lod1_wynik"
opcje_zapisu.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteFile

blad, komunikat, nowa_sciezka, nowa_warstwa = (
    QgsVectorFileWriter.writeAsVectorFormatV3(
        buildings_result,
        sciezka_gpkg,
        QgsProject.instance().transformContext(),
        opcje_zapisu
    )
)

if blad == QgsVectorFileWriter.NoError:
    print("SUKCES! Dane zapisane do GeoPackage.")
else:
    print(f"BŁĄD ZAPISU: {komunikat}")