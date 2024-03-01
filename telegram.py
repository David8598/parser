import requests


def send_telegram(text: str):
    token = '6876459293:AAHRQx6fxcA-yqyZeLaavb4zqOgrOsIeu1g'
    url = "https://api.telegram.org/bot"
    channel_id = '651653922'
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text,
        "parse_mode": "HTML"
    })

    if r.status_code != 200:
        raise Exception("post_text error")


def main():
    send_telegram('Привет, чувак!')


if __name__ == '__main__':
    main()