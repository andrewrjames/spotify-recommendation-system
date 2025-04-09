import os
import shutil

# Change this to your project directory
base_path = os.getcwd()

# Define the structure
structure = {
    "notebooks": [
        "Data Cleaning.ipynb",
        "RecommendationSystem_v2.ipynb",
        "Song Clustering.ipynb",
        "Team6_Spotify_prediction.ipynb"
    ],
    "data": [
        "top_10000_1960-now.csv"
    ],
    "docs": [
        "Team Presentation.pdf"
    ]
}

# Create folders and move files accordingly
for folder, files in structure.items():
    folder_path = os.path.join(base_path, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file in files:
        original_path = os.path.join(base_path, file)
        new_path = os.path.join(folder_path, file)
        if os.path.exists(original_path):
            shutil.move(original_path, new_path)

print("✅ Files organized successfully!")