# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
#import the item defined in items.py
from icc.items import IccItem

class IccspiderSpider(scrapy.Spider):
    name = "iccspider"
    allowed_domains = ["http://www.intelligentcontentconference.com/"]
    start_urls = ['http://www.intelligentcontentconference.com/speakers/joe-pulizzi/','http://www.intelligentcontentconference.com/speakers/robert-rose/','http://www.intelligentcontentconference.com/speakers/scott-abel/','http://www.intelligentcontentconference.com/speakers/ann-rockley/','http://www.intelligentcontentconference.com/speakers/ardath-albee/','http://www.intelligentcontentconference.com/speakers/joe-gollner/','http://www.intelligentcontentconference.com/speakers/664/','http://www.intelligentcontentconference.com/speakers/melissa-breker/','http://www.intelligentcontentconference.com/speakers/yoon-chung/','http://www.intelligentcontentconference.com/speakers/noz-urbina/','http://www.intelligentcontentconference.com/speakers/steve-stegelin/','http://www.intelligentcontentconference.com/speakers/mark-fries/','http://www.intelligentcontentconference.com/speakers/derek-phillips/','http://www.intelligentcontentconference.com/speakers/dechay-watts/','http://www.intelligentcontentconference.com/speakers/sarah-okeefe/','http://www.intelligentcontentconference.com/speakers/cruce-saunders/','http://www.intelligentcontentconference.com/speakers/carlos-abler/','http://www.intelligentcontentconference.com/speakers/lisa-welchman/','http://www.intelligentcontentconference.com/speakers/jenny-magic/','http://www.intelligentcontentconference.com/speakers/don-day/','http://www.intelligentcontentconference.com/speakers/michael-priestley/','http://www.intelligentcontentconference.com/speakers/james-mathewson/','http://www.intelligentcontentconference.com/speakers/gavin-austin/','http://www.intelligentcontentconference.com/speakers/deborah-s-bosley/','http://www.intelligentcontentconference.com/speakers/jodi-shimp/','http://www.intelligentcontentconference.com/speakers/ahava-leibtag/','http://www.intelligentcontentconference.com/speakers/andrew-bredenkamp/','http://www.intelligentcontentconference.com/speakers/tracy-macdonald/','http://www.intelligentcontentconference.com/speakers/paula-land/','http://www.intelligentcontentconference.com/speakers/shana-pearlman/','http://www.intelligentcontentconference.com/speakers/val-swisher/','http://www.intelligentcontentconference.com/speakers/carmen-simon/','http://www.intelligentcontentconference.com/speakers/buddy-scalera/','http://www.intelligentcontentconference.com/speakers/michelle-killebrew/','http://www.intelligentcontentconference.com/speakers/lila-giuili/','http://www.intelligentcontentconference.com/speakers/toni-pashley/','http://www.intelligentcontentconference.com/speakers/michael-arnold/','http://www.intelligentcontentconference.com/speakers/alan-horvath/','http://www.intelligentcontentconference.com/speakers/todd-resnick/','http://www.intelligentcontentconference.com/speakers/1191/','http://www.intelligentcontentconference.com/speakers/cleve-gibbon/','http://www.intelligentcontentconference.com/speakers/linda-francis/','http://www.intelligentcontentconference.com/speakers/jim-romano/','http://www.intelligentcontentconference.com/speakers/michael-margolis/','http://www.intelligentcontentconference.com/speakers/james-turcotte/','http://www.intelligentcontentconference.com/speakers/laurel-counts/','http://www.intelligentcontentconference.com/speakers/philip-wisniewski/','http://www.intelligentcontentconference.com/speakers/mark-lewis/','http://www.intelligentcontentconference.com/speakers/paul-perrotta/','http://www.intelligentcontentconference.com/speakers/rahel-anne-bailie/','http://www.intelligentcontentconference.com/speakers/todd-wheatland/','http://www.intelligentcontentconference.com/speakers/ian-walsh/','http://www.intelligentcontentconference.com/speakers/rebecca-schneider/','http://www.intelligentcontentconference.com/speakers/charles-cooper/','http://www.intelligentcontentconference.com/speakers/nick-bell/','http://www.intelligentcontentconference.com/speakers/nataly-kelly/','http://www.intelligentcontentconference.com/speakers/ben-cornelius/','http://www.intelligentcontentconference.com/speakers/susie-dickson/','http://www.intelligentcontentconference.com/speakers/elizabeth-quispe/','http://www.intelligentcontentconference.com/speakers/kate-kenyon/','http://www.intelligentcontentconference.com/speakers/scott-brinker/','http://www.intelligentcontentconference.com/speakers/vishal-khanna/','http://www.intelligentcontentconference.com/speakers/greg-verdino/','http://www.intelligentcontentconference.com/speakers/andrea-ames/','http://www.intelligentcontentconference.com/speakers/karen-mcgrane/','http://www.intelligentcontentconference.com/speakers/jeff-julian/','http://www.intelligentcontentconference.com/speakers/andrea-fryrear/','http://www.intelligentcontentconference.com/speakers/josepf-haslam/','http://www.intelligentcontentconference.com/speakers/jason-sims/','http://www.intelligentcontentconference.com/speakers/colleen-jones/','http://www.intelligentcontentconference.com/speakers/wendy-stengel/','http://www.intelligentcontentconference.com/speakers/gregory-yates/','http://www.intelligentcontentconference.com/speakers/scott-liewehr/','http://www.intelligentcontentconference.com/speakers/jake-athey/','http://www.intelligentcontentconference.com/speakers/james-barnes/','http://www.intelligentcontentconference.com/speakers/matthew-grocki/','http://www.intelligentcontentconference.com/speakers/kat-robinson/','http://www.intelligentcontentconference.com/speakers/alp-mimaroglu/','http://www.intelligentcontentconference.com/speakers/k-scott-rosenberg/','http://www.intelligentcontentconference.com/speakers/andy-weir/','http://www.intelligentcontentconference.com/speakers/peter-loibl/','http://www.intelligentcontentconference.com/speakers/cathy-mcphillips/','http://www.intelligentcontentconference.com/speakers/clare-mcdermott/','http://www.intelligentcontentconference.com/speakers/marcia-riefer-johnston/','http://www.intelligentcontentconference.com/speakers/jay-pongonis/','http://www.intelligentcontentconference.com/speakers/greg-marlin/','http://www.intelligentcontentconference.com/speakers/jeff-french/','http://www.intelligentcontentconference.com/speakers/arje-cahn/','http://www.intelligentcontentconference.com/speakers/josh-manton/','http://www.intelligentcontentconference.com/speakers/maria-osipova/','http://www.intelligentcontentconference.com/speakers/david-lesue/','http://www.intelligentcontentconference.com/speakers/joe-staples/','http://www.intelligentcontentconference.com/speakers/richard-sikes/','http://www.intelligentcontentconference.com/speakers/pat-grady/']

    def parse(self, response):
        i = IccItem()

        i['url'] = response.url
        i['title'] = response.xpath('/html/head/title/text()').extract()[0]

        #splitting response on <hr> below bio paragraphs
        top = response.body.split('<hr/>')[0]

        #defining a Selector to only parse the text above the <hr>
        sel = Selector(text=top)

        #getting <p> elements with custom selector
        i['bio'] = sel.css('p').extract()

        #getting h1, and stripping whitespace
        i['h1'] = response.css('h1::text').extract_first().strip()

        #getting profile image url using css and xpath selectors
        i['image'] = response.css('img').css('.wp-post-image').xpath('@src').extract_first()

        #using xpath selctors to capture Open Graph values
        i['og_locale'] = response.xpath('//meta[@property="og:locale"]/@content').extract_first()
        i['og_type'] = response.xpath('//meta[@property="og:type"]/@content').extract_first()
        i['og_title'] = response.xpath('//meta[@property="og:title"]/@content').extract_first()
        i['og_description'] = response.xpath('//meta[@property="og:description"]/@content').extract_first()
        i['og_url'] = response.xpath('//meta[@property="og:url"]/@content').extract_first()
        i['og_site_name'] = response.xpath('//meta[@property="og:site_name"]/@content').extract_first()
        i['og_image'] = response.xpath('//meta[@property="og:image"]/@content').extract_first()
        #using xpath selctors to capture Twitter Card values
        i['twitter_card'] = response.xpath('//meta[@property="og:title"]/@content').extract_first()
        i['twitter_description'] = response.xpath('//meta[@name="twitter:description"]/@content').extract_first()
        i['twitter_title'] = response.xpath('//meta[@name="twitter:title"]/@content').extract_first()
        i['twitter_site'] = response.xpath('//meta[@name="twitter:site"]/@content').extract_first()
        i['twitter_domain'] = response.xpath('//meta[@name="twitter:domain"]/@content').extract_first()
        i['twitter_image'] = response.xpath('//meta[@name="twitter:image:src"]/@content').extract_first()
        i['twitter_creator'] = response.xpath('//meta[@name="twitter:creator"]/@content').extract_first()

        #returning item
        return i




