# pca_and_clustering.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt

def run_pca_and_clustering(input_csv, n_clusters=4):
    df = pd.read_csv(input_csv)
    features = df[['Strategic planning', 'Leadership style', 'Risk management',
                   'Operational detail', 'Sustainability', 'Innovation', 'Financial stability']]

    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(features_scaled)
    df[['PC1', 'PC2']] = principal_components

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['KMeansCluster'] = kmeans.fit_predict(features_scaled)

    hier = AgglomerativeClustering(n_clusters=n_clusters)
    df['HierCluster'] = hier.fit_predict(features_scaled)

    df.to_csv("clustered_results.csv", index=False)

    plt.figure()
    plt.scatter(df['PC1'], df['PC2'], c=df['KMeansCluster'], cmap='tab10')
    plt.title("K-Means Clustering (PCA)")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.savefig("kmeans_pca_plot.png")

# Example usage:
# run_pca_and_clustering("merged_results.csv")
