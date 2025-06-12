# dbscan_kmeans_hybrid.py
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def hybrid_clustering_with_dbscan(csv_path, eps=0.6, min_samples=5):
    df = pd.read_csv(csv_path)
    features = df[['Strategic planning', 'Leadership style', 'Risk management',
                   'Operational detail', 'Sustainability', 'Innovation', 'Financial stability']]

    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    pca = PCA(n_components=2)
    pca_components = pca.fit_transform(features_scaled)

    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    df["DBSCAN_Cluster"] = dbscan.fit_predict(pca_components)

    df.to_csv("hybrid_dbscan_results.csv", index=False)

# Example usage:
# hybrid_clustering_with_dbscan("clustered_results.csv")
