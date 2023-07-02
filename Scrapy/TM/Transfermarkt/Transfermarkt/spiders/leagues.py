import scrapy
from urllib.parse import urlparse
import re
import json

class LeaguesSpider(scrapy.Spider):
    name = 'leagues'

    
    def start_requests(self):
        urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2021',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2020',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2019',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2018',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2017',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2016',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2015',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2014',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2013',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2012',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2011',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2010',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2009',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2008',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2007',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2006',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2005',
        'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2004',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2021',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2020',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2019',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2018',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2017',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2016',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2015',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2014',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2013',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2012',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2011',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2010',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2009',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2008',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2007',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2006',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2005',
        'https://www.transfermarkt.co.uk/super-lig/startseite/wettbewerb/TR1/plus/?saison_id=2004',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2021',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2021',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2020',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2019',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2018',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2017',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2016',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2015',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2014',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2013',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2012',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2011',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2010',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2009',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2008',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2007',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2006',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2005',
        'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1/plus/?saison_id=2004',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2020',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2019',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2018',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2017',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2016',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2015',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2014',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2013',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2012',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2011',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2010',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2009',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2008',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2007',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2006',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2005',
        'https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2004',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2021',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2020',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2019',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2018',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2017',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2016',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2015',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2014',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2013',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2012',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2011',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2010',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2009',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2008',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2007',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2006',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2005',
        'https://www.transfermarkt.co.uk/ligue-1/startseite/wettbewerb/FR1/plus/?saison_id=2004',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2021',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2020',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2019',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2018',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2017',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2016',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2015',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2014',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2013',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2012',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2011',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2010',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2009',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2008',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2007',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2006',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2005',
        'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2004'
            ] ## Excell'de düzenlediğin tüm linkleri içersine yolla.
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)    
            
            

    def parse(self, response):
        toplam=[]

        
        teams=response.xpath("//div[@id='yw1']/table/tbody/tr") ## her bir takımın bulunduğu satır
        for team in teams:
            
            league_name = re.search(r"/wettbewerb/([^/]+)/", response.url).group(1)  ##Hangi takımın hangi ligde olduğu bilgisi.
            
            team_dict={
                'name':team.xpath(".//td[@class='hauptlink no-border-links']/a/text()").get(),
                'squad':team.xpath(".//td[@class='zentriert'][1]/a/text()").get(),
                'ageAvg':team.xpath(".//td[@class='zentriert'][2]/text()").get(),
                'foreigners':team.xpath(".//td[@class='zentriert'][3]/text()").get(),
                'marketValueAvg':team.xpath(".//td[@class='rechts'][1]/text()").get(),
                'totalMarketValue':team.xpath(".//td[@class='rechts'][2]/a/text()").get(),
                'rank':None,
                'points':None,
                'teamAverage':None,
                'teamMatches':None,               
                'leagueName':league_name
                
                }

            toplam.append(team_dict)
            


            
        rankings=response.xpath("//div[@id='yw4']/table[@class='items']/tbody/tr")
        for ranking in rankings:
            team_rank = ranking.xpath(".//td[@class='rechts hauptlink']/text()").get()
            team_name = ranking.xpath(".//td[@class='no-border-links hauptlink']/a/@title").get()
            team_matches = ranking.xpath(".//td[4]/text()").get()
            team_average=ranking.xpath(".//td[5]/text()").get()
            team_points = ranking.xpath(".//td[6]/text()").get()
                
            # print("2. Kısım:"+team_name)
            # for i in ekle:
            #     if i==team_name:
            #         print("**********"+i)
            
            


            for x in toplam:
                if x['name']==team_name:
                    x['rank']=team_rank
                    x['points']=team_points
                    x['teamMatches']=team_matches
                    x['teamAverage']=team_average
                    


        for team_dict in toplam:
            yield team_dict
  




#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$






