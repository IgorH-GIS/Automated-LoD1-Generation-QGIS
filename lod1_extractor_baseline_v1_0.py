import processing
from qgis.core import QgsProject

print("Rozpoczynamy wektorową ekstrakcję wysokości dla akustyka...")

# Pobranie warstw z projektu 
buildings = QgsProject.instance().mapLayersByName('Polygons')[0]
dsm = QgsProject.instance().mapLayersByName('dsm')[0]
dtm = QgsProject.instance().mapLayersByName('dtm_prudnik_clean')[0]

# 1. Wstrzyknięcie rzędnych dachu z DSM
print("1/2: Pobieram wysokości dachów...")
processing.run("qgis:zonalstatistics", {
    'INPUT_RASTER': dsm.source(),
    'RASTER_BAND': 1,
    'INPUT_VECTOR': buildings,
    'COLUMN_PREFIX': 'ROOF_',
    'STATS': [3] # Mediana (odrzuca kominy i anteny)
})

# 2. Wstrzyknięcie rzędnych gruntu z DTM
print("2/2: Pobieram rzędne fundamentów...")
processing.run("qgis:zonalstatistics", {
    'INPUT_RASTER': dtm.source(),
    'RASTER_BAND': 1,
    'INPUT_VECTOR': buildings,
    'COLUMN_PREFIX': 'GND_',
    'STATS': [3] 
})

# --- ZAPIS DO FIZYCZNEJ BAZY DANYCH (Rozwiązanie błędu 'Silent Failure') ---

# 1. Zdefiniuj bezwzględną ścieżkę do Twojego pliku GPKG (zmień na swoją!)
sciezka_gpkg = r"C:\Project\Cemetery Spatial Data Restructuring\cemetery_records.gpkg"

# 2. Skonfiguruj opcje zapisu dla GeoPackage
opcje_zapisu = QgsVectorFileWriter.SaveVectorOptions()
opcje_zapisu.driverName = "GPKG"
opcje_zapisu.layerName = "buildings_lod1_wynik" # Nazwa tabeli, która powstanie w bazie
opcje_zapisu.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteLayer # Nadpisz tabelę, jeśli istnieje

# 3. Zapisz warstwę 'buildings' na dysk
blad, komunikat = QgsVectorFileWriter.writeAsVectorFormatV3(
    buildings, 
    sciezka_gpkg, 
    QgsProject.instance().transformContext(), 
    opcje_zapisu
)

if blad == QgsVectorFileWriter.NoError:
    print("SUKCES! Dane zintegrowane i zapisane fizycznie do bazy GPKG.")
else:
    print(f"BŁĄD ZAPISU: {komunikat}")