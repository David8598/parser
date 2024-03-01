import requests
def send_telegram(text: str):
    id = 1
    get_url = "https://api.telegram.org/bot6876459293:AAHRQx6fxcA-yqyZeLaavb4zqOgrOsIeu1g/getUpdates"
    result_req = requests.get(get_url)
    get_json = result_req.json()
    for items in get_json["result"]:
        meseg = items["message"]
        if meseg["from"]["id"] != id:
            id =  meseg["from"]["id"]            
            token = '6876459293:AAHRQx6fxcA-yqyZeLaavb4zqOgrOsIeu1g'
            url = "https://api.telegram.org/bot"
            channel_id = meseg["from"]["id"]
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