"""
class LeaguesSpider(scrapy.Spider):
    name = 'leagues'
    start_urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2021'] #Buraya tüm takımların linklerini ekleyeceğiz.
    
    #hauptlink no-border-links
    #no-border-links hauptlink
    
    def parse(self, response):
        
        teams=response.xpath("//div[@id='yw4']/table[@class='items']/tbody/tr")
        
        for team in teams:
                team_rank = team.xpath(".//td[@class='rechts hauptlink']/text()").get()
                team_name = team.xpath(".//td[@class='no-border-links hauptlink']/a/@title").get()
                team_matches_played = team.xpath(".//td[4]/text()").get()
                team_average=team.xpath(".//td[5]/text()").get()
                team_points = team.xpath(".//td[6]/text()").get()
        

                yield {
                'Position': team_rank,
                'Team':team_name,
                'Matches Played': team_matches_played,
                'average':team_average,
                'Points': team_points
                }   
                
"""

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$




"""
class LeaguesSpider(scrapy.Spider):
    name = 'leagues'
    # start_urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1'] #Buraya tüm takımların linklerini ekleyeceğiz.
    
    def start_requests(self):
        urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1'
                #'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1',  ## Excell'de düzenlediğin tüm linkleri içersine yolla.
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        
        teams=response.xpath("//div[@id='yw1']/table/tbody/tr") ## her bir takımın bulunduğu satır
        for team in teams:
            name=team.xpath(".//td[@class='hauptlink no-border-links']/a/text()").get()
            squad=team.xpath(".//td[@class='zentriert'][1]/a/text()").get()
            ageAvg=team.xpath(".//td[@class='zentriert'][2]/text()").get()
            foreigners=team.xpath(".//td[@class='zentriert'][3]/text()").get()
            marketValueAvg=team.xpath(".//td[@class='rechts'][1]/text()").get()
            totalMarketValue=team.xpath(".//td[@class='rechts'][2]/a/text()").get()
            links=team.xpath(".//td[@class='hauptlink no-border-links']/a[1]/@href").get()
            yield{
                'Name':name,
                'Squad':squad,
                'Age Avg':ageAvg,
                'Foreigners':foreigners,
                'Market Value Avg':marketValueAvg,
                'Total Market Value':totalMarketValue,
                'linkler':"https://www.transfermarkt.co.uk"+links
    
                }   
"""            
   
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
""" 
class LeaguesSpider(scrapy.Spider):
    name = 'leagues'
    # start_urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1'] #Buraya tüm takımların linklerini ekleyeceğiz.
    
    start_urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1']
    

    def parse(self, response):
        
        teams=response.xpath("//div[@id='yw1']/table/tbody/tr") ## her bir takımın bulunduğu satır
        for team in teams:
            name=team.xpath(".//td[@class='hauptlink no-border-links']/a/text()").get()
            squad=team.xpath(".//td[@class='zentriert'][1]/a/text()").get()
            ageAvg=team.xpath(".//td[@class='zentriert'][2]/text()").get()
            foreigners=team.xpath(".//td[@class='zentriert'][3]/text()").get()
            marketValueAvg=team.xpath(".//td[@class='rechts'][1]/text()").get()
            totalMarketValue=team.xpath(".//td[@class='rechts'][2]/a/text()").get()
            #links=team.xpath(".//td[@class='hauptlink no-border-links']/a[1]/@href").get()
            yield{
                'Name':name,
                'Squad':squad,
                'Age Avg':ageAvg,
                'Foreigners':foreigners,
                'Market Value Avg':marketValueAvg,
                'Total Market Value':totalMarketValue,
                #'linkler':"https://www.transfermarkt.co.uk"+links
    
                }   
        yield scrapy.Request(url='https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/tabelle', callback=self.parse_table)
            
            
            
    def start_requests(self):
        urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/tabelle']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_table)



    def parse_table(self, response):
        for row in response.xpath("//div[@id='yw5']/table/tbody/tr"):
            position = row.xpath("td[@class='rechts hauptlink']/text()").get()
            team = row.xpath(".//td[3]/a/@title").get()
            matches_played = row.xpath(".//td[4]/text()").get()
            average=row.xpath(".//td[5]/text()").get()
            points = row.xpath(".//td[6]/text()").get()
            yield {
                'Position': position,
                'Team': team,
                'Matches Played': matches_played,
                'average':average,
                'Points': points
        }

"""         
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$         
                

