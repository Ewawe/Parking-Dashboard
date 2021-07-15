from django.shortcuts import render
import os
import psycopg2

try:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
except:
    conn = psycopg2.connect(database="d7pibsdo79jogi",host="ec2-52-86-25-51.compute-1.amazonaws.com",port=5432,user="cccbiffnldwfkf",password="605444bcd83d702da6e7f56cb2fba0ebb74fb3db14dc5a0c1555bbfa75a357a1")


# Create your views here.
def login_page(request):
    return render(request, 'Auth/index.html')

def dashboard_page(request):
    context = dict
    with conn.cursor() as cursor:
        cursor.execute("""SELECT  "Date", "PlateNum", "EntryGateId", "CheckinTime", "CheckoutTime", "ExitGateId", "Status", "Duration", "Cash"
                          FROM public."ParkingLog"
                          WHERE "CustomerId" = 'EGPCI-AAA01-0001';""")
                          
    return render(request, 'Auth/dashboard.html')

def all_vehicle_page(request):
    context = dict
    with conn.cursor() as cursor:
        cursor.execute("""SELECT  "Date", "PlateNum", "EntryGateId", "CheckinTime", "CheckoutTime", "ExitGateId", "Status", "Duration", "Cash"
                          FROM public."ParkingLog"
                          WHERE "CustomerId" = 'EGPCI-AAA01-0001';""")
        
        ParkingLogs = list
        for i in cursor.fetchall():
            ParkingLog = {"Date": i[0]}
            ParkingLog['platenum'] = i[1]
            ParkingLog['entrygate'] = i[2]
            ParkingLog['checkintime'] = i[3]
            ParkingLog['checkouttime'] = i[4]
            ParkingLog['exitgate'] = i[5]
            ParkingLog['status'] = i[6]
            ParkingLog['duration'] = i[7]
            ParkingLog['cash'] = i[8]
            
            ParkingLogs.append(ParkingLog)  
    context = {"ParkingLogs":[ParkingLogs]}         
    return render(request, 'Auth/all_vehicle.html', context)

def pricing_page(request):
    context = dict
    with conn.cursor() as cursor:
        cursor.execute("""SELECT "FromTime", "ToTime", "Cost"
                            FROM public."Tarrif"
                            where "CustomerId" = 'EGPCI-AAA01-0001';""")
        tarrifs = []
        for i in cursor.fetchall():            
            tarrif = {}
            #tarrif['Id'] = i
            tarrif['fromtime'] = i[0]
            tarrif['totime'] = i[1]
            tarrif['cost'] = i[2]
            tarrifs.append(tarrif)         
    context = {'tarrifs' : tarrifs} 
    return render(request, 'Auth/pricing.html', context)

def today_page(request):
    return render(request, 'Auth/today.html')

def user_page(request):
    return render(request, 'Auth/user.html')