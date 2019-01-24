# -*- coding: utf-8 -*- 
from Jhoda.linepy import *
from Jhoda.akad.ttypes import Message
from Jhoda.akad.ttypes import ContentType as Type
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
#from gtts import gTTS
from googletrans import Translator
#=======================================================================================#
botStart = time.time()
#============================Akun Utama==================================================#
cl = LINE("EAvPgrO7deMZJS8JbVLd.n4NBqtezXHi1HkIErwUrhq.9NOAEoF0cGAH0C8j47WMpzX6Jw97DyMLpH4iiB1O2Y0=")
#===============Asist 1===============================================================#
#ki = LINE("EAdUKTPbJcXspTNFOksf.HO+eqcEYrT3bNWVA9J6VpW.MAgqL9Q8op1RdGGUij7/KKsoiOCymxadFzyupRytu+I=")
#===============Asist2===============================================================================#
#kk = LINE("EAmtaSqQxK8oAgdXIehc.RahvNIqVRtGSn/XH6Yonha./8/UoIzEGB5gXNcZiuxKRvMlUiJ0cO5vnI3Y40x1Y2c=")
#===============Asist3===============================================================================#
#kc = LINE("EAaGZgSUu8WyZQ8AUSR2.6zBt+mj7YEQB0R0CxE428G.I2zHEgfebl9fxS0tE3NgmIzQyrcudKzgz6NQkbdKmVY=")
#===============Anti js===============================================================================#
#km = LINE("EAVJhgAhzOVsj31IgDr0.v8o1zdFWUdN41eQgmcOQGa.Dfpqc0EpYcgNTTNgGBijKVe092+acJgBn9uExbjhMzk=")
#===============Anti js===============================================================================#
#kb = LINE("EAM2KSaiU6ALd68SuxU5.OkroYZmkaO9crfq8Y830bq.Un4JkmNhAKzvmPqAjBvQCBlOgqRlQxVFir3e6JCHjf0=")
#===============Anti js===============================================================================#
#sw = LINE("EAguYDGsaupGlNoGgaq1.l0Lfx6ZsNdD+RgK9+srNGq.iW88daIycbDCtnmc8okQ6JfMts6o1LjGdHXKqkPyId8=")
#========================================================================================#
print ("==========[ Jhoda Login sukses ]===========")
#========================================================================================#
poll = OEPoll(cl)
call = (cl)
baraya = ["u3789db413119c6123584a89e456b911d","ue1256f092267ec054bb4a5d62d2eedfe"]
creator = ["u3789db413119c6123584a89e456b911d","ue1256f092267ec054bb4a5d62d2eedfe"]
owner = ["u3789db413119c6123584a89e456b911d","ue1256f092267ec054bb4a5d62d2eedfe"]
admin = ["u3789db413119c6123584a89e456b911d","ue1256f092267ec054bb4a5d62d2eedfe"]
staff = ["u3789db413119c6123584a89e456b911d","ue1256f092267ec054bb4a5d62d2eedfe"]
mid = cl.getProfile().mid
#Amid = ki.getProfile().mid
#Bmid = kk.getProfile().mid
#Cmid = kc.getProfile().mid
#Dmid = km.getProfile().mid
#Emid = kb.getProfile().mid
#Zmid = sw.getProfile().mid
#KAC = [cl,ki,kk,kc,km,kb,sw]
#ABC = [ki,kk,kc,km,kb,sw]
#BIMA = [sw1,sw2]
Bots = [mid]
Bima = [mid]
Saints = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
welcome = []

responsename1 = cl.getProfile().displayName
#responsename2 = ki.getProfile().displayName
#responsename3 = kk.getProfile().displayName
#responsename4 = kc.getProfile().displayName
#responsename5 = km.getProfile().displayName
#responsename6 = kb.getProfile().displayName
#responsename5 = sw.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "baraya":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "mention":"NGINTIPPP!!!",
    "Respontag":"Nah, ngetag mele ntar beper ngak ada yang tanggung jawab.. jangan sampek puskun ya beb,,,,,!!!",
    "welcome":"Selamat datang & betah",
    "comment":"Like like & like by 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ ",
    "message":"T̸͟͞e̸͟͞r̸͟͞i̸͟͞m̸͟͞a̸͟͞ k̸͟͞a̸͟͞s̸͟͞i̸͟͞h̸͟͞ t̸͟͞e̸͟͞l̸͟͞a̸͟͞h̸͟͞ a̸͟͞d̸͟͞d̸͟͞   😃\n☆| 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴☆\n\nOpen Tikungan:\n┃🇮🇩┃ 1 hari 1000c\n┃🇮🇩┃ 1 minggu 2 juta 😁\n\nMinat?\nChat aja...\nhttps://line.me/ti/p/Dr8B9wDicC",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = " ●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━━╮\n	BIMA MENTIONS「{}」\n╰━━━━━━━━━━━━━━━╯\n ●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n╠☬➣[Ngopi Cuy ]\n".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠☬➣"
                num=(num+1)
            else:
                try:
                    textx += "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    textx += "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\nAssalamualaikum ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "╠☬➣"
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIdsx()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"┃🇮🇩┃ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n┃🇮🇩┃ Group : "+str(len(gid))+"\n┃🇮🇩┃ Teman : "+str(len(teman))+"\n┃🇮🇩┃ Expired : In "+hari+"\n┃🇮🇩┃ Version : 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \n┃🇮🇩┃ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃🇮🇩┃ Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = " ●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		エリートゲンベル v777@212\n╰━━━━━━━━━━━━━━╯\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃ MEDIA ┃\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n" + \
                  "╠🛑➣ " + key + "Help2\n" + \
                  "╠🛑➣ " + key + "Help3\n" + \
                  "╠🛑➣ " + key + "Help4\n" + \
                  "╠🔘➣ " + key + "Me\n" + \
                  "╠🔘➣ " + key + "Mid「@」\n" + \
                  "╠🔘➣ " + key + "Info「@」\n" + \
                  "╠🔘➣ " + key + "Nk「@」\n" + \
                  "╠🔘➣ " + key + "Kick1「@」\n" + \
                  "╠🔘➣ " + key + "Contact bot\n" + \
                  "╠🔘➣ " + key + "Status\n" + \
                  "╠🔘➣ " + key + "About\n" + \
                  "╠🔘➣ " + key + "Restart\n" + \
                  "╠🔘➣ " + key + "Runtime\n" + \
                  "╠🔘➣ " + key + "Speed/Sp\n" + \
                  "╠🔘➣ " + key + "Sprespon\n" + \
                  "╠🔘➣ " + key + "Tagall\n" + \
                  "╠🔘➣ " + key + "Joinall\n" + \
                  "╠🔘➣ " + key + "Byeall\n" + \
                  "╠🔘➣ " + key + "Byeme\n" + \
                  "╠🔘➣ " + key + "Leave「Namagrup」\n" + \
                  "╠🔘➣ " + key + "Ginfo\n" + \
                  "╠🔘➣ " + key + "Open\n" + \
                  "╠🔘➣ " + key + "Close\n" + \
                  "╠🔘➣ " + key + "Url grup\n" + \
                  "╠🔘➣ " + key + "Gruplist\n" + \
                  "╠🔘➣ " + key + "Infogrup「angka」\n" + \
                  "╠🔘➣ " + key + "Infomem「angka」\n" + \
                  "╠🔘➣ " + key + "Hapus chat\n" + \
                  "╠🔘➣ " + key + "Lurking「on/off」\n" + \
                  "╠🔘➣ " + key + "Lurkers\n" + \
                  "╠🔘➣ " + key + "Sider「on/off」\n" + \
                  "╠🔘➣ " + key + "Updatefoto\n" + \
                  "╠🔘➣ " + key + "Broadcast:「Text」\n" + \
                  "╠🔘➣ " + key + "Setkey「New Key」\n" + \
                  "╠🔘➣ " + key + "Mykey\n" + \
                  "╠🔘➣ " + key + "Resetkey\n" + \
                  " ●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\nhttp://line.me/ti/p/qEaRIT2R3N\n"
    return helpMessage

def helpmedia():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		エリートゲンベル v777@212\n╰━━━━━━━━━━━━━━╯\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃ MEDIA ┃\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n" + \
                  "╠🔘➣ " + key + "ID line:「Id Line nya」\n" + \
                  "╠🔘➣ " + key + "Sholat:「Nama Kota」\n" + \
                  "╠🔘➣ " + key + "Cuaca:「Nama Kota」\n" + \
                  "╠🔘➣ " + key + "profilesmule:「ID Smule」\n" + \
                  "╠🔘➣ " + key + "Lokasi:「Nama Kota」\n" + \
                  "╠🔘➣ " + key + "Music:「Judul Lagu」\n" + \
                  "╠🔘➣ " + key + "Lirik:「Judul Lagu」\n" + \
                  "╠🔘➣ " + key + "Ytmp3:「Judul Lagu」\n" + \
                  "╠🔘➣ " + key + "Ytmp4:「Judul Video」\n" + \
                  "╠🔘➣ " + key + "Profileig:「Nama IG」\n" + \
                  "╠🔘➣ " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "╠🔘➣ " + key + "Jumlah:「angka」\n" + \
                  "╠🔘➣ " + key + "Spamtag「@」\n" + \
                  "╠🔘➣ " + key + "Spamcall:「jumlahnya」\n" + \
                  "╠🔘➣ " + key + "Spamcall\n" + \
                  "●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\nhttp://line.me/ti/p/qEaRIT2R3N\n"
    return helpMessage1                
                  
def helpsetting():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		エリートゲンベル v777@212\n╰━━━━━━━━━━━━━━╯\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃ MEDIA ┃\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n" + \
                  "╠🛑➣ " + key + "Protecturl「on/off」\n" + \
                  "╠🛑➣ " + key + "Protectjoin「on/off」\n" + \
                  "╠🛑➣ " + key + "Protectkick「on/off」\n" + \
                  "╠🛑➣ " + key + "Protectcancel「on/off」\n" + \
                  "╠🛑➣ " + key + "Protectinvite「on/off」\n" + \
                  "╠🛑➣ " + key + "Antijs「on/off」\n" + \
                  "╰━━━━━━━━━━━━━━╯\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁??!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃ SETTING ┃\n		──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━╮\n" + \
                  "╠🔘➣ " + key + "Sticker「on/off」\n" + \
                  "╠🔘➣ " + key + "Respon「on/off」\n" + \
                  "╠🔘➣ " + key + "Contact「on/off」\n" + \
                  "╠🔘➣ " + key + "Autojoin「on/off」\n" + \
                  "╠🔘➣ " + key + "Autoadd「on/off」\n" + \
                  "╠🔘➣ " + key + "Welcome「on/off」\n" + \
                  "╠🔘➣ " + key + "Autoleave「on/off」\n" + \
                  "╰━━━━━━━━━━━━━━╯\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃ ADMIN ┃\n		──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━╮\n" + \
                  "╠🔘➣ " + key + "Adminadd「@」\n" + \
                  "╠🔘➣ " + key + "Admindell「@」\n" + \
                  "╠🔘➣ " + key + "Staffadd「@」\n" + \
                  "╠🔘➣ " + key + "Staffdell「@」\n" + \
                  "╠🔘➣ " + key + "Botadd「@」\n" + \
                  "╠🔘➣ " + key + "Botdell「@」\n" + \
                  "╠🔘➣ " + key + "Refresh\n" + \
                  "╠🔘➣ " + key + "Listbot\n" + \
                  "╠🔘➣ " + key + "Listadmin\n" + \
                  "╠🔘➣ " + key + "Listprotect\n" + \
                  "●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\nhttp://line.me/ti/p/qEaRIT2R3N\n"
    return helpMessage2

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n	エリートゲンベル v777@212\n╰━━━━━━━━━━━━━━╯\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃ MEDIA ┃\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n" + \
                  "╠🔘➣ " + key + "Blc\n" + \
                  "╠🔘➣ " + key + "Ban「@」\n" + \
                  "╠🔘➣ " + key + "Unban「@」\n" + \
                  "╠🔘➣ " + key + "Talkban「@」\n" + \
                  "╠🔘➣ " + key + "Untalkban「@」\n" + \
                  "╠🔘➣ " + key + "Talkban:on\n" + \
                  "╠🔘➣ " + key + "Untalkban:on\n" + \
                  "╠🔘➣ " + key + "Banlist\n" + \
                  "╠🔘➣ " + key + "Talkbanlist\n" + \
                  "╠🔘➣ " + key + "Clearban\n" + \
                  "╠🔘➣ " + key + "Refresh\n" + \
                  "╰━━━━━━━━━━━━━━╯\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n		──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━╮\n" + \
                  "╠🔘➣ " + key + "Cek sider\n" + \
                  "╠🔘➣ " + key + "Cek spam\n" + \
                  "╠🔘➣ " + key + "Cek pesan \n" + \
                  "╠🔘➣ " + key + "Cek respon \n" + \
                  "╠🔘➣ " + key + "Cek welcome\n" + \
                  "╠🔘➣ " + key + "Set sider:「Text」\n" + \
                  "╠🔘➣ " + key + "Set spam:「Text」\n" + \
                  "╠🔘➣ " + key + "Set pesan:「Text」\n" + \
                  "╠🔘➣ " + key + "Set respon:「Text」\n" + \
                  "╠🔘➣ " + key + "Set welcome:「Text」\n" + \
                  "╠🔘➣ " + key + "Myname:「Nama」\n" + \
                  "╠🔘➣ " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ♠️ ۩ஜ▬▬▬▬●\nhttp://line.me/ti/p/qEaRIT2R3N\n"
    return helpMessage3

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass
                    
        if op.type == 11:
            if op.param1 in protectqr:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 == '1':
                        try:
                            G = cl.getGroup(op.param1)
                            G.name = wait['pro_name'][op.param1]
                            cl.updateGroup(G)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass
  
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Dmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
                        km.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        km.leaveGroup(op.param1)
                    else:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
                        km.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Emid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Hai " + str(ginfo.name))

        
            

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        pass

        

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendText(op.param1, wait["message"])

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        pass

