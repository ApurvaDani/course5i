# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:14:02 2019

@author: Apurva
"""

import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from oneplus.items import OneplusItem
 
# Creating a new class to implement Spide
class oneplus(scrapy.Spider):
     
    # Spider name
    name = 'oneplus'
    start_urls = ['https://www.amazon.in/dp/B07DJHY82F/ref=gbph_img_m-5_d182_b23b14bf?smid=A23AODI1X2CEAE&pf_rd_p=a3a8dc53-aeed-4aa1-88bb-72ce9ddad182&pf_rd_s=merchandised-search-5&pf_rd_t=101&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=P3FSQH2KEB3B5QQ1NQD5']
    
    # Defining a Scrapy parser
    def parse(self, response):
        item = OneplusItem()
        
        name = response.css('#productTitle::text').extract()
        revnio = response.css('#acrCustomerReviewText').css('::text').extract()
        price = response.css('#priceblock_dealprice').css('::text').extract()
        #exprice = response.css('#sopp_feature_div .a-spacing-top-small:nth-child(1) .a-list-item').css('::text').extract()
        exprice = response.css('#maxBuyBackDiscountSection .a-color-price').css('::text').extract()
        imgg = response.css('.imgTagWrapper::attr(src)').extract()
        colours = response.css('#variation_color_name .selection').css('::text').extract()
        rating = response.css('.arp-rating-out-of-text').css('::text').extract()
        description = response.css('.aplus-module-1-description , .aplus-p3 , .aplus-p1 , #productDescription p').css('::text').extract()
        techdet = response.css('.col1 .attrG').css('::text').extract()
        
        item['title']=name
        item['description']=description
        item['image']=imgg
        item['price']=price
        item['exprice']=exprice
        item['colours']=colours
        item['noreview']=revnio
        item['rating']=rating
        item['techdetails']=techdet
        
        yield item
