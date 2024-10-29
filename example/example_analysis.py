# examples/example_analysis.py
from src.analysis.power_generation import analyze_power_generation
from src.visualization.maps import create_analysis_maps
from src.visualization.plots import create_summary_table

def main():
    # Example paths - replace with your data paths
    time_series_path = 'data/generation_data.csv'
    plant_features_path = 'data/plant_features.csv'
    price_data_path = 'data/price_data.csv'

    # Run analysis
    results = analyze_power_generation(
        time_series_path=time_series_path,
        plant_features_path=plant_features_path,
        price_data_path=price_data_path
    )

    # Create visualizations
    create_analysis_maps(results)
    create_summary_table(results)

if __name__ == "__main__":
    main()