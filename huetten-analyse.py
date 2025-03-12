import polars as pl

# Define the file path
file_path = "./data/SAC-Huetten.csv"

# Read the CSV file into a Polars DataFrame
df = pl.read_csv(file_path, separator=';', encoding='UTF-8')

# Print the DataFrame
print(df)