from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt

# Initialize PySpark session
spark = SparkSession.builder.appName("CompareCarModels").getOrCreate()

# Load CSV data into PySpark DataFrame
data_path = "car_data.csv"  # Replace with the actual path to your CSV file
df = spark.read.csv(data_path, header=True, inferSchema=True)

# Show the loaded data
df.show()

# Select relevant columns for analysis
selected_columns = df.select("Year", "Month", "Make", "Model", "Pct")
selected_columns.show()

# Convert PySpark DataFrame to Pandas DataFrame for Scikit-learn
pandas_df = selected_columns.toPandas()

# Encode categorical data (Make, Model) for Scikit-learn
pandas_df_encoded = pd.get_dummies(pandas_df, columns=["Make", "Model"], drop_first=True)

# Features and target variable
X = pandas_df_encoded.drop(columns=["Year", "Month", "Pct"])
y = pandas_df_encoded["Pct"]

# Scale the features using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Visualize comparison of models
plt.figure(figsize=(10, 6))
pandas_df.groupby("Model")["Pct"].mean().plot(kind="bar", color="skyblue")
plt.title("Comparison of Car Models by Percentage Shares")
plt.xlabel("Car Model")
plt.ylabel("Percentage Share")
plt.xticks(rotation=45)
plt.show()

# Stop the Spark session
spark.stop()
