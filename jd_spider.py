# -*- coding:utf-8 -*-

import requests
import time


def jd_spider_flights(depcity,arrcity,date,price):


    headers = {
        'Host': "jipiao.jd.com",
        'Accept': "application/json, text/javascript, */*; q=0.01",
		'Accept-Encoding': "gzip, deflate, br",
		'Accept-Language': "zh-CN,zh;q=0.9",
		'Cache-Control': "no-cache",
		'Connection': "keep-alive",
        'X-Requested-With' : 'XMLHttpRequest',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }

    roon_session = requests.session()

    payload = {'depCity': depcity, 'arrCity': arrcity, 'depDate': date, 'arrDate': date, 'queryModule': '1',
               'lineType': 'OW', 'queryType': 'jipiaoindexquery'}

    url = 'https://jipiao.jd.com/search/queryFlight.action'
    for i in range(10):
        text = ''
        flag = 0
        page = roon_session.get(url,headers=headers, params=payload).json()
        if not page['data']['flights'] is None:
            print('Found!')
            text = date + ','+depcity + '->' + arrcity + ',价格低于' + str(price) + ': \n'
            flag = 0
            #print(text)
            for plan in page['data']['flights']:
                if (plan['bingoLeastClassInfo']['price'])<=price:
                    flag = 1
                    text += str(plan['carrierFlightNo']) + ',' + \
                    str(plan['depTime'][:2]) + ':' + str(plan['depTime'][2:]) + '->' + \
                    str(plan['arrTime'][:2]) + ':' + str(plan['arrTime'][2:]) + \
                    ',价格' + str(plan['bingoLeastClassInfo']['price']) + \
                    ',剩余' + str(plan['bingoLeastClassInfo']['seatNum']) + '张' + '. \n'
            #print(text)
            break
        else:
        	print ('Failed for the %d requests, please wait 10 seconds'%i)
  	        time.sleep(3)
    return flag, text


if __name__ == "__main__":
    depcity = '烟台'
    arrcity = '合肥'
    date = '2019-01-02'
    price = 500
    flag, text = jd_spider_flights(depcity,arrcity,date,price)
    print(text)