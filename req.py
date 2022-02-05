from generate_random import aleatoriu as R
from eth_account import Account
from bs4 import BeautifulSoup
import secrets, sys
import requests

initial_url = "https://www.etherchain.org/account/{}"

#lista_magica = [0,1,2,3,4,5,6,7,8,9]


def getReq(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        balance = float(soup.find('span', class_='badge badge-success').text.split()[0])
        if balance != 0.0:
            with open("adrs.txt", "a") as file_text:
                file_text.write(('='*66) +'\n'+ acct +'\n'+ private_key +'\n'+ ('='*66))
                print(res.status_code, acct, private_key, balance)

        print(res.status_code, acct, private_key, balance)

    except Exception as ee:
        return "Message : {}".format(ee)

while True:
    try:
        #priv = R(lista_magica)
        priv = secrets.token_hex(32)
        private_key = "0x" + priv
        acct = Account.from_key(private_key).address
        URL = initial_url.format(acct)
        getReq(URL)
    except KeyboardInterrupt:
        sys.exit()
