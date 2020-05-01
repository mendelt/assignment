import requests

URL = "http://localhost:8888"



EXAMPLE_EMAIL = {"subject": "Hi Mum!", "body": "This is an example email", "to": "mum@home.nl"}

def main():
    response = requests.get(URL)
    print(response.content)

    response = requests.post(URL, json=EXAMPLE_EMAIL)
    print(response.content)


if __name__ == "__main__":
    main()
