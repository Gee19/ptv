import requests
from bs4 import BeautifulSoup

# this won't work because they do some stupid infinite scroll shit
# need a full rendering to run the JS

user = ""
base = "https://web.archive.org/web/20191210053418/https://plays.tv/u/"


def extract_url(url):
    return "https://web.archive.org" + url.split("?")[0]


if __name__ == "__main__":
    full_url = f"{base}{user}"
    print(full_url)
    response = requests.get(full_url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a", attrs={"class": "thumb-link"})
    for link in links:
        # print(link["href"])
        print("--- \n\n")
        print(extract_url(link["href"]))
        # print(link)

