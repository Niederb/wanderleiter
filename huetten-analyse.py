import os
import matplotlib.pyplot as plt
import polars as pl

file_path = "./data/SAC-Huetten.csv"
df = pl.read_csv(file_path, separator=';', encoding='UTF-8')

kanton_series = df['Kanton'].drop_nulls()
kanton_counts = kanton_series.value_counts().sort('count')
print(len(kanton_series))

# Convert the sorted counts to lists for plotting
kanton_labels = kanton_counts['Kanton'].to_list()
kanton_frequencies = kanton_counts['count'].to_list()

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.bar(kanton_labels, kanton_frequencies, edgecolor='black', text_auto=True)
plt.xlabel('Kanton')
plt.ylabel('Anzahl')
plt.title('Anzahl SAC-Hütten pro Kanton')
plt.xticks(rotation=90)
plt.tight_layout()
os.makedirs("output", exist_ok = True)
plt.savefig("output/SAC-Hütten-pro-Kanton.png", dpi=300)