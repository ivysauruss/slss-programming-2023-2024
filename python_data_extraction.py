# Excel Pandas 
# Author: Alissa Xu
# Date Created: 2 November 2023
from pathlib import Path
import pandas as pd

CURRENT_DIR = Path(__file__).parent


dataset = CURRENT_DIR / './kNNRegressor_LHS_Base_Case_v0_Results.xlsx'


df = pd.read_excel(dataset, sheet_name=0)


df["difference greenR2 blueR2"] = df["green_R2_test_subsample"] - df["blue_R2_test_subsample"]
df["difference greenR2 redR2"] = df["green_R2_test_subsample"] - df["red_R2_test_subsample"]
df["difference greenR2 yellowR2"] = df["green_R2_test_subsample"] - df["yellow_R2_test_subsample"]
df["difference blueR2 redR2"] = df["blue_R2_test_subsample"] - df["red_R2_test_subsample"]
df["difference blueR2 yellowR2"] = df["blue_R2_test_subsample"] - df["yellow_R2_test_subsample"]
df["difference redR2 yellowR2"] = df["red_R2_test_subsample"] - df["yellow_R2_test_subsample"]


df['max_R2_difference'] = df[['difference greenR2 blueR2', 'difference greenR2 redR2', 'difference greenR2 yellowR2', 'difference blueR2 redR2', 'difference blueR2 yellowR2', 'difference redR2 yellowR2']].max(axis=1)
df['max_R2_difference_id'] = df[['difference greenR2 blueR2', 'difference greenR2 redR2', 'difference greenR2 yellowR2', 'difference blueR2 redR2', 'difference blueR2 yellowR2', 'difference redR2 yellowR2']].idxmax(axis=1)

max_R2_diff = df['max_R2_difference']
max_R2_id = df['max_R2_difference_id']

df["difference green rmse blue rmse"] = df["green_rmse_test_subsample"] - df["blue_rmse_test_subsample"]
df["difference green rmse red rmse"] = df["green_rmse_test_subsample"] - df["red_rmse_test_subsample"]
df["difference green rmse yellow rmse"] = df["green_rmse_test_subsample"] - df["yellow_rmse_test_subsample"]
df["difference blue rmse red rmse"] = df["blue_rmse_test_subsample"] - df["red_rmse_test_subsample"]
df["difference blue rmse yellow rmse"] = df["blue_rmse_test_subsample"] - df["yellow_rmse_test_subsample"]
df["difference red rmse yellow rmse"] = df["red_rmse_test_subsample"] - df["yellow_rmse_test_subsample"]


df['max_rmse_difference'] = df[['difference green rmse blue rmse', 'difference green rmse red rmse', 'difference green rmse yellow rmse', 'difference blue rmse red rmse', 'difference blue rmse yellow rmse', 'difference red rmse yellow rmse']].max(axis=1)
df['max_rmse_difference_id'] = df[['difference green rmse blue rmse', 'difference green rmse red rmse', 'difference green rmse yellow rmse', 'difference blue rmse red rmse', 'difference blue rmse yellow rmse', 'difference red rmse yellow rmse']].idxmax(axis=1)

max_rmse_diff = df['max_rmse_difference']
max_rmse_id = df['max_rmse_difference_id']

print(f"{max_R2_diff}, {max_R2_id}")

print(f"{max_rmse_diff}, {max_rmse_id}")


import matplotlib.pyplot as plt

plt.figure(figsize=(20, 14))
plt.plot(df['num_samples'], df['max_R2_difference'], marker='o', linestyle='-')
plt.title('R2 Maximum Difference vs Sample Size')
plt.xlabel('Sample Size')
plt.ylabel('R2 Maximum Difference')
plt.grid(True)
plt.show()

plt.figure(figsize=(20, 14))
plt.plot(df['num_samples'], df['max_rmse_difference'], marker='o', linestyle='-')
plt.title('rmse Maximum Difference vs Sample Size')
plt.xlabel('Sample Size')
plt.ylabel('rmse Maximum Difference')
plt.grid(True)
plt.show()