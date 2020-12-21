import re
import requests

year = 2019
def crawler(url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as err:
        return err
    r.encoding = r.apparent_encoding
    # put the re expression on one line
    pattern = re.compile('href="/en/vnl/%s/women/teams/.*?">(.*?)</a></figcaption>\s+</figure>\s+</td>\s+<td></td>\s+<td class=".*?">(.*?)</td>\s+<td class=".*?">(.*?)</td>\s+<td class=".*?">(.*?)</td>' % year)
    p = re.findall(pattern, r.text)
    return p


url = 'http://www.volleyball.world/en/vnl/{}/women/resultsandranking/round1'.format(year)
result = crawler(url)
for i in result:
    print(i)