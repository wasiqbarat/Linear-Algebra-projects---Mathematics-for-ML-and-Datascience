import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# You can check value returned by this function for
# your provided DataFrame "scaled_df", and "k" as
# number of used singular values
def get_percentage(scaled_df: pd.DataFrame, k: int):
    solver = PCA()
    solver.fit_transform(scaled_df)
    return solver.explained_variance_ratio_[:k].sum() * 100


def visualize(original_data, rcnst_list):
    plt.figure(figsize=(10, 10))
    plt.scatter(original_data[:, 0], original_data[:, 1], label='Original Data')
    for i in range(len(rcnst_list)):
        plt.scatter(rcnst_list[i][:, 0], rcnst_list[i][:, 1], label=f"Reconstructed Data {i}")
    plt.title('First two dimensions of Original Data vs. Reconstructed Data')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.legend()
    plt.show()


## Your Code Here!
# df =



# Needs no change
scaler = StandardScaler()
scaled_df = scaler.fit_transform(df)


## Your Code Here!
# You should call your SVD function on scaled_df
# and also use the result for reconstructing the main matrix, for k = 3, 5, 8, 10, 15



## Your Code Here!
# Print retained_percentage for values of k, and check with get_percentage()


## Visualization
# give a list of your reconstructed data as well as original data to visualize()
