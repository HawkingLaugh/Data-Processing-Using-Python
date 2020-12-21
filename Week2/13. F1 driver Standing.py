import re
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.formula1.com/en/results.html/2020/drivers.html')
soup = BeautifulSoup(r.text, 'lxml')

"""
2. Retrieve the  data of the athletes from the website of https://www.volleyball.world/en/vnl/2019/women/resultsandranking/round1(include TEAMS and TOTAL, WON, LOST of MATCHES) 

Note: Although we can get the every item just like 'USA' or '15' using the way we have learned, 
but it will ccut off the link between the data. It is better to parse the data in groups. 
Because the source codes including the athletes' data are located in some lines and there are many spaces  
in the front of the lines, we can use the  '\s+' representing the whitespaces(spaces and \n) to match the multiple lines.
"""