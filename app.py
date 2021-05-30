import requests
import json
import time
import datetime
from requests import sessions


#proxy = {
#    "https": "https://14.140.131.82:3128",
#    "http": "https://14.140.131.82:3128"}
proxy = {
    "https": "14.140.131.82:3128",
    "http": "14.140.131.82:3128"}
#response=requests.get('https://httpbin.org/ip', proxies=proxy)

# faking chrome browser
browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def main():
    while(1):
        #if datetime.datetime.now().hour==9 and datetime.datetime.now().minute==1 and datetime.datetime.now().second>1 and datetime.datetime.now().second<5:
        welcome="https://api.telegram.org/bot1825518407:AAGvVNzW1QgLmlJ8fRuSCl1yuM63q7PBgx0/sendMessage?chat_id=-1001288829686&text=Welcome, Developed by:- Sumit K Kumawat"
        requests.get(welcome)
        for i in range(532,533):
            i=str(i)
            x="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+i+"&date=" + datetime.date.today().strftime('%d-%m-%Y')   #"29-05-2021" datetime.date.today().strftime('%d-%m-%Y')
            data=requests.get(x,headers=browser_header,proxies=proxy)
            results=json.loads(data.text)
            print(x)
            #print(results)
            print("-----------------------------------------------")
            count=results["sessions"]
            #count=results
            if len(count)>0:
                for session in count:
                    msg=[]
                    msg.append({"district_name":session["district_name"],"centre_name":session["name"],"centre_address":session["address"],"vaccine":session["vaccine"],"fee":session["fee"],"availability":session["available_capacity"],"minage":session["min_age_limit"],"date":session["date"],"slots":session["slots"]})
                    if session["available_capacity"]!=0:
                        parse_data=json.dumps(msg)
                        parse_data=parse_data.replace("{","")
                        parse_data=parse_data.replace("}","\n\n")
                        parse_data=parse_data.replace("[","")
                        parse_data=parse_data.replace("]","")
                        parse_data=parse_data.replace(",","\n")
                        nd_url="https://api.telegram.org/bot1825518407:AAGvVNzW1QgLmlJ8fRuSCl1yuM63q7PBgx0/sendMessage?chat_id=-1001288829686&text= "+parse_data
                        requests.get(nd_url)
                        parse_data=""
                        #y=requests.get(nd_url)
                        #time.sleep(50)
        #time.sleep(4)


if __name__ == '__main__':
    #app.run()
    main()

