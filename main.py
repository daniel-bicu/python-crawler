from bs4 import BeautifulSoup as page_handler
from urllib.request import urlopen as url_request


if __name__ == '__main__':
    page_url = "https://sites.google.com/site/fiipythonprogramming/administrative?authuser=0"

    # opens the connection and downloads html page from url
    uClient = url_request(page_url)
    page_soup = page_handler(uClient.read(), "html.parser")
    #uClient.close()

    print(page_soup.findAll("h1"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
