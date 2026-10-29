from pathlib import Path
folder = Path("sample_files")

for item in folder.iterdir():
    if item.is_file():
        print(f"{item.name} -> {item.suffix}")