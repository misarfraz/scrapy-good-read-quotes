# -*- coding: utf-8 -*-
import scrapy
from ..items import GoodreadquotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    page_number_inspirational = 2
    page_number_love = 2
    page_number_humor = 2
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/quotes?page=1', 'https://www.goodreads.com/quotes/tag/inspirational?page=1', 
    'https://www.goodreads.com/quotes/tag/love?page=1', 'https://www.goodreads.com/quotes/tag/humor?page=1']

    def parse(self, response):
        items = GoodreadquotesItem()
        
        if 'inspirational' in response.url:
            source = 'inspirational'
        elif 'love' in response.url:
            source = 'love'
        elif 'humor' in response.url:
            source = 'humor'
        else:
            source = 'popular'

        all_div_quotes = response.css('div.quoteDetails')

        for quotes in all_div_quotes:
            quote_title = quotes.css('div.quoteText::text').extract()
            quote_author = quotes.css('div.quoteText span::text').extract()
            quote_likes = quotes.css(
                'div.quoteFooter div.right a.smallText::text').extract()
            quote_tags = quotes.css(
                'div.quoteFooter div.greyText.smallText.left a::text').extract()

            items['source'] = source
            items['title'] = quote_title[0]
            items['length'] = len(quote_title[0])
            items['author'] = quote_author[0]
            likes = quote_likes[0].split()
            items['likes'] = likes[0]
            items['tags'] = quote_tags

            yield items

        next_page = 'https://www.goodreads.com/quotes?page=' + str(QuotesSpider.page_number)
        if QuotesSpider.page_number < 101:
        	QuotesSpider.page_number += 1
        	yield response.follow(next_page, callback=self.parse)


        next_page_inspirational = 'https://www.goodreads.com/quotes/tag/inspirational?page=' + str(QuotesSpider.page_number_inspirational)
        if QuotesSpider.page_number_inspirational < 101:
            QuotesSpider.page_number_inspirational += 1
            yield response.follow(next_page_inspirational, callback=self.parse)


        next_page_love = 'https://www.goodreads.com/quotes/tag/love?page=' + str(QuotesSpider.page_number_love)
        if QuotesSpider.page_number_love < 101:
            QuotesSpider.page_number_love += 1
            yield response.follow(next_page_love, callback=self.parse)


        next_page_humor = 'https://www.goodreads.com/quotes/tag/humor?page=' + str(QuotesSpider.page_number_humor)
        if QuotesSpider.page_number_humor < 101:
            QuotesSpider.page_number_humor += 1
            yield response.follow(next_page_humor, callback=self.parse)

