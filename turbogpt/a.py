from turbogpt import TurboGpt

from dotenv import load_dotenv
# .envファイルから環境変数を読み込み
load_dotenv()


turbogpt = TurboGpt(model="gpt-4")  # or "text-davinci-002-render-sha" (default)(AKA GPT-3.5)
session = turbogpt.start_session()
q = turbogpt.send_message(input(">>> "), session)
print(q['message']['content']['parts'][0])
