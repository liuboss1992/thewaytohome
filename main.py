# -*- coding:utf-8 -*-


import time
import datetime
from jd_spider import jd_spider_flights
from mailapp import ustcmail
import argparse



def main():
    parser = argparse.ArgumentParser(description='Thewaytohome')
    parser.add_argument('--sn', default='lcb592', type=str, help='name of sender account, must be ustc mail')
    parser.add_argument('--pw', default='123456', type=str, help='password of your account')
    parser.add_argument('--ra', default='774054270@qq.com', type=str, help='address of the receiver')
    parser.add_argument('--dd', default='20190102', type=str, help='Departure date')
    parser.add_argument('--tp', default='300', type=int, help='ticket price')
    args = parser.parse_args()
    
    depcity = '烟台'
    arrcity = '合肥'
    dd = args.dd
    date = str(dd[0]+dd[1]+dd[2]+dd[3]+'-'+dd[4]+dd[5]+'-'+dd[6]+dd[7])
    price = args.tp
    while True:
        flag, text = jd_spider_flights(depcity,arrcity,date,price)
        time_stamp = datetime.datetime.now()
        print(time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))
        print(text)
        if flag:
            ustcmail(args.sn,args.pw,args.ra,text)
        time.sleep(1200)

if __name__ == "__main__":
    main()