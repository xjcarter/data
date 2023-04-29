
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import datetime
import argparse

WEEKDAYS = ['MON','TUE','WED','THU','FRI','SAT','SUN']

## scrapes holiday calendar website 
## to create a csv calendar file

def convert(string):
    # divide date and holiday
    v = re.sub("</td><td>", "|", string)
    # remove row and cell html tags
    k = re.sub("<.*?>", "", v)
    pp = k.split("|")
    # keep holiday tag and covert date string
    holiday, date = pp[0], datetime.datetime.strptime(pp[1], "%B %d, %Y")
    holiday = re.sub(",", "",holiday)
    date_str = datetime.datetime.strftime(date, "%Y-%m-%d")
    return f'{date_str},{WEEKDAYS[date.weekday()]},{holiday}'


if __name__ == "__main__":

    hols = []
    root = "http://www.market-holidays.com/"
    for year in range(1990, datetime.datetime.now().year+1):
        url = root + f'/{year}'
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        jj = str(soup)

        ## 'v' is an array of holiday calendar entries 
        ## each looks like '<tr><td>Thanksgiving</td><td>November 24, 2022</td></tr>'
        v = re.findall("<tr>.*</tr>",jj)
        hols = hols + v

    print('Date,DayOfWeek,Holiday')
    cvt = [ convert(d) for d in hols ]
    for c in cvt: 
        print(c)

    
