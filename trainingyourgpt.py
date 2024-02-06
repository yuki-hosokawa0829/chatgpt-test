import os
from dotenv import load_dotenv
from openai import OpenAI

# 環境変数の読み込み
load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

# 学習用データのファイルパス
uploaded_file_id = "file-xNMhnFEnqrVgwmCwXRSUKWha"

FineTune = client.fine_tuning.jobs.create(
    training_file = uploaded_file_id,    # アップロードしたファイルのID
    model = "gpt-3.5-turbo"
)

# 出力
print(FineTune)