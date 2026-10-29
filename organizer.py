from pathlib import Path


CATEGORIES = {
    ".pdf": "documents",
    ".txt": "documents",
    ".jpg": "images",
    ".png": "images",
    ".csv": "data",
}


folder = Path("sample_files")

for item in folder.iterdir():
    if item.is_file():
        folder_name = CATEGORIES.get(item.suffix, "others")
        dest = folder / folder_name / item.name
        print(f"{item} -> {dest}")