"""

############### ÇALIŞAN KOD
# from urllib.parse import urlparse
# import re

class LeaguesSpider(scrapy.Spider):
    name = 'leagues'

    
    #start_urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1']
    def start_requests(self):
        urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1',
                'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1'  ## Excell'de düzenlediğin tüm linkleri içersine yolla.
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
            
    def parse(self, response):
        toplam=[]

        


        
        teams=response.xpath("//div[@id='yw1']/table/tbody/tr") ## her bir takımın bulunduğu satır
        for team in teams:
            team_dict={
                'name':team.xpath(".//td[@class='hauptlink no-border-links']/a/text()").get(),
                'squad':team.xpath(".//td[@class='zentriert'][1]/a/text()").get(),
                'ageAvg':team.xpath(".//td[@class='zentriert'][2]/text()").get(),
                'foreigners':team.xpath(".//td[@class='zentriert'][3]/text()").get(),
                'marketValueAvg':team.xpath(".//td[@class='rechts'][1]/text()").get(),
                'totalMarketValue':team.xpath(".//td[@class='rechts'][2]/a/text()").get(),
                'rank':None,
                'points':None

                
                }

            toplam.append(team_dict)
            
        
            
   
        

            
            
        for ranking in response.xpath("//div[@id='yw5']/table/tbody/tr"):
            team_rank = ranking.xpath("td[@class='rechts hauptlink']/text()").get()
            team_name = ranking.xpath(".//td[3]/a/@title").get()
            #team_matches_played = ranking.xpath(".//td[4]/text()").get()
            #team_average=ranking.xpath(".//td[5]/text()").get()
            team_points = ranking.xpath(".//td[6]/text()").get()
        #     yield {
        #         'Position': team_rank,
        #         'Team':team_name,
        #         # 'Matches Played': team_matches_played,
        #         # 'average':team_average,
        #         'Points': team_points
        # }   
   
            
        


            for x in toplam:
                if x['name']==team_name:
                    x['rank']=team_rank
                    x['points']=team_points
                    

    

        for team_dict in toplam:
            yield team_dict
"""
 #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""    
