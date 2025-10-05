import requests
import time
import os

TOKEN = os.getenv("BOT_TOKEN")
API = f"https://api.telegram.org/bot{TOKEN}"

MEU_LINK = "https://linkbio.co/wellingtonribeiro"  

def get_updates(offset=None):
    params = {"timeout": 30, "offset": offset}
    r = requests.get(API + "/getUpdates", params=params)
    return r.json()

def send_message(chat_id, text):
    requests.post(API + "/sendMessage", json={"chat_id": chat_id, "text": text})

def main():
    last_update_id = None
    while True:
        try:
            updates = get_updates(last_update_id)
            for u in updates.get("result", []):
                last_update_id = u["update_id"]
                message = u.get("message", {})
                chat_id = message.get("chat", {}).get("id")
                if chat_id:
                    send_message(chat_id, f"Aqui está meu link: {MEU_LINK}")
        except Exception as e:
            print("Erro:", e)
            time.sleep(2)

if name == "__main__":
    main()
