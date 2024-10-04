def create_new_features(df):
    """Create new features for the dataset."""
    df['new_feature'] = df['existing_column'] ** 2  # Example of feature engineering
    print("New features created successfully!")
    return df

if __name__ == "__main__":
    from data_loading import load_data
    df = load_data("data/dataset.csv")
    df = create_new_features(df)
