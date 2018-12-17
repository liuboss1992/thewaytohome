# -*- coding:utf-8 -*-


import time
import datetime
from jd_spider import jd_spider_flights
from mailapp import ustcmail
import argparse



def main():
    depcity = '烟台'
    arrcity = '合肥'
    date = '2019-01-02'
    price = 300
    while True:
        flag, text = jd_spider_flights(depcity,arrcity,date,price)
        if flag:
            ustcmail(args.sn,args.pw,args.ra,text)
        time.sleep(1200)

    print(text)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Thewaytohome')
    parser.add_argument('--sn', default='lcb592', type=str, help='name of sender account, must be ustc mail')
    parser.add_argument('--pw', default='123456', type=str, help='password of your account')
    parser.add_argument('--ra', default='774054270@qq.com', type=str, help='address of the receiver')
    args = parser.parse_args()

    main()