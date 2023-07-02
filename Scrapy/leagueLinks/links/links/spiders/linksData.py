import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse
import re
##BUNUN ALTINDAKİ 2 KODDA AYNI İŞLEVDE KULLANILIYOR. ÜSTTEKİNİN İLERLEMEMİŞ HALİDİR. ÜSTTEKİ ARTIK BU VARKEN KULLANILMIYOR AMA YİNE DE KODUN HAM HALİ 
#OLDUGU İÇİN SİLMEYECEĞİM. SELF.URLS İÇERSİNE EKLEDİĞİM LİG LİNKLERİNE TEK TEK GİDECEK O LİGDEKİ KAYITLI YILLARI BULACAK. SONRASINDA İSE BU KAYITLI YILLARIN
#LİNKLERİNİ ALACAK. BÖYLELİKLE TM İÇERSİNDEKİ TÜM LİGLERİ KAYITLI OLDUKLARI YILLARA KADAR ÇEKECEK.
class TransfermarktSpider(scrapy.Spider):
    name = 'linksData'


    def start_requests(self):
        urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1',
                'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1',
                'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1',
                'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1',
                'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1',
                'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_years)
            # self.wettbewerb = re.search(r"/wettbewerb/([^/]+)/", url).group(1)
            

    def parse_years(self, response):
        years_links = []
        for year_link in response.xpath("//select[@name='saison_id']/option"):
            year = year_link.xpath(".//@value").extract_first()
            years_links.append(f"{response.url}/plus/?saison_id={year}")  ##response.url her zaman istek gönderdiğimiz sitenin temel linkini alır.
            
        ## TRANSFERMARKTTA YER ALAN TUM YILLARIN DATASININ GELMESİ YERİNE SADECE 2021-2001 arasındaki verileri alıyoruz
        for year_link in years_links:
            lastFour=year_link[-4:]
            lastFour=int(lastFour)
            leagueName=re.search(r"/wettbewerb/([^/]+)/", year_link).group(1)
            if lastFour>=2004 and lastFour<=2021:
                yield {
                "year_link": year_link,
                  "leagueName":leagueName
                }
                



## GİRİLEN URL'DEKİ LİG LİNKLERİNİ ÇEKİP BİR SONRAKİ SAYFAYA GEÇİŞ YAPIYOR. BÖYLELİKLE ÖRNEĞİN AVRUPA KITASINDA YER ALAN TÜM LİGLERİN LİNKLERİNİ ÇEKMİŞ OLUYOR.
# class TransfermarktSpider(scrapy.Spider):
#     name = 'linksData'
#     start_urls = ["https://www.transfermarkt.co.uk/wettbewerbe/europa"]   
    

#     def parse(self, response):
#         for items in response.css('table.inline-table'):
#             # Her bir element içindeki tüm linkleri alın
            
#             yield {
#                     'link':items.css('a::attr(href)')[1].get(),
#                     'ad':items.css('a::attr(title)').get()
#                         }
# #"https://www.transfermarkt.co.uk"+nextPage
#         nextPage=response.xpath("//a[@title='Go to next page']/@href").get()  ##NextPage değişkenine bi sonraki sayfaya tıklamak için gerekli olan buton linkini atıyoruz.
#         nextPageFull=f"https://www.transfermarkt.co.uk{nextPage}"
        
#         if nextPage:
#             yield scrapy.Request(url=nextPageFull, callback=self.parse)
            



##---------------------------------------------------------------------------------------------------------------------------------------------------##

## START_URLS'E EKLEDİĞİN LİNKTEKİ LİGİN İÇERSİNE GİDİP TÜM SEZONLARININ LİNKLERİNİ BULUP ÇEKİYOR. BURAYA TÜM LİGLERİN LİNKLERİNİ EKLEYECEĞİZ VE TEK TEK LİGLERE
# GİDEREK KAYITLI SEZONLARININ HEPSİNİN LİNKİNİ ALACAKLAR.
# class TransfermarktSpider(scrapy.Spider):
#     name = 'linksData'
#     start_urls = ["https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1"] 
    


#     def parse(self, response):
#         links=response.xpath("//select[@name='saison_id']/option")
#         for link in links:
#             years=link.xpath(".//@value").extract_first()
#             full_url=f"{self.start_urls[0]}/plus/?saison_id={years}"  ## self.start_urls[0] yerine self.start_urls dediğimde linke köşeli parantezler de dahil oluyor.
            
            
#             yield{
#                 "years":full_url
#                 }
        

