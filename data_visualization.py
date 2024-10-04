import matplotlib.pyplot as plt

def plot_histogram(df, column):
    """Plot histogram of a specific column."""
    plt.hist(df[column], bins=20, color='blue', edgecolor='black')
    plt.title(f"Histogram of {column}")
    plt.show()

if __name__ == "__main__":
    from data_loading import load_data
    df = load_data("data/dataset.csv")
    plot_histogram(df, 'age')  # Example column
