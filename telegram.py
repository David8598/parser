import requests

id = {}
def check_id():
    get_url = "https://api.telegram.org/bot6876459293:AAHRQx6fxcA-yqyZeLaavb4zqOgrOsIeu1g/getUpdates"
    result_req = requests.get(get_url)
    get_json = result_req.json()
    for items in get_json["result"]:
        meseg = items["message"]
        if meseg["from"]["id"] == meseg["from"]["id"]:
          id =  meseg["from"]["id"]
          print(id)



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
    send_telegram("q")


if __name__ == '__main__':
    main()