##---------------------------------------------------------------------------------------------------------------------------------------------------##
##BUNUN ALTINDAKİ 2 KODDA AYNI İŞLEVDE KULLANILIYOR. ÜSTTEKİNİN İLERLEMEMİŞ HALİDİR. ÜSTTEKİ ARTIK BU VARKEN KULLANILMIYOR AMA YİNE DE KODUN HAM HALİ 
#OLDUGU İÇİN SİLMEYECEĞİM. SELF.URLS İÇERSİNE EKLEDİĞİM LİG LİNKLERİNE TEK TEK GİDECEK O LİGDEKİ KAYITLI YILLARI BULACAK. SONRASINDA İSE BU KAYITLI YILLARIN
#LİNKLERİNİ ALACAK. BÖYLELİKLE TM İÇERSİNDEKİ TÜM LİGLERİ KAYITLI OLDUKLARI YILLARA KADAR ÇEKECEK.
## BU VE ALTINDAKİ KOD İKİSİ DE TAMAMEN AYNI İŞLEVDE. İKİSİNİ DE EKLEMEK İSTEDİM FARKLI YOLLAR OLDUGUNDAN.
"""
class TransfermarktSpider(scrapy.Spider):
    name = 'linksData'
   
    
    def start_requests(self):
        
        urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1',
                'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1',  ## Excell'de düzenlediğin tüm linkleri içersine yolla.
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    


    def parse(self, response):
        
         links=response.xpath("//select[@name='saison_id']/option")
         for link in links:
             years=link.xpath(".//@value").extract_first()
             full_url=f"{response.url}/plus/?saison_id={years}"  ## self.start_urls[0] yerine self.start_urls dediğimde linke köşeli parantezler de dahil oluyor.
             #response.url --> istek gönderdiğimiz sayfanın temel(ana) linkini tutar -->https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1            
             yield{
                 "years":full_url
                 }
             
"""
                          ##------------------------------------------------------------##



            
            
        
        # yil=[]
        # for year_link in years_links:
        #     lastFour=year_link[-4:]
        #     lastFour=int(lastFour)
        #     yil.append(lastFour)
            
            
        # print(yil)    
            # print(lastFour) 
            # if year_link[-4:] >=1993 and year_link[-4:] <=2021:    
            #     print(year_link.type)
                # yield {
                # "year_link": year_link
                # }
                
       #Bu şekilde, start_requests fonksiyonunda self.urls dizisindeki her lig sayfası için bir istek yapılır ve döndürülen cevap self.parse_years fonksiyonuna gönderilir.
       #Bu fonksiyon, sayfadaki tüm yılların linklerini elde eder ve döngü ile bu linkler üzerinde geçerek her bir yıl için bir dizi döndürür.



##---------------------------------------------------------------------------------------------------------------------------------------------------##





# # scrapy crawl linksData

# class LinksdataSpider(scrapy.Spider):
#     name = 'linksData'
#     allowed_domains = ['www.transfermarkt.co.uk']
#     start_urls = ['https://www.transfermarkt.com/wettbewerbe/europa'] #https://www.transfermarkt.com/wettbewerbe/europa

#     def parse(self, response):
#         links=response.xpath("//div[@id='yw1']/table/tbody/tr[@class]") #  //div[@id='yw1']/table/tbody/tr[@class]  //table[@class='inline-table
#         for link in links:
#             leagueLink=link.xpath(".//td[@class='hauptlink']/table/tbody/tr/td[2]/a/@href").get()  #//tr[@class]/td[@class='hauptlink']/table/tbody/tr/td[2]/a[@href]/text()
#             clubs=link.xpath(".//td[@class='zentriert'][2]/text()").get()
#             players=link.xpath(".//td[@class='zentriert'][3]/text()").get()
#             # hrefs=link.xpath(".//tbody/tr/td[2]/a/text()").get()
            
#             yield{
#                 'lig Linki':leagueLink,
#                 'club':clubs,
#                 'players':players,
#                 # 'hrefler':hrefs
#                 }#//td[@class='hauptlink']/table/tbody/tr/td[2]/a/@title



# class MySpider(scrapy.Spider):
#     name = 'linksData'
#     start_urls = [
#         "https://www.transfermarkt.co.uk/wettbewerbe/europa"
#     ]

#     def parse(self, response):
#         for link in response.css("#yw1 li a"):
#             name = link.css("::text").extract_first()
#             if name == "Premier League":
#                 yield {
#                     "link": link.css("::attr(href)").extract_first()
#                 }







## BU ALTTAKİ 19 SAYFANIN LİNKİ TEK TEK
# class MySpider(scrapy.Spider):
#     name = 'linksData'
#     start_urls = [
#         "https://www.transfermarkt.co.uk/wettbewerbe/europa"
#     ]

#     def parse(self, response):
#         for link in response.css("#yw1 li a::attr(href)").extract():
#             yield {
#                 "link": link
#             }





# class MySpider(scrapy.Spider):
#     name = "linksData"
#     start_urls = ["https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1"]

#     def parse(self, response):
#         for link in response.css('a::attr(href)'):
#             yield {'link': link.get()}







################ MAİN KOD BU!!!!!
# class TransfermarktSpider(scrapy.Spider):
#     name = 'linksData'
    
#     def start_requests(self):
        
#         urls = ['https://www.transfermarkt.co.uk/wettbewerbe/europa','https://www.transfermarkt.co.uk/wettbewerbe/europa?page=2']
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         links = response.xpath('//a/@href').extract()
#         for link in links:
#             yield{
#                 "linkler":link                
#                 }
            
            
# class TransfermarktSpider(scrapy.Spider):
#     name = 'linksData'
#     start_urls = ["https://www.transfermarkt.co.uk/wettbewerbe/europa"]
    
    
#     def parse(self, response):
#         for items in response.css('table.inline-table'):
#             # Her bir element içindeki tüm linkleri alın
#             for link in items.css('a::attr(href)'):
#                 yield {
#                     'link': link.get()
                    
                       
                       
#                        }
                
                







