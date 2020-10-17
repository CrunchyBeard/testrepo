# -*- coding: utf-8 -*-
#prompt for hours and rate per hours then get back gross pay

hrs = input('Enter hours: ')
rte = input('Enter Rate per Hour: ')

shrs = float(hrs)
srte = float(rte)

grspy = shrs * srte

print('Pay: ', grspy)

