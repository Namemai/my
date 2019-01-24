#SIMPAN AKUN UTAMA KALIAN DI bima1 = LINE("Token")
#Kalo Ada yang Lebih Kurangin,,, Kalo Ada yang Kurang Tambahin,,,!!!😅😅😅
#MOGA BERMANFAAT#
#Thank's For All Mastah,,,,,!!!
# -*- coding: utf-8 -*- 
from Bima.linepy import *
from Bima.akad.ttypes import Message
from Bima.akad.ttypes import ContentType as Type
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==================================================================================================#
botStart = time.time()
#===============[Akun Utama]==========================================================================#
bima = LINE("Token")
#===============[Asist 1]==============================================================================#
b1 = LINE("Token")
#===============[Asist2]===============================================================================#
b2 = LINE("Token")
#===============[Asist3]===============================================================================#
b3 = LINE("Token")
#===============[Asist 4]===============================================================================#
b4 = LINE("Token")
#===============[Asist 5]===============================================================================#
b5 = LINE("Token")
#===============[Asist 6]===============================================================================#
b6 = LINE("Token")
#===============[Asist 7]===============================================================================#
b7 = LINE("Token")
#===============[Asist 8]===============================================================================#
b8 = LINE("Token")
#===============[Asist 9]===============================================================================#
b9 = LINE("Token")
#===============[BackupQr]=============================================================================#
bima1 = LINE("Token")
#===============[Pendingan/AntiJs]======================================================================#
bima2 = LINE("Token")
#===============[Ghost]================================================================================#
bima3 = LINE("Token")
#===============[Ghost]================================================================================#
bima4 = LINE("Token")
#====================================================================================================#
print ("==========[ Bima Login sukses ]===========")
#====================================================================================================#
poll = OEPoll(bima)
call = (bima)
baraya = ["Mid_bima","ue1256f092267ec054bb4a5d62d2eedfe"]
creator = ["Mid_bima","Mid_bima1"]
owner = ["Mid_bima","Mid_bima1"]
admin = ["Mid_bima","Mid_bima1"]
staff = ["Mid_bima","Mid_bima1"]
mid = bima.getProfile().mid
Amid = b.getProfile().mid
Bmid = b.getProfile().mid
Cmid = b.getProfile().mid
Dmid = b.getProfile().mid
Emid = b.getProfile().mid
Fmid = b.getProfile().mid
Gmid = b.getProfile().mid
Hmid = b.getProfile().mid
Imid = b.getProfile().mid
Qmid = b.getProfile().mid
Zmid = b.getProfile().mid
Xmid = b.getProfile().mid
Ymid = b.getProfile().mid
KAC = [bima,b1,b2,b3,b4,b5,b6,b7,b8,b9,bima1,bima2,bima3,bima4]
ABC = [bima,b1,b2,b3,b4,b5,b6,b7,b8,b9,bima1,bima2,bima3,bima4]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Qmid,Xmid,Ymid,Zmid]
Bima = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Qmid,Xmid,Ymid,Zmid]
Saints = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
welcome = []

