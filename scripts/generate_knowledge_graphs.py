# generate_knowledge_graphs.py
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def bin_score(value):
    if value >= 0.75:
        return "High"
    elif value >= 0.6:
        return "Medium"
    else:
        return "Low"

def market_cap_bin(value):
    if value >= 200:
        return "Mega-Cap"
    elif value >= 10:
        return "Large-Cap"
    else:
        return "Mid-Cap"

def build_kg_for_cluster(df, cluster_id, label_column, output_path):
    G = nx.Graph()
    cluster_df = df[df[label_column] == cluster_id].copy()

    for _, row in cluster_df.iterrows():
        company = row['Company']
        G.add_node(company, type='company')

        # Add categorical trait nodes
        for trait in ['Strategic planning', 'Leadership style', 'Risk management', 'Sustainability', 'Innovation', 'Financial stability']:
            level = bin_score(row[trait])
            node_name = f"{trait}: {level}"
            G.add_node(node_name, type='trait')
            G.add_edge(company, node_name)

        # Add MarketCap category
        cap = market_cap_bin(row['MarketCap'])
        G.add_node(cap, type='size')
        G.add_edge(company, cap)

    pos = nx.spring_layout(G, seed=42)
    node_colors = ['lightblue' if G.nodes[n]['type'] == 'company' else
                   'lightgreen' if G.nodes[n]['type'] == 'trait' else
                   'orange' for n in G.nodes]

    plt.figure(figsize=(14, 10))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=600, font_size=8)
    plt.title(f"Knowledge Graph for Cluster {cluster_id}")
    plt.tight_layout()
    plt.savefig(f"{output_path}/knowledge_graph_cluster_{cluster_id}.png")
    plt.close()
    print(f"Saved Cluster {cluster_id} KG.")

def generate_all_knowledge_graphs(input_csv, label_column='KMeansCluster', output_path='kg_outputs'):
    import os
    os.makedirs(output_path, exist_ok=True)

    df = pd.read_csv(input_csv)
    for cluster_id in sorted(df[label_column].dropna().unique()):
        build_kg_for_cluster(df, cluster_id, label_column, output_path)

# Example usage:
# generate_all_knowledge_graphs("clustered_results.csv")
