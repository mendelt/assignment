import requests

BASE_URL = "http://localhost:8888"
EXAMPLE_EMAIL = {"subject": "Hi Mum!", "body": "This is an example email", "to": "mum@home.nl"}


def main():

    # Store an email
    response = requests.post(BASE_URL, json=EXAMPLE_EMAIL)
    id = response.json()["id"]
    print("added id {}".format(id))

    # Try to retrieve it
    response = requests.get("{}/email/{}".format(BASE_URL, id))
    print(response.content)

    # Check database state
    response = requests.get(BASE_URL)
    print(response.content)


if __name__ == "__main__":
    main()
