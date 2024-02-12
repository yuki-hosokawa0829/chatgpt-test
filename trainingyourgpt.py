import os
from dotenv import load_dotenv
from openai import OpenAI

# 環境変数の読み込み
load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

model = "ft:gpt-3.5-turbo-1106:personal::8pczsXuo"

# 学習用データのファイルパス
uploaded_file_id = "file-w3naoHHvxwmHB8rYzt9Aiqx0"

FineTune = client.fine_tuning.jobs.create(
    training_file = uploaded_file_id,    # アップロードしたファイルのID
    model = model,                       # モデルのID
)

# 出力
#print(FineTune)