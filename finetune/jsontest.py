import json
import os.path

# データを呼び出して文字列なら間の改行コードは削除する関数
def remove_newline(data):
    new_data = {}
    for key, value in data.items():
        if isinstance(key, str):
            key = key.replace('\n', '')
        if isinstance(value, str):
            value = value.replace('\n', '')
        new_data[key] = value
    return new_data

# ファイルパスを入力させる
while True:
    file_path = input("Enter the file path: ")
    if os.path.isfile(file_path):
        break
    else:
        print("Invalid file path. Please try again.")

# ファイルを読み込む
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# ファイルの改行削除をする
data = remove_newline(data)

# ファイルを上書きする
while True:
    save_path = input("Enter the save path: ")
    if os.path.isdir(os.path.dirname(save_path)):
        break
    else:
        print("Invalid save path. Please try again.")
with open(save_path, 'w', encoding='utf-8') as file:
    json.dump(data, file)
