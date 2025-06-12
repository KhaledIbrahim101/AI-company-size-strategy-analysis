# MBA Thesis Project

**Objective:** Map the relationship between company size and long‑term strategies using AI on SEC 10‑K filings and financial data.

**Folder Structure:**
   - data:
      -  Zero-Shot Company Label Scores: Contains strategic labels scores of each company.
      -  Yahoo Finance Dataset: Contains company size metrics like revenues, market cap and number of employees.
      -  Clustering Assignments: Contains assignments of clusters to companies.
      -  Hybrid_DBSCSN_Cluster_AssignmentS: Contains refined assignments of DBSCAN algorithm
      -  Full Results: Contains the merged full results of the data pipeline.
   - scripts: explained in data pipeline section
      
## 📥 Data Pipeline

1. **Parsing Step**  
   - `sec_parser.py`: download 10‑K filings from SEC.  
   - `yahoo_finance_parser.py`: fetch financial data (MarketCap, P/E, etc.) from Yahoo Finance.

2. **Merge Step**  
   - `merge_yahoo_and_10k.py`: combines SEC sentence‑level strategic labels with financial data.

3. **Classification Step**  
   - `zero_shot_classifier.py`: use zero‑shot BART to label sentences.

4. **Clustering Step**  
   - `pca_and_clustering.py`: scale features, run PCA, K‑Means & Hierarchical clustering.

5. **Refinement Step**  
   - `dbscan_kmeans_hybrid.py`: fine‑tune clusters using DBSCAN.

6. **Visualization Step**  
   - `generate_knowledge_graphs.py`: create cluster‑wise knowledge graphs.  
   - `generate_decision_tree.py`: build a decision tree to explain cluster assignments.

## ⚙️ Setup
-  pip install -r requirements.txt

### Conda
-  conda env create -f environment.yml
-  conda activate mba-thesis

## 🚀 Usage
-  Run the workflow in sequence:
   -  python scripts/sec_parser.py
   -  python scripts/yahoo_finance_parser.py
   -  python scripts/merge_yahoo_and_10k.py
   -  python scripts/zero_shot_classifier.py
   -  python scripts/pca_and_clustering.py
   -  python scripts/dbscan_kmeans_hybrid.py
   -  python scripts/generate_knowledge_graphs.py
   -  python scripts/generate_decision_tree.py

## 📦 Outputs
-  data/*.csv – Intermediate and final datasets
-  data/kg_outputs/*.png – Knowledge graphs
-  decision_tree*.png/.dot/.txt – Decision tree visualizations

