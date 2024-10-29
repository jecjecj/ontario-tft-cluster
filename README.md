# GenCluster_CONCAPAN_XLII
This repository contains a comprehensive tool for analyzing power generation patterns using clustering and time series analysis techniques.

## Features
- Power plant clustering using HDBSCAN
- Time series analysis with Dynamic Time Warping (DTW)
- Geographical visualization of power plants
- Generation pattern analysis
- Price response analysis

## Installation
```bash
git clone https://github.com/yourusername/power-generation-analysis.git
cd power-generation-analysis
pip install -r requirements.txt
```

## Usage
```python
from src.analysis.power_generation import analyze_power_generation
from src.visualization.maps import create_analysis_maps

# Run analysis
results = analyze_power_generation(
    time_series_path='path/to/generation_data.csv',
    plant_features_path='path/to/plant_features.csv',
    price_data_path='path/to/price_data.csv'
)

# Create visualizations
create_analysis_maps(results)
```

## Data Format
### Required CSV files:
1. Generation Data (time_series_path):
   - time: datetime
   - streamName: string
   - power_generated: float

2. Plant Features (plant_features_path):
   - streamName: string
   - lat: float
   - lon: float
   - fuel: string
   - capacity: float

3. Price Data (price_data_path):
   - time: datetime
   - Price - Disp [HOEP]: float

## License
MIT License
