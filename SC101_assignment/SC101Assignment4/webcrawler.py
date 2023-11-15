"""
File: webcrawler.py
Name: Jim
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all('table', {'class': 't-stripe'})
        m_total = 0
        f_total = 0
        for tag in tags:
            target = tag.tbody.text.split()
            new_data = [target[i:i+5] for i in range(0, 1000, 5)]
            for data in new_data:
                m_total += int(data[2].replace(',', ''))
                f_total += int(data[4].replace(',', ''))
            print(f'Male Number: {m_total}')
            print(f'Female Number: {f_total}')


if __name__ == '__main__':
    main()
