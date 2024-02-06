import twint
import nest_asyncio

nest_asyncio.apply()

# Configure
c = twint.Config()
#特定のユーザー名
c.Username = "AbesiTawaraba"
#実行日から数えて過去何日分のツイートを取得するか
#c.Limit = 1
#csv形式で保存するか
c.Store_csv = True
#保存ファイルの名前
c.Output = "Sample.csv"

# Run
twint.run.Search(c)
