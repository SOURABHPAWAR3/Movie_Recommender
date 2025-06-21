# download_dataset.py

import os
import zipfile
import requests

# URL for MovieLens small dataset
url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
zip_path = "data/ml-latest-small.zip"
extract_path = "data/"

def download_dataset():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(zip_path):
        print("📥 Downloading dataset...")
        response = requests.get(url)
        with open(zip_path, "wb") as f:
            f.write(response.content)
        print("✅ Download complete.")
    else:
        print("✅ Dataset zip already exists.")

    # Extract the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
        print("📦 Extracted successfully.")

if __name__ == "__main__":
    download_dataset()
