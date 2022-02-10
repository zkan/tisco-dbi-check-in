from flask import Flask, request

from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    BeaconEvent,
    TextSendMessage,
)


app = Flask(__name__)


CHANNEL_ACCESS_TOKEN = ""
CHANNEL_SECRET = ""

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        print("Data received from Webhook is: ", request.json)

        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        print("Request body: ", body)

        handler.handle(body, signature)

        return "Webhook received!"


@handler.add(BeaconEvent)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Hello!"))


if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)
