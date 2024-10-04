import seaborn as sns
import matplotlib.pyplot as plt

def correlation_matrix(df):
    """Generate and plot a correlation matrix."""
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Matrix")
    plt.show()

if __name__ == "__main__":
    from data_loading import load_data
    df = load_data("data/dataset.csv")
    correlation_matrix(df)
