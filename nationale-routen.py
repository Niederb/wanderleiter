import matplotlib.pyplot as plt
import polars as pl

file_path = "./data/Nationale-Routen.csv"
df = pl.read_csv(file_path, separator=',', encoding='UTF-8')
df = df.with_columns((pl.col("KM") + 10/1000 * pl.col("HM")).alias("LKM"))
df = df.with_columns((pl.col("HM") / pl.col("Etappen")).alias("HM/T"))
df = df.with_columns((pl.col("KM") / pl.col("Etappen")).alias("KM/T"))
df = df.with_columns((pl.col("LKM") / pl.col("Etappen")).alias("LKM/T"))


column_to_plot = "HM/T"
df = df.sort(column_to_plot, descending=False)
print(df)

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.barh(df['Name'], df[column_to_plot], edgecolor='black')
plt.xlabel('Länge (Kilometer)')
# plt.ylabel('Name')
plt.title('Längenvergleich der Nationalen Routen')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()