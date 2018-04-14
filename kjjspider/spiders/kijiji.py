# -*- coding: utf-8 -*-
import scrapy
from kjjspider.items import KjjspiderItem


class KijijiSpider(scrapy.Spider):
    name = 'kijiji'
    allowed_domains = ['kijiji.ca']
    URL="https://www.kijiji.ca/b-tickets/gta-greater-toronto-area/page-{0}/c14l1700272"
    start_urls = []
    for i in range(101):
        start_urls.append(URL.format(str(i)))


    def parse(self, response):
        ticket_list = response.xpath('//div[@class="info"]')
        for i in range (len(ticket_list)):
            item=KjjspiderItem()
            item['title']=ticket_list[i].xpath('div[@class="info-container"]/div[@class="title"]/a/text()').extract()[0].strip()
            item['description'] = ticket_list[i].xpath('div[@class="info-container"]/div[@class="description"]/text()').extract()[0].strip()
            v =ticket_list[i].xpath('div[@class="info-container"]/div[@class="title"]/a/@href').extract()[0]
            if v.startswith("http"):
                item['url']=v
            else:
                item['url'] = "https://www.kijiji.ca" + \
                          ticket_list[i].xpath('div[@class="info-container"]/div[@class="title"]/a/@href').extract()[0]

            # deal with the price item

            price_list= ticket_list[i].xpath('div[@class="info-container"]/div[@class="price"]/text()').extract()
            item['price']=price_list[-1].strip()

            # deal with the date-posted  item
            kjj = ticket_list[i].xpath('div[@class="info-container"]/div[@class="location"]/span[@class="date-posted"]/text()')
            if (len(kjj)==0):
                item['postdate']='N/A'
            else:
                item['postdate']=ticket_list[i].xpath('div[@class="info-container"]/div[@class="location"]/span[@class="date-posted"]/text()').extract()[0].strip()

            # deal with the location  item
            kjj =ticket_list[i].xpath('div[@class="info-container"]/div[@class="location"]/text()')
            if (len(kjj)==0):
                item['location']='N/A'
            else:
                item['location']=ticket_list[i].xpath('div[@class="info-container"]/div[@class="location"]/text()').extract()[0].strip()

            #deal with ticket info
            kjj =ticket_list[i].xpath('div[@class="info-container"]/div[@class="ticket-info"]')
            if (len(kjj)==0):
                item['ticket_info']='N/A'
            else:
                item['ticket_info']=ticket_list[i].xpath('div[@class="info-container"]/div[@class="ticket-info"]/text()').extract()[0].strip()


            #deal with ticket availabe number
            kjj = ticket_list[i].xpath('div[@class="info-container"]/div[@class="price"]/span[@class="tickets-available"]/text()')
            if (len(kjj) == 0):
                item['ticket_avail'] = 'N/A'
            else:
                item['ticket_avail'] = ticket_list[i].xpath('div[@class="info-container"]/div[@class="price"]/span[@class="tickets-available"]/text()').extract()[0].strip()
            yield item




