import requests

URL = "http://localhost:8888"


def main():
    response = requests.get(URL)
    print(response.content)


if __name__ == "__main__":
    main()
