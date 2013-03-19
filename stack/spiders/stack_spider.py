from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from stack.items import StackItem


class StackSpider(BaseSpider):
    name = "stack"
    allowed_domains = ["http://stackoverflow.com/"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        summaries = hxs.select('//div[@class="summary"]')
        items = []

        for summary in summaries:
            item = StackItem()
            item['title'] = summary.select('//a[@class="question-hyperlink"]/text()').extract()
            items.append(item)

        return items
