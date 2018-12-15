# thewaytohome

一个帮助你找到回家机票的软件


## jd_spider.py

监视[京东旅行-机票](https://jipiao.jd.com/)

**使用方法**

将代码中 payload 结构体中的 depCity、arrCity、depDate、arrDate 修改为你的需要。例如：

```
    payload = {'depCity': '烟台', 'arrCity': '合肥', 'depDate': '2019-01-02', 'arrDate': '2019-01-02', 'queryModule': '1',
               'lineType': 'OW', 'queryType': 'jipiaoindexquery'}
```
监视2019年1月2号从烟台到合肥的机票。

**使用效果**
依次显示 航班号 发出时间 到达时间 最低价格
![image](./img/jd.png)

## 修改记录

    20181216
        添加监视京东机票程序。
---

如有其他疑问联系本人：liuchuanbin1992@gmail.com
