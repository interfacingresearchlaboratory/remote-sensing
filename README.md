# Remote Sensing Library

A working archive of Google Earth Engine scripts and geospatial reference datasets for remote sensing, infrastructure mapping, and environmental change analysis.

The repository brings together small Python recipes for Landsat, Sentinel-1, Sentinel-2, and SRTM workflows, alongside vector datasets for China, Hong Kong, the United Kingdom, and global infrastructure systems.

## Contents

### Earth Engine scripts

| File | Sensor / dataset | Purpose |
| --- | --- | --- |
| `L.py` | Landsat 4/5/7/8 | Builds a low-cloud RGB Landsat composite across multiple missions. |
| `L_HKUrbanChange_2017.py` | Landsat 4/5/7/8 | Creates multi-temporal RGB composites for Hong Kong urban-change inspection. |
| `L_MT.py` | Landsat 4/5/7/8 | Compares Landsat composites across historical time windows. |
| `L_NDVI.py` | Landsat 4/5/7/8 | Computes vegetation signal using Normalized Difference Vegetation Index. |
| `L_NDVI_MT.py` | Landsat 4/5/7/8 | Compares vegetation change across multiple Landsat periods. |
| `L_NDWI_MT.py` | Landsat 4/5/7/8 | Compares water signal across multiple Landsat periods. |
| `L_NDMI.py` | Landsat 4/5/7/8 | Computes moisture signal using Normalized Difference Moisture Index. |
| `L_NDMI_MT.py` | Landsat 4/5/7/8 | Compares moisture signal across multiple Landsat periods. |
| `L_NDBI_MT.py` | Landsat 4/5/7/8 | Compares built-up area signal across multiple Landsat periods. |
| `L_NDCI.py` | Landsat 4/5/7/8 | Computes chlorophyll-related index signal. |
| `L_NDCI_MT.py` | Landsat 4/5/7/8 | Compares chlorophyll-related signal across multiple Landsat periods. |
| `S1_Shipping.py` | Sentinel-1 SAR GRD | Creates VH radar composites for shipping and surface-structure inspection. |
| `S2_NDVI.py` | Sentinel-2 | Computes cloud-masked vegetation signal. |
| `S2_NDWI.py` | Sentinel-2 | Computes cloud-masked water signal. |
| `S2_NDCI.py` | Sentinel-2 | Computes cloud-masked chlorophyll-related signal. |
| `SRTM30.py` | SRTM 30 m DEM | Displays terrain elevation from SRTM. |
| `js_to_py.ipynb` | Notebook | Scratch notebook for translating Earth Engine JavaScript examples into Python. |

### Dataset folders

| Folder | Contents |
| --- | --- |
| `China Datasets/` | Administrative boundaries, road, rail, water, hydro basin, airport, railway, and sea-port datasets. |
| `Hong Kong Datasets/` | Administrative boundaries, roads, rails, water layers, and storm-pipe data. |
| `UK Datasets/` | Green belts, rail, road, canal, regional boundary, HS2, mining, and historical-road layers. |
| `Global Dams/` | GOOD, GRanD, OSM dam, reservoir, and catchment datasets. |
| `Global Ports/` | World Port Index and WFP global port datasets. |
| `Global Power Plants/` | Global Power Plant Database archive and documentation. |
| `Global Railroads/` | Natural Earth global railroad shapefile and metadata. |

## Requirements

The scripts are designed for Google Earth Engine's Python API and the QGIS Earth Engine plugin map interface:

```bash
pip install earthengine-api
```

You also need:

- A Google Earth Engine account.
- Earth Engine authentication on your machine.
- QGIS with `ee_plugin` if you want to run the scripts exactly as written with `from ee_plugin import Map`.

Authenticate Earth Engine:

```bash
earthengine authenticate
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/interfacingresearchlaboratory/remote-sensing.git
cd remote-sensing
```

2. Open a script in QGIS Python Console, a notebook, or your preferred Python environment with Earth Engine configured.

3. Adjust the date ranges, cloud thresholds, regions of interest, and visualization palettes inside the script.

4. Run the script and inspect the generated layer on the Earth Engine map.

Example:

```python
import ee
from ee_plugin import Map

dataset = ee.Image("USGS/SRTMGL1_003").select("elevation")

Map.addLayer(
    dataset,
    {"min": 0, "max": 2000, "palette": ["Black", "White"], "opacity": 1},
    "SRTM elevation",
)
```

## Notes

- Several scripts use older Earth Engine Landsat Collection 1 IDs. If a dataset has been deprecated in your Earth Engine environment, migrate the asset IDs and band names to the current collection before running.
- Some files are research sketches rather than packaged library functions. Treat them as starting points for analysis workflows.
- Large geospatial datasets may have their own licenses and attribution requirements. Check source documentation before reuse or redistribution.
- Shapefile layers require their companion files (`.shp`, `.shx`, `.dbf`, `.prj`) to stay together.

## Data Sources

| Data | Link |
| --- | --- |
| Administrative Boundaries | [https://gadm.org/data.html](https://gadm.org/data.html) |
| Global Humanitarian Data | [https://data.humdata.org/](https://data.humdata.org/) |
| Global Dam Database | [http://globaldamwatch.org/data/#core_global](http://globaldamwatch.org/data/#core_global) |
| Global River Basins | [https://www.bafg.de/GRDC/EN/02_srvcs/22_gslrs/221_MRB/riverbasins_node.html#Start](https://www.bafg.de/GRDC/EN/02_srvcs/22_gslrs/221_MRB/riverbasins_node.html#Start) |
| Global railroads | [Natural Earth](https://www.naturalearthdata.com/) |
| Global power plants | [World Resources Institute Global Power Plant Database](https://datasets.wri.org/dataset/globalpowerplantdatabase) |

## Contributing

Contributions are welcome, especially:

- Updated Earth Engine Collection 2 versions of the Landsat scripts.
- Clearer regions of interest and reproducible example parameters.
- Additional spectral indices or sensor recipes.
- Dataset source notes, licenses, and citations.
- Cleanup of generated files such as `.DS_Store` and notebook checkpoints.

Please keep contributions small and documented. If you add a script, include:

- Sensor or dataset name.
- Index or analysis purpose.
- Date range.
- Required region of interest.
- Output layer name and visualization parameters.

## License

No license is currently declared in this repository. Until one is added, reuse of code and bundled datasets may be restricted. Dataset-specific licenses still apply.
