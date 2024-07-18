import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city/amaravati/acb-will-probe-alienation-of-govt-and-endowments-lands-at-visakhapatnam-involving-ysrcp-mp-vijayasai-reddy-ap-endowments-minister/articleshow/111843507.cms"
fetchAndSaveToFile(url, "data/neettest.html")
