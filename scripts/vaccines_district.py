import requests
import json
import time
import smtplib, ssl
import datetime

port = 465  # For SSL
from_email='from_email' 
password='App password' # need to create from https://myaccount.google.com/apppasswords
toemail='receipeint email' # to notify the open slot
context = ssl.create_default_context()

def mailnow(email,sub):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(from_email, password) 
        message = 'Subject: {}\n\n{}'.format(sub, 'Please book your slot')
        server.sendmail(from_email, email, message)
#Date format
today_date = datetime.date.today()
new_today_date = today_date.strftime("%d-%m-%Y")

while True:
    pincodes=['1'] #change pincode for your area
    for pincode in pincodes:
        print('Vaccination availability checking for ',pincode)
        url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={}&date={}'.format(294,new_today_date) #294 is for Bangalore city
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
        
                    message='Vaccines available for 18+ age in {} center:{} capacity:{}'.format(pincode,center['name'],str(each['available_capacity']))
                    print(message)
                    mailnow(toemail,message)
                elif((age==45) and (capacity> 0)):
                    #if required you can enable 45+ age slot notification also
                    message='Vaccines available for 45+ age in {} center:{} capacity:{}'.format(pincode,center['name'],str(each['available_capacity']))
                    print(message)
                    # mailnow('dharmakrish6@gmail.com',message)
                else:
                    pass
    time.sleep(60) # Run every one minutes. You can change if you want 


                
            
    
    