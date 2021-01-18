from bs4 import BeautifulSoup as bs
import requests
import pandas
from openpyxl import workbook
URL = 'https://cracku.in/'
LOGIN_ROUTE = 'users/login'

HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
           , 'origin' : URL, 'referer' : URL + LOGIN_ROUTE}
s = requests.Session()
csrf_token = s.get(URL).cookies['csrftoken']

login_payload = {'email' : 'asbs51237@gmail.com' ,
                 'password' : 'xyz@123',
                 'csrfmiddlewaretoken' : csrf_token}
login_req = s.post(URL+LOGIN_ROUTE, headers=HEADERS,data=login_payload)
#print (login_req.status_code)
marks = {'RANK' : [],
         'VARC' : [],
         'LRDI' : [],
         'QUANT' : [],
         'TOTAL' : []}
for i in range(1,26) :
    soup = bs(s.get(URL+'cat-toppers-list?page='+str(i)).text,'html.parser')
    data = soup.findAll('td')
    for j in range(6,len(data),6) :
        marks['RANK'].append(data[j].text)
        marks['VARC'].append(float(data[j+1].text))
        marks['LRDI'].append(float(data[j+2].text))
        marks['QUANT'].append(float(data[j+3].text))
        marks['TOTAL'].append(float(data[j+4].text))
'''    if i == 3 :
        break'''

df = pandas.DataFrame(marks,columns=['RANK','VARC','LRDI','QUANT','TOTAL'])
print(df)
df.to_excel(r'C:/Users/hp/Desktop/WebScrapper/CATDATA.xlsx',index=False,header=True)
#print(type(marks[1][1]))
'''for i in range(len(marks)) :
    print(marks[i])'''




