#LÄ°NK =>https://youtu.be/C5cfpY7Gedk
import scrapy
#    //div[@class='abc']/p/text()
## //ul[@class='topic-list partial']/li/a/text()
##   //ul[@class='topic-list partial']/li/a[starts-with(@href,"/hayatin-tadi")]/text() --> Özellikle a'nın href özelliğini alıp o href'in "hayatin-tadi" ile baslayanını almak istiyorsak
## ends-with olanı da var

## //ul[@class='topic-list partial']/li/a[contains(text(), "22 ekim")] ## texte göre almak için de bu şekilde
## xpath'ini yazarken başına nokta koymazsan ilk veriyi tekrar eder.

class CokSatanlarSpider(scrapy.Spider):
    name = 'cok_satanlar'
    allowed_domains = ['www.kidega.com']
    start_urls = ['https://www.kidega.com/cok-satan-kitaplar']

    def parse(self, response):
        kitaplar=response.xpath("//div[@class='prd-list']/ul/li")
        for kitap in kitaplar:
            kitapAdi=kitap.xpath(".//div[@class='prd-name title display-flex justify-between align-items-center']/h3/text()").get() # Bu da uzun hali-> kitapAdi=kitap.xpath("//div[@class='prd-list']/ul/li/div/div[@class='prd-body itemHeader']/div[@class='prd-name title display-flex justify-between align-items-center']/h3/text()")
            kitapLink=kitap.xpath(".//div[@class='prd-image-org loaded-img']/img/@data-original").get()
            detayLink=kitap.xpath(".//div[@class='prd-image image']/div/img/@data-original").get()
            kitapFiyat=kitap.xpath(".//div[@class='lastPrice']/div/text()").get()
            kitapYazar=kitap.xpath(".//div[@class='manufacturer']/a/span/text()").get()
            kitapYayin=kitap.xpath(".//span[@class='distributor-name']/text()").get()
            
            
            
            # kitapLink=kitap.xpath(".//div[@class='prd-image-org loaded-img']/img/@src").get()
            
            
            yield{ #yield'ı return olarak düşünebiliriz
                'kitap ismi':kitapAdi,
                'kitap link':kitapLink,
                'kitap fiyat':int(kitapFiyat),
                'kitap yazari':kitapYazar,
                'kitap Yayıncısı':kitapYayin,
                'detay':detayLink
                
                }
        # nextPage=response.xpath("//a[@id='ctl00_u8_ascUrunList_ascPagingDataAlt_lnkNext']/@href").get()
        # fullLink=f"https://www.kidega.com{nextPage}"
        # # fullLink=response.urljoin(nextPage) #bu da usttekiyle aynı aslında. allowed_domain ile nextPage linkini birleştiriyor.
        # if nextPage: #eger nextPage varsa(çünkü son sayfaya geldiginde durması gerek)  ##BUNU KULLANMAK İSTİYORSAK ALLOWED_DOMAİNSTEKİ "WWW." 'YI KALDIRCAZ CÜNKÜ ZATEN KENDİ EKLİYOR
        #     yield scrapy.Request(url=fullLink, callback=self.parse) ##callback=self.parse --> tekrar diğer sayfalar için de aynı parse işlemlerini yapmamızı sağlıyor.
   
        
   
    
   
    
   
            
# class CokSatanlarSpider(scrapy.Spider):
#     name = 'cok_satanlar'
#     allowed_domains = ['www.kidega.com']
#     start_urls = ['https://www.kidega.com/cok-satan-kitaplar']
    
#     def start_requests(self):
#         yield scrapy.Request(url='https://www.kidega.com/cok-satan-kitaplar',callback=self.parse,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'} )
#         #bu varken ustteki  start_urls = ['https://www.kidega.com/cok-satan-kitaplar'] silinebilir.
#     def parse(self, response):
#         kitaplar=response.xpath("//ul[@class='emosInfinite product-list-grid view-box']/li")
#         for kitap in kitaplar:
#             kitapAdi=kitap.xpath(".//div[@class='prd-name title display-flex justify-between align-items-center']/h3/text()").get()
#             imgLink=kitap.xpath(".//div[@class='prd-image-org loaded-img']/img/@data-original").get()
#             yazarAdi=kitap.xpath(".//div[@class='authorArea']/div/a/span/text()").get()
#             yield{
#                 # 'kitapİsmi':kitapAdi,
#                 # 'kitapLinki':imgLink,
#                 # 'kitapYazari':yazarAdi
#                 }
            
            
#         nextPage=response.xpath("//a[@id='ctl00_u8_ascUrunList_ascPagingDataAlt_lnkNext']/@href").get()
#         fullLink=f"https://www.kidega.com{nextPage}"
#         print(fullLink)

#         if fullLink:
#             print(fullLink)
#             yield scrapy.Request(url=fullLink,callback=self.parse,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    