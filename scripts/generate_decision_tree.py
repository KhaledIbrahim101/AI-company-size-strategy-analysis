# generate_decision_tree.py
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz, plot_tree
import matplotlib.pyplot as plt

def build_and_visualize_decision_tree(input_csv,
                                      label_col='Cluster',  # or any aggregated target
                                      feature_cols=None,
                                      max_depth=3,
                                      output_prefix='decision_tree'):
    df = pd.read_csv(input_csv)
    if not feature_cols:
        feature_cols = [c for c in df.columns
                        if c not in ('Company', label_col)]
    
    # Discard rows with missing data
    df = df.dropna(subset=feature_cols + [label_col])
    
    X = df[feature_cols]
    y = df[label_col]
    
    clf = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    clf.fit(X, y)
    
    # 1. Text summary
    from sklearn.tree import export_text
    text = export_text(clf, feature_names=feature_cols)
    with open(f"{output_prefix}.txt", "w") as f:
        f.write(text)
    print(f"✅ Text tree saved to {output_prefix}.txt")
    
    # 2. Matplotlib plot
    plt.figure(figsize=(20,10))
    plot_tree(clf,
              feature_names=feature_cols,
              class_names=[str(c) for c in clf.classes_],
              filled=True, rounded=True)
    plt.savefig(f"{output_prefix}.png")
    plt.close()
    print(f"✅ Tree plot saved to {output_prefix}.png")
    
    # 3. Graphviz export (DOT)
    dot = export_graphviz(clf,
                          out_file=None,
                          feature_names=feature_cols,
                          class_names=[str(c) for c in clf.classes_],
                          filled=True, rounded=True)
    with open(f"{output_prefix}.dot", "w") as f:
        f.write(dot)
    print(f"✅ Graphviz DOT saved to {output_prefix}.dot")
    print("\nYou can convert .dot to image via:")
    print(f"  dot -Tpng {output_prefix}.dot -o {output_prefix}_graphviz.png")