#================

        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    	wait["blacklist"][op.param2] = True
                    	try:
                            sw.acceptGroupInvitation(op.param1)
  #                          sw2.acceptGroupInvitation(op.param1)
                            sw.inviteIntoGroup(op.param1,[op.param3])
                            sw.kickoutFromGroup(op.param1,[op.param2])  
#                            sw2.kickoutFromGroup(op.param1,[op.param2])                      
#                            sw2.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitationByTicket(op.param1)
                    	except:
                          try:
                                G = sw.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                sw.updateGroup(G)
                                Ticket = sw.reissueGroupTicket(op.param1)
    #                    Ticket = ki.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                bb.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                cc.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                dd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                sw.kickoutFromGroup(op.param1,[op.param2])
                                sw.leaveGroup(op.param1)
   #                             sw2.leaveGroup(op.param1)
                                X = cl.getGroup(op.param1)
                                X.preventeJoinByTicket = True
                                cl.updateGroup(X)
                                ginfo = cl.getGroup(msg.to)
 #                               cl.inviteIntoGroup(msg.to, [Ymid])
                                cl.inviteIntoGroup(msg.to, [Zmid])
                                contact = cl.getContact(msg._from)
                                Ticket = sw.reissueGroupTicket(op.param1)
                          except:
                              try:
                              	sw.inviteIntoGroup(op.param1,[op.param3])
#                              	sw1.inviteIntoGroup(op.param1,[op.param3])
                              	cl.acceptGroupInvitation(op.param1)
                              	sw.kickoutFromGroup(op.param1,[op.param2])
 #                             	sw2.kickoutFromGroup(op.param1,[op.param2])
                              except:
                              	pass
                                                        
                                                 			
   #             if op.param3 in Ymid:
   #                 if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
   #                     cl.kickoutFromGroup(op.param1,[op.param2])
   #                     cl.findAndAddContactsByMid(op.param3)
   #                     cl.inviteIntoGroup(op.param1,[Ymid])
   #                     cl.sendMessage(op.param1,"=AntiJS Invited=")
   #                 else:
   #                     cl.kickoutFromGroup(op.param1,[op.param2])
   #                     cl.findAndAddContactsByMid(op.param3)
   #                     cl.inviteIntoGroup(op.param1,[Ymid])
   #                     cl.sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            cl.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

#===================

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

                return

        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                    	km.cancleGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                        	kb.cancleGroupInvitation(op.param1,[op.param2])
                                        except:
                                            pass
                                                    
                return                                       
#====================================================================
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                    	km.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                        	kb.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                                    
                return                                
