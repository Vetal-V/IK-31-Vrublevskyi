import requests
import json
import logging
from requests.exceptions import HTTPError
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError as http_err:
        logging.error("Сервер недоступний. Будь ласка, перезапустіть сервер ще раз. Помилка: %s", http_err)
    except Exception as err:
        logging.error("Сервер недоступний. Будь ласка, запустіть сервер ще раз. Помилка: %s", err)
    else:
        data = json.loads(r.content)
        logging.info("Сервер доступний. Час на сервері: %s", data['date'])
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Відповідь сервера місти наступні поля:")
        for key in data.keys():
            logging.info("Ключ: %s, Значення: %s", key, data[key])

if __name__ == '__main__':
    while True:
        main("http://localhost:8000/health")
        time.sleep(60)