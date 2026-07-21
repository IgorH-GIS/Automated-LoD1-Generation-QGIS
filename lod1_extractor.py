import processing
from qgis.core import QgsProject

print("Rozpoczynamy wektorową ekstrakcję wysokości dla akustyka...")

# Pobranie warstw z projektu 
buildings = QgsProject.instance().mapLayersByName('building')[0]
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

print("SUKCES! Dane zintegrowane.")
