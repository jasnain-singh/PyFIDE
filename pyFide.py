# Importing dependenciesimport numpy as np
import pickle
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

# from pl_list import _players_list
# from id_fide import _fide_ids

with open('_players_list.pickle', 'rb') as f1:
    _players_list = pickle.load(f1)
with open('_fide_ids.pickle', 'rb') as f2:
    _fide_ids = pickle.load(f2)

# Setting selenium options
options = Options() 
options.add_argument("-headless")

# exception lists for players that have more than their first and last name on the website.
# prevents errors during string splitting and slicing while getting the individual data of a player.
# if a new player is added with 3 or 4 names, append FIRST NAME to the suitable list.
name3_exception = ['Dominguez', 'Le,', 'Vidit,', 'Tabatabaei,', 'Narayanan','Martirosyan,',
                   'Niemann,','Anton', 'Van', 'Aravindh,','Vallejo','Li,', 'Bjerre,']
name4_exception = ['Howell,', 'Nguyen,']


class FideInfo:
    
    def __init__(self, players_list = _players_list, fide_ids = _fide_ids):
        self.players_list = players_list
        self.fide_ids = fide_ids
        
    URL1 = 'https://ratings.fide.com'
    URL2 = 'https://ratings.fide.com/profile/'
    XPATH = '/html/body/section[3]/div[2]/div/div[4]/div/div[1]/div[2]/div/div[2]/table/tbody/tr'
        
    
    def getTop(self, max:int = 100):
        p_ranks = []
        p_name = []
        p_country = []
        p_elo = []
        p_year = []
        p_ranks
        for players in self.players_list[1:max+1]:
            players = players.split(' ')
            
            if players[1] in name3_exception:
                p_ranks.append(players[0])
                p_name.append(players[1] + ' ' + players[2] + ' ' + players[3].split('\n')[0])
                p_country.append(players[3].split('\n')[1])
                p_elo.append(players[4])
                p_year.append(players[7])
                continue
            
            if players[1] in name4_exception:
                p_ranks.append(players[0])
                p_name.append(players[1] + ' ' + players[2] + ' ' + players[3] +  ' ' + players[4].split('\n')[0])
                p_country.append(players[4].split('\n')[1])
                p_elo.append(players[5])
                p_year.append(players[8])
                continue
                
            p_ranks.append(players[0])
            p_name.append(players[1] + ' ' + players[2].split('\n')[0])
            p_country.append(players[2].split('\n')[1])
            p_elo.append(players[3])
            p_year.append(players[6])
            
        return pd.DataFrame(list(zip(p_ranks, p_name, p_country, p_elo, p_year)),
                            columns=['Ranking', 'Name', 'Country', 'Elo', 'Birth Year'])
            
            
    def updateTop100(self, ) -> list:
        players_list = []
        with webdriver.Firefox(options=options) as driver:
            res = driver.get(self.URL1)
            table = driver.find_element(By.CLASS_NAME, 'table-top')
            rows = table.find_elements(By.TAG_NAME, 'tr')
            
            for x in range(len(rows)):
                players_list.append(rows[x].text)
                
        return players_list
    
    
    def getFideIds(self, ) -> pd.DataFrame:
        x = pd.DataFrame(self.fide_ids.items(), columns=['Name', 'FIDE id'])
        y = pd.concat([FideInfo.getTop(self,).set_index('Name'), x.set_index('Name')], axis=1).reset_index()
        
        return y
        
    
    def updateFideId(self, ) -> dict:
        with webdriver.Firefox(options=options) as driver:
            wait = WebDriverWait(driver, 100)
            res = driver.get(self.URL1)
                
            idscrape = []
            names = []
            for x in range(len(list(FideInfo.getTop(self,)['Name']))):
                idscrape.append(wait.until(EC.visibility_of_element_located(
                    (By.XPATH, f'{self.XPATH}[{x+1}]/td[2]/a'))).get_attribute('href')
                            )
                
                names.append(wait.until(EC.visibility_of_element_located(
                    (By.XPATH, f'{self.XPATH}[{x+1}]/td[2]/a'))).text
                            )
        
        fide_ids = {}
        for idx, ids in enumerate(idscrape):
            x = ids.strip(self.URL2)
            fide_ids[f'{names[idx]}'] = x
            
        return fide_ids
            
            
    def getFideId(self, name:str) -> int:
        return int(self.fide_ids[name])
    
    
    def getAllRatings(self, name:str):
        new_list = []
        x = self.fide_ids[name]
        
        with webdriver.Firefox(options=options) as driver:
            wait = WebDriverWait(driver, 100)
            res = driver.get(f'{self.URL2}{x}/chart')
            table = driver.find_element(By.CSS_SELECTOR, 'table.profile-table.profile-table_chart-table').text.split('\n')
            
            for values in table[1:]:
                new_list.append(values.strip().split('   '))
    
        return new_list
    
    
    def classical(self, name:str = None) -> pd.DataFrame: 
        period1 = []
        classical_rtngs = []
        classical_gms = []
       
        
        for idx, item in enumerate(FideInfo.getAllRatings(self, name=name)):
            period1.append(item[0])
            classical_rtngs.append(item[1])
            classical_gms.append(item[2])
            
        return pd.DataFrame(list(zip(period1, classical_rtngs, classical_gms)),
                            columns=['Period', 'Classical Rating', 'Classical GMS'])
        
    
    def rapid(self, name:str = None) -> pd.DataFrame:
        period2 = []
        rapid_rtngs = []
        rapid_gms = []

        for idx, item in enumerate(FideInfo.getAllRatings(self, name=name)):
            try:
                period2.append(item[0])
                rapid_rtngs.append(item[3])
                rapid_gms.append(item[4])
            except:
                print(f'Operation complete')
                print(f'Cause: IndexError at {item}, index[{idx}]')
                break
            
        return pd.DataFrame(list(zip(period2, rapid_rtngs, rapid_gms)),
                            columns=['Period', 'Rapid Rating', 'Rapid GMS'])
    
    
    def blitz(self, name:str = None) -> pd.DataFrame:
        period3 = []
        blitz_rtngs = []
        blitz_gms =[]

        for idx, item in enumerate(FideInfo.getAllRatings(self, name=name)):
            try:
                period3.append(item[0])
                blitz_rtngs.append(item[5])
                blitz_gms.append(item[6])
            except:
                print(f'Operation complete')
                print(f'Cause: IndexError at {item}, index[{idx}]')
                break
            
        return pd.DataFrame(list(zip(period3, blitz_rtngs, blitz_gms)),
                            columns=['Period', 'Blitz Rating', 'Blitz GMS'])
