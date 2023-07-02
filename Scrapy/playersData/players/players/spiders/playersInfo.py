import scrapy
#scrapy crawl playersInfo

class PlayersinfoSpider(scrapy.Spider):
    name = 'playersInfo'
    def start_requests(self):
        
        urls = ['https://www.transfermarkt.co.uk/ederson/profil/spieler/238223',
                'https://www.transfermarkt.co.uk/ruben-dias/profil/spieler/258004',  ## Excell'de düzenlediğin tüm linkleri içersine yolla.
                'https://www.transfermarkt.co.uk/aymeric-laporte/profil/spieler/176553',
                'https://www.transfermarkt.co.uk/nathan-ake/profil/spieler/177476',
                'https://www.transfermarkt.co.uk/joao-cancelo/profil/spieler/182712',
                'https://www.transfermarkt.co.uk/kyle-walker/profil/spieler/95424',
                'https://www.transfermarkt.co.uk/rodri/profil/spieler/357565',
                'https://www.transfermarkt.co.uk/rico-lewis/profil/spieler/701057',
                'https://www.transfermarkt.co.uk/kalvin-phillips/profil/spieler/351749',
                'https://www.transfermarkt.co.uk/phil-foden/profil/spieler/406635',
                'https://www.transfermarkt.co.uk/ilkay-gundogan/profil/spieler/53622',
                'https://www.transfermarkt.co.uk/kevin-de-bruyne/profil/spieler/88755',
                'https://www.transfermarkt.co.uk/bernardo-silva/profil/spieler/241641',
                'https://www.transfermarkt.co.uk/jack-grealish/profil/spieler/203460',
                'https://www.transfermarkt.co.uk/julian-alvarez/profil/spieler/576024',
                'https://www.transfermarkt.co.uk/riyad-mahrez/profil/spieler/171424',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

#https://www.transfermarkt.co.uk/erling-haaland/profil/spieler/418560 , #https://www.transfermarkt.co.uk/ruben-dias/profil/spieler/258004

    def parse(self, response):
        # playerData=response.xpath("//div[@class='box viewport-tracking']/div") ##her oyuncunun kendine ait kutucuğu
        
        # for player in playerData:
        
        name=response.xpath(".//div[@class='large-6 large-pull-6 small-12 columns spielerdatenundfakten']/div/span[2]/text()").get()
        agent=response.xpath(".//div[@class='large-6 large-pull-6 small-12 columns spielerdatenundfakten']/div/span[18]/a/text()").get()
        age=response.xpath(".//div[@class='large-6 large-pull-6 small-12 columns spielerdatenundfakten']/div/span[8]/text()").get()   
        country=response.xpath(".//div[@class='large-6 large-pull-6 small-12 columns spielerdatenundfakten']/div/span[12]/img[1]/@title").get() 
        currentClub=response.xpath(".//span[@class='info-table__content info-table__content--bold info-table__content--flex']/a[2]/text()").get() 
        position=response.xpath(".//div[@class='large-6 large-pull-6 small-12 columns spielerdatenundfakten']/div/span[14]/text()").get()
        marktValue=response.xpath(".//div[@class='tm-player-market-value-development__current-value']/a[1]/text()").get()
        datas=[name,agent,age,country,currentClub,position,marktValue]
        for data in datas:
            if data is None:
                data='0'
        yield{

                
              "name":name,
              "age":age,              
              "city":country,
              "current Club":currentClub,
              "agent":agent,
              "position":position.strip(),
              "markt Value":marktValue
                }


##//div[@class='large-6 large-push-6 small-12 columns']/div/div[@class='detail-position__box' or @class='detail-position']/div[@class='detail-position__box' or @class='detail-position__inner-box' ]/dd/text()
##position=response.xpath(".//div[@class='large-6 large-push-6 small-12 columns']/div/div[@class='detail-position']/div[@class='detail-position__box']/dd/text()").get()




##-------------------------------------------------------------------------------------------------------------------------------------------------###


# ÇOK İYİ BİR YAPIM YÖNTEMİ KULLAN. EKLEDİĞİMİZ TAKIMIN LİNKİ İÇERSİNDEKİ TÜM KADRONUN OYUNCULARININ LİNKİNİ VE ADINI ALIR
"""class PlayersinfoSpider(scrapy.Spider): 
    name = 'playersInfo'
    def start_requests(self):
        urls = ['https://www.transfermarkt.co.uk/manchester-city/startseite/verein/281/saison_id/2022']
              
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for player in response.css("table.items tbody tr td.posrela"):
            name=player.css(" td.hauptlink a::text").get()
            link=player.css("td.hauptlink a::attr(href)").get()
            yield {
                
                "name":name,
                "link":f"https://www.transfermarkt.co.uk{link}"

            }
"""

##-------------------------------------------------------------------------------------------------------------------------------------------------###


# class TransfermarktSpider(scrapy.Spider):
#     name = 'playersInfo'
#     start_urls = ["https://www.transfermarkt.co.uk/manchester-city/startseite/verein/281/saison_id/2022"]   
    

#     def parse(self, response):
#         for items in response.css('td.posrela'):
#             # Her bir element içindeki tüm linkleri alın
            
#             yield {
#                     'link':items.css('a::attr(href)').get()
#                     # 'ad':items.css('a::attr(title)').get()
#                         }




        
# class PlayersinfoSpider(scrapy.Spider):
#     name = 'playersInfo'
#     start_urls = ["https://www.transfermarkt.co.uk/manchester-city/startseite/verein/281/saison_id/2022"]

#     def parse(self, response):
#         players=response.xpath("//td[@class='posrela']") ##her oyuncunun kendine ait kutucuğu
        
#         for player in players:
#             name=player.xpath(".//td[@class='hide']/text()").get()
#             link=player.xpath(".//td[@class='posrela']/table/tbody/tr[1]/td[2]/div[1]/span/a/text()").get()
#             # number=player.xpath(".//td[@title='Goalkeeper']/div/text()").get()
#             xd=player.xpath(".//table/tbody/tr[1]/td[2]/div[1]/span/a/text()").get()            
#             yield{
#                 "name":name,
#                 "link":link,
#                 # "number":number,
#                 "xd":xd
                
#                 }