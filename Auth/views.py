from Auth import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os
import psycopg2

try:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
except:
    conn = psycopg2.connect(database="d7pibsdo79jogi",host="ec2-52-86-25-51.compute-1.amazonaws.com",port=5432,user="cccbiffnldwfkf",password="605444bcd83d702da6e7f56cb2fba0ebb74fb3db14dc5a0c1555bbfa75a357a1")

# Create your views here.
class responses:
    def login_page(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username == 'admin':
                if password == 'admin123':
                    request.session['user_id'] = 'EGPCI-AAA01-0001'
                    request.session['is_auth'] = True

                    return redirect(responses.dashboard_page)
                else:
                    context={'msg':'Incorrect username or password!', 'code': 302 }
                    return render(request, 'Auth/login.html', context)
            
            else:
                context={'msg':'Incorrect username or password!', 'code': 302 }
                return render(request, 'Auth/login.html', context)
        else:
            return render(request, 'Auth/login.html')

    #@login_required(login_url="login.html?next=dashboard.html")
    def dashboard_page(request):
        if request.session.get('is_auth') == None or False:
            return redirect(responses.login_page) 

        else:
            context = models.dashboard_page_context.compile(request.session.get('user_id'))
            print(context)
                                            
            return render(request, 'Auth/dashboard.html', context)

    def history_page(request):
        context = dict
        with conn.cursor() as cursor:
            cursor.execute("""SELECT  "Date", "PlateNum", "EntryGateId", "CheckinTime", "CheckoutTime", "ExitGateId", "Status", "Duration", "Cash" FROM public."ParkingLog" WHERE "CustomerId" = '{0}';""".format(request.session.get('user_id')))
            
            ParkingLogs = []
            for i in cursor.fetchall():
                ParkingLog = {'date': i[0]}
                ParkingLog['platenum'] = i[1]
                ParkingLog['entrygate'] = i[2]
                ParkingLog['checkintime'] = i[3]
                ParkingLog['checkouttime'] = i[4]
                ParkingLog['exitgate'] = i[5]
                ParkingLog['status'] = i[6]
                ParkingLog['duration'] = i[7]
                ParkingLog['cash'] = i[8]
                
                ParkingLogs.append(ParkingLog) 
        context = {"ParkingLogs":ParkingLogs}
        return render(request, 'Auth/history.html',context)

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

    def parked_page(request):
        context = dict
        with conn.cursor() as cursor:
            cursor.execute("""SELECT  "Date", "PlateNum", "EntryGateId", "CheckinTime", "CheckoutTime", "ExitGateId", "Status", "Duration", "Cash"
                            FROM public."ParkingLog"
                            WHERE "CustomerId" = 'EGPCI-AAA01-0001' and "Status" = 'Parked';""")
            
            parkedcars = []
            for i in cursor.fetchall():
                parkedcar = {'entry_date': i[0]}
                parkedcar['platenum'] = i[1]
                parkedcar['entrygate'] = i[2]
                parkedcar['checkintime'] = i[3]
                parkedcar['checkouttime'] = i[4]
                parkedcar['exitgate'] = i[5]
                parkedcar['status'] = i[6]
                parkedcar['elapsed'] = i[7]
                parkedcar['cash'] = i[8]
                
                parkedcars.append(parkedcar) 
        context = {"parked_cars":parkedcars}

        return render(request, 'Auth/parked.html', context)

    def user_page(request):
        return render(request, 'Auth/user.html')