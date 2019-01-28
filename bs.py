import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                        (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/"}


def get_url(url):
    response = requests.get(url,headers=headers)
    html = response.content.decode("gbk")
    return html


def parse_url(html):
    bs = BeautifulSoup(html, "lxml")
    div = bs.find("div",class_="dw_table")

    els = div.find_all("p",class_="t1")
    urls = []
    for el in els:
        a = el.find("a")
        url = a['href']
        urls.append(url)
    return urls


informations = []


def parse_information(urls):
    for url in urls:
        html = get_url(url)
        bs = BeautifulSoup(html, "lxml")
        h1 = bs.find_all("h1")[0]
        title = h1["title"]
        a = bs.find("a",class_="catn")
        company = a['title']
        p = bs.find("p",class_="msg ltype")
        other = p['title'].strip()
        other = other.replace("  |  ", ",")
        information = {"title": title, "company": company, "information": other}
        informations.append(information)
    return informations


def main():
    url = "https://search.51job.com/list/070400,000000,0000,00,9,99,python,2,1.html?"
    html = get_url(url)
    urls = parse_url(html)
    infos = parse_information(urls)
    for information in infos:
        print(information)
# def main():
#     for x in range(1, 10):
#         url = "https://search.51job.com/list/070400,000000,0000,00,9,99,python,2,{}.html?".format(x)
#         html = get_url(url)
#         urls = parse_url(html)


if __name__ == "__main__":
    main()
