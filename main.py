import click
import requests
from os import system


@click.command()
@click.argument('username')
@click.argument('password')
def main(username,password):
    API_ENDPOINT = "http://127.0.0.1:8000/api/Seguridad/login"
    data = {'username':username,
        'password':password}
    r = requests.post(url = API_ENDPOINT, json = data)
    pastebin_url = r.text
    print(pastebin_url)

if __name__ == '__main__':
    main()