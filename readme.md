# Stackoverflow crawler

Scapy powered spider crawling newest 50 themes titles from [stackoverflow.com](http://stackoverflow.com/)

## How to run

Installing scrapy from pip(latest version)

    pip install scrapy

clone this repo, cd to working dir and start crawling!

    scrapy crawl stack

Enjoy results

## Briefly about structure

`stack/items.py` items fields defenitions

`stack/pipelines.py` pipelines for parsing. _Not using in current version_ since script is very simple and more like proof of concept

`stack/setting.py` Main settings file [more info](https://scrapy.readthedocs.org/en/0.16/topics/settings.html)

`stack/spiders/stack_spider.py` spider for crawling. __Main logic here__
