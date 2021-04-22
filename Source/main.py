import requests
import time
r = requests.session()
print("""
    ████████▀▀▀████
    ████████────▀██
    ████████──█▄──█
    ███▀▀▀██──█████
    █▀──▄▄██──█████
    █──█████──█████
    █▄──▀▀▀──▄█████
    ███▄▄▄▄▄███████
    
    Tiktok linked Emails
    
    @givt_ops | @680068
""")
def check():
    try:
        file = open("emails.txt", "r")
        for email in file:
            time.sleep(5)
            url = 'https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/?residence=AE&device_id=6923575826752275974&os_version=14.3&app_id=1233&iid=6951746276598204161&app_name=musical_ly&pass-route=1&vendor_id=EF3C1478-2AFC-4B8E-8030-C608120AECF9&locale=ar&pass-region=1&ac=WIFI&sys_region=US&ssmix=a&version_code=17.2.0&vid=EF3C1478-2AFC-4B8E-8030-C608120AECF9&channel=App%20Store&op_region=AE&os_api=18&idfa=00000000-0000-0000-0000-000000000000&install_id=6951746276598204161&idfv=EF3C1478-2AFC-4B8E-8030-C608120AECF9&device_platform=iphone&device_type=iPhone9%2C4&openudid=3ce553bec09070081e5a698d3a14a988f3642ac4&account_region=&tz_name=Asia%2FDubai&tz_offset=14400&app_language=ar&carrier_region=AE&current_region=AE&aid=1233&mcc_mnc=42402&screen_width=1242&uoo=1&content_language=&language=ar&cdid=FBF67CFE-39E1-4556-A3EB-624A20A434E1&build_number=172025&app_version=17.2.0&resolution=1242%2A2208'
            headers = {
                'Host': 'api16-normal-c-alisg.tiktokv.com',
                'Connection': 'close',
                'Content-Length': '76',
                'Cookie': f'sessionid=b0b2ed352b9394eefc29754dfe80926c',
                'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0',
                'Content-Type': 'application/x-www-form-urlencoded',
                'x-tt-passport-csrf-token': 'b0b2ed352b9394eefc29754dfe80926c',
                'sdk-version': '2',
                'passport-sdk-version': '5.12.1'
            }
            data = {
                'account_sdk_source': 'app',
                'email': email,
                'mix_mode': '1',
                'type': '31'
            }
            r1 = r.post(url, data=data, headers=headers).text
            if '"message":"success"' in r1:
                print(f"[+] Linked :{email}")
                with open("Checked_Email.txt", "a") as x:
                    x.write(f"{email}\n")
            elif '"description":"غير مسجل بعد"' in r1:
                print(f"[-] Not Linked : {email}")
            else:
                print(f"[-] Not Linked : {email}")
                time.sleep(10)
    except:
        print("[X] File emails.txt Not Found")
        input()
        exit()
check()
