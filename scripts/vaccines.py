import requests
import json
import time
import smtplib, ssl

port = 465  # For SSL

context = ssl.create_default_context()
def mailnow(email,sub):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("makemeappz@gmail.com", 'jvzxuiqhbfozbykf')
        message = 'Subject: {}\n\n{}'.format(sub, 'Please book')
        server.sendmail('dharma@gmail.com', email, message)


while True:
    pincodes=['560076','560011','560078','560060']
    for pincode in pincodes:
        print('Vaccination availability checking for ',pincode)
        url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode='+pincode+'&date=08-05-2021'
        headers = {
        'User-Agent': 'PostmanRuntime/7.26.8'
        }

        response = requests.request("GET", url, headers=headers)
        print(response)
        res = response.json()
        print(res)
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
                    mailnow('suma.s16@gmail.com',message)
                elif((age==45) and (capacity> 0)):
                    
                    message='Vaccines available for 45+ age in {} center:{} capacity:{}'.format(pincode,center['name'],str(each['available_capacity']))
                    print(message)
                    # mailnow('dharmakrish6@gmail.com',message)
                else:
                    pass
    time.sleep(10)


                
            
    
    