'''
Created on 2016年1月4日

@author: cqychen
'''
import time as dt
import loaddata.loadcompanydata as lc

if __name__ == '__main__':
    '''
    程序运行开始计时
    '''
    print("======================start to go=======================")
    print("=================task start,calculate start time==================")
    start_time=dt.time()
    start_date_formate=dt.strftime("%Y-%m-%d %H:%M:%S",dt.localtime())
    print("start time is :",start_date_formate," start seconds is :",start_time)
    print("===================================================================")
    
    '''
    运行代码区域，调用数据下载接口，计算接口，报表短信推送接口。
    '''
    lc.company_industry_data();
    '''
    程序运行结束计时
    '''
    print("===========================task finished,caculate the end time ====================")
    end_time=dt.time()
    end_date_formate=dt.strftime("%Y-%m-%d %H:%M:%S",dt.localtime())
    print("start time is :",end_date_formate," start seconds is :",end_time," the program cost :",end_time-start_time,"seconds")
    print("===================================================================================")
    