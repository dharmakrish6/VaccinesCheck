import requests
import json
import time
import datetime


#telegram bot details
botToken='<Bot_token>'
chat_id='@delhi_vaccine'

def notifyTelegram(message):
    url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(botToken,chat_id,message)
    response = requests.request("GET", url)
    print(response)
     
#Date format
today_date = datetime.date.today()
new_today_date = today_date.strftime("%d-%m-%Y")

while True:
    try:
        pincodes=['141','142','143','144','145','146','147','148','149','150'] #change pincode for your area
        for pincode in pincodes:
            print('Vaccination availability checking for ',pincode)
            url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={}&date={}'.format(pincode,new_today_date) #294 is for Bangalore city
            headers = {
            'User-Agent': 'PostmanRuntime/7.26.8'
            }

            response = requests.request("GET", url, headers=headers)
            # print(response)
            res = response.json()
            # print(res)
            allcenter=res['centers']
            for center in allcenter:
                session_c=center['sessions']
                print('******************checking******************')
                session_len=len(session_c)
                for each in session_c:
                    capacity=int(each['available_capacity'])
                    age=int(each['min_age_limit'])

                    if ((age==18) and (capacity> 0)):
            
                        message='Vaccination centers for 18+ age {} \ncenter:{} \navailable on:{} \navailble slot:{}'.format(center['pincode'],center['name'],each['date'],str(each['available_capacity']))
                        # print(message)
                        notifyTelegram(message)
                    elif((age==45) and (capacity> 0)):
                        #if required you can enable 45+ age slot notification also
                        message='Vaccines available for 45+ age {} \ncenter:{} \navailable on:{} \navailble slot:{}'.format(center['pincode'],center['name'],each['date'],str(each['available_capacity']))
                        # print(message)
                        # notifyTelegram(message)

                    else:
                        pass
    except:
        pass                
    print('Watinging for next round')
    time.sleep(600) # Run every one minutes. You can change if you want 


                
            
    
    