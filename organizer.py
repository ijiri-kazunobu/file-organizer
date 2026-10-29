import argparse
from pathlib import Path


CATEGORIES = {
    ".pdf": "documents",
    ".txt": "documents",
    ".jpg": "images",
    ".png": "images",
    ".csv": "data",
}

def organize(folder, dry_run):
    if dry_run:
        print("[確認モード] 実際には移動しません")

    count = 0
    for item in folder.iterdir():
        if item.is_file():
            folder_name = CATEGORIES.get(item.suffix, "others")
            dest = folder / folder_name / item.name

            if dest.exists():
                print(f"[スキップ] {dest} は既に存在します")
                continue

            print(f"{item} -> {dest}")
            if not dry_run:
                dest.parent.mkdir(exist_ok = True)
                item.rename(dest)
            count += 1

    print(f"合計 {count} ファイル")


parser = argparse.ArgumentParser(description="拡張子ごとにファイルを仕分けるツール")
parser.add_argument("folder", help="整理するフォルダのパス")
parser.add_argument("--dry-run", action="store_true", help="実際には移動せず、結果だけを表示する")
args = parser.parse_args()

organize(Path(args.folder), args.dry_run)