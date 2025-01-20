import re

import scrapy


class GetUrlsSpider(scrapy.Spider):
    name = "get_urls"
    allowed_domains = ["index.minfin.com.ua"]
    start_urls = ["https://index.minfin.com.ua/ua/russian-invading/casualties/"]    # Вписуємо стартовий url самостійно

    def parse(self, response):  # noqa
        prefix = "/month.php?month="
        links = response.xpath("/html//div[@class='ajaxmonth']/h4/a")  # // - означає що може бути все що завгодно. Атрибути беремо через @
        for link in links:
            yield {       # Дані роблять yield у вигляді словника
                "link": prefix + re.search(r"\d{4}-\d{2}", link.xpath("@href").get()).group()  # .// - означає що починаємо від корня
            }