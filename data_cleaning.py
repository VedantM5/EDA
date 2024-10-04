def clean_data(df):
    """Clean the provided DataFrame."""
    df = df.dropna()  # Drop missing values as an example
    print("Data cleaned successfully!")
    return df

if __name__ == "__main__":
    from data_loading import load_data
    df = load_data("data/dataset.csv")
    cleaned_df = clean_data(df)
