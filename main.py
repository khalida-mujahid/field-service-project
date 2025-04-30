from fastapi import FastAPI
import pandas as pd
import os
import uvicorn
from config import BASE_DIR

app = FastAPI()

# Load pre-engineered feature dataset
# Make sure correct csv file name from notebooks/sample_features
df = pd.read_csv(os.path.join(BASE_DIR, "notebooks\sample_features\part-00000-e3e9e96d-05d1-4dcf-9131-cd7d6e09bdce-c000.csv"))

@app.get("/features/")
async def get_features(n: int = 5):
    clean_df = df.head(n).replace([float('inf'), float('-inf')], None).fillna("")
    return clean_df.head(n).to_dict(orient="records")

# This block allows running the server with `python main.py`
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
