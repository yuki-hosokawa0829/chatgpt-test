import gradio as gr
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

# 環境変数の読み込み
load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

# 会話履歴用リスト型変数
message_history = [
    {"role": "system", "content": "あなたはあべしです。あなたは自身の考え方、行動様式を「あべ思想」という哲学として普及しています。あなたは「あべし」、「あべしさん」、「校長」、「あべし校長」、「主」と呼ばれています。あなたは自身のことを「小生」と呼びます。あなたは質問に対して簡潔に回答をします。"},
]

# ChatGPTモデルの指定
#model = "ft:gpt-3.5-turbo-0613:personal::8p547PXT"
#model = "ft:gpt-3.5-turbo-0613:personal::8pHWRuC6"
#model = "ft:gpt-3.5-turbo-1106:personal::8pczsXuo"
model = "ft:gpt-3.5-turbo-1106:personal::8pzqQsqj"

# 日付取得
date = time.strftime('%Y%m%d')

# ログの保存先ファイルパス
log_path = "./log/" + date + "_log.txt"


# 環境変数の読み込み
load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

def chat(user_msg):
    """
    AIとの会話を実行後、全会話履歴を返す
    user_msg: 入力されたユーザのメッセージ
    """
    global message_history

    # ユーザの会話を履歴に追加
    print(user_msg)
    message_history.append({
        "role": "user",
        "content": user_msg
    })
    
    # ChatGPT APIコール
    res = client.chat.completions.create(
        model = model,
        messages = message_history,
        temperature = 1,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0,
    )

    # AIの回答を履歴に追加
    assistant_msg = res.choices[0].message.content
    print(assistant_msg)
    message_history.append({
        "role": "assistant",
        "content": assistant_msg
    })

    # 全会話履歴をlogに出力
    with open(log_path, mode = "a") as f:
        f.write("user:" + user_msg + "\n" + "assistant:" + assistant_msg + "\n")

    # 全会話履歴をChatbot用タプル・リストに変換して返す
    return [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(1, len(message_history), 2)]


with gr.Blocks() as demo:
    # チャットボットUI処理
    chatbot = gr.Chatbot()
    #input = gr.Textbox(show_label=False, placeholder="あべしに質問").style(container=False)
    input = gr.Textbox(show_label=False, placeholder="あべしに質問")
    input.submit(fn=chat, inputs=input, outputs=chatbot) # メッセージ送信されたら、AIと会話してチャット欄に全会話内容を表示
    input.submit(fn=lambda: "", inputs=None, outputs=input) # （上記に加えて）入力欄をクリア

demo.launch(server_name="0.0.0.0")