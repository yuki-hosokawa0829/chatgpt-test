import os
from dotenv import load_dotenv
from openai import OpenAI

# 環境変数の読み込み
load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

# 学習用データのファイルパス
job_id = "ftjob-Cpe1RRRsUmodczViQHsXYfcD"

print("# List 10 fine-tuning jobs")
client.fine_tuning.jobs.list(limit=10)
print(" ")

print("# Retrieve the state of a fine-tune")
client.fine_tuning.jobs.retrieve(job_id)
print(" ")

print("# List up to 10 events from a fine-tuning job")
client.fine_tuning.jobs.list_events(fine_tuning_job_id=job_id, limit=10) 
print(" ")