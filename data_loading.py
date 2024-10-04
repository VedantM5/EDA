import pandas as pd

def load_data(file_path):
    """Loads the dataset from the provided file path."""
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    file_path = "data/dataset.csv"  # Example path
    data = load_data(file_path)