from urllib.parse import urlparse
import re
class LeaguesSpider(scrapy.Spider):
    name = 'leagues'

    
    #start_urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1']
    # def start_requests(self):
    #     urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1',
    #             'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1'  ## Excell'de düzenlediğin tüm linkleri içersine yolla.
    #             ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
            

    start_urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2021']


    # def start_requests(self):
    #     urls = ['https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2021',
    #                   'https://www.transfermarkt.co.uk/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2021'] ## Excell'de düzenlediğin tüm linkleri içersine yolla.
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse) 
            



            
            
    def parse(self, response):
        toplam=[]

        


        
        # teams=response.xpath("//div[@id='yw1']/table/tbody/tr") ## her bir takımın bulunduğu satır
        # for team in teams:
            
        #     # league_name = re.search(r"/wettbewerb/([^/]+)/", response.url).group(1)  ##Hangi takımın hangi ligde olduğu bilgisi.
        #     # print(league_name)
            
        #     team_dict={
        #         'name':team.xpath(".//td[@class='hauptlink no-border-links']/a/text()").get(),
        #         'squad':team.xpath(".//td[@class='zentriert'][1]/a/text()").get(),
        #         'ageAvg':team.xpath(".//td[@class='zentriert'][2]/text()").get(),
        #         'foreigners':team.xpath(".//td[@class='zentriert'][3]/text()").get(),
        #         'marketValueAvg':team.xpath(".//td[@class='rechts'][1]/text()").get(),
        #         'totalMarketValue':team.xpath(".//td[@class='rechts'][2]/a/text()").get(),
        #         'rank':None,
        #         'points':None
        #         #'leagueName':league_name

                
        #         }

        #     toplam.append(team_dict)
            
        
            
   
        teams=response.xpath("//div[@id='yw4']/table/tbody/tr") ## her bir takımın bulunduğu satır
        for team in teams:
           team_name=team.xpath(".td[3]/a/text()").get()

           yield {
                # 'Position': team_rank,
                'Team':team_name
                # 'Matches Played': team_matches_played,
                # 'average':team_average,
                # 'Points': team_points
        }   

            
            
        # for ranking in response.xpath("//div[@id='yw4']/table/tbody/tr"):
        #     # team_rank = ranking.xpath(".td[@class='rechts hauptlink']/text()").get()
        #     team_name = ranking.xpath(".td[@class='no-border-links hauptlink']/a/@title").get()
        #     #team_matches_played = ranking.xpath(".//td[4]/text()").get()
        #     #team_average=ranking.xpath(".//td[5]/text()").get()
        #     # team_points = ranking.xpath(".td[@class='zentriert'][3]/text()").get()
        #     yield {
        #         # 'Position': team_rank,
        #         'Team':team_name
        #         # 'Matches Played': team_matches_played,
        #         # 'average':team_average,
        #         # 'Points': team_points
        # }   
   
            
        


        #     for x in toplam:
        #         if x['name']==team_name:
        #             x['rank']=team_rank
        #             x['points']=team_points
                    

    

        # for team_dict in toplam:
        #     yield team_dict





"""






     #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$         
"""   
from urllib.parse import urlparse
import re

class LeaguesSpider(scrapy.Spider):
    name = 'leagues'

    
    def start_requests(self):
        urls = ['https://www.transfermarkt.co.uk/serie-a/startseite/wettbewerb/IT1/plus/?saison_id=2020',
                      'https://www.transfermarkt.co.uk/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2021'] ## Excell'de düzenlediğin tüm linkleri içersine yolla.
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)    
            
            

    def parse(self, response):
        toplam=[]

        
        teams=response.xpath("//div[@id='yw1']/table/tbody/tr") ## her bir takımın bulunduğu satır
        for team in teams:
            
            league_name = re.search(r"/wettbewerb/([^/]+)/", response.url).group(1)  ##Hangi takımın hangi ligde olduğu bilgisi.
            
            team_dict={
                'name':team.xpath(".//td[@class='hauptlink no-border-links']/a/text()").get(),
                'squad':team.xpath(".//td[@class='zentriert'][1]/a/text()").get(),
                'ageAvg':team.xpath(".//td[@class='zentriert'][2]/text()").get(),
                'foreigners':team.xpath(".//td[@class='zentriert'][3]/text()").get(),
                'marketValueAvg':team.xpath(".//td[@class='rechts'][1]/text()").get(),
                'totalMarketValue':team.xpath(".//td[@class='rechts'][2]/a/text()").get(),
                'rank':None,
                'points':None,
                'leagueName':league_name
                
                }

            toplam.append(team_dict)
            


            
        rankings=response.xpath("//div[@id='yw4']/table[@class='items']/tbody/tr")
        for ranking in rankings:
            team_rank = ranking.xpath(".//td[@class='rechts hauptlink']/text()").get()
            team_name = ranking.xpath(".//td[@class='no-border-links hauptlink']/a/@title").get()
            team_matches_played = ranking.xpath(".//td[4]/text()").get()
            team_average=ranking.xpath(".//td[5]/text()").get()
            team_points = ranking.xpath(".//td[6]/text()").get()
                
            # print("2. Kısım:"+team_name)
            # for i in ekle:
            #     if i==team_name:
            #         print("**********"+i)
            
            


            for x in toplam:
                if x['name']==team_name:
                    x['rank']=team_rank
                    x['points']=team_points
                    


        for team_dict in toplam:
            yield team_dict
"""  
   
            
            
            
            
            
            