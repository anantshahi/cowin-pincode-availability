import requests
import datetime
import json

from requests import sessions

number_of_days = int(input("""
                           Enter number of days to get data for/
                           आने वाले दिनों की संख्या दर्ज करें जिसके लिए डेटा की आवश्यकता है
                           
                           """))
age = int(input("Enter your age / अपनी आयु दर्ज करें"))
pincode = int(input("Enter your pincode / अपने क्षेत्र का पिनकोड दर्ज करें "))
print_flag = "Y"



base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(number_of_days)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]

for INP_DATE in date_str:
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={0}&date={1}".format(pincode, INP_DATE)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
    response = requests.get(URL,headers=headers)
    #print(response)
    if response.ok:
        resp_json = response.json()
        # print(json.dumps(resp_json, indent = 1))
        flag = False
        #print(resp_json)
        if resp_json["sessions"]:
            print("Available on: {}".format(INP_DATE))
            if(print_flag=='y' or print_flag=='Y'):
                total_centers = resp_json.get('sessions')
                print("""Total available centres are : {0} \n कुल उपलब्ध केंद्र हैं {0}""".format(len(total_centers)))
                for center in total_centers:
                    if age>=center.get('min_age_limit'):
                        print("""
                              Available / उपलब्ध : {0}
                              Vaccine / टीका : {1}
                              Name/ नाम : {2}
                              Slots/ स्लॉट्स : {3}
                              Address/ पता : {4}
                              Block/ खंड : {5}
                              District/ जिला : {6}
                              State/ राज्य : {7}
                              Fee type/ शुल्क का प्रकार : {8}
                              Fees/ शुल्क : {9}
                              """.format(center.get('available_capacity'),
                                         center.get('vaccine'),
                                         center.get('name'),
                                         center.get('slots'),
                                         center.get('address'),
                                         center.get('block_name'),
                                         center.get('district_name'),
                                         center.get('state_name'),
                                         center.get('fee_type'),
                                         center.get('fee')
                                         ))
                    else:
                        print("No available slots on {}".format(INP_DATE))

