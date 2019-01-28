import requests
from lxml import etree
# 请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
                          (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}
# 获取详细的htmlE


def get_url(url):
    response = requests.get(url,headers=headers)
    html = response.content.decode("gbk")
    htmlE = etree.HTML(html)
    return htmlE
# 获取每个页面详细url


def parse_url(url):
    html = get_url(url)
    urls = html.xpath('//div[@class="el"]//p[@class="t1 "]//a/@href')
    return urls
    print(urls)
# 获取详细信息


def parse_information(urls):
    for url in urls:
        html = get_url(url)
        title = html.xpath('//div[@class="in"]//h1/@title')[0].strip()
        company = html.xpath('//div[@class="in"]//a/@title')[0].strip()
        infos = html.xpath('//div[@class="in"]//p[2]/text()')
        infolist = []
        for info in infos:
            infolist.append(info.strip())
        dict_infomation = {"title": title, "company": company, "information": infolist}
        print(dict_infomation)


def main():
    for x in range(1,11):
        url = "https://search.51job.com/list/070400,000000,0000,00,9,99,python,2,{}.html?".format(x)
        urls = parse_url(url)
        parse_information(urls)


if __name__ == "__main__":
    main()
