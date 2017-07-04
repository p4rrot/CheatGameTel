#encoding:utf-8
#Supports just Gamee and Gamebot games
import requests
import re
import string
from selenium import webdriver
from time import sleep

class jobs(object):
    def __init__(self):
        pass
    def get(self,links):
        if links[0:7]=='https://':
            return links
        else :
            return 'https://'+links
    def create_payload(self,links):
        return re.split('['+string.punctuation+']',links.split('#')[1])[0]
    def Inject_js(self,links,payload):
        print "[*] wait please ..."
        links=links[8:]
        print links
        d = webdriver.Chrome()
        sleep(4)
        d.get(links)
        d.execute_script(payload)
        print "[*] Done successful . enjoy ."
        raw_input("[!] ENTER to exit")
        exit(0)
print "**************************************"
print "*** Coded by PARR0T _ parsa timury ***"
print "*** SUPPORTS JUST GAMEE AND GAMEBOT***"
print "**************************************"
print "*** Give me Your Gaming link       ***"
Link = raw_input("[*] link : ")
print "*** What is your favorite score ?  ***"
score = raw_input("[*] score : ")
start = jobs()
link = start.get(Link)
if 'tbot.xyz' in link:
    payload = start.create_payload(link)
    try:
        r = requests.post('https://tbot.xyz/api/setScore','data='+payload+'%3D%3D&score='+score)
        if r.status_code==200:
            print "[*] Done successful . enjoy ."
            raw_input("[!] ENTER to exit ...")
        else :
            print "[!] Failed ."
            raw_input("[!] ENTER to exit ...")
    except:
        print "[!] Failed ."
        raw_input("[!] ENTER to exit ...")
elif 'gameeapp.com' in link:
    payload = 'var a = window.location.pathname,n = (new Date).getTime(),t = $("#dataId").data(),s = CryptoJS.AES.encrypt(JSON.stringify({score: %s,timestamp: n}), t.id, {format: CryptoJSAesJson}).toString(),r = {score: %s,url: a,play_time: gameeUI.playTime,hash: s};if (isFacebook()) {var i = FacebookUserData.getUserData();r.app_scoped_user_id = i.app_scoped_user_id, r.user_id = i.user_id}gameeUI.sendScoreData(r)'%(score,score)
    try:
        start.Inject_js(link,payload)
    except:
        print "[!] Failed ."
        raw_input("[!] ENTER to exit ...")
else :
    print "[!] This game is not able to be hacked ."
    raw_input("[!] ENTER to exit ...")