#====================================================================                            
        if op.type == 19:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                    	km.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                        	kb.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass

                return

        if op.type == 19 or op.type == 32:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[mid,Bmid,Cmid,Dmid,Emid])
                        cl.acceptGroupInvitation(op.param1)                        
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        km.acceptGroupInvitation(op.param1)
                        kb.acceptGroupInvitation(op.param1)
                        ki.cancelGroupInvitation(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            sw.acceptGroupInvitation(op.param1)
                            sw.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid])
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            km.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)                                                            
                            cl.inviteIntoGroup(op.param1, [Zmid])                        
                            wait["blacklist"][op.param2] = True
                        except:
                            pass
        if op.type == 19 or op.type == 32:
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[Amid,mid,Cmid,Dmid,Emid])
                        ki.acceptGroupInvitation(op.param1)
                        cl.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        km.acceptGroupInvitation(op.param1)
                        kb.acceptGroupInvitation(op.param1)                        
                        kk.cancelGroupInvitation(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            sw.acceptGroupInvitation(op.param1)
                            sw.inviteIntoGroup(op.param1,[Amid,mid,Bmid,Cmid,Dmid,Emid])
                            ki.acceptGroupInvitation(op.param1)
                            cl.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            km.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)                                                            
                            ki.inviteIntoGroup(op.param1, [Zmid])                        
                            wait["blacklist"][op.param2] = True
                        except:
                            pass
        if op.type == 19 or op.type == 32:
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[Bmid,mid,Amid,Dmid,Emid])
                        kk.acceptGroupInvitation(op.param1)
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        km.acceptGroupInvitation(op.param1)
                        kb.acceptGroupInvitation(op.param1)
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            sw.acceptGroupInvitation(op.param1)
                            sw.inviteIntoGroup(op.param1,[Bmid,mid,Amid,Cmid,Dmid,Emid])
                            kk.acceptGroupInvitation(op.param1)
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            km.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)                                                            
                            kk.inviteIntoGroup(op.param1, [Zmid])                        
                            wait["blacklist"][op.param2] = True
                        except:
                            pass
        if op.type == 19 or op.type == 32:
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        km.kickoutFromGroup(op.param1,[op.param2])
                        km.inviteIntoGroup(op.param1,[Cmid,mid,Amid,Bmid,Emid])
                        kc.acceptGroupInvitation(op.param1)
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kb.acceptGroupInvitation(op.param1)
                        km.cancelGroupInvitation(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            sw.acceptGroupInvitation(op.param1)
                            sw.inviteIntoGroup(op.param1,[Cmid,mid,Amid,Bmid,Dmid,Emid])
                            kc.acceptGroupInvitation(op.param1)
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            km.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)                                                            
                            kc.inviteIntoGroup(op.param1, [Zmid])                        
                            wait["blacklist"][op.param2] = True
                        except:
                            pass
        if op.type == 19 or op.type == 32:
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[Dmid,mid,Amid,Bmid,Cmid])
                        km.acceptGroupInvitation(op.param1)
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        kb.cancelGroupInvitation(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            sw.acceptGroupInvitation(op.param1)
                            sw.inviteIntoGroup(op.param1,[Dmid,mid,Amid,Bmid,Cmid,Emid])
                            km.acceptGroupInvitation(op.param1)
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)                                                            
                            km.inviteIntoGroup(op.param1, [Zmid])                        
                            wait["blacklist"][op.param2] = True
                        except:
                            pass
        if op.type == 19 or op.type == 32:
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[Emid,Amid,Bmid,Cmid,Dmid])
                        kb.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        km.acceptGroupInvitation(op.param1)
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            sw.acceptGroupInvitation(op.param1)
                            sw.inviteIntoGroup(op.param1,[Emid,mid,Amid,Bmid,Cmid,Dmid])
                            kb.acceptGroupInvitation(op.param1)
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            km.acceptGroupInvitation(op.param1)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)                                                            
                            kb.inviteIntoGroup(op.param1, [Zmid])                        
                            wait["blacklist"][op.param2] = True
                        except:
                            pass
            if mid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[mid])
                        cl.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[Amid,Bmid,Cmid,Dmid,Emid,Zmid])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[mid])
                            cl.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[mid])
                                cl.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    km.inviteIntoGroup(op.param1,[mid])
                                    cl.acceptGroupInvitation(op.param1)
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass            
            if Zmid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.inviteIntoGroup(op.param1,[Zmid])
                        kb.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            km.inviteIntoGroup(op.param1,[Zmid])
                            km.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[Zmid])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kk.inviteIntoGroup(op.param1,[Zmid])
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki.inviteIntoGroup(op.param1,[Zmid])
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
            
                                  
            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,staff)
                        cl.inviteIntoGroup(op.param1,staff)
                    except:
                        pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
               try:
               	ki.cancelGroupInvitation(op.param1,[op.param2])
               	ki.kickoutFromGroup(op.param1,[op.param2])
               except:
                   try:
                   	kk.cancelGroupInvitation(op.param1,[op.param2])
                   	kk.kickoutFromGroup(op.param1,[op.param2])
                   except:
                       try:
                       	kc.cancelGroupInvitation(op.param1,[op.param2])
                       	kc.kickoutFromGroup(op.param1,[op.param2])
                       except:
                           try:
                           	km.cancelGroupInvitation(op.param1,[op.param2])
                           	km.kickoutFromGroup(op.param1,[op.param2])
                           except:
                           	try:
                                   kb.cancelGroupInvitation(op.param1,[op.param2])
                                   kb.kickoutFromGroup(op.param1,[op.param2])
                           	except:
                                   pass

        

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
        
                                  
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              ki.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(KAC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendImageWithURL(msg.to,image)
                           rnd = ["Nah, ngetag mele ntar beper ngak ada yang tanggung jawab.. jangan sampek puskun ya beb"]
                           p = random.choice(rnd)
                           lang = 'id'
                           tts = gTTS(text=p, lang=lang)
                           tts.save("hasil.mp3")
                #           cl.sendAudio(msg.to,"hasil.mp3")
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"12641049","STKPKGID":"1313075","STKVER":"1"}, contentType=7)
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n┃🇮🇩┃ STKID : " + msg.contentMetadata["STKID"] + "\n┃🇮🇩┃ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n┃🇮🇩┃ STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"┃🇮🇩┃ Nama : " + msg.contentMetadata["displayName"] + "\n┃🇮🇩┃ MID : " + msg.contentMetadata["mid"] + "\n┃🇮🇩┃ Status Msg : " + contact.statusMessage + "\n┃🇮🇩┃ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"┃🇮🇩┃ Nama : " + msg.contentMetadata["displayName"] + "\n┃🇮🇩┃ MID : " + msg.contentMetadata["mid"] + "\n┃🇮🇩┃ Status Msg : " + contact.statusMessage + "\n┃🇮🇩┃ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot saints")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendText(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["RAfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["RAfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["RAfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["RAfoto"]:
                            path = km.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Dmid]
                            km.updateProfilePicture(path)
                            km.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["RAfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Emid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = km.downloadObjectMsg(msg_id)
                     path5 = kb.downloadObjectMsg(msg_id)
#                     path6 = cc.downloadObjectMsg(msg_id)
#                     path7 = dd.downloadObjectMsg(msg_id)
#                     path8 = g1.downloadObjectMsg(msg_id)
#                     path8 = g2.downloadObjectMsg(msg_id)
#                     path9 = sw1.downloadObjectMsg(msg_id)
#                     path9 = sw2.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     km.updateProfilePicture(path1)
                     km.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kb.updateProfilePicture(path2)
                     kb.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
#                     cc.updateProfilePicture(path3)
#                     cc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
#                     dd.updateProfilePicture(path3)
#                     dd.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
#                     g1.updateProfilePicture(path1)
#                     g1.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
#                     g2.updateProfilePicture(path2)
 #                    g2.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
#                     sw1.updateProfilePicture(path3)
#                     sw1.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
#                     sw2.updateProfilePicture(path3)
#                     sw2.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = sw.downloadObjectMsg(msg_id)
         #            path2 = kk.downloadObjectMsg(msg_id)
          #           path3 = kc.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     sw.updateProfilePicture(path1)
                     sw.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
         #            kk.updateProfilePicture(path2)
         #            kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
         #            kc.updateProfilePicture(path3)
         #            kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendText(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendText(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpmedia()
                               cl.sendMessage(msg.to, str(helpMessage1))
                               contact = cl.getContact(msg._from)
                               cl.sendMessage(msg.to, str(ret_),{'AGENT_LINK': 'line://ti/p/~xsetail','AGENT_ICON': "http://dl.profile.line-cdn.net/" + contact.pictureStatus,'AGENT_NAME': "~• 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ •~"})

                                                            
                               
                        elif cmd == "help3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = helpsetting()
                               cl.sendMessage(msg.to, str(helpMessage2))
                               contact = cl.getContact(msg._from)
                               cl.sendMessage(msg.to, str(ret_),{'AGENT_LINK': 'line://ti/p/~xsetail','AGENT_ICON': "http://dl.profile.line-cdn.net/" + contact.pictureStatus,'AGENT_NAME': "~• 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ •~"})
                               
                        elif cmd == "help4":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage3 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage3))
                               contact = cl.getContact(msg._from)
                               cl.sendMessage(msg.to, str(ret_),{'AGENT_LINK': 'line://ti/p/~xsetail','AGENT_ICON': "http://dl.profile.line-cdn.net/" + contact.pictureStatus,'AGENT_NAME': "~• 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ •~"})

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "┃🛡┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Protection\n\n"
                                if wait["sticker"] == True: md+="┃🛠┃ Sticker「📳」\n"
                                else: md+="┃👿┃ Sticker「📴」\n"
                                if wait["contact"] == True: md+="┃🛠┃ Contact「📳」\n"
                                else: md+="┃👿┃ Contact「📴」\n"
                                if wait["talkban"] == True: md+="┃🛠┃ Talkban「📳」\n"
                                else: md+="┃👿┃ Talkban「📴」\n"
                                if wait["Mentionkick"] == True: md+="┃🛠┃ Notag「📳」\n"
                                else: md+="┃👿┃ Notag「📴」\n"
                                if wait["detectMention"] == True: md+="┃🛠┃ Respon「📳」"
                                else: md+="┃👿┃ Respon「📴」\n"
                                if wait["autoJoin"] == True: md+="┃🛠┃ Autojoin「📳」\n"
                                else: md+="┃👿┃ Autojoin「📴」\n"
                                if wait["autoAdd"] == True: md+="┃🛠┃ Autoadd「📳」\n"
                                else: md+="┃👿┃ Autoadd「📴」\n"
                                if msg.to in welcome: md+="┃🛠┃ Welcome「📳」\n"
                                else: md+="┃👿┃ Welcome「📴」\n"
                                if wait["autoLeave"] == True: md+="┃🛠┃ Autoleave「📳」\n"
                                else: md+="┃👿┃ Autoleave「📴」\n"
                                if msg.to in protectqr: md+="┃🛠┃ Protecturl「🛡」\n"
                                else: md+="┃👿┃ Protecturl「📴」\n"
                                if msg.to in protectjoin: md+="┃🛠┃ Protectjoin「🛡」\n"
                                else: md+="┃👿┃ Protectjoin「📴」\n"
                                if msg.to in protectkick: md+="┃🛠┃ Protectkick「🛡」\n"
                                else: md+="┃👿┃ Protectkick「📴」\n"
                                if msg.to in protectcancel: md+="┃🛠┃ Protectcancel「🛡」\n"
                                else: md+="┃👿┃ Protectcancel「📴」\n"
                                if msg.to in protectinvite: md+="┃🛠┃ Protectinvite「🛡」\n"
                                else: md+="┃👿┃ Protectinvite「📴」\n"                                
                                cl.sendMessage(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendText(msg.to,"Creator :\nD̸͟͞k̸͟͞f̸͟͞  T̸͟͞e̸͟͞a̸͟͞m̸͟͞   B̸͟͞o̸͟͞t̸͟͞  p̸͟͞r̸͟͞o̸͟͞t̸͟͞e̸͟͞c̸͟͞t̸͟͞.  \nhttp://line.me/ti/p/qEaRIT2R3N ") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 Type Selfbot 」\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'creator':
                            if msg._from in admin:
                                ma = ""
                                for i in baraya:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)
                               
                        elif text.lower() == "me":
                               cl.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "┃👿┃ Nama : "+str(mi.displayName)+"\n┃🇮🇩┃ Mid : " +key1+"\n┃🇮🇩┃ Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)                                                              

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "hc":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   km.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)                                   
                                   cl.sendText(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Silahkan gunakan seperti semula...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Stay " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Family Grup Info\n\n┃🇮🇩┃ Nama Group : {}".format(G.name)+ "\n┃🇮🇩┃ ID Group : {}".format(G.id)+ "\n┃🇮🇩┃ Pembuat : {}".format(G.creator.displayName)+ "\n┃🇮🇩┃ Waktu Dibuat : {}".format(str(timeCreated))+ "\n┃🇮🇩┃ Jumlah Member : {}".format(str(len(G.members)))+ "\n┃🇮🇩┃ Jumlah Pending : {}".format(gPending)+ "\n┃🇮🇩┃ Group Qr : {}".format(gQr)+ "\n┃🇮🇩┃ Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Family Grup Info\n"
                                ret_ += "\n┃🇮🇩┃ Nama Group : {}".format(G.name)
                                ret_ += "\n┃??🇩┃ ID Group : {}".format(G.id)
                                ret_ += "\n┃🇮🇩┃ Pembuat : {}".format(gCreator)
                                ret_ += "\n┃🇮🇩┃ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n┃🇮🇩┃ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n┃🇮🇩┃ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┃🇮🇩┃ Group Qr : {}".format(gQr)
                                ret_ += "\n┃🇮🇩┃ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "┃🇮🇩┃ "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"┃🇮🇩┃ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    km.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    kd.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    kf.leaveGroup(i)
                                    kg.leaveGroup(i)
                                    kh.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "clp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "kip":
                            if msg._from in admin:
                                Setmain["RAfoto"][Amid] = True
                                ki.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "kkp":
                            if msg._from in admin:
                                Setmain["RAfoto"][Bmid] = True
                                kk.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "kcp":
                            if msg._from in admin:
                                Setmain["RAfoto"][Cmid] = True
                                kc.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "kmp":
                            if msg._from in admin:
                                Setmain["RAfoto"][Dmid] = True
                                km.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "kbp":
                            if msg._from in admin:
                                Setmain["RAfoto"][Emid] = True
                                kb.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "pp":
                            if msg._from in admin:
                                Setmain["RAfoto"][Zmid] = True
                                sw1.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myn: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("kin: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("kkn: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("kcn: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("kmn: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = km.getProfile()
                                profile.displayName = string
                                km.updateProfile(profile)
                                km.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("kbn: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("pbots: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "tagall" or text.lower() == 'hai':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, jml = [], [], [], [], [], [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-0):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-0):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-0):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-0):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-0):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-0):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-0):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                               if jml > 160 and jml < 180:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, len(nama)-0):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                               if jml > 180 and jml < 200:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, len(nama)-0):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)										                 
                               
                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Family bot\n\n"+ma+"\nTotal「%s」Family Bots" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Family admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」Family Saints" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protecturl
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Family Protection\n\n┃🇮🇩┃ PROTECT QR :\n"+ma+"\n┃🇮🇩┃ PROTECT KICK :\n"+mb+"\n┃🇮🇩┃ PROTECT JOIN :\n"+md+"\n┃🇮🇩┃ PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                cl.sendMessage(msg.to,responsename1)
                                ki.sendMessage(msg.to,responsename2)
                                kk.sendMessage(msg.to,responsename3)
                                kc.sendMessage(msg.to,responsename4)
                                km.sendMessage(msg.to,responsename5)
                                kb.sendMessage(msg.to,responsename6)
                                sw.sendMessage(msg.to,responsename7)                                

                        elif cmd == "stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)                                    
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                      #              cl.inviteIntoGroup(msg.to, [Zmid])
  #                                  cl.sendMessage(msg.to,"Grup ã"+str(ginfo.name)+"ã Aman Dari JS")
                                except:
                                    pass

                        elif cmd == "joinall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
             #                   ginfo = cl.getGroup(msg.to)                                    
             #                   cl.inviteIntoGroup(msg.to, [Zmid])
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)
                                ginfo = kb.getGroup(msg.to)                                    
                                kb.inviteIntoGroup(msg.to, [Zmid])
                                

                        elif cmd == "byeall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
 #                               ki.sendText(msg.to, "Bye bye fams "+str(G.name))
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                km.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                
                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendText(msg.to, "Bye bye fams "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        cl.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "assist1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "assist2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "assist3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "kicker join":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                    #            sw2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                    #            G = sw2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "kicker bye":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)
                    #            sw2.leaveGroup(msg.to)

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "spall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} km/jam".format(str(elapsed_time)))
                               ki.sendMessage(msg.to, "{} km/jam".format(str(elapsed_time)))
                               kk.sendMessage(msg.to, "{} km/jam".format(str(elapsed_time)))
                               kc.sendMessage(msg.to, "{} km/jam".format(str(elapsed_time)))
                               km.sendMessage(msg.to, "{} km/jam".format(str(elapsed_time)))
                               kb.sendMessage(msg.to, "{} km/jam".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 cl.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 cl.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nCek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nCek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                #        elif cmd.startswith("sholat: "):
                #          if msg._from in admin:
                #             sep = text.split(" ")
                #             location = text.replace(sep[0] + " ","")
                #             with requests.session() as web:
                #                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                #                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                #                  data = r.text
                #                  data = json.loads(data)
                #                  tz = pytz.timezone("Asia/Jakarta")
                #                  timeNow = datetime.now(tz=tz)
                #                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                #                         ret_ = "「Jadwal Sholat」"
                #                         ret_ += "\n┃🇮🇩┃ Lokasi : " + data[0]
                #                         ret_ += "\n┃🇮🇩┃ " + data[1]
                #                         ret_ += "\n┃🇮🇩┃ " + data[2]
                #                         ret_ += "\n┃🇮🇩┃ " + data[3]
                #                         ret_ += "\n┃🇮🇩┃ " + data[4]
                #                         ret_ += "\n┃🇮🇩┃ " + data[5]
                #                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                #                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                #                  cl.sendMessage(msg.to, str(ret_))

       #                 elif cmd.startswith("cuaca: "):
       #                   if msg._from in admin:
       #                     separate = text.split(" ")
       #                     location = text.replace(separate[0] + " ","")
       #                     with requests.session() as web:
        #                        web.headers["user-agent"] = random.choice(settings["userAgent"])
        #                        r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
        #                        data = r.text
        #                        data = json.loads(data)
        #                        tz = pytz.timezone("Asia/Jakarta")
        #                        timeNow = datetime.now(tz=tz)
        #                        if "result" not in data:
        #                            ret_ = "「Status Cuaca」"
        #                            ret_ += "\n┃🇮🇩┃ Lokasi : " + data[0].replace("Temperatur di kota ","")
        #                            ret_ += "\n┃🇮🇩┃ Suhu : " + data[1].replace("Suhu : ","") + " C"
        #                            ret_ += "\n┃🇮🇩┃ Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
        #                            ret_ += "\n┃🇮🇩┃ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
        #                            ret_ += "\n┃🇮🇩┃ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
        #                            ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
        #                            ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
        #                        cl.sendMessage(msg.to, str(ret_))

      #                  elif cmd.startswith("lokasi: "):
      #                    if msg._from in admin:
      #                      separate = msg.text.split(" ")
      #                      location = msg.text.replace(separate[0] + " ","")
      #                      with requests.session() as web:
      #                          web.headers["user-agent"] = random.choice(settings["userAgent"])
      #                          r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
      #                          data = r.text
      #                          data = json.loads(data)
      #                          if data[0] != "" and data[1] != "" and data[2] != "":
      #                              link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
      #                              ret_ = "「Info Lokasi」"
      #                              ret_ += "\n┃🇮🇩┃ Location : " + data[0]
      #                              ret_ += "\n┃🇮🇩┃ Google Maps : " + link
      #                          else:
       #                             ret_ = "[Details Location] Error : Location not found"
       #                         cl.sendMessage(msg.to,str(ret_))

         #               elif cmd.startswith("lirik: "):
         #                  if msg._from in admin:
         #                      sep = msg.text.split(" ")
         #                      search = msg.text.replace(sep[0] + " ","")
         #                      params = {'songname': search}
         #                      with requests.session() as web:
         #                          web.headers["User-Agent"] = random.choice(settings["userAgent"])
         #                          r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
         #                          try:
         #                             data = json.loads(r.text)
         #                             for song in data:
         #                                 songs = song[5]
          #                                lyric = songs.replace('ti:','Title - ')
          #                                lyric = lyric.replace('ar:','Artist - ')
          #                                lyric = lyric.replace('al:','Album - ')
          #                                removeString = "[1234567890.:]"
          #                                for char in removeString:
          #                                    lyric = lyric.replace(char,'')
          #                                ret_ = "╔══[ Lyric ]"
          #                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
          #                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
          #                                ret_ += "\n╠ Link : {}".format(str(song[3]))
          #                                ret_ += "\n╚══[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
          #                                cl.sendText(msg.to, str(ret_))
          #                         except:
          #                             cl.sendText(to, "Lirik tidak ditemukan")
                            
     #                   elif cmd.startswith("music: "):
     #                      if msg._from in admin:
     #                         sep = msg.text.split(" ")
     #                         search = msg.text.replace(sep[0] + " ","")
     #                         params = {'songname': search}
     #                         with requests.session() as web:
     #                             web.headers["User-Agent"] = random.choice(settings["userAgent"])
     #                             r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
     #                             try:
     #                                 data = json.loads(r.text)
     #                                 for song in data:
     #                                     ret_ = "╔══[ Music ]"
     #                                     ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
     #                                     ret_ += "\n╠ Durasi : {}".format(str(song[1]))
     #                                     ret_ += "\n╠ Link : {}".format(str(song[3]))
     #                                     ret_ += "\n╚══[ Waiting Audio ]"
     #                                 cl.sendText(msg.to, str(ret_))
     #                                 cl.sendText(msg.to, "Mohon bersabar musicnya lagi di upload")
     #                                 cl.sendAudioWithURL(msg.to, song[3])
     #                             except:
     #                                 cl.sendText(to, "Musik tidak ditemukan")

 #                       elif cmd.startswith("gimage: "):
 #                         if msg._from in admin:
 #                           sep = msg.text.split(" ")
 #                           search = msg.text.replace(sep[0] + " ","")
 #                           url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
 #                           with requests.session() as web:
 #                               web.headers["User-Agent"] = random.choice(settings["userAgent"])
 #                               r = web.get(url)
 #                               data = r.text
 #                               data = json.loads(data)
 #                               if data["data"] != []:
 #                                   start = timeit.timeit()
 #                                   items = data["data"]
  #                                  path = random.choice(items)
  #                                  a = items.index(path)
  #                                  b = len(items)
  #                                  cl.sendText(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
  #                                  cl.sendImageWithURL(msg.to, str(path))

#                        elif cmd.startswith("ytmp4: "):
#                          if msg._from in admin:
#                            try:
#                                sep = msg.text.split(" ")
#                                textToSearch = msg.text.replace(sep[0] + " ","")
#                                query = urllib.parse.quote(textToSearch)
#                                search_url="https://www.youtube.com/results?search_query="
#                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
#                                sb_url = search_url + query
#                                sb_get = requests.get(sb_url, headers = mozhdr)
#                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
#                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
#                                x = (yt_links[1])
#                                yt_href =  x.get("href")
#                                yt_href = yt_href.replace("watch?v=", "")
#                                qx = "https://youtu.be" + str(yt_href)
#                                vid = pafy.new(qx)
#                                stream = vid.streams
#                                best = vid.getbest()
#                                best.resolution, best.extension
#                                for s in stream:
 #                                   me = best.url
 #                                   hasil = ""
 #                                   title = "Judul [ " + vid.title + " ]"
 #                                   author = '\n\n┃🇮🇩┃ Author : ' + str(vid.author)
 #                                   durasi = '\n┃🇮🇩┃ Duration : ' + str(vid.duration)
 #                                   suka = '\n┃🇮🇩┃ Likes : ' + str(vid.likes)
 #                                   rating = '\n┃🇮🇩┃ Rating : ' + str(vid.rating)
  #                                  deskripsi = '\n┃🇮🇩┃ Deskripsi : ' + str(vid.description)
  #                              cl.sendVideoWithURL(msg.to, me)
  #                              cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
  #                          except Exception as e:
  #                              cl.sendText(msg.to,str(e))

  #                      elif cmd.startswith("ytmp3: "):
  #                        if msg._from in admin:
  #                          try:
  #                              sep = msg.text.split(" ")
  #                              textToSearch = msg.text.replace(sep[0] + " ","")
  #                              query = urllib.parse.quote(textToSearch)
  #                              search_url="https://www.youtube.com/results?search_query="
  #                              mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
  #                              sb_url = search_url + query
  #                              sb_get = requests.get(sb_url, headers = mozhdr)
  #                              soupeddata = BeautifulSoup(sb_get.content, "html.parser")
  #                              yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
  #                              x = (yt_links[1])
  #                              yt_href =  x.get("href")
  #                              yt_href = yt_href.replace("watch?v=", "")
  #                              qx = "https://youtu.be" + str(yt_href)
   #                             vid = pafy.new(qx)
   #                             stream = vid.streams
  #                              bestaudio = vid.getbestaudio()
  #                              bestaudio.bitrate
  #                              best = vid.getbest()
  #                              best.resolution, best.extension
  #                              for s in stream:
  #                                  shi = bestaudio.url
  #                                  me = best.url
  #                                  vin = s.url
  #                                  hasil = ""
   #                                 title = "Judul [ " + vid.title + " ]"
   #                                 author = '\n\n┃🇮🇩┃ Author : ' + str(vid.author)
  #                                  durasi = '\n┃🇮🇩┃ Duration : ' + str(vid.duration)
  #                                  suka = '\n┃🇮🇩┃ Likes : ' + str(vid.likes)
  #                                  rating = '\n┃🇮🇩┃ Rating : ' + str(vid.rating)
  #                                  deskripsi = '\n┃🇮🇩┃ Deskripsi : ' + str(vid.description)
  #                              cl.sendImageWithURL(msg.to, me)
  #                              cl.sendAudioWithURL(msg.to, shi)
  #                              cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
  #                          except Exception as e:
  #                              cl.sendText(msg.to,str(e))

#                        elif cmd.startswith("profileig: "):
#                          if msg._from in admin:
#                            try:
#                                sep = msg.text.split(" ")
#                                instagram = msg.text.replace(sep[0] + " ","")
#                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
#                                data = response.json()
#                                namaIG = str(data['user']['full_name'])
#                                bioIG = str(data['user']['biography'])
#                                mediaIG = str(data['user']['media']['count'])
#                                verifIG = str(data['user']['is_verified'])
#                                usernameIG = str(data['user']['username'])
#                                followerIG = str(data['user']['followed_by']['count'])
#                                profileIG = data['user']['profile_pic_url_hd']
#                                privateIG = str(data['user']['is_private'])
#                                followIG = str(data['user']['follows']['count'])
#                                link = "┃🇮🇩┃ Link : " + "https://www.instagram.com/" + instagram
#                                text = "┃🇮🇩┃ Name : "+namaIG+"\n┃🇮🇩┃ Username : "+usernameIG+"\n┃🇮🇩┃ Biography : "+bioIG+"\n┃🇮🇩┃ Follower : "+followerIG+"\n┃🇮🇩┃ Following : "+followIG+"\n┃🇮🇩┃ Post : "+mediaIG+"\n┃🇮🇩┃ Verified : "+verifIG+"\n┃🇮🇩┃ Private : "+privateIG+"" "\n" + link
#                                cl.sendImageWithURL(msg.to, profileIG)
#                                cl.sendMessage(msg.to, str(text))
#                            except Exception as e:
#                                    cl.sendMessage(msg.to, str(e))

#                        elif cmd.startswith("cekdate: "):
#                          if msg._from in admin:
#                            sep = msg.text.split(" ")
#                            tanggal = msg.text.replace(sep[0] + " ","")
#                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
#                            data=r.text
#                            data=json.loads(data)
#                            lahir = data["data"]["lahir"]
#                            usia = data["data"]["usia"]
#                            ultah = data["data"]["ultah"]
#                            zodiak = data["data"]["zodiak"]
#                            cl.sendMessage(msg.to,"┃🇮🇩┃ I N F O R M A S I ┃🇮🇩┃\n\n"+"┃🇮🇩┃ Date Of Birth : "+lahir+"\n┃🇮🇩┃ Age : "+usia+"\n┃🇮🇩┃ Ultah : "+ultah+"\n┃🇮🇩┃ Zodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nTotal Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nTotal Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 100000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 100000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 100000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    cl.sendText(msg.to,"Jumlah melebihi batas")

                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                cl.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                cl.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                cl.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass
                                
                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 100000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 100000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kk.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kc.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nWelcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nWelcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    
						 
                        elif 'Protectinvite ' in msg.text:
                            if msg._from in admin:
                               spl = msg.text.replace('Protectinvite ','')
                               if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nProtect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nProtect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                               elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nProtect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nProtect invite sudah tidak aktif"
                                    cl.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)                                    

                        elif 'O ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('O ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nAnti DESAH sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nAnti DESAH Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nAnti DESAH Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nAnti DESAH Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)

                        elif 'Semua pro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Semua pro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nSemua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nSemua protect sudah off\nDi Group : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#
                        elif ("Nk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif ("K1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	wait["blacklist"][op.param2] = True
                            	key = eval(msg.contentMetadata["MENTION"])
                            	key["MENTIONEES"][0]["M"]
                            	targets = []
                            	for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                            	for target in targets:
                                   if target not in Bots:
                                       try:
                                           ki.kickoutFromGroup(msg.to, [target])                                           
                                       except:
                                           pass

                        elif ("K2 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	wait["blacklist"][op.param2] = True
                            	key = eval(msg.contentMetadata["MENTION"])
                            	key["MENTIONEES"][0]["M"]
                            	targets = []
                            	for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                            	for target in targets:
                                   if target not in Bots:
                                       try:
                                           kk.kickoutFromGroup(msg.to, [target])                                           
                                       except:
                                           pass

                        elif ("K3 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	wait["blacklist"][op.param2] = True
                            	key = eval(msg.contentMetadata["MENTION"])
                            	key["MENTIONEES"][0]["M"]
                            	targets = []
                            	for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                            	for target in targets:
                                   if target not in Bots:
                                       try:
                                           kc.kickoutFromGroup(msg.to, [target])                                           
                                       except:
                                           pass

                        elif ("K4 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	wait["blacklist"][op.param2] = True
                            	key = eval(msg.contentMetadata["MENTION"])
                            	key["MENTIONEES"][0]["M"]
                            	targets = []
                            	for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                            	for target in targets:
                                   if target not in Bots:
                                       try:
                                           km.kickoutFromGroup(msg.to, [target])                                           
                                       except:
                                           pass

                        elif ("K5 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	wait["blacklist"][op.param2] = True
                            	key = eval(msg.contentMetadata["MENTION"])
                            	key["MENTIONEES"][0]["M"]
                            	targets = []
                            	for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                            	for target in targets:
                                   if target not in Bots:
                                       try:
                                           kb.kickoutFromGroup(msg.to, [target])                                           
                                       except:
                                           pass

                        elif ("K6 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	wait["blacklist"][op.param2] = True
                            	key = eval(msg.contentMetadata["MENTION"])
                            	key["MENTIONEES"][0]["M"]
                            	targets = []
                            	for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                            	for target in targets:
                                   if target not in Bots:
                                       try:
                                           sw.kickoutFromGroup(msg.to, [target])                                           
                                       except:
                                           pass

                        elif ("S7 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	wait["blacklist"][op.param2] = True
                            	key = eval(msg.contentMetadata["MENTION"])
                            	key["MENTIONEES"][0]["M"]
                            	targets = []
                            	for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                            	for target in targets:
                                   if target not in Bots:
                                       try:
                                           cl.kickoutFromGroup(msg.to, [target])                                           
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'fresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendText(msg.to,"⚀...")
                                ki.sendText(msg.to,"⚁.....")
                                kk.sendText(msg.to,"⚂.......")
                                kc.sendText(msg.to,"⚃.........")
                                km.sendText(msg.to,"⚄...........")
                                kb.sendText(msg.to,"⚅.............")
                                cl.sendText(msg.to,"🔥􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴🔥/n❄❄DONE Fresh❄❄")
                                

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nNotag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nNotag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nDeteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nDeteksi contact dinonaktifkan")

                        elif ("respon on" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAuto respon diaktifkan")

                        elif ("respon off" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAuto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAutojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAutojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAutoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAutoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAuto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAuto add dinonaktifkan")

                        elif ("sticker on" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nDeteksi sticker diaktifkan")
                                
                        elif msg.text in ["Res3 on"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 wait["detectMention"] = False
                                 wait["detectMention2"] = False
                                 wait["detectMention3"] = True
                                 wait["Mentiongift"] = False
                                 wait["Mentiongift2"] = False
                                 wait["Mentiongift3"] = False
                                 wait["kickMention"] = False
                                 cl.sendText(msg.to,"Auto Respon3 Sudah Aktif")		
                          
                        elif msg.text in ["Res3 off"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 wait["detectMention3"] = False
                                 cl.sendText(msg.to,"Auto Respon3 Sudah Off")		
		
                        elif ("sticker off" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nDeteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nJoin ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nNotag dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ ┃ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nTidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ ┃ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nTidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'cb':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nSukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass