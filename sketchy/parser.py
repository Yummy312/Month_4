import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = 'https://kinokrad.co/zarubezhnye-4/'

HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}


@csrf_exempt
def get_html(url,  params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@ csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.findAll("div", class_="shorbox")
    container = []
    for item in items:
        container.append(
            {
              "title":item.find("div", class_="shorposterbox").find("div", class_="postershort").find("img", class_="postr").get("alt"),
              "image": item.find("div", class_="shorposterbox").find("div", class_="postershort").find("img", class_="postr").get("src"),
               "url": item.find("div", class_="shorposterbox").find("div", class_="postertitle").find("a").get("href"),

            },

        )

    return container


@csrf_exempt
def parser_func():
    html = get_html(HOST)
    if html.status_code == 200:
        container = []
        for page in range(1, 5):
            html = get_html(f"https://kinokrad.co/zarubezhnye-4/page/{page}/")
            container.extend(get_data(html.text))
        return container








