import requests
import math
import json
import sys

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
querystring = {"country":"Canada"}
headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "2e50398222mshf98a0c9a10f5206p128af4jsnfd780e15b976"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


data = response.json()['data']['covid19Stats']
def all():
    global data
    cases = [int(i['confirmed']) for i in data]
    deaths = [int(i['deaths']) for i in data]
    recovered = [i['recovered'] for i in data if i['recovered']!=None]

    death_rate = tols(sum(cases), sum(deaths))
    recovery_percentage = tols(sum(cases),sum(recovered))

    print('Canada:')
    print(' confirmed cases:',sum(cases))
    print(' deaths:',sum(deaths))
    print(' Recovered: ', sum(recovered))
    print(' Rate of Recovery: ',recovery_percentage,'%')
    print(' Death Rate: ', death_rate,'%')

def search():
    global data
    search_by_province = sys.argv[2]
    for i in data:
        if search_by_province.capitalize() in i['province']:
            target_province = i

            death_rate = tols(int(i['confirmed']),int(i['deaths']))
            recovery_percentage = tols(int(i['confirmed']),int(i['recovered']))
            
            print(target_province['province'])
            print(' Confirmed: ', target_province['confirmed'])
            print(' Deaths: ', target_province['deaths'])
            print(' Recovered: ', target_province['recovered'])
            print(' Rate of Recovery: ', recovery_percentage,'%')
            print(' Death Rate: ', death_rate,'%')
            print(' Last Updated: ', target_province['lastUpdate'])
            break
        #ADD TOLS TO SEARCH FEATURE
def tols(big, small):
    return round(float(small/big)*100, 3)
if __name__ == '__main__':
    if sys.argv[1] == '-s':
        search()
    elif sys.argv[1] == '-a':
        all()