responsename1 = bima.getProfile().displayName
responsename2 = bima1.getProfile().displayName
responsename3 = b1.getProfile().displayName
responsename4 = b2.getProfile().displayName
responsename5 = b3.getProfile().displayName
responsename6 = b4.getProfile().displayName
responsename7 = b5.getProfile().displayName
responsename8 = b6.getProfile().displayName
responsename9 = b7.getProfile().displayName
responsename10 = b8.getProfile().displayName
responsename11 = b9.getProfile().displayName

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
    "mention":"Sini Nikung Bareng Sama Kami,,,,,,!!!",
    "Respontag":"Maaf Orang Nya Sibuk Nikung,,,,,,,!!!",
    "welcome":"Selamat datang & betah",
    "comment":"Like like & like by 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ ",
    "message":"T̸͟͞e̸͟͞r̸͟͞i̸͟͞m̸͟͞a̸͟͞ k̸͟͞a̸͟͞s̸͟͞i̸͟͞h̸͟͞ t̸͟͞e̸͟͞l̸͟͞a̸͟͞h̸͟͞ a̸͟͞d̸͟͞d̸͟͞   😃\n☆|􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ ☆\n\nOpen Tikungan:\n┃🇮🇩┃ 1 hari 1000c\n┃🇮🇩┃ 1 minggu 2 juta 😁\n\nMinat?\nChat aja...!!!!\nCreator:\nhttps://line.me/ti/p/Dr8B9wDicC",
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
                    textx += "\n╚══[ {} ]".format(str(bima.getGroup(to).name))
                except:
                    textx += "\n╚══[ Success ]"
        bima.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        bima.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Tersangka CCTV「{}」\nAssalamualaikum ".format(str(len(mid)))
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
                    no = "\n╚══[ {} ]".format(str(bima.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        bima.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        bima.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = bima.getGroup(to)
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
                    no = "\n╚══[ {} ]".format(str(bima.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        bima.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        bima.sendMessage(to, "[ INFO ] Error :\n" + str(error))

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
        teman = bima.getAllContactIdsx()
        gid = bima.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"┃🇮🇩┃ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n┃🇮🇩┃ Group : "+str(len(gid))+"\n┃🇮🇩┃ Teman : "+str(len(teman))+"\n┃🇮🇩┃ Expired : In "+hari+"\n┃🇮🇩┃ Version : 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \n┃🇮🇩┃ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃🇮🇩┃ Runtime : \n • "+bot
        bima.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        bima.sendMessage(to, "[ INFO ] Error :\n" + str(error))

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
    helpMessage = "●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		エリートゲンベル v777@212\n╰━━━━━━━━━━━━━━╯\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃⚔ MENU⚔ ┃\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n" + \
                  "╠📂➣ " + key + "BimBot\n" + \
                  "╠📂➣ " + key + "BimSet\n" + \
                  "╠📂➣ " + key + "BimPro\n" + \
                  "╠❄➣ " + key + "Test\n" + \
                  "╠❄➣ " + key + "Tagall\n" + \
                  "╠❄➣ " + key + "Status\n" + \
                  "╠❄➣ " + key + "Contact bot\n" + \
                  "╠❄➣ " + key + "Hapus chat\n" + \
                  "╠❄➣ " + key + "Gruplist\n" + \
                  "╠❄➣ " + key + "Infogrup「angka」\n" + \
                  "╠❄➣ " + key + "Left「Namagrup」\n" + \
                  "╠❄➣ " + key + "Infomem「angka」\n" + \
                  "╠❄➣ " + key + "Spamcall:「jumlahnya」\n" + \
                  "╠❄➣ " + key + "Sider 「on/off」\n" + \
                  "╠❄➣ " + key + "Spamcall\n" + \
                  "●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n⚔Creator:\nhttps://line.me/ti/p/Dr8B9wDicC\n"
    return helpMessage                
                  
def helppro():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		エリートゲンベル v777@212\n╰━━━━━━━━━━━━━━╯\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃ ⚔ PROTECT ⚔┃\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n" + \
                  "╠🛡➣ " + key + "Protecturl「on/off」\n" + \
                  "╠🛡➣ " + key + "Protectjoin「on/off」\n" + \
                  "╠🛡➣ " + key + "Protectkick「on/off」\n" + \
                  "╠🛡➣ " + key + "Protectcancel「on/off」\n" + \
                  "╠🛡➣ " + key + "Protectinvite「on/off」\n" + \
                  "╠🛡➣ " + key + "ProJs「on/off」\n" + \
                  "╰━━━━━━━━━━━━━━╯\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃ ♻️MEDIA♻️┃\n		──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━╮\n" + \
                  "╠☠➣ " + key + "Sticker「on/off」\n" + \
                  "╠☠➣ " + key + "Respon「on/off」\n" + \
                  "╠☠➣ " + key + "Autojoin「on/off」\n" + \
                  "╠☠➣ " + key + "Autoadd「on/off」\n" + \
                  "╠☠➣ " + key + "Welcome「on/off」\n" + \
                  "╠☠➣ " + key + "Autoleave「on/off」\n" + \
                  "╰━━━━━━━━━━━━━━╯\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃ ☠ADMIN☠┃\n		──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━╮\n" + \
                  "╠☠➣ " + key + "Adminadd「@」\n" + \
                  "╠☠➣ " + key + "Admindell「@」\n" + \
                  "╠☠➣ " + key + "Staffadd「@」\n" + \
                  "╠☠➣ " + key + "Staffdell「@」\n" + \
                  "╠☠➣ " + key + "Botadd「@」\n" + \
                  "╠☠➣ " + key + "Botdell「@」\n" + \
                  "╠☠➣ " + key + "Refresh\n" + \
                  "╠☠➣ " + key + "Listbot\n" + \
                  "╠☠➣ " + key + "Listadmin\n" + \
                  "╠☠➣ " + key + "Listprotect\n" + \
                  "●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\nCreator:\nhttps://line.me/ti/p/Dr8B9wDicC\n"
    return helpMessage2

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		エリートゲンベル v777@212\n╰━━━━━━━━━━━━━━╯\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃ ⚔BOTS⚔┃\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n" + \
                  "╠☠➣ " + key + "Bimall\n" + \
                  "╠☠➣ " + key + "Bimbye\n" + \
                  "╠☠➣ " + key + "Bim join\n" + \
                  "╠☠➣ " + key + "Bim bye\n" + \
                  "╠☠➣ " + key + "Byeme\n" + \
                  "╠☠➣ " + key + "Bim1 「@」\n" + \
                  "╠☠➣ " + key + "Respon\n" + \
                  "╰━━━━━━━━━━━━━━╯\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃ ♻️CEK BOT♻️┃\n		──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━╮\n" + \
                  "╠☠➣ " + key + "Speed\n" + \
                  "╠☠➣ " + key + "Sprespon\n" + \
                  "╠☠➣ " + key + "Open\n" + \
                  "╠☠➣ " + key + "Link group\n" + \
                  "╠☠➣ " + key + "Close\n" + \
                  "╠☠➣ " + key + "Restar\n" + \
                  "●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\nCreator:\nhttps://line.me/ti/p/Dr8B9wDicC\n"
    return helpMessage3

def helpset():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage4 = "●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n	エリートゲンベル v777@212\n╰━━━━━━━━━━━━━━╯\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n╠☬➣	┃ ⚔SETTING⚔ ┃\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n" + \
                  "╠☠➣ " + key + "Blc\n" + \
                  "╠☠➣ " + key + "Ban「@」\n" + \
                  "╠☠➣ " + key + "Unban「@」\n" + \
                  "╠☠➣ " + key + "Talkban「@」\n" + \
                  "╠☠➣ " + key + "Untalkban「@」\n" + \
                  "╠☠➣ " + key + "Talkban:on\n" + \
                  "╠☠➣ " + key + "Untalkban:on\n" + \
                  "╠☠➣ " + key + "Banlist\n" + \
                  "╠☠➣ " + key + "Talkbanlist\n" + \
                  "╠☠➣ " + key + "Clearban\n" + \
                  "╠☠➣ " + key + "Refresh\n" + \
                  "╰━━━━━━━━━━━━━━╯\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n		──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━╮\n" + \
                  "╠☠➣ " + key + "Cek sider\n" + \
                  "╠☠➣ " + key + "Cek spam\n" + \
                  "╠☠➣ " + key + "Cek pesan \n" + \
                  "╠☠➣ " + key + "Cek respon \n" + \
                  "╠☠➣ " + key + "Cek welcome\n" + \
                  "╠☠➣ " + key + "Set sider:「Text」\n" + \
                  "╠☠➣ " + key + "Set spam:「Text」\n" + \
                  "╠☠➣ " + key + "Set pesan:「Text」\n" + \
                  "╠☠➣ " + key + "Set respon:「Text」\n" + \
                  "╠☠➣ " + key + "Set welcome:「Text」\n" + \
                  "╠☠➣ " + key + "Myname:「Nama」\n" + \
                  "╠☠➣ " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\n╭━━━━━━━━━━━━━━╮\n		──┅━✥ ======= ✥━┅──\n╠☬➣	􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\n		──┅━✥ ======= ✥━┅──\n╰━━━━━━━━━━━━━━╯\n●▬▬▬▬ஜ۩ ⚔♠️⚔ ۩ஜ▬▬▬▬●\nCreator:\nhttps://line.me/ti/p/Dr8B9wDicC\n"
    return helpMessage4

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
                    if bima.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            bima.reissueGroupTicket(op.param1)
                            X = bima.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            bima.updateGroup(X)
                            bima.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass
                    
        if op.type == 11:
            if op.param1 in protectqr:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 == '1':
                        try:
                            G = bima.getGroup(op.param1)
                            G.name = wait['pro_name'][op.param1]
                            bima.updateGroup(G)
                            bima.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        bima.kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        bima.acceptGroupInvitation(op.param1)
                        ginfo = bima.getGroup(op.param1)                        
                    else:
                        bima.acceptGroupInvitation(op.param1)
                        ginfo = bima.getGroup(op.param1)                        
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b1.acceptGroupInvitation(op.param1)
                        ginfo = b1.getGroup(op.param1)                        
                    else:
                        b1.acceptGroupInvitation(op.param1)
                        ginfo = b1.getGroup(op.param1)                        
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b2.acceptGroupInvitation(op.param1)
                        ginfo = b2.getGroup(op.param1)                        
                    else:
                        b2.acceptGroupInvitation(op.param1)
                        ginfo = b2.getGroup(op.param1)                        
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b3.acceptGroupInvitation(op.param1)
                        ginfo = b3.getGroup(op.param1)                        
                    else:
                        b3.acceptGroupInvitation(op.param1)
                        ginfo = b3.getGroup(op.param1)                        
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b4.acceptGroupInvitation(op.param1)
                        ginfo = b4.getGroup(op.param1)                        
                    else:
                        b4.acceptGroupInvitation(op.param1)
                        ginfo = b4.getGroup(op.param1)                        
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b5.acceptGroupInvitation(op.param1)
                        ginfo = b5.getGroup(op.param1)                        
                    else:
                        b5.acceptGroupInvitation(op.param1)
                        ginfo = b5.getGroup(op.param1)
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b6.acceptGroupInvitation(op.param1)
                        ginfo = b6.getGroup(op.param1)                        
                    else:
                        b6.acceptGroupInvitation(op.param1)
                        ginfo = b6.getGroup(op.param1)                        
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b7.acceptGroupInvitation(op.param1)
                        ginfo = b7.getGroup(op.param1)                        
                    else:
                        b7.acceptGroupInvitation(op.param1)
                        ginfo = b7.getGroup(op.param1)                        
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b8.acceptGroupInvitation(op.param1)
                        ginfo = b8.getGroup(op.param1)                        
                    else:
                        b8.acceptGroupInvitation(op.param1)
                        ginfo = b8.getGroup(op.param1)                        
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b9.acceptGroupInvitation(op.param1)
                        ginfo = b9.getGroup(op.param1)                        
                    else:
                        b9.acceptGroupInvitation(op.param1)
                        ginfo = b9.getGroup(op.param1)                        
            if Qmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        bima1.acceptGroupInvitation(op.param1)
                        ginfo = bima1.getGroup(op.param1)                        
                    else:
                        bima1.acceptGroupInvitation(op.param1)
                        ginfo = bima1.getGroup(op.param1)                                  
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        bima.acceptGroupInvitation(op.param1)
                        ginfo = bima.getGroup(op.param1)
                        bima.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        bima.leaveGroup(op.param1)
                    else:
                        bima.acceptGroupInvitation(op.param1)
                        ginfo = bima.getGroup(op.param1)
                        bima.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b1.acceptGroupInvitation(op.param1)
                        ginfo = b1.getGroup(op.param1)
                        b1.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        b1.leaveGroup(op.param1)
                    else:
                        b1.acceptGroupInvitation(op.param1)
                        ginfo = b1.getGroup(op.param1)
                        b1.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b2.acceptGroupInvitation(op.param1)
                        ginfo = b2.getGroup(op.param1)
                        b2.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        b2.leaveGroup(op.param1)
                    else:
                        b2.acceptGroupInvitation(op.param1)
                        ginfo = b2.getGroup(op.param1)
                        b2.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b3.acceptGroupInvitation(op.param1)
                        ginfo = b3.getGroup(op.param1)
                        b3.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        b3.leaveGroup(op.param1)
                    else:
                        b3.acceptGroupInvitation(op.param1)
                        ginfo = b3.getGroup(op.param1)
                        b3.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Dmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b4.acceptGroupInvitation(op.param1)
                        ginfo = b4.getGroup(op.param1)
                        b4.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        b4.leaveGroup(op.param1)
                    else:
                        b4.acceptGroupInvitation(op.param1)
                        ginfo = b4.getGroup(op.param1)
                        b4.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Emid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b5.acceptGroupInvitation(op.param1)
                        ginfo = b5.getGroup(op.param1)
                        b5.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        b5.leaveGroup(op.param1)
                    else:
                        b5.acceptGroupInvitation(op.param1)
                        ginfo = b5.getGroup(op.param1)
                        b5.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Fmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b6.acceptGroupInvitation(op.param1)
                        ginfo = b6.getGroup(op.param1)
                        b6.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        b6.leaveGroup(op.param1)
                    else:
                        b6.acceptGroupInvitation(op.param1)
                        ginfo = b6.getGroup(op.param1)
                        b6.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Gmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b7.acceptGroupInvitation(op.param1)
                        ginfo = b7.getGroup(op.param1)
                        b7.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        b7.leaveGroup(op.param1)
                    else:
                        b7.acceptGroupInvitation(op.param1)
                        ginfo = b7.getGroup(op.param1)
                        b7.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Hmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b8.acceptGroupInvitation(op.param1)
                        ginfo = b8.getGroup(op.param1)
                        b8.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        b8.leaveGroup(op.param1)
                    else:
                        b8.acceptGroupInvitation(op.param1)
                        ginfo = b8.getGroup(op.param1)
                        b8.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Imid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        b9.acceptGroupInvitation(op.param1)
                        ginfo = b9.getGroup(op.param1)
                        b9.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        b9.leaveGroup(op.param1)
                    else:
                        b9.acceptGroupInvitation(op.param1)
                        ginfo = b9.getGroup(op.param1)
                        b9.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Zmid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        bima1.acceptGroupInvitation(op.param1)
                        ginfo = bima1.getGroup(op.param1)
                        bima1.sendMessage(op.param1,"Maaf Anda Bukan Admin Bot 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴/nSelamat Tinggal\n Group " +str(ginfo.name))
                        bima1.leaveGroup(op.param1)
                    else:
                        bima1.acceptGroupInvitation(op.param1)
                        ginfo = bima1.getGroup(op.param1)
                        bima1.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = bima1.getGroup(op.param1)
                contact = bima1.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                bima1.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	b1.kickoutFromGroup(op.param1,[op.param2])
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
                        bima.sendText(op.param1, wait["message"])

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = bima.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            b1.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        pass
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
                        bima.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            b1.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                b2.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    b3.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                    	b4.cancleGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                        	b5.cancleGroupInvitation(op.param1,[op.param2])
                                        except:
                                            try:
                                                b6.cancleGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    b7.cancleGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        b8.cancleGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            b9.cancleGroupInvitation(op.param1,[op.param2])
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
                        bima.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            b1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                b2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    b3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                    	b4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                        	b5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                b6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    b7.kickoutFromGroup(op.param1,[op.param2])
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
                        bima.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            b1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                b2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    b3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                    	b4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                        	b5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                b6.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    b7.kickoutFromGroup(op.param1,[op.param2])
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
                            bima2.acceptGroupInvitation(op.param1)
  #                          sw2.acceptGroupInvitation(op.param1)
                            bima2.inviteIntoGroup(op.param1,[op.param3])
                            bima2.kickoutFromGroup(op.param1,[op.param2])  
#                            sw2.kickoutFromGroup(op.param1,[op.param2])                      
#                            sw2.inviteIntoGroup(op.param1,[op.param3])
                            bima.acceptGroupInvitationByTicket(op.param1)
                    	except:
                          try:
                                G = bima2.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                bima2.updateGroup(G)
                                Ticket = bima2.reissueGroupTicket(op.param1)
    #                    Ticket = ki.reissueGroupTicket(op.param1)
                                bima.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                bb.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                cc.acceptGroupInvitationByTicket(op.param1,Ticket)
#                                dd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                bima2.kickoutFromGroup(op.param1,[op.param2])
                                bima2.leaveGroup(op.param1)
   #                             sw2.leaveGroup(op.param1)
                                X = bima.getGroup(op.param1)
                                X.preventeJoinByTicket = True
                                bima.updateGroup(X)
                                ginfo = bima.getGroup(msg.to)
 #                               cl.inviteIntoGroup(msg.to, [Ymid])
                                bima.inviteIntoGroup(msg.to, [Zmid])
                                contact = bima.getContact(msg._from)
                                Ticket = bima2.reissueGroupTicket(op.param1)
                          except:
                              try:
                              	bima2.inviteIntoGroup(op.param1,[op.param3])
#                              	sw1.inviteIntoGroup(op.param1,[op.param3])
                              	bima.acceptGroupInvitation(op.param1)
                              	bima2.kickoutFromGroup(op.param1,[op.param2])
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
                        bima.kickoutFromGroup(op.param1,[op.param2])
                        bima.findAndAddContactsByMid(op.param3)
                        bima.inviteIntoGroup(op.param1,[Zmid])
                        bima.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        bima.kickoutFromGroup(op.param1,[op.param2])
                        bima.findAndAddContactsByMid(op.param3)
                        bima.inviteIntoGroup(op.param1,[Zmid])
                        bima.sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            bima.kickoutFromGroup(op.param1,[op.param2])
                            bima.findAndAddContactsByMid(op.param3)
                            bima.inviteIntoGroup(op.param1,[op.param3])
                            bima.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass
        
#===================

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            b1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass                
                return

        if op.type == 19:
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
                        b1.inviteIntoGroup(op.param1,[mid])
                        b1.kickoutFromGroup(op.param1,[op.param2])
                        b2.cancelGroupInvitation(op.param1,[op.param2])                                                
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            b2.inviteIntoGroup(op.param1,[mid])                            
                            b2.kickoutFromGroup(op.param1,[op.param2])
                            b3.cancelGroupInvitation(op.param1,[op.param2])                            
                            wait["blacklist"][op.param2] = True
                        except:
                            try:                                
                                b3.inviteIntoGroup(op.param1,[mid])
                                b3.kickoutFromGroup(op.param1,[op.param2])
                                b4.cancelGroupInvitation(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                            except:
                                try:                                    
                                    b4.inviteIntoGroup(op.param1,[mid])
                                    b4.kickoutFromGroup(op.param1,[op.param2])
                                    b5.cancelGroupInvitation(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        b5.inviteIntoGroup(op.param1,[mid])
                                        b5.kickoutFromGroup(op.param1,[op.param2])
                                        b6.cancelGroupInvitation(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            b6.inviteIntoGroup(op.param1,[mid])
                                            b6.kickoutFromGroup(op.param1,[op.param2])
                                            b7.cancelGroupInvitation(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            try:
                                                b7.inviteIntoGroup(op.param1,[mid])
                                                b7.kickoutFromGroup(op.param1,[op.param2])
                                                b8.cancelGroupInvitation(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True
                                            except:
                                                try:
                                                    b8.inviteIntoGroup(op.param1,[mid])
                                                    b8.kickoutFromGroup(op.param1,[op.param2])
                                                    b9.cancelGroupInvitation(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True
                                                except:
                                                    try:
                                                        b9.inviteIntoGroup(op.param1,[mid])
                                                        b9.kickoutFromGroup(op.param1,[op.param2])
                                                        b1.cancelGroupInvitation(op.param1,[op.param2])
                                                        wait["blacklist"][op.param2] = True
                                                    except:
                                                        try:
                                                            G = b1.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            b1.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = b1.reissueGroupTicket(op.param1)
                                                            b1.kickoutFromGroup(op.param1,[op.param2])
                                                            bima.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = b9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            b9.updateGroup(G)
                                                            ginfo = b9.getGroup(op.param1)
                                                            wait["blacklist"][op.param2] = True
                                                        except:
                                                            try:
                                                                G = b2.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                b2.updateGroup(G)
                                                                invsend = 0
                                                                Ticket = b2.reissueGroupTicket(op.param1)
                                                                b2.kickoutFromGroup(op.param1,[op.param2])
                                                                bima.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                G = b9.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                b9.updateGroup(G)
                                                                ginfo = b9.getGroup(op.param1)
                                                                wait["blacklist"][op.param2] = True
                                                            except:
                                                                try:
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    bima1.updateGroup(G)
                                                                    invsend = 0
                                                                    Ticket = bima1.reissueGroupTicket(op.param1)                                                                    
                                                                    b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b1.kickoutFromGroup(op.param1,[op.param2])                        
                                                                    bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b3.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b9.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                    
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = True
                                                                    bima1.updateGroup(G)
                                                                    ginfo = bima1.getGroup(op.param1)
                                                                    wait["blacklist"][op.param2] = True
                                                                except:
                                                                    pass
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
                        b2.inviteIntoGroup(op.param1,[Amid])
                        b2.kickoutFromGroup(op.param1,[op.param2])
                        b3.cancelGroupInvitation(op.param1,[op.param2])                                                
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            b3.inviteIntoGroup(op.param1,[Amid])                            
                            b3.kickoutFromGroup(op.param1,[op.param2])
                            b4.cancelGroupInvitation(op.param1,[op.param2])                            
                            wait["blacklist"][op.param2] = True
                        except:
                            try:                                
                                b4.inviteIntoGroup(op.param1,[Amid])
                                b4.kickoutFromGroup(op.param1,[op.param2])
                                b5.cancelGroupInvitation(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                            except:
                                try:                                    
                                    b5.inviteIntoGroup(op.param1,[Amid])
                                    b5.kickoutFromGroup(op.param1,[op.param2])
                                    b6.cancelGroupInvitation(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        b6.inviteIntoGroup(op.param1,[Amid])
                                        b6.kickoutFromGroup(op.param1,[op.param2])
                                        b7.cancelGroupInvitation(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            b7.inviteIntoGroup(op.param1,[Amid])
                                            b7.kickoutFromGroup(op.param1,[op.param2])
                                            b8.cancelGroupInvitation(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            try:
                                                b8.inviteIntoGroup(op.param1,[Amid])
                                                b8.kickoutFromGroup(op.param1,[op.param2])
                                                b9.cancelGroupInvitation(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True
                                            except:
                                                try:
                                                    b9.inviteIntoGroup(op.param1,[Amid])
                                                    b9.kickoutFromGroup(op.param1,[op.param2])
                                                    bima.cancelGroupInvitation(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True
                                                except:
                                                    try:
                                                        bima.inviteIntoGroup(op.param1,[Amid])
                                                        bima.kickoutFromGroup(op.param1,[op.param2])
                                                        b2.cancelGroupInvitation(op.param1,[op.param2])
                                                        wait["blacklist"][op.param2] = True
                                                    except:
                                                        try:
                                                            G = b2.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            b2.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = b2.reissueGroupTicket(op.param1)
                                                            b2.kickoutFromGroup(op.param1,[op.param2])
                                                            b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = b9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            b9.updateGroup(G)
                                                            ginfo = b9.getGroup(op.param1)
                                                            wait["blacklist"][op.param2] = True
                                                        except:
                                                            try:
                                                                G = b3.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                b3.updateGroup(G)
                                                                invsend = 0
                                                                Ticket = b3.reissueGroupTicket(op.param1)
                                                                b3.kickoutFromGroup(op.param1,[op.param2])
                                                                b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                G = b9.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                b9.updateGroup(G)
                                                                ginfo = b9.getGroup(op.param1)
                                                                wait["blacklist"][op.param2] = True
                                                            except:
                                                                try:
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    bima1.updateGroup(G)
                                                                    invsend = 0
                                                                    Ticket = bima1.reissueGroupTicket(op.param1)                                                                    
                                                                    b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b2.kickoutFromGroup(op.param1,[op.param2])                        
                                                                    b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b3.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b9.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                    
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = True
                                                                    bima1.updateGroup(G)
                                                                    ginfo = bima1.getGroup(op.param1)
                                                                    wait["blacklist"][op.param2] = True
                                                                except:
                                                                    pass
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
                        b3.inviteIntoGroup(op.param1,[Bmid])
                        b3.kickoutFromGroup(op.param1,[op.param2])
                        b4.cancelGroupInvitation(op.param1,[op.param2])                                                
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            b4.inviteIntoGroup(op.param1,[Bmid])                            
                            b4.kickoutFromGroup(op.param1,[op.param2])
                            b5.cancelGroupInvitation(op.param1,[op.param2])                            
                            wait["blacklist"][op.param2] = True
                        except:
                            try:                                
                                b5.inviteIntoGroup(op.param1,[Bmid])
                                b5.kickoutFromGroup(op.param1,[op.param2])
                                b6.cancelGroupInvitation(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                            except:
                                try:                                    
                                    b6.inviteIntoGroup(op.param1,[Bmid])
                                    b6.kickoutFromGroup(op.param1,[op.param2])
                                    b7.cancelGroupInvitation(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        b7.inviteIntoGroup(op.param1,[Bmid])
                                        b7.kickoutFromGroup(op.param1,[op.param2])
                                        b8.cancelGroupInvitation(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            b8.inviteIntoGroup(op.param1,[Bmid])
                                            b8.kickoutFromGroup(op.param1,[op.param2])
                                            b9.cancelGroupInvitation(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            try:
                                                b9.inviteIntoGroup(op.param1,[Bmid])
                                                b9.kickoutFromGroup(op.param1,[op.param2])
                                                bima.cancelGroupInvitation(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True
                                            except:
                                                try:
                                                    bima.inviteIntoGroup(op.param1,[Bmid])
                                                    bima.kickoutFromGroup(op.param1,[op.param2])
                                                    b1.cancelGroupInvitation(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True
                                                except:
                                                    try:
                                                        b1.inviteIntoGroup(op.param1,[Bmid])
                                                        b1.kickoutFromGroup(op.param1,[op.param2])
                                                        b3.cancelGroupInvitation(op.param1,[op.param2])
                                                        wait["blacklist"][op.param2] = True
                                                    except:
                                                        try:
                                                            G = b3.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            b3.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = b3.reissueGroupTicket(op.param1)
                                                            b3.kickoutFromGroup(op.param1,[op.param2])
                                                            b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = b9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            b9.updateGroup(G)
                                                            ginfo = b9.getGroup(op.param1)
                                                            wait["blacklist"][op.param2] = True
                                                        except:
                                                            try:
                                                                G = b4.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                b4.updateGroup(G)
                                                                invsend = 0
                                                                Ticket = b4.reissueGroupTicket(op.param1)
                                                                b4.kickoutFromGroup(op.param1,[op.param2])
                                                                b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b3.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                G = b9.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                b9.updateGroup(G)
                                                                ginfo = b9.getGroup(op.param1)
                                                                wait["blacklist"][op.param2] = True
                                                            except:
                                                                try:
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    bima1.updateGroup(G)
                                                                    invsend = 0
                                                                    Ticket = bima1.reissueGroupTicket(op.param1)                                                                    
                                                                    b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b3.kickoutFromGroup(op.param1,[op.param2])                        
                                                                    b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b9.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                    
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = True
                                                                    bima1.updateGroup(G)
                                                                    ginfo = bima1.getGroup(op.param1)
                                                                    wait["blacklist"][op.param2] = True
                                                                except:
                                                                    pass
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
                        b4.inviteIntoGroup(op.param1,[Cmid])
                        b4.kickoutFromGroup(op.param1,[op.param2])
                        b5.cancelGroupInvitation(op.param1,[op.param2])                                                
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            b5.inviteIntoGroup(op.param1,[Cmid])                            
                            b5.kickoutFromGroup(op.param1,[op.param2])
                            b6.cancelGroupInvitation(op.param1,[op.param2])                            
                            wait["blacklist"][op.param2] = True
                        except:
                            try:                                
                                b6.inviteIntoGroup(op.param1,[Cmid])
                                b6.kickoutFromGroup(op.param1,[op.param2])
                                b7.cancelGroupInvitation(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                            except:
                                try:                                    
                                    b7.inviteIntoGroup(op.param1,[Cmid])
                                    b7.kickoutFromGroup(op.param1,[op.param2])
                                    b8.cancelGroupInvitation(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        b8.inviteIntoGroup(op.param1,[Cmid])
                                        b8.kickoutFromGroup(op.param1,[op.param2])
                                        b9.cancelGroupInvitation(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            b9.inviteIntoGroup(op.param1,[Cmid])
                                            b9.kickoutFromGroup(op.param1,[op.param2])
                                            bima.cancelGroupInvitation(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            try:
                                                bima.inviteIntoGroup(op.param1,[Cmid])
                                                bima.kickoutFromGroup(op.param1,[op.param2])
                                                b1.cancelGroupInvitation(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True
                                            except:
                                                try:
                                                    b1.inviteIntoGroup(op.param1,[Cmid])
                                                    b1.kickoutFromGroup(op.param1,[op.param2])
                                                    b2.cancelGroupInvitation(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True
                                                except:
                                                    try:
                                                        b2.inviteIntoGroup(op.param1,[Cmid])
                                                        b2.kickoutFromGroup(op.param1,[op.param2])
                                                        b4.cancelGroupInvitation(op.param1,[op.param2])
                                                        wait["blacklist"][op.param2] = True
                                                    except:
                                                        try:
                                                            G = b4.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            b4.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = b4.reissueGroupTicket(op.param1)
                                                            b4.kickoutFromGroup(op.param1,[op.param2])
                                                            b3.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = b9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            b9.updateGroup(G)
                                                            ginfo = b9.getGroup(op.param1)
                                                            wait["blacklist"][op.param2] = True
                                                        except:
                                                            try:
                                                                G = b5.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                b5.updateGroup(G)
                                                                invsend = 0
                                                                Ticket = b5.reissueGroupTicket(op.param1)
                                                                b5.kickoutFromGroup(op.param1,[op.param2])
                                                                b3.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                G = b9.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                b9.updateGroup(G)
                                                                ginfo = b9.getGroup(op.param1)
                                                                wait["blacklist"][op.param2] = True
                                                            except:
                                                                try:
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    bima1.updateGroup(G)
                                                                    invsend = 0
                                                                    Ticket = bima1.reissueGroupTicket(op.param1)                                                                    
                                                                    b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b4.kickoutFromGroup(op.param1,[op.param2])                        
                                                                    b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b9.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                    
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = True
                                                                    bima1.updateGroup(G)
                                                                    ginfo = bima1.getGroup(op.param1)
                                                                    wait["blacklist"][op.param2] = True
                                                                except:
                                                                    pass
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
                        b5.inviteIntoGroup(op.param1,[Dmid])
                        b5.kickoutFromGroup(op.param1,[op.param2])
                        b6.cancelGroupInvitation(op.param1,[op.param2])                                                
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            b6.inviteIntoGroup(op.param1,[Dmid])                            
                            b6.kickoutFromGroup(op.param1,[op.param2])
                            b7.cancelGroupInvitation(op.param1,[op.param2])                            
                            wait["blacklist"][op.param2] = True
                        except:
                            try:                                
                                b7.inviteIntoGroup(op.param1,[Dmid])
                                b7.kickoutFromGroup(op.param1,[op.param2])
                                b8.cancelGroupInvitation(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                            except:
                                try:                                    
                                    b8.inviteIntoGroup(op.param1,[Dmid])
                                    b8.kickoutFromGroup(op.param1,[op.param2])
                                    b9.cancelGroupInvitation(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        b9.inviteIntoGroup(op.param1,[Dmid])
                                        b9.kickoutFromGroup(op.param1,[op.param2])
                                        bima.cancelGroupInvitation(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            bima.inviteIntoGroup(op.param1,[Dmid])
                                            bima.kickoutFromGroup(op.param1,[op.param2])
                                            b1.cancelGroupInvitation(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            try:
                                                b1.inviteIntoGroup(op.param1,[Dmid])
                                                b1.kickoutFromGroup(op.param1,[op.param2])
                                                b2.cancelGroupInvitation(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True
                                            except:
                                                try:
                                                    b2.inviteIntoGroup(op.param1,[Dmid])
                                                    b2.kickoutFromGroup(op.param1,[op.param2])
                                                    b3.cancelGroupInvitation(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True
                                                except:
                                                    try:
                                                        b3.inviteIntoGroup(op.param1,[Dmid])
                                                        b3.kickoutFromGroup(op.param1,[op.param2])
                                                        b5.cancelGroupInvitation(op.param1,[op.param2])
                                                        wait["blacklist"][op.param2] = True
                                                    except:
                                                        try:
                                                            G = b5.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            b5.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = b5.reissueGroupTicket(op.param1)
                                                            b5.kickoutFromGroup(op.param1,[op.param2])
                                                            b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = b9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            b9.updateGroup(G)
                                                            ginfo = b9.getGroup(op.param1)
                                                            wait["blacklist"][op.param2] = True
                                                        except:
                                                            try:
                                                                G = b6.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                b6.updateGroup(G)
                                                                invsend = 0
                                                                Ticket = b6.reissueGroupTicket(op.param1)
                                                                b6.kickoutFromGroup(op.param1,[op.param2])
                                                                b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                G = b9.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                b9.updateGroup(G)
                                                                ginfo = b9.getGroup(op.param1)
                                                                wait["blacklist"][op.param2] = True
                                                            except:
                                                                try:
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    bima1.updateGroup(G)
                                                                    invsend = 0
                                                                    Ticket = bima1.reissueGroupTicket(op.param1)                                                                    
                                                                    b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b5.kickoutFromGroup(op.param1,[op.param2])                        
                                                                    b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b9.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                    
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = True
                                                                    bima1.updateGroup(G)
                                                                    ginfo = bima1.getGroup(op.param1)
                                                                    wait["blacklist"][op.param2] = True
                                                                except:
                                                                    pass
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
                        b6.inviteIntoGroup(op.param1,[Emid])
                        b6.kickoutFromGroup(op.param1,[op.param2])
                        b7.cancelGroupInvitation(op.param1,[op.param2])                                                
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            b7.inviteIntoGroup(op.param1,[Emid])                            
                            b7.kickoutFromGroup(op.param1,[op.param2])
                            b8.cancelGroupInvitation(op.param1,[op.param2])                            
                            wait["blacklist"][op.param2] = True
                        except:
                            try:                                
                                b8.inviteIntoGroup(op.param1,[Emid])
                                b8.kickoutFromGroup(op.param1,[op.param2])
                                b9.cancelGroupInvitation(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                            except:
                                try:                                    
                                    b9.inviteIntoGroup(op.param1,[Emid])
                                    b9.kickoutFromGroup(op.param1,[op.param2])
                                    bima.cancelGroupInvitation(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        bima.inviteIntoGroup(op.param1,[Emid])
                                        bima.kickoutFromGroup(op.param1,[op.param2])
                                        b1.cancelGroupInvitation(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            b1.inviteIntoGroup(op.param1,[Emid])
                                            b1.kickoutFromGroup(op.param1,[op.param2])
                                            b2.cancelGroupInvitation(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            try:
                                                b2.inviteIntoGroup(op.param1,[Emid])
                                                b2.kickoutFromGroup(op.param1,[op.param2])
                                                b3.cancelGroupInvitation(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True
                                            except:
                                                try:
                                                    b3.inviteIntoGroup(op.param1,[Emid])
                                                    b3.kickoutFromGroup(op.param1,[op.param2])
                                                    b4.cancelGroupInvitation(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True
                                                except:
                                                    try:
                                                        b4.inviteIntoGroup(op.param1,[Emid])
                                                        b4.kickoutFromGroup(op.param1,[op.param2])
                                                        b6.cancelGroupInvitation(op.param1,[op.param2])
                                                        wait["blacklist"][op.param2] = True
                                                    except:
                                                        try:
                                                            G = b6.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            b6.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = b6.reissueGroupTicket(op.param1)
                                                            b6.kickoutFromGroup(op.param1,[op.param2])
                                                            b5.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = b9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            b9.updateGroup(G)
                                                            ginfo = b9.getGroup(op.param1)
                                                            wait["blacklist"][op.param2] = True
                                                        except:
                                                            try:
                                                                G = b7.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                b7.updateGroup(G)
                                                                invsend = 0
                                                                Ticket = b7.reissueGroupTicket(op.param1)
                                                                b7.kickoutFromGroup(op.param1,[op.param2])
                                                                b5.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                G = b9.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                b9.updateGroup(G)
                                                                ginfo = b9.getGroup(op.param1)
                                                                wait["blacklist"][op.param2] = True
                                                            except:
                                                                try:
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    bima1.updateGroup(G)
                                                                    invsend = 0
                                                                    Ticket = bima1.reissueGroupTicket(op.param1)                                                                    
                                                                    b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b6.kickoutFromGroup(op.param1,[op.param2])                        
                                                                    b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b9.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                    
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = True
                                                                    bima1.updateGroup(G)
                                                                    ginfo = bima1.getGroup(op.param1)
                                                                    wait["blacklist"][op.param2] = True
                                                                except:
                                                                    pass
            if Fmid in op.param3:
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
                        b7.inviteIntoGroup(op.param1,[Fmid])
                        b7.kickoutFromGroup(op.param1,[op.param2])
                        b8.cancelGroupInvitation(op.param1,[op.param2])                                                
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            b8.inviteIntoGroup(op.param1,[Fmid])                            
                            b8.kickoutFromGroup(op.param1,[op.param2])
                            b9.cancelGroupInvitation(op.param1,[op.param2])                            
                            wait["blacklist"][op.param2] = True
                        except:
                            try:                                
                                b9.inviteIntoGroup(op.param1,[Fmid])
                                b9.kickoutFromGroup(op.param1,[op.param2])
                                bima.cancelGroupInvitation(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                            except:
                                try:                                    
                                    bima.inviteIntoGroup(op.param1,[Fmid])
                                    bima.kickoutFromGroup(op.param1,[op.param2])
                                    b1.cancelGroupInvitation(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        b1.inviteIntoGroup(op.param1,[Fmid])
                                        b1.kickoutFromGroup(op.param1,[op.param2])
                                        b2.cancelGroupInvitation(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            b2.inviteIntoGroup(op.param1,[Fmid])
                                            b2.kickoutFromGroup(op.param1,[op.param2])
                                            b3.cancelGroupInvitation(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            try:
                                                b3.inviteIntoGroup(op.param1,[Fmid])
                                                b3.kickoutFromGroup(op.param1,[op.param2])
                                                b4.cancelGroupInvitation(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True
                                            except:
                                                try:
                                                    b4.inviteIntoGroup(op.param1,[Fmid])
                                                    b4.kickoutFromGroup(op.param1,[op.param2])
                                                    b5.cancelGroupInvitation(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True
                                                except:
                                                    try:
                                                        b5.inviteIntoGroup(op.param1,[Fmid])
                                                        b5.kickoutFromGroup(op.param1,[op.param2])
                                                        b7.cancelGroupInvitation(op.param1,[op.param2])
                                                        wait["blacklist"][op.param2] = True
                                                    except:
                                                        try:
                                                            G = b7.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            b7.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = b7.reissueGroupTicket(op.param1)
                                                            b7.kickoutFromGroup(op.param1,[op.param2])
                                                            b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b5.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = b9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            b9.updateGroup(G)
                                                            ginfo = b9.getGroup(op.param1)
                                                            wait["blacklist"][op.param2] = True
                                                        except:
                                                            try:
                                                                G = b8.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                b8.updateGroup(G)
                                                                invsend = 0
                                                                Ticket = b8.reissueGroupTicket(op.param1)
                                                                b8.kickoutFromGroup(op.param1,[op.param2])
                                                                b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b5.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                G = b9.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                b9.updateGroup(G)
                                                                ginfo = b9.getGroup(op.param1)
                                                                wait["blacklist"][op.param2] = True
                                                            except:
                                                                try:
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    bima1.updateGroup(G)
                                                                    invsend = 0
                                                                    Ticket = bima1.reissueGroupTicket(op.param1)                                                                    
                                                                    b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b7.kickoutFromGroup(op.param1,[op.param2])                        
                                                                    b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b9.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                    
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = True
                                                                    bima1.updateGroup(G)
                                                                    ginfo = bima1.getGroup(op.param1)
                                                                    wait["blacklist"][op.param2] = True
                                                                except:
                                                                    pass
            if Gmid in op.param3:
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
                        b8.inviteIntoGroup(op.param1,[Gmid])
                        b8.kickoutFromGroup(op.param1,[op.param2])
                        b9.cancelGroupInvitation(op.param1,[op.param2])                                                
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            b9.inviteIntoGroup(op.param1,[Gmid])                            
                            b9.kickoutFromGroup(op.param1,[op.param2])
                            bima.cancelGroupInvitation(op.param1,[op.param2])                            
                            wait["blacklist"][op.param2] = True
                        except:
                            try:                                
                                bima.inviteIntoGroup(op.param1,[Gmid])
                                bima.kickoutFromGroup(op.param1,[op.param2])
                                b1.cancelGroupInvitation(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                            except:
                                try:                                    
                                    b1.inviteIntoGroup(op.param1,[Gmid])
                                    b1.kickoutFromGroup(op.param1,[op.param2])
                                    b2.cancelGroupInvitation(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        b2.inviteIntoGroup(op.param1,[Gmid])
                                        b2.kickoutFromGroup(op.param1,[op.param2])
                                        b3.cancelGroupInvitation(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            b3.inviteIntoGroup(op.param1,[Gmid])
                                            b3.kickoutFromGroup(op.param1,[op.param2])
                                            b4.cancelGroupInvitation(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            try:
                                                b4.inviteIntoGroup(op.param1,[Gmid])
                                                b4.kickoutFromGroup(op.param1,[op.param2])
                                                b5.cancelGroupInvitation(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True
                                            except:
                                                try:
                                                    b5.inviteIntoGroup(op.param1,[Gmid])
                                                    b5.kickoutFromGroup(op.param1,[op.param2])
                                                    b6.cancelGroupInvitation(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True
                                                except:
                                                    try:
                                                        b6.inviteIntoGroup(op.param1,[Gmid])
                                                        b6.kickoutFromGroup(op.param1,[op.param2])
                                                        b8.cancelGroupInvitation(op.param1,[op.param2])
                                                        wait["blacklist"][op.param2] = True
                                                    except:
                                                        try:
                                                            G = b8.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            b8.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = b8.reissueGroupTicket(op.param1)
                                                            b8.kickoutFromGroup(op.param1,[op.param2])
                                                            b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b5.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = b9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            b9.updateGroup(G)
                                                            ginfo = b9.getGroup(op.param1)
                                                            wait["blacklist"][op.param2] = True
                                                        except:
                                                            try:
                                                                G = b9.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                b9.updateGroup(G)
                                                                invsend = 0
                                                                Ticket = b9.reissueGroupTicket(op.param1)
                                                                b9.kickoutFromGroup(op.param1,[op.param2])
                                                                b7.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b5.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                G = b8.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                b8.updateGroup(G)
                                                                ginfo = b8.getGroup(op.param1)
                                                                wait["blacklist"][op.param2] = True
                                                            except:
                                                                try:
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    bima1.updateGroup(G)
                                                                    invsend = 0
                                                                    Ticket = bima1.reissueGroupTicket(op.param1)                                                                    
                                                                    b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b8.kickoutFromGroup(op.param1,[op.param2])                        
                                                                    b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b9.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                    
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = True
                                                                    bima1.updateGroup(G)
                                                                    ginfo = bima1.getGroup(op.param1)
                                                                    wait["blacklist"][op.param2] = True
                                                                except:
                                                                    pass
            if Hmid in op.param3:
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
                        b9.inviteIntoGroup(op.param1,[Hmid])
                        b9.kickoutFromGroup(op.param1,[op.param2])
                        bima.cancelGroupInvitation(op.param1,[op.param2])                                                
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            bima.inviteIntoGroup(op.param1,[Hmid])                            
                            bima.kickoutFromGroup(op.param1,[op.param2])
                            b1.cancelGroupInvitation(op.param1,[op.param2])                            
                            wait["blacklist"][op.param2] = True
                        except:
                            try:                                
                                b1.inviteIntoGroup(op.param1,[Hmid])
                                b1.kickoutFromGroup(op.param1,[op.param2])
                                b2.cancelGroupInvitation(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                            except:
                                try:                                    
                                    b2.inviteIntoGroup(op.param1,[Hmid])
                                    b2.kickoutFromGroup(op.param1,[op.param2])
                                    b3.cancelGroupInvitation(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        b3.inviteIntoGroup(op.param1,[Hmid])
                                        b3.kickoutFromGroup(op.param1,[op.param2])
                                        b4.cancelGroupInvitation(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            b4.inviteIntoGroup(op.param1,[Hmid])
                                            b4.kickoutFromGroup(op.param1,[op.param2])
                                            b5.cancelGroupInvitation(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            try:
                                                b5.inviteIntoGroup(op.param1,[Hmid])
                                                b5.kickoutFromGroup(op.param1,[op.param2])
                                                b6.cancelGroupInvitation(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True
                                            except:
                                                try:
                                                    b6.inviteIntoGroup(op.param1,[Hmid])
                                                    b6.kickoutFromGroup(op.param1,[op.param2])
                                                    b7.cancelGroupInvitation(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True
                                                except:
                                                    try:
                                                        b7.inviteIntoGroup(op.param1,[Hmid])
                                                        b7.kickoutFromGroup(op.param1,[op.param2])
                                                        b9.cancelGroupInvitation(op.param1,[op.param2])
                                                        wait["blacklist"][op.param2] = True
                                                    except:
                                                        try:
                                                            G = b9.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            b9.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = b9.reissueGroupTicket(op.param1)
                                                            b9.kickoutFromGroup(op.param1,[op.param2])
                                                            b8.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b5.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = b7.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            b7.updateGroup(G)
                                                            ginfo = b7.getGroup(op.param1)
                                                            wait["blacklist"][op.param2] = True
                                                        except:
                                                            try:
                                                                G = bima.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                bima.updateGroup(G)
                                                                invsend = 0
                                                                Ticket = bima.reissueGroupTicket(op.param1)
                                                                bima.kickoutFromGroup(op.param1,[op.param2])
                                                                b8.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b3.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                G = b9.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                b9.updateGroup(G)
                                                                ginfo = b9.getGroup(op.param1)
                                                                wait["blacklist"][op.param2] = True
                                                            except:
                                                                try:
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    bima1.updateGroup(G)
                                                                    invsend = 0
                                                                    Ticket = bima1.reissueGroupTicket(op.param1)                                                                    
                                                                    b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b9.kickoutFromGroup(op.param1,[op.param2])                        
                                                                    b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b7.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                    
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = True
                                                                    bima1.updateGroup(G)
                                                                    ginfo = bima1.getGroup(op.param1)
                                                                    wait["blacklist"][op.param2] = True
                                                                except:
                                                                    pass
            if Imid in op.param3:
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
                        bima.inviteIntoGroup(op.param1,[Imid])
                        bima.kickoutFromGroup(op.param1,[op.param2])
                        b1.cancelGroupInvitation(op.param1,[op.param2])                                                
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            b1.inviteIntoGroup(op.param1,[Imid])                            
                            b1.kickoutFromGroup(op.param1,[op.param2])
                            b2.cancelGroupInvitation(op.param1,[op.param2])                            
                            wait["blacklist"][op.param2] = True
                        except:
                            try:                                
                                b2.inviteIntoGroup(op.param1,[Imid])
                                b2.kickoutFromGroup(op.param1,[op.param2])
                                b3.cancelGroupInvitation(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                            except:
                                try:                                    
                                    b3.inviteIntoGroup(op.param1,[Imid])
                                    b3.kickoutFromGroup(op.param1,[op.param2])
                                    b4.cancelGroupInvitation(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        b4.inviteIntoGroup(op.param1,[Imid])
                                        b4.kickoutFromGroup(op.param1,[op.param2])
                                        b5.cancelGroupInvitation(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            b5.inviteIntoGroup(op.param1,[Imid])
                                            b5.kickoutFromGroup(op.param1,[op.param2])
                                            b6.cancelGroupInvitation(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            try:
                                                b6.inviteIntoGroup(op.param1,[Imid])
                                                b6.kickoutFromGroup(op.param1,[op.param2])
                                                b7.cancelGroupInvitation(op.param1,[op.param2])
                                                wait["blacklist"][op.param2] = True
                                            except:
                                                try:
                                                    b7.inviteIntoGroup(op.param1,[Imid])
                                                    b7.kickoutFromGroup(op.param1,[op.param2])
                                                    b8.cancelGroupInvitation(op.param1,[op.param2])
                                                    wait["blacklist"][op.param2] = True
                                                except:
                                                    try:
                                                        b8.inviteIntoGroup(op.param1,[Imid])
                                                        b8.kickoutFromGroup(op.param1,[op.param2])
                                                        bima.cancelGroupInvitation(op.param1,[op.param2])
                                                        wait["blacklist"][op.param2] = True
                                                    except:
                                                        try:
                                                            G = bima.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            bima.updateGroup(G)
                                                            invsend = 0
                                                            Ticket = bima.reissueGroupTicket(op.param1)
                                                            bima.kickoutFromGroup(op.param1,[op.param2])
                                                            b9.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b3.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                            b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            G = b8.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            b8.updateGroup(G)
                                                            ginfo = b8.getGroup(op.param1)
                                                            wait["blacklist"][op.param2] = True
                                                        except:
                                                            try:
                                                                G = b1.getGroup(op.param1)
                                                                G.preventedJoinByTicket = False
                                                                b1.updateGroup(G)
                                                                invsend = 0
                                                                Ticket = b1.reissueGroupTicket(op.param1)
                                                                b1.kickoutFromGroup(op.param1,[op.param2])
                                                                b9.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b3.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                G = b8.getGroup(op.param1)
                                                                G.preventedJoinByTicket = True
                                                                b8.updateGroup(G)
                                                                ginfo = b8.getGroup(op.param1)
                                                                wait["blacklist"][op.param2] = True
                                                            except:
                                                                try:
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    bima1.updateGroup(G)
                                                                    invsend = 0
                                                                    Ticket = bima1.reissueGroupTicket(op.param1)                                                                    
                                                                    bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    bima.kickoutFromGroup(op.param1,[op.param2])                        
                                                                    b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b5.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                                                                    b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    b8.acceptGroupInvitationByTicket(op.param1,Ticket)                                                                    
                                                                    G = bima1.getGroup(op.param1)
                                                                    G.preventedJoinByTicket = True
                                                                    bima1.updateGroup(G)
                                                                    ginfo = bima1.getGroup(op.param1)
                                                                    wait["blacklist"][op.param2] = True
                                                                except:
                                                                    pass
            if Qmid in op.param3:
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
                        bima2.acceptGroupInvitation(op.param1)
                        G = bima2.getGroup(op.param1)
                        G = bima2.getGroup(op.param1)
                        bima2.updateGroup(G)
                        invsend = 0
                        Ticket = bima2.reissueGroupTicket(op.param1)
                        bima3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        bima4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        bima3.kickoutFromGroup(op.param1,[op.param2])
                        bima4.kickoutFromGroup(op.param1,[op.param2])
                        bima3.leaveGroup(op.param1)
                        bima4.leaveGroup(op.param1)                        
                        bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                        bima1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b9.acceptGroupInvitationByTicket(op.param1,Ticket)                                                            
                        X = bima2.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        bima2.updateGroup(X)
                        bima2.leaveGroup(op.param1)
                        bima1.inviteIntoGroup(op.param1,[Zmid])                                                            
                        wait["blacklist"][op.param2] = True
                    except:
                        pass            
                return

        if op.type == 13 or op.type == 17 or op.type == 55:
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
                        bima.cancelGroupInvitation(op.param1,[op.param2])
                        bima.kickoutFromGroup(op.param1,[op.param2])                        
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            b1.cancelGroupInvitation(op.param1,[op.param2])
                            b1.kickoutFromGroup(op.param1,[op.param2])                            
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                b2.cancelGroupInvitation(op.param1,[op.param2])
                                b2.kickoutFromGroup(op.param1,[op.param2])                                
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    b3.cancelGroupInvitation(op.param1,[op.param2])
                                    b3.kickoutFromGroup(op.param1,[op.param2])                                    
                                    wait["blacklist"][op.param2] = True
                                except:
                                    pass
                return

        if op.type == 32:
            if mid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bima1.updateGroup(G)
                        invsend = 0
                        Ticket = bima1.reissueGroupTicket(op.param1)                        
                        b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b2.kickoutFromGroup(op.param1,[op.param2])                        
                        bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b3.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        bima1.updateGroup(G)
                        ginfo = bima1.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
            if Amid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bima1.updateGroup(G)
                        invsend = 0
                        Ticket = bima1.reissueGroupTicket(op.param1)                        
                        b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b3.kickoutFromGroup(op.param1,[op.param2])                        
                        b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        bima1.updateGroup(G)
                        ginfo = bima1.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
            if Bmid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bima1.updateGroup(G)
                        invsend = 0
                        Ticket = bima1.reissueGroupTicket(op.param1)                        
                        b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b4.kickoutFromGroup(op.param1,[op.param2])                        
                        b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        bima1.updateGroup(G)
                        ginfo = bima1.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
            if Cmid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bima1.updateGroup(G)
                        invsend = 0
                        Ticket = bima1.reissueGroupTicket(op.param1)                        
                        b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b5.kickoutFromGroup(op.param1,[op.param2])                        
                        b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b6.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        bima1.updateGroup(G)
                        ginfo = bima1.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
            if Dmid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bima1.updateGroup(G)
                        invsend = 0
                        Ticket = bima1.reissueGroupTicket(op.param1)                        
                        b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b6.kickoutFromGroup(op.param1,[op.param2])                        
                        b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b5.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        bima1.updateGroup(G)
                        ginfo = bima1.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
            if Emid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bima1.updateGroup(G)
                        invsend = 0
                        Ticket = bima1.reissueGroupTicket(op.param1)                        
                        b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b7.kickoutFromGroup(op.param1,[op.param2])                        
                        b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        bima1.updateGroup(G)
                        ginfo = bima1.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
            if Fmid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bima1.updateGroup(G)
                        invsend = 0
                        Ticket = bima1.reissueGroupTicket(op.param1)                        
                        b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b8.kickoutFromGroup(op.param1,[op.param2])                        
                        b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        bima1.updateGroup(G)
                        ginfo = bima1.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
            if Gmid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bima1.updateGroup(G)
                        invsend = 0
                        Ticket = bima1.reissueGroupTicket(op.param1)                        
                        b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b9.kickoutFromGroup(op.param1,[op.param2])                        
                        b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        bima1.updateGroup(G)
                        ginfo = bima1.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
            if Hmid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bima1.updateGroup(G)
                        invsend = 0
                        Ticket = bima1.reissueGroupTicket(op.param1)                        
                        bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                        bima.kickoutFromGroup(op.param1,[op.param2])                        
                        b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b1.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b4.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        bima1.updateGroup(G)
                        ginfo = bima1.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
            if Imid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bima1.updateGroup(G)
                        invsend = 0
                        Ticket = bima1.reissueGroupTicket(op.param1)                        
                        b1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b1.kickoutFromGroup(op.param1,[op.param2])                        
                        b9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        bima.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b2.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b5.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        b6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        b8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = bima1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        bima1.updateGroup(G)
                        ginfo = bima1.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        pass
            if Zmid in op.param3:
                if op.param2 in Bima:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        bima.inviteIntoGroup(op.param1,[Zmid])
                        bima.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            b1.inviteIntoGroup(op.param1,[Zmid])
                            b1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                b2.inviteIntoGroup(op.param1,[Zmid])
                                b2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    b3.inviteIntoGroup(op.param1,[Zmid])
                                    b3.kickoutFromGroup(op.param1,[op.param2])
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
               	bima.cancelGroupInvitation(op.param1,[op.param2])
               	bima.kickoutFromGroup(op.param1,[op.param2])
               except:
                   try:
                   	b1.cancelGroupInvitation(op.param1,[op.param2])
                   	b1.kickoutFromGroup(op.param1,[op.param2])
                   except:
                       try:
                       	b2.cancelGroupInvitation(op.param1,[op.param2])
                       	b2.kickoutFromGroup(op.param1,[op.param2])
                       except:
                           try:
                           	b3.cancelGroupInvitation(op.param1,[op.param2])
                           	b3.kickoutFromGroup(op.param1,[op.param2])
                           except:
                           	pass
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = bima.getContact(op.param2).displayName
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
                          random.choice(Bima).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(Bima).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(Bima).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = bima.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           bima.sendMessage(msg.to, wait["Respontag"])
                           bima.sendImageWithURL(msg.to,image)
                           rnd = ["Nah, ngetag mele ntar beper ngak ada yang tanggung jawab.. jangan sampek puskun ya beb"]
                           p = random.choice(rnd)
                           lang = 'id'
                           tts = gTTS(text=p, lang=lang)
                           tts.save("hasil.mp3")
                #           cl.sendAudio(msg.to,"hasil.mp3")
                           bima.sendMessage(msg.to, None, contentMetadata={"STKID":"12641049","STKPKGID":"1313075","STKVER":"1"}, contentType=7)
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    bima.sendMessage(msg.to,"「Cek ID Sticker」\n┃🇮🇩┃ STKID : " + msg.contentMetadata["STKID"] + "\n┃🇮🇩┃ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n┃🇮🇩┃ STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    bima.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = bima.getContact(msg.contentMetadata["mid"])
                        path = bima.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        bima.sendMessage(msg.to,"┃🇮🇩┃ Nama : " + msg.contentMetadata["displayName"] + "\n┃🇮🇩┃ MID : " + msg.contentMetadata["mid"] + "\n┃🇮🇩┃ Status Msg : " + contact.statusMessage + "\n┃🇮🇩┃ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        bima.sendImageWithURL(msg.to, image)

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
                    bima.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    bima.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = bima.getContact(msg.contentMetadata["mid"])
                        path = bima.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        bima.sendMessage(msg.to,"┃🇮🇩┃ Nama : " + msg.contentMetadata["displayName"] + "\n┃🇮🇩┃ MID : " + msg.contentMetadata["mid"] + "\n┃🇮🇩┃ Status Msg : " + contact.statusMessage + "\n┃🇮🇩┃ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        bima.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        bima.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        bima.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        bima.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        bima.sendMessage(msg.to,"Contact itu bukan anggota bot saints")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        bima.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        bima.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        bima.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        bima.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        bima.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        bima.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        bima.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        bima.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        bima.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        bima.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        bima.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        bima.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        bima.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        bima.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        bima.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        bima.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
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
                            bima.sendText(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = bima.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     bima.updateGroupPicture(msg.to, path)
                     bima.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            bima.updateProfilePicture(path)
                            bima.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["RAfoto"]:
                            path = b1.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Amid]
                            b1.updateProfilePicture(path)
                            b1.sendMessage(msg.to,"Foto berhasil dirubah")                        
                        elif Zmid in Setmain["RAfoto"]:
                            path = bima2.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Zmid]
                            bima2.updateProfilePicture(path)
                            bima2.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = bima.downloadObjectMsg(msg_id)                     
                     settings["changePicture"] = False
                     bima.updateProfilePicture(path1)
                     bima.sendMessage(msg.to, "Berhasil mengubah foto profile bot")                     

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        bima.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage5 = help()
                               bima.sendMessage(msg.to, str(helpMessage5))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                bima.sendText(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                bima.sendText(msg.to, "Selfbot dinonaktifkan")
                        
                        elif cmd == "bimpro":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = helppro()
                               bima.sendMessage(msg.to, str(helpMessage2))
                               contact = bima.getContact(msg._from)
                               bima.sendMessage(msg.to, str(ret_),{'AGENT_LINK': 'line://ti/p/~xsetail','AGENT_ICON': "http://dl.profile.line-cdn.net/" + contact.pictureStatus,'AGENT_NAME': "~• 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ •~"})
                    
                        elif cmd == "bimkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               bima.sendMessage(msg.to, str(helpMessage))
                               contact = bima.getContact(msg._from)
                               bima.sendMessage(msg.to, str(ret_),{'AGENT_LINK': 'line://ti/p/~xsetail','AGENT_ICON': "http://dl.profile.line-cdn.net/" + contact.pictureStatus,'AGENT_NAME': "~• 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ •~"})

                                                            
                               
                        elif cmd == "bimbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage3 = helpbot()
                               bima.sendMessage(msg.to, str(helpMessage3))
                               contact = bima.getContact(msg._from)
                               bima.sendMessage(msg.to, str(ret_),{'AGENT_LINK': 'line://ti/p/~xsetail','AGENT_ICON': "http://dl.profile.line-cdn.net/" + contact.pictureStatus,'AGENT_NAME': "~• 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ •~"})
                               
                        elif cmd == "bimset":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage4 = helpset()
                               bima.sendMessage(msg.to, str(helpMessage4))
                               contact = bima.getContact(msg._from)
                               bima.sendMessage(msg.to, str(ret_),{'AGENT_LINK': 'line://ti/p/~xsetail','AGENT_ICON': "http://dl.profile.line-cdn.net/" + contact.pictureStatus,'AGENT_NAME': "~• 􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ •~"})

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "┃🛡┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Protection\n\n"
                                if wait["sticker"] == True: md+="┃🛠┃ Sticker「✅」\n"
                                else: md+="┃♻️┃ Sticker「❌」\n"
                                if wait["contact"] == True: md+="┃🛠┃ Contact「✅」\n"
                                else: md+="┃♻️┃ Contact「❌」\n"
                                if wait["talkban"] == True: md+="┃🛠┃ Talkban「✅」\n"
                                else: md+="┃♻️┃ Talkban「❌」\n"
                                if wait["Mentionkick"] == True: md+="┃🛠┃ Notag「✅」\n"
                                else: md+="┃♻️┃ Notag「❌」\n"
                                if wait["detectMention"] == True: md+="┃🛠┃ Respon「✅」\n"
                                else: md+="┃♻️┃ Respon「❌」\n"
                                if wait["autoJoin"] == True: md+="┃🛠┃ Autojoin「✅」\n"
                                else: md+="┃♻️┃ Autojoin「❌」\n"
                                if wait["autoAdd"] == True: md+="┃🛠┃ Autoadd「✅」\n"
                                else: md+="┃♻️┃ Autoadd「❌」\n"
                                if msg.to in welcome: md+="┃🛠┃ Welcome「✅」\n"
                                else: md+="┃♻️┃ Welcome「❌」\n"
                                if wait["autoLeave"] == True: md+="┃🛠┃ Autoleave「✅」\n"
                                else: md+="┃♻️┃ Autoleave「❌」\n"
                                if msg.to in protectqr: md+="┃⚔┃ Protecturl「✔」\n"
                                else: md+="┃♻️┃ Protecturl「☠」\n"
                                if msg.to in protectjoin: md+="┃⚔┃ Protectjoin「✔」\n"
                                else: md+="┃♻️┃ Protectjoin「☠」\n"
                                if msg.to in protectkick: md+="┃⚔┃ Protectkick「✔」\n"
                                else: md+="┃♻️┃ Protectkick「☠」\n"
                                if msg.to in protectcancel: md+="┃⚔┃ Protectcancel「✔」\n"
                                else: md+="┃♻️┃ Protectcancel「☠」\n"
                                if msg.to in protectinvite: md+="┃⚔┃ Protectinvite「✔」\n"
                                else: md+="┃♻️┃ Protectinvite「☠」\n"
                                if msg.to in protectantijs: md+="┃⚔┃ Protectantijs「✔」\n"
                                else: md+="┃♻️┃ Protectantijs「☠」\n"                                
                                bima.sendMessage(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                bima.sendText(msg.to,"Creator :\nD̸͟͞k̸͟͞f̸͟͞  T̸͟͞e̸͟͞a̸͟͞m̸͟͞   B̸͟͞o̸͟͞t̸͟͞  p̸͟͞r̸͟͞o̸͟͞t̸͟͞e̸͟͞c̸͟͞t̸͟͞.  \nhttp://line.me/ti/p/qEaRIT2R3N ") 
                                ma = ""
                                for i in creator:
                                    ma = bima.getContact(i)
                                    bima.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 Type Selfbot 」\n")
                               bima.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "test" or text.lower() == 'creator':
                            if msg._from in admin:
                                ma = ""
                                for i in baraya:
                                    ma = bima.getContact(i)
                                    bima.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif text.lower() == "mid":
                               bima.sendMessage(msg.to, msg._from)
                               
                        elif text.lower() == "me":
                               bima.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = bima.getContact(key1)
                               bima.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               bima.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = bima.getContact(key1)
                               bima.sendMessage(msg.to, "┃👿┃ Nama : "+str(mi.displayName)+"\n┃🇮🇩┃ Mid : " +key1+"\n┃🇮🇩┃ Status Msg"+str(mi.statusMessage))
                               bima.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(bima.getContact(key1)):
                                   bima.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   bima.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Amid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Bmid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Cmid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Dmid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Emid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Fmid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Gmid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Hmid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Imid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Qmid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Xmid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Ymid}
                               bima.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Zmid}
                               bima.sendMessage1(msg)                                                             

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   b1.removeAllMessages(op.param2)
                                   b2.removeAllMessages(op.param2)
                                   b3.removeAllMessages(op.param2)
                                   b4.removeAllMessages(op.param2)
                                   b5.removeAllMessages(op.param2)
                                   b6.removeAllMessages(op.param2)
                                   b7.removeAllMessages(op.param2)
                                   b8.removeAllMessages(op.param2)
                                   b9.removeAllMessages(op.param2)
                                   bima1.removeAllMessages(op.param2)
                                   bima2.removeAllMessages(op.param2)
                                   bima3.removeAllMessages(op.param2)
                                   bima4.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   bima.removeAllMessages(op.param2)                                   
                                   bima.sendText(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = bima.getGroupIdsJoined()
                               for group in saya:
                                   bima.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               bima.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   bima.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   bima.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               bima.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               bima.sendMessage(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               bima.sendMessage(msg.to, "Silahkan gunakan seperti semula...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               bima.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = bima.getGroup(msg.to)
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
                                bima.sendMessage(msg.to, "┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Family Grup Info\n\n┃🇮🇩┃ Nama Group : {}".format(G.name)+ "\n┃🇮🇩┃ ID Group : {}".format(G.id)+ "\n┃🇮🇩┃ Pembuat : {}".format(G.creator.displayName)+ "\n┃🇮🇩┃ Waktu Dibuat : {}".format(str(timeCreated))+ "\n┃🇮🇩┃ Jumlah Member : {}".format(str(len(G.members)))+ "\n┃🇮🇩┃ Jumlah Pending : {}".format(gPending)+ "\n┃🇮🇩┃ Group Qr : {}".format(gQr)+ "\n┃🇮🇩┃ Group Ticket : {}".format(gTicket))
                                bima.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                bima.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                bima.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = bima.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = bima.getGroup(group)
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
                                ret_ += "\n┃🇮🇩┃ ID Group : {}".format(G.id)
                                ret_ += "\n┃🇮🇩┃ Pembuat : {}".format(gCreator)
                                ret_ += "\n┃🇮🇩┃ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n┃🇮🇩┃ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n┃🇮🇩┃ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┃🇮🇩┃ Group Qr : {}".format(gQr)
                                ret_ += "\n┃🇮🇩┃ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                bima.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = bima.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "┃🇮🇩┃ "+ str(no) + ". " + mem.displayName
                                bima.sendMessage(to,"┃🇮🇩┃ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = bima.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    b1.leaveGroup(i)
                                    b2.leaveGroup(i)
                                    b3.leaveGroup(i)
                                    b4.leaveGroup(i)
                                    b5.leaveGroup(i)
                                    b6.leaveGroup(i)
                                    b7.leaveGroup(i)
                                    b8.leaveGroup(i)
                                    b9.leaveGroup(i)
                                    bima1.leaveGroup(i)
                                    bima.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = bima.getAllContactIds()
                               for i in gid:
                                   G = bima.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               bima.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = bima.getGroupIdsJoined()
                               for i in gid:
                                   G = bima.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               bima.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = bima1.getGroupIdsJoined()
                               for i in gid:
                                   G = bima1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               bima1.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = b1.getGroupIdsJoined()
                               for i in gid:
                                   G = b1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               b2.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = b3.getGroupIdsJoined()
                               for i in gid:
                                   G = b3.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               b3.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = bima1.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   bima1.updateGroup(X)
                                   bima1.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = bima.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   bima.updateGroup(X)
                                   bima.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = bima.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      bima.updateGroup(x)
                                   gurl = bima.reissueGroupTicket(msg.to)
                                   bima.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                bima.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                bima.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                bima.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["RAfoto"][Amid] = True
                                bima1.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["RAfoto"][Bmid] = True
                                b1.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["RAfoto"][Cmid] = True
                                b2.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["RAfoto"][Zmid] = True
                                b3.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = bima.getProfile()
                                profile.displayName = string
                                bima.updateProfile(profile)
                                bima.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = bima1.getProfile()
                                profile.displayName = string
                                bima1.updateProfile(profile)
                                bima1.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = b1.getProfile()
                                profile.displayName = string
                                b1.updateProfile(profile)
                                b1.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = b2.getProfile()
                                profile.displayName = string
                                b2.updateProfile(profile)
                                b2.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("botkicker: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = bima2.getProfile()
                                profile.displayName = string
                                bima2.updateProfile(profile)
                                bima2.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "tagall" or text.lower() == 'hai':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = bima.getGroup(msg.to)
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
                                    ma += str(a) + ". " +bima.getContact(m_id).displayName + "\n"
                                bima.sendMessage(msg.to,"┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Family bot\n\n"+ma+"\nTotal「%s」Family Bots" %(str(len(Bots))))

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
                                    ma += str(a) + ". " +bima.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +bima.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +bima.getContact(m_id).displayName + "\n"
                                bima.sendMessage(msg.to,"┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Family admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」Family Saints" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                mf = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                f = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +bima.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +bima.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +bima.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +bima.getGroup(group).name + "\n"
                                gid = protectantijs
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +bima.getGroup(group).name + "\n"
                                bima.sendMessage(msg.to,"┃☠┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Family Protection\n\n┃🔥┃ PROTECT Qr :\n"+ma+"\n┃🔥┃ PROTECT KICK :\n"+mb+"\n┃🔥┃ PROTECT JOIN :\n"+md+"\n┃🔥┃ PROTECT CANCEL:\n"+mc+"\n ┃🔥┃ PROTECT ANJS:\n"+mf+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectantijs))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                bima.sendMessage(msg.to,responsename1)
                                bima1.sendMessage(msg.to,responsename2)
                                b1.sendMessage(msg.to,responsename3)
                                b2.sendMessage(msg.to,responsename4)
                                b3.sendMessage(msg.to,responsename5)
                                b4.sendMessage(msg.to,responsename6)
                                b5.sendMessage(msg.to,responsename7)
                                b6.sendMessage(msg.to,responsename8)
                                b7.sendMessage(msg.to,responsename9)
                                b8.sendMessage(msg.to,responsename10)
                                b9.sendMessage(msg.to,responsename11)                                

                        elif cmd == "bim":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    bima.sendMessage(msg.to,"Siap Bos,,,,,!!!")
                                    ginfo = bima.getGroup(msg.to)                                    
                                    bima.inviteIntoGroup(msg.to, [Zmid])                                    
                                    bima.sendMessage(msg.to,"🔥Grup Ini"+str(ginfo.name)+"☠ Aman Dari Orang2 Yang Tidak Bertanggung Jawab,,,,,!!!!😂😂")
                                except:
                                    pass

                        elif cmd == "bimall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:                                
                                G = bima.getGroup(msg.to)
                                ginfo = bima.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                bima.updateGroup(G)
                                invsend = 0
                                Ticket = bima.reissueGroupTicket(msg.to)
                                b1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                b2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                b3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                b4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                b5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                b6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                b7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                b8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                b9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                bima1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = bima1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                bima1.updateGroup(G)
                                ginfo = bima1.getGroup(msg.to)                                    
                                bima1.inviteIntoGroup(msg.to, [Zmid])
                                

                        elif cmd == "byeall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = bima.getGroup(msg.to)
                                bima1.sendText(msg.to, "☠Baraya Pulang,,,,,,!!! "+str(G.name))
                                b1.leaveGroup(msg.to)
                                b2.leaveGroup(msg.to)
                                b3.leaveGroup(msg.to)
                                b4.leaveGroup(msg.to)
                                b5.leaveGroup(msg.to)
                                b6.leaveGroup(msg.to)
                                b7.leaveGroup(msg.to)
                                b8.leaveGroup(msg.to)
                                b9.leaveGroup(msg.to)
                                bima1.sendText(msg.to, "☠Pasukan Udah Pulang,,,,,,!!!\n☠Aim Pamit Stah,,,,,,!!! ")
                                bima.leaveGroup(msg.to)
                                
                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = bima.getGroup(msg.to)
                                bima.sendText(msg.to, "☠Aim Pamit Stah,,,,,,!!! "+str(G.name))
                                bima.leaveGroup(msg.to)
                        
                        elif cmd == "bim join":
                            if msg._from in admin:
                                G = bima.getGroup(msg.to)
                                ginfo = bima.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                bima.updateGroup(G)
                                invsend = 0
                                Ticket = bima.reissueGroupTicket(msg.to)
                                bima2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                bima3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                bima4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = bima2.getGroup(msg.to)
                                G = bima3.getGroup(msg.to)
                                G = bima4.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                bima4.updateGroup(G)

                        elif cmd == "bim bye":
                            if msg._from in admin:
                                G = bima.getGroup(msg.to)
                                bima2.leaveGroup(msg.to)
                                bima3.leaveGroup(msg.to)
                                bima4.leaveGroup(msg.to)

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = bima.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = bima.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = bima.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                bima.sendMessage(msg.to, "┃🔥┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴┃ Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "spall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               bima.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               bima.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))                               

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 bima.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 bima.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
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
                                                    no = "[ {} ]".format(str(bima.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        bima.sendMessage1(msg)
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
                                    bima.sendText(msg.to, "User kosong...")
                            else:
                                bima.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  bima.sendMessage(msg.to, "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nCek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
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
                                  bima.sendMessage(msg.to, "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nCek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  bima.sendMessage(msg.to, "Sudak tidak aktif")

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nTotal Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nTotal Spamcall Diubah Menjadi " +strnum)

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
                                                bima.sendMessage1(msg)
                                            except Exception as e:
                                                bima.sendText(msg.to,str(e))
                                    else:
                                        bima.sendText(msg.to,"Jumlah melebihi 100000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = bima.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                bima.sendMessage(msg.to, "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 9999999:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        bima.sendText(msg.to,str(e))
                                else:
                                    bima.sendText(msg.to,"Jumlah melebihi batas")

                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                bima.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                bima.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                bima.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass                                                        
                        
                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = bima.findContactsByUserid(msgs)
                              if True:
                                  bima.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  bima.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = bima.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nWelcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  bima.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = bima.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nWelcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    bima.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectqr ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectqr ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect Qr sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = bima.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  bima.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = bima.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    bima.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = bima.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  bima.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = bima.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    bima.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = bima.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  bima.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = bima.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    bima.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = bima.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  bima.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = bima.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nProtect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    bima.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    
						 
                        elif 'Protectinvite ' in msg.text:
                            if msg._from in admin:
                               spl = msg.text.replace('Protectinvite ','')
                               if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nProtect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = bima.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nProtect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  bima.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                               elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = bima.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nProtect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nProtect invite sudah tidak aktif"
                                    bima.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)                                    

                        elif 'ProJs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ProJs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nAnti DESAH sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = bima.getGroup(msg.to)
                                       msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nAnti DESAH Diaktifkan\nDi Group : " +str(ginfo.name)
                                  bima.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = bima.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nAnti DESAH Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴\nAnti DESAH Sudah Tidak Aktif"
                                    bima.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)

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
                                      ginfo = bima.getGroup(msg.to)
                                      msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nSemua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = bima.getGroup(msg.to)
                                      msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  bima.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
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
                                         ginfo = bima.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = bima.getGroup(msg.to)
                                         msgs = "􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nSemua protect sudah off\nDi Group : " +str(ginfo.name)
                                    bima.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

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
                                           G = bima.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           bima.updateGroup(G)
                                           invsend = 0
                                           Ticket = bima.reissueGroupTicket(msg.to)
                                           bima3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           bima3.kickoutFromGroup(msg.to, [target])
                                           bima3.leaveGroup(msg.to)
                                           X = bima.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           bima.updateGroup(X)
                                       except:
                                           pass

                        elif ("Bim1 " in msg.text):
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
                                           bima.kickoutFromGroup(msg.to, [target])
                                           wait["blacklist"][op.param2] = True
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
                                           bima.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menambahkan admin")
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
                                           bima.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menambahkan staff")
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
                                           bima.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menghapus admin")
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
                                           bima.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menghapus admin")
                                       except:
                                           pass                        
                        
                        elif ("refresh" in msg.text):
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
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = bima.getContact(i)
                                    bima.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = bima.getContact(i)
                                    bima.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = bima.getContact(i)
                                    bima.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nNotag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nNotag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nDeteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nDeteksi contact dinonaktifkan")

                        elif ("respon on" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAuto respon diaktifkan")

                        elif ("respon off" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAuto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAutojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAutojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAutoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAutoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAuto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nAuto add dinonaktifkan")

                        elif ("sticker on" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nDeteksi sticker diaktifkan")
                                                        
                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nJoin ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                bima.sendText(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nNotag dinonaktifkan")

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
                                           bima.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menambahkan blacklist")
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
                                           bima.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menghapus blacklist")
                                       except:
                                           pass
                        
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
                                           bima.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menambahkan blacklist")
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
                                           bima.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nBerhasil menghapus blacklist")
                                       except:
                                           pass
                        
                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                bima.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +bima.getContact(m_id).displayName + "\n"
                                bima.sendMessage(msg.to,"┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ ┃ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                bima.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nTidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +bima.getContact(m_id).displayName + "\n"
                                bima.sendMessage(msg.to,"┃🇮🇩┃ ┃􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ ┃ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    bima.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nTidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = bima.getContact(i)
                                        bima.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = bima.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              bima.sendMessage(msg.to,"􀠁􀠁!!ᵀᴱᴬᴹᴃᴀƦ͞ᴀ͞ʏ͞ᴀ᮴᮴᮴ \nSukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  bima.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  bima.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  bima.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  bima.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  bima.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  bima.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  bima.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  bima.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  bima.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  bima.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               bima.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               bima.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               bima.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               bima.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               bima.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

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
                                     group = bima.findGroupByTicket(ticket_id)
                                     bima.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     bima.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = bima1.findGroupByTicket(ticket_id)
                                     bima1.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     bima1.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = b1.findGroupByTicket(ticket_id)
                                     b1.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     b1.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = b2.findGroupByTicket(ticket_id)
                                     b2.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     b2.sendMessage(msg.to, "Masuk : %s" % str(group.name))

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
