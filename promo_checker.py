import requests

promo_code = str(input('Enter Promo code: '))
url = "https://cn-sjc1.uber.com/rt/users/apply-clients-promotions"

payload = "{\"code\":\""+promo_code+"\",\"confirmed\":false}"
headers = {
    'x-uber-client-id': "com.ubercab",
    'x-uber-client-name': "client",
    'x-uber-client-version': "3.96.0",
    'x-uber-device': "android",
    'x-uber-device-epoch': "1470916054617",
    'x-uber-device-id': "3eab5e19418172765a6dbe432b57ba8c",
    'x-uber-device-ids': "3eab5e19418172765a6dbe432b57ba8cdeviceImei:143007881887744,",
    'x-uber-device-language': "en_GB",
    'x-uber-device-model': "SM-G360H",
    'x-uber-device-mobile-iso2': "in",
    'x-uber-device-os': "4.4.4",
    'x-uber-device-serial': "RZ1G31GMEEV",
    'x-uber-token': "63f33b0c50a2c250972ccf3a21fc7208",
    'x-uber-protocol-version': "0.73.0",
    'X-Uber-RedirectCount': "0",
    'X-Uber-DCURL': "https://cn-sjc1.uber.com/",
    'Content-Type': "application/json; charset=UTF-8",
    'Content-Length': "39",
    'Host': "cn-sjc1.uber.com",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'User-Agent': "okhttp/12.7.2",
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)