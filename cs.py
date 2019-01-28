import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                        (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/"}


def get_url(url):
    response = requests.get(url,headers=headers)
    html = response.content.decode("gbk")
    text = BeautifulSoup(html,"lxml")
    return text


def parse_url(url):
    hrefs = []
    text = get_url(url)
    ps = text.select("p.t1")
    for p in ps:
        a = p.select("a")[0]
        href = a["href"]
        hrefs.append(href)
    return hrefs


informations = []
def parse_information(urls):
    for url in urls:
        text = get_url(url)
        title = text.select("h1")[0]["title"]
        p = text.select("p.cname")[0]
        company = p.select("a")[0]["title"]
        strong = text.select("strong")[1].string

        infos = list(text.select("p.msg")[0].stripped_strings)
        for info in infos:
            if info == "|":
                infos.remove("|")
        information = {"title": title, "company": company, "monetey": strong, "infos": infos}
        informations.append(information)
    return informations


def main():
    for x in range(1,6):
        url = "https://search.51job.com/list/070400,000000,0000,00,9,99,python,2,{}.html?".format(x)
        parse_url(url)
        urls = parse_url(url)
        print(parse_information(urls))


if __name__ == '__main__':
    main()
