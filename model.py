import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
import catboost as cb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("Jewelry_Dataset.csv")

data.columns = [
    "Order_Datetime",
    "Order_ID",
    "Product_id",
    "SKU_Quantity",
    "Category_ID",
    "Category",
    "Brand_ID",
    "Price_USD",
    "User_ID",
    "Target_Gender",
    "Main_Color",
    "Main_Metal",
    "Main_Gem",
]

# Convert Order_Datetime to datetime type
data["Order_Datetime"] = pd.to_datetime(data["Order_Datetime"])

# Extract useful features from Order_Datetime
data["Order_Year"] = data["Order_Datetime"].dt.year
data["Order_Month"] = data["Order_Datetime"].dt.month
data["Order_Day"] = data["Order_Datetime"].dt.day
data["Order_Hour"] = data["Order_Datetime"].dt.hour

# Drop the original Order_Datetime column
data = data.drop(columns=["Order_Datetime"])

# Drop rows with NaN values in the target column
data = data.dropna(subset=["Price_USD"])

# Define feature columns and target column
target = "Price_USD"
features = [col for col in data.columns if col != target]

# Identify categorical features
categorical_features = [
    "Order_ID",
    "Product_id",
    "Category_ID",
    "Category",
    "Brand_ID",
    "User_ID",
    "Target_Gender",
    "Main_Color",
    "Main_Metal",
    "Main_Gem"
]

# Convert categorical features to strings
for col in categorical_features:
    data[col] = data[col].astype(str)

# Split data
X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2, random_state=42)

# Start MLflow experiment
mlflow.set_experiment("Jewelry Price Optimization")

models = {
    "CatBoost": cb.CatBoostRegressor(verbose=0)
}

best_model = None
best_mse = float("inf")

for name, model in models.items():
    with mlflow.start_run(run_name=name):
        model.fit(X_train, y_train, cat_features=categorical_features)
        preds = model.predict(X_test)
        mse = mean_squared_error(y_test, preds)
        
        # Log metrics and model
        mlflow.log_param("model", name)
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, name)
        
        print(f"{name} MSE: {mse}")
        
        if mse < best_mse:
            best_mse = mse
            best_model = model

# Save the best model
mlflow.sklearn.log_model(best_model, "best_model")
print("Best model logged in MLflow.")