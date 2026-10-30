# File Organizer

拡張子ごとにファイルを自動で仕分けるPythonツールです。

## 使い方

```
$ python organizer.py sample_files --dry-run
$ python organizer.py sample_files

```

| 引数 | 説明 |
|---|---|
| `folder` | 整理するフォルダのパス |
| `--dry-run` | 実際には移動せず、移動予定だけを表示する |

## 実行例

```
$ python organizer.py sample_files --dry-run

[確認モード] 実際には移動しません
sample_files\data.csv -> sample_files\data\data.csv
sample_files\image.png -> sample_files\images\image.png
sample_files\memo.txt -> sample_files\documents\memo.txt
sample_files\photo.jpg -> sample_files\images\photo.jpg
sample_files\report.pdf -> sample_files\documents\report.pdf
sample_files\song.mp3 -> sample_files\others\song.mp3
合計 6 ファイル

$ python organizer.py sample_files

sample_files\data.csv -> sample_files\data\data.csv
sample_files\image.png -> sample_files\images\image.png
sample_files\memo.txt -> sample_files\documents\memo.txt
sample_files\photo.jpg -> sample_files\images\photo.jpg
sample_files\report.pdf -> sample_files\documents\report.pdf
sample_files\song.mp3 -> sample_files\others\song.mp3
合計 6 ファイル

$ python organizer.py sample_files --dry-run

[確認モード] 実際には移動しません
[スキップ] sample_files\data\data.csv は既に存在します
[スキップ] sample_files\images\image.png は既に存在します
[スキップ] sample_files\documents\memo.txt は既に存在します
[スキップ] sample_files\images\photo.jpg は既に存在します
[スキップ] sample_files\documents\report.pdf は既に存在します
[スキップ] sample_files\others\song.mp3 は既に存在します
合計 0 ファイル

```

## 安全のための工夫

- **確認モード（--dry-run）**：ファイルの移動は、間違えると元に戻すのが大変です。そこで、実際には移動せずに移動予定だけを表示する確認モードを用意し、結果を確かめてから本番を実行できるようにしました。
- **上書きの防止**：移動先に同じ名前のファイルがある場合は、移動せずにスキップします。この確認がないと、Windowsではエラーで処理が途中で止まり、LinuxやmacOSでは既存のファイルが上書きされて失われるおそれがあります。

## 工夫した点

- **仕分けルールを設定として分離**：拡張子と仕分け先の対応を、ファイル冒頭の辞書 `CATEGORIES` にまとめました。たとえば `".docx": "documents"` を1行追加するだけで新しい拡張子に対応でき、処理部分のコードを変更する必要がありません。
- **未知の拡張子への対応**：辞書にない拡張子のファイルは `others` フォルダにまとめ、仕分けから漏れるファイルが出ないようにしました。

## 使用技術

- Python 3.12
- 標準ライブラリのみ（argparse、pathlib）