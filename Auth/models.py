from django.db import models
import psycopg2
import os


try:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
except:
    conn = psycopg2.connect(database="d7pibsdo79jogi",host="ec2-52-86-25-51.compute-1.amazonaws.com",port=5432,user="cccbiffnldwfkf",password="605444bcd83d702da6e7f56cb2fba0ebb74fb3db14dc5a0c1555bbfa75a357a1")

# Create your models here.

class dashboard_page_context:
    def compile(CustomerId):
        self = dict()
        self['Revenue'] = dashboard_page_context.revenue(CustomerId)
        self['parked'] = dashboard_page_context.parked(CustomerId)
        return self

    def revenue(CustomerId):
        return {'Hul':'None'}

    def parked(CustomerId):
        with conn.cursor() as cursor:
            cursor.execute("""SELECT  COUNT("Date") FROM public."ParkingLog" WHERE "CustomerId" = '{}' and "Status" = 'Parked';""".format(CustomerId))
            parking = {'now':cursor.fetchall()[0][0]}
            cursor.execute("""SELECT  COUNT("Date") FROM public."ParkingLog" WHERE "CustomerId" = '{}' and DATE("Date") = CURRENT_DATE;""".format(CustomerId))
            parking['today']=cursor.fetchall()[0][0]
            
        return  parking

class pricing_page_context:
    def compile(CustomerId=None):
        if CustomerId == None:
            CustomerId = 'EGPCI-AAA01-0001'
            return pricing_page_context.tarrifs(CustomerId)
        else:
            return pricing_page_context.tarrifs(CustomerId)

    def tarrifs(CustomerId):
        with conn.cursor() as cursor:
            cursor.execute("""SELECT "FromTime", "ToTime", "Cost"
                              FROM public."Tarrif"
                              where "CustomerId" = '{}';""".format(CustomerId))
            tarrifs = []
            for i in cursor.fetchall():            
                tarrif = {}
                tarrif['fromtime'] = i[0]
                tarrif['totime'] = i[1]
                tarrif['cost'] = i[2]
                tarrifs.append(tarrif)         
        return {'tarrifs' : tarrifs}




