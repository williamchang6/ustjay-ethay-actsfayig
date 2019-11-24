import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def send_fact():

    pig_url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    pig_data = {"input_text": str(get_fact())}
    return requests.post(pig_url, pig_data).url


@app.route('/')
def home():
    return send_fact()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

