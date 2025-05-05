import os
import matplotlib.pyplot as plt
import polars as pl

file_path = "./data/Nationale-Routen.csv"
df = pl.read_csv(file_path, separator=',', encoding='UTF-8')
df = df.with_columns((pl.col("KM") + 10/1000 * pl.col("HM")).alias("LKM"))
df = df.with_columns((pl.col("HM") / pl.col("Etappen")).alias("HM/T"))
df = df.with_columns((pl.col("KM") / pl.col("Etappen")).alias("KM/T"))
df = df.with_columns((pl.col("LKM") / pl.col("Etappen")).alias("LKM/T"))
print(df)


column_to_plot = "KM"
df = df.sort(column_to_plot, descending=False)

plt.figure(figsize=(10, 6))
plt.barh(df['Name'], df[column_to_plot], edgecolor='black')
plt.xlabel('Länge (Kilometer)')
plt.title('Längenvergleich der Nationalen Routen')
plt.xticks(rotation=90)
plt.tight_layout()
os.makedirs("output", exist_ok = True)
plt.savefig("output/Nationale-Routen-Länge.png", dpi=300)

column_to_plot = "HM"
df = df.sort(column_to_plot, descending=False)
plt.figure(figsize=(10, 6))
plt.barh(df['Name'], df[column_to_plot], edgecolor='black')
plt.xlabel('Höhenmeter')
plt.title('Höhenmetervergleich der Nationalen Routen')
plt.xticks(rotation=90)
plt.tight_layout()
os.makedirs("output", exist_ok = True)
plt.savefig("output/Nationale-Routen-Höhenmeter.png", dpi=300)