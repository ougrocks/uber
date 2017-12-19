import requests, json, random, string


def create_account():
    try:
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']
        mobile = gen_mobile()
        email = gen_email()

        url = "https://www.uber.com/a/driver-signup"

        payload = "{\"first_name\":\"Shubham\",\"last_name\":\"rDx\",\"email\":\""+email+"\",\"contactinfo\":\""+mobile+"\",\"password\":\"qwerty123\",\"lat\":\""+lat+"\",\"lng\":\""+lon+"\",\"location\":\"Delhi%2C%20India\",\"place_id\":\"ChIJL_P_CXMEDTkRw0ZdG-0GVvw\",\"is_commercial_partner\":\"true\",\"referral_code\":\"\",\"custom_user_tag\":\"chameleon_default_us_p2p\",\"flow_type\":\"P2P\",\"route\":\"chameleon\",\"use_psh\":true}"
        headers = {
            'accept': "application/json",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.8",
            'connection': "keep-alive",
            'content-length': "391",
            'content-type': "application/json",
            'cookie': "AMCVS_0FEC8C3E55DB4B027F000101%40AdobeOrg=1; AMCV_0FEC8C3E55DB4B027F000101%40AdobeOrg=1611084164%7CMCMID%7C22079644526839507944490216434145012732%7CMCAAMLH-1509381640%7C3%7CMCAAMB-1509381640%7C1OLQZwRir6sHx7pCvMB4jIyafHpR2MN12BblrTDgc1yf7xY%7CMCOPTOUT-1508784040s%7CNONE; __LOCALE__=en; _LOCALE_=en; ambassador:sess=vSUQt_Nn72J-2JrpKTe10A.29JVWLbqVt__JyU68qJkD96JP1L5-M44FIdxGzsvrdpYmiVnF2sEDSwQXV0yML7yfTzcZfwnA1da2FOgQHeS27tv3-U11oBUdVLitIkbtQ_mfZ1A5dmLTHprovHEnFFieDKilcI5tSNu-7luwS829h6g8PDc5izaU2hRR2kHPqPTm8SVfosbNfOEbo3hJnU0kD_nXCqSSWaQabcDNNWazRT8-JMQvQJhI7wShEgM1S-vSs6Jf0-MwIX9yXAW91Rl.1508777837086.1209600000.QtENdI0chX-FhNHDo2LkF4SYNHmHFh12zMUtC-53OBQ; optimizelyEndUserId=oeu1508777838834r0.8936791423432253; utag_utm_exp=70801c; utag_geo_code=IN; utag_main=v_id:015f4a1b8676001c214f6dcc9f6d04079001507100ac2$_sn:1$_ss:0$_st:1508779639279$ses_id:1508776838777%3Bexp-session$_pn:2%3Bexp-session$segment:b$optimizely_segment:b$convertingpage:%3Bexp-session; _ga=GA1.2.1486499781.1508776840; _gid=GA1.2.1493112642.1508776840; aam_uuid=21674246371360949334530633111369828323; _ceg.s=oyacfp; _ceg.u=oyacfp; _gat_tealium_0=1; NaN_hash=ab2e5c35SUZLNSKO1508056161484; marketing_vistor_id=c8685d35-3268-4d4a-a5a8-ad30adb525b2; uber-com:sess=UGJYU3SbJwdlGWRq79ZWng.aR3Z7dNqRu2DDboBLH1oyWjYyVIJi4Yaudnzb28r-Hb3FsLYgmTIPJ8xxypcFsz4PLZ1ONOMbDW4BTy-Vq8FBC5RREIRSFmZ7tZ29JAxP2LObp7R3IC-TVPguDiKoZOa1JyjSmdqooveuQMwh0sbUODf6Xo-wlN6G687cqs28HduM1oPe8hBf0xwJz9_PKZS.1508777875548.1209600000.m2nnpltnyuhgolissSe4i4oIItXHuC3bqNwzOUDtXZM; _ua=%7B%22id%22%3A%2200ae41e2-f1c8-48c4-8887-eb41e19954f0%22%2C%22ts%22%3A1508777838705%7D; AMCVS_0FEC8C3E55DB4B027F000101%40AdobeOrg=1; _ceg.s=oyacfp; _ceg.u=oyacfp; uber-com:sess=UGJYU3SbJwdlGWRq79ZWng.aR3Z7dNqRu2DDboBLH1oyWjYyVIJi4Yaudnzb28r-Hb3FsLYgmTIPJ8xxypcFsz4PLZ1ONOMbDW4BTy-Vq8FBC5RREIRSFmZ7tZ29JAxP2LObp7R3IC-TVPguDiKoZOa1JyjSmdqooveuQMwh0sbUODf6Xo-wlN6G687cqs28HduM1oPe8hBf0xwJz9_PKZS.1508777875548.1209600000.m2nnpltnyuhgolissSe4i4oIItXHuC3bqNwzOUDtXZM; sid=QA.CAESEMmvpptkgk7Ev075lQzeTqAYl42T0wUiATEqJDM5OTQ5ZWZjLWMxODktNDgxNi1iNWIxLWQxZTJiNDdmZjFiYjI8yj8wkhMzJkapgcyWK1FAMoaeZveJOj_wXrRJmgT3eOP5rcmbopT4LQDfrglyYTZzn11slG4sHKVl-e8oOgExQgh1YmVyLmNvbQ.__-xAVoIR7xKygR7bks451HWqccPwjZ2gFMZZBI_xTU; _hp2_id.2741060973=%7B%22userId%22%3A%220910869600167222%22%2C%22pageviewId%22%3A%220097953931353071%22%2C%22sessionId%22%3A%225751430596500576%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%223.0%22%7D; su=1; __zlcmid=j8gqHrOIce4n07; ambassador:sess=l5jBzMERtZZnMGw4CLLpXg.YEvRqayqsgRjuSJig7pxKRig07tHp49Pn-pU9_uR6hxXuim7BYv5UVDGZETsIkLGedJ2W2jvvhvBmVtfsIJVuiA5IzzRNh_n9Nzqr_iZm6KV-P227yt40SRXwUTHsyMybttCwsNqc7MPL6d8pJ9S_iYwErFZtx-4RJxG2XH8IRS-GLZttymmvQHJ5oXWtue0MGELVZtAzXNqSRom4-9ImAagTtZzjCCmIXixibYsDQ9zkxXWhAvLCXxwkw4qGdDbPMebK2w1__lLGhzh8-mEbd0lbi-Hd4kxvQx18sUWPOGgIJJAgLhC11_ONbgsolP2.1508777837086.1209600000.t5jVjOgEUHgVAROhzFlp7l53bpDIY_AUZzBoaBUdY2M; utag_utm_exp=70801c; __LOCALE__=en; _LOCALE_=en; AMCV_0FEC8C3E55DB4B027F000101%40AdobeOrg=1611084164%7CMCMID%7C22079644526839507944490216434145012732%7CMCAAMLH-1509381640%7C3%7CMCAAMB-1509551012%7C-ySfS9UHgGt65n1RVYzn7B13KrK_fGO7LH4k1W0uP4c1V4M%7CMCOPTOUT-1508953412s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C474876093; marketing_vistor_id=c8685d35-3268-4d4a-a5a8-ad30adb525b2; dot-chameleon:sess=MvPAjpGjrTVAwoObbACD-g.O3zDRLVcweLg50ualsBkNp0FLiMZ1TRWn42b6SqTn2Ct7SJ9TPgXZaEyzr7hBj98h_ek23_6pdy5CmgXSKeDaL8p-ebNdqOaA-ntVKpUAL9FIDcafqgNz88_lnda-23LDuXlZiE7Ev17W_2CjnDAOmt0bwg4BajUAb5pTlrEg-OgwL75JMCg-LFaJ4CjAU0czZwD6DuWWe81WGpkGChwLg.1508946237949.1209600000.XoGi7gPm8PFKlwO3RBbDBy_WxTnXEeO1BiZTV-Od8zw; optimizelyEndUserId=oeu1508777838834r0.8936791423432253; utag_geo_code=IN; _ga=GA1.2.1486499781.1508776840; _gid=GA1.2.1493112642.1508776840; NaN_hash=ab2e5c35SUZLNSKO1508056161484; _gat_tealium_0=1; aam_uuid=21674246371360949334530633111369828323; utag_main=v_id:015f4a1b8676001c214f6dcc9f6d04079001507100ac2$_sn:2$_ss:0$_st:1508948080735$segment:b$optimizely_segment:b$userid:39949efc-c189-4816-b5b1-d1e2b47ff1bb$city:197%3Bexp-1511197087727$ses_id:1508946200706%3Bexp-session$_pn:3%3Bexp-session$convertingpage:%3Bexp-session",
            'host': "www.uber.com",
            'origin': "https://www.uber.com",
            'referer': "https://www.uber.com/signup/drive/us/",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            'x-csrf-token': "1508946289-01-8PRXM_eAS6GAgQY7WKrN6ebwg2CrmLDMZY0yNJoax9E",
            'cache-control': "no-cache",
            'postman-token': "0d975589-90a7-e620-4084-ae9e9635d4e5"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

        file = open('accNew.txt', 'a+')
        file.write(email + "|" + mobile + "|qwerty123 \n")
        file.close()
    except:
        pass


def gen_mobile():
    first_5 = random.randrange(80000, 99999)
    last_5 = random.randrange(10000, 99999)
    return str(first_5) + str(last_5)


def gen_email():
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    return random_string + "@gmail.com"


while (1):
    
    create_account()
