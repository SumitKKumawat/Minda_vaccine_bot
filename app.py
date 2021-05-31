import requests
import json
import time
import datetime
from requests import sessions


proxy = {
    "https": "https://14.140.131.82:3128",
    "http": "https://14.140.131.82:3128"}
#proxy = {
#    "https": "14.140.131.82:3128",
#    "http": "14.140.131.82:3128"}
#response=requests.get('https://httpbin.org/ip', proxies=proxy)

# faking chrome browser
browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def main():
    minda0=""
    minda1=""
    minda2=""
    minda3=""
    minda4=""
    nawa0=""
    nawa1=""
    nawa2=""
    nawa3=""
    nawa4=""
    devli0=""
    devli1=""
    devli2=""
    devli3=""
    devli4=""
    maroth0=""
    maroth1=""
    maroth2=""
    maroth3=""
    maroth4=""
    n_times=""

    while(1):
        tme0=datetime.date.today()

        if n_times=="" or n_times==0:
            n_times=0
            tme1=datetime.timedelta(days=n_times)
            n_times=1
        elif n_times==1:
            tme1=datetime.timedelta(days=n_times)
            n_times=2
        elif n_times==2:
            tme1=datetime.timedelta(days=n_times)
            n_times=3
        elif n_times==3:
            tme1=datetime.timedelta(days=n_times)
            n_times=4
        elif n_times==4:
            tme1=datetime.timedelta(days=n_times)
            n_times=0

        if datetime.datetime.now().hour==9 and datetime.datetime.now().minute==1 and datetime.datetime.now().second>1 and datetime.datetime.now().second<20:
            welcome="https://api.telegram.org/bot1825518407:AAGvVNzW1QgLmlJ8fRuSCl1yuM63q7PBgx0/sendMessage?chat_id=-1001288829686&text=Welcome, Developed by:- Sumit K Kumawat"
            requests.get(welcome,headers=browser_header,proxies=proxy)
        for i in range(532,533):
            i=str(i)
            #tme0=datetime.date.today()
            #tme1=datetime.timedelta(days=1)
            tmr=tme0+tme1
            tmr=tmr.strftime('%d-%m-%Y')
            x="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+i+"&date=" + tmr   #"29-05-2021" datetime.date.today().strftime('%d-%m-%Y')
            data=requests.get(x,headers=browser_header,proxies=proxy)
            #data=requests.get(x,headers=browser_header)
            results=json.loads(data.text)
            #print(x)
            #print("-----------------------------------------------")
            count=results["sessions"]
            #print(len(count))
            if len(count)>0:
                #print(len(count))
                for session in count:
                    #print(session)
                    msg=[]
                    msg.append({"district_name":session["district_name"],"centre_name":session["name"],"centre_address":session["address"],"vaccine":session["vaccine"],"fee":session["fee"],"availability":session["available_capacity"],"minage":session["min_age_limit"],"date":session["date"],"slots":session["slots"]})
                    #print(msg)
                    #time.sleep(1)
                    #if session["available_capacity"]!=0 and ("MINDA" in session["name"].upper() or "DEVLI KALLAN" in session["name"].upper() or "CHC NAWA" in session["name"].upper() or "MAROTH" in session["name"].upper()):
                    if "MINDA" in session["name"].upper() and ((minda0!=msg and n_times==1) or (minda1!=msg and n_times==2) or (minda2!=msg and n_times==3) or (minda3!=msg and n_times==4) or (minda4!=msg and n_times==0)):
                        #print("yes yes yes...........")
                        if n_times==1:
                            minda0=msg
                        elif n_times==2:
                            minda1=msg
                        elif n_times==3:
                            minda2=msg
                        elif n_times==4:
                            minda3=msg
                        elif n_times==0:
                            minda4=msg

                        parse_data=json.dumps(msg)
                        parse_data=parse_data.replace("{","")
                        parse_data=parse_data.replace("}","\n\n")
                        parse_data=parse_data.replace("[","")
                        parse_data=parse_data.replace("]","")
                        parse_data=parse_data.replace(",","\n")
                        nd_url="https://api.telegram.org/bot1825518407:AAGvVNzW1QgLmlJ8fRuSCl1yuM63q7PBgx0/sendMessage?chat_id=-1001288829686&text= "+parse_data
                        requests.get(nd_url)
                        print(requests.get(nd_url))
                        #print(parse_data)
                        parse_data=""
                        #time.sleep(10)

                    elif "DEVLI KALLAN" in session["name"].upper() and ((devli0!=msg and n_times==1) or (devli1!=msg and n_times==2) or (devli2!=msg and n_times==3) or (devli3!=msg and n_times==4) or (devli4!=msg and n_times==0)):
                        if n_times==1:
                            devli0=msg
                        elif n_times==2:
                            devli1=msg
                        elif n_times==3:
                            devli2=msg
                        elif n_times==4:
                            devli3=msg
                        elif n_times==0:
                            devli4=msg

                        parse_data=json.dumps(msg)
                        parse_data=parse_data.replace("{","")
                        parse_data=parse_data.replace("}","\n\n")
                        parse_data=parse_data.replace("[","")
                        parse_data=parse_data.replace("]","")
                        parse_data=parse_data.replace(",","\n")
                        nd_url="https://api.telegram.org/bot1825518407:AAGvVNzW1QgLmlJ8fRuSCl1yuM63q7PBgx0/sendMessage?chat_id=-1001288829686&text= "+parse_data
                        requests.get(nd_url)
                        print(requests.get(nd_url))
                        parse_data=""

                    elif "CHC NAWA" in session["name"].upper() and ((nawa0!=msg and n_times==1) or (nawa1!=msg and n_times==2) or (nawa2!=msg and n_times==3) or (nawa3!=msg and n_times==4) or (nawa4!=msg and n_times==0)):
                        if n_times==1:
                            nawa0=msg
                        elif n_times==2:
                            nawa1=msg
                        elif n_times==3:
                            nawa2=msg
                        elif n_times==4:
                            nawa3=msg
                        elif n_times==0:
                            nawa4=msg
                        parse_data=json.dumps(msg)
                        parse_data=parse_data.replace("{","")
                        parse_data=parse_data.replace("}","\n\n")
                        parse_data=parse_data.replace("[","")
                        parse_data=parse_data.replace("]","")
                        parse_data=parse_data.replace(",","\n")
                        nd_url="https://api.telegram.org/bot1825518407:AAGvVNzW1QgLmlJ8fRuSCl1yuM63q7PBgx0/sendMessage?chat_id=-1001288829686&text= "+parse_data
                        requests.get(nd_url)
                        print(requests.get(nd_url))
                        parse_data=""
                        #session["available_capacity"]!=0 and

                    elif "MAROTH" in session["name"].upper() and ((maroth0!=msg and n_times==1) or (maroth1!=msg and n_times==2) or (maroth2!=msg and n_times==3) or (maroth3!=msg and n_times==4) or (maroth4!=msg and n_times==0)):
                        if n_times==1:
                            maroth0=msg
                        elif n_times==2:
                            maroth1=msg
                        elif n_times==3:
                            maroth2=msg
                        elif n_times==4:
                            maroth3=msg
                        elif n_times==0:
                            maroth4=msg
                        parse_data=json.dumps(msg)
                        parse_data=parse_data.replace("{","")
                        parse_data=parse_data.replace("}","\n\n")
                        parse_data=parse_data.replace("[","")
                        parse_data=parse_data.replace("]","")
                        parse_data=parse_data.replace(",","\n")
                        nd_url="https://api.telegram.org/bot1825518407:AAGvVNzW1QgLmlJ8fRuSCl1yuM63q7PBgx0/sendMessage?chat_id=-1001288829686&text= "+parse_data
                        requests.get(nd_url)
                        print(requests.get(nd_url))
                        parse_data=""

        #time.sleep(4)


if __name__ == '__main__':
    #app.run()
    main()

