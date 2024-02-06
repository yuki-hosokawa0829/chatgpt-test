import json
import os
from dotenv import load_dotenv
from openai import OpenAI

# 環境変数の読み込み
load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

# 学習用データのファイルパス
filepath_to_jsonl = "./data/training.jsonl"

# ファイルアップロード（学習）
upload_file_train = client.files.create(
    file=open(filepath_to_jsonl, "rb"),    # ファイルJSON
    purpose='fine-tune'                 # ファイルのアップロード目的
    )

# 出力
print(upload_file_train)