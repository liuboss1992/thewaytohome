# -*- coding:utf-8 -*-

import requests
import time

def jd_spider_flights():


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

    payload = {'depCity': '烟台', 'arrCity': '合肥', 'depDate': '2019-01-02', 'arrDate': '2019-01-02', 'queryModule': '1',
               'lineType': 'OW', 'queryType': 'jipiaoindexquery'}

    url = 'https://jipiao.jd.com/search/queryFlight.action'

    for i in range(10):
        page = roon_session.get(url,headers=headers, params=payload).json()
        if not page['data']['flights'] is None:
        	break
        else:
        	print ('Failed for the %d requests, please wait 10 seconds'%i)
  	        time.sleep(10)


    for plan in page['data']['flights']:
        print ("%s %s %s %s"%(plan['carrierFlightNo'], \
        	plan['depTime'], \
        	plan['arrTime'], \
        	plan['bingoLeastClassInfo']['price']))


if __name__ == "__main__":
    jd_spider_flights()