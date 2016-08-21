#! /usr/bin/env python
#coding=utf-8
def delta_box(lamda,Tgw,RH,Tgn):
    """根据输入的保温材料导热系数计算矩形管道的保温材料防结露厚度

    :lamda: 保温材料导热系数
    :Tgw: 保温层外温度
    :RH: 保温层外相对湿度
    :Tgn: 保温层内流体温度
    :returns: 保温材料厚度(m)

    """
    agw=8.14 #保温层外表面换热系数
    #  Tgn=21.0   #管道内流体温度
    #  Tgw=29.0   #保温层外空气温度
    Tl=dewpoint(Tgw,RH)#保温层外空气露点
    delta_box=lamda*(Tl-Tgn)/agw/(Tgw-Tl)
    return delta_box
def dewpoint(Temp,RH):
    """露点温度计算

    :Temp: 温度
    :RH: 相对湿度
    :returns: 空气露点

    """
    import math
    a=17.27
    b=237.7
    R=a*Temp/(b+Temp)+math.log(RH/100.0)
    dewpoint=b*R/(a-R)
    return dewpoint

#  print delta_box(0.035,29.,75.,9.)*1000, dewpoint(25,75)

