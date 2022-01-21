from numpy import e
import pyautogui as pa
import time
import cv2
import win32gui, win32con
import subprocess

secretshit='-'

BOMBERS = 12
PERIOD = 20



pa.FAILSAFE = False
NAVI = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe' 

def setPwd(pwd):
    global secretshit
    secretshit = pwd

def findOnScreen(img):
    return pa.locateOnScreen(img, confidence=0.9)

def clickOnScreen(img, last=False):
    if last:
        gen = pa.locateAllOnScreen(img, confidence=0.9)
        btn = None
        for btn in gen:
            pass
    else:
        btn = pa.locateOnScreen(img, confidence=0.9)
    if btn:
        center = pa.center(btn)
        clickk(center.x,center.y)
    return btn

def sl(i):
    time.sleep(i)

def clickk(x,y):
    #pa.moveTo('assets/full-screen.png')
    pa.click(x,y)# 362,187

def clickph(img):
    btn = None
    findWin("sponsored session", True)
    btn = clickOnScreen(img)
    if not btn:
        print('[{}] {} not found'.format(time.strftime('%d/%m %X'), img))
        raise Exception
    return btn  

def findWin(w, close=False, fg=True):
    def myHandler(hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    top_windows = []
    win32gui.EnumWindows(myHandler, top_windows)
    res = False
    for i in top_windows:
        if w in i[1].lower():
            res = True
            if close:
                print("[{}] closing {}".format(time.strftime('%d/%m %X'),w))
                win32gui.PostMessage(i[0],win32con.WM_CLOSE,0,0)             
            else:
                print("[{}] found {}".format(time.strftime('%d/%m %X'),w))
                win32gui.ShowWindow(i[0],win32con.SW_SHOW)
                if fg: 
                    pa.press('alt')
                    win32gui.SetForegroundWindow(i[0])
            break
    sl(2)
    return res


def startBrowser():
    global secretshit

    print("[{}] start new - wrong windows".format(time.strftime('%d/%m %X')))
    subprocess.Popen(["taskkill","/f","/im","chrome.exe"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    sl(2)
    subprocess.Popen([NAVI,"app.bombcrypto.io"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    sl(2)
    nav_found = findWin("bombcrypto - google chrome")
    while(not nav_found): nav_found = findWin("bombcrypto - google chrome")    

    sl(6) # wait for metamask notification to disapear
    clickOnScreen('assets/metamask.png')
    sl(4)
    print("[{}] metamask password".format(time.strftime('%d/%m %X')))
    for c in secretshit:
        pa.press(c)

    screenshot()

    sl(1)
    pa.press('enter')
    sl(3)
    pa.hotkey('ctrl','f5')
    sl(8)

def connectWallet():
    print("[{}] connect wallet".format(time.strftime('%d/%m %X')))
    clickph('assets/connect-wallet.png') # connect wallet #clickk(978,785) # connect wallet
    sl(5) # for metamask notification to disapear
    findWin("metamask notification")
    clickph('assets/sign.png')         # sign metamask #clickk(1805,689) # sign 1440,446
    sl(15)                              # loading

def onStart():
    startBrowser()

    # fermer les anciennes page MetaMask
    found = findWin("metamask notification", True)
    print("[{}] close metamask if any".format(time.strftime('%d/%m %X')))
    while(found): 
        found = findWin("metamask notification", True)

    connectWallet()
    toMap()


def toMap():
    #clickk(985,555) # treasure hunt
    clickph('assets/treasure-hunt.png')
    sl(2)
def toGain1():
    #clickk(1523,232)
    clickph('assets/gain1.png')
    sl(3)
def toGain2():
    #clickk(1523,232)
    clickph('assets/gain2.png')
    sl(3)    
def toHero1():
    clickph('assets/hero1.png')
    #clickk(1490,850) # from main
    sl(3)
    #screenshot()
def toHero2():
    clickph('assets/up-arrow.png')
    #clickk(975,918) # white arrow
    sl(3)
    clickph('assets/hero2.png')
    #clickk(973,884) # hero
    sl(5)             # load
    #screenshot()

def backFromMap():
    clickph('assets/back-from-map.png')
    #clickk(430,229) # green arrow
    sl(2)
def backFromGain():
    clickph('assets/back-from-gain.png')
    #clickk(1306,334) # gain red cross
    sl(3)  
def backFromHero1():
    clickph('assets/back-from-hero.png')
    sl(1)     
def backFromHero2():
    clickph('assets/back-from-hero.png')
    sl(1)
    clickph('assets/down-arrow.png')
    #clickk(1047,329) # hero red cross
    sl(3)

# OK
def scroll1(f_bomber=0, dir=-1):
    ra=4
    if f_bomber == 1: ra=3
    for i in range(ra):  pa.scroll(dir)

def scroll5(f_bomber=0, dir=-1):
    ra=5
    if f_bomber == 1: 
        scroll1(f_bomber, dir)
        ra = 4
    for i in range(ra):
        scroll1(f_bomber, dir)

def scrollToBottom(dir=-1):
    #scroll1(0,dir) # since all button no need for special case of 1st bomber
    for ii in range(BOMBERS-5): scroll1(0, dir) # +1 to make sure its the end


def bomber(nb = 0, order='work', delay=4, offset=0):
    dy = 88
    dx = 0
    if order == 'rest': dx= 73

    clickk(872+dx, 430+nb*dy+offset)
    sl(delay)

def bomberState():
    print("[{}] bomberstate()".format(time.strftime('%d/%m %X')))
    screenshot()
    backFromMap()
    toHero1()
    clickph('assets/home2.png')
    screenshot()
    for i in range(2):
        scroll5()
        screenshot()
    backFromHero1()
    toMap()

def screenshot():
    sl(1)
    sc = pa.screenshot()
    #scdir = str(Path(__file__).parent)#.replace('\\','\\')
    scdir = "screen/{}.png".format(time.strftime('%d-%m__%H-%M-%S'))
    #print('[{}] screenshot()'.format(time.strftime('%d/%m %X')))
    sc.save(scdir)


#all except Legendary
def toWork(legendary=False):
    offset=30 # px 
    findWin("bombcrypto - google chrome")
    screenshot()
    backFromMap()
    print("[{}] -- toWork()".format(time.strftime('%d/%m %X')))
    toHero1()
    sl(3)
    clickph('assets/home2.png')  # place mouse to scroll  
                                 # TODO click of first bomber icon
    scrollToBottom()
    sl(1)
    for i in range(BOMBERS):
        bomber(4,'work', 3, offset) # TODO locate work botton
#    if not legendary:
#        for ii in range(2): scroll1(0,1)
#        clickOnScreen('assets/rest-off.png') # first rest (off) on screen
    backFromHero1()
    toMap()

def allToRest():
    findWin("bombcrypto - google chrome")
    screenshot()
    backFromMap()
    print("[{}] -- AllToRest()".format(time.strftime('%d/%m %X')))
    toHero1()
    sl(3)
    for i in range(BOMBERS): bomber(0, 'rest') 
    backFromHero1()
    toMap()

def allToRestNew():
    findWin("bombcrypto - google chrome")
    screenshot()
    backFromMap()
    print("[{}] -- AllToRest()".format(time.strftime('%d/%m %X')))
    toHero1()
    sl(3)
    clickph('assets/rest-all.png') 
    sl(3)


def sleepInPeriods(d, p=15, state=False):
    assert(d*p != 0)
    print("[{}] -- sleepInPeriods()".format(time.strftime('%d/%m %X')))
    if d < p: 
        d = p 
    count = int(d/p)

    for i in range(int(d/p)):
        if state:
            bomberState()
        #e = random.randint(-1,1)
        e=0
        assert(p+e > 0)
        print("[{}] sleep {} min - ({}x / {} min)".format(time.strftime('%d/%m %X'), e+p, count,d))
        count -= 1
        sl((p+e)*60)

        for i in range(2): 
            found = findWin("bombcrypto - google chrome")
        toGain2();
        backFromGain();

#all except Legendary
def toWorkNew(legendary=True):
    findWin("bombcrypto - google chrome")
    screenshot()
    backFromMap()
    print("[{}] -- toWorkNew()".format(time.strftime('%d/%m %X')))
    toHero1()
    sl(2)

    if not findOnScreen('assets/work-all.PNG'):
        clickph('assets/rest-all.png')
    clickph('assets/work-all.png')
    sl(2)

    #clickph('assets/home2.png')  # place mouse to scroll TODO click of first bomber icon
    #scrollToBottom()
    #sl(2)
    #if legendary:
    #    #for ii in range(2): scroll1(0,1)
    #    scroll1(0,1)
    #    clickOnScreen('assets/rest-off.png') # first rest off on screen
    backFromHero1()
    toMap()

def dayMode(p=15):
    count=0
    while(True):
        count += 1
        print("[{}] cycle {}".format(time.strftime('%d/%m %X'), count))
        try:
            onStart()
            dayModeOnce(p)
        except Exception as e:
            print(e)
            #continue

def dayModeOnce(p=15):
    for i in range(2): findWin("bombcrypto - google chrome")
    if not findOnScreen('assets/gain2.png'):
        toMap()

    toWorkNew()
#    sleepInPeriods(10*2,10, False)

    d = 60*3 #(60 + random.randint(-5,5))
    p = 60
    sleepInPeriods(d,p, True)

#dayMode()

#sleepInPeriods(45,15)
#toWork()
#btn =  pa.locateOnScreen('assets/home2.png', grayscale=True)
#
#btn =  pa.locateOnScreen('assets/home2.png', grayscale=True) # add
#if btn:
#    center = pa.center(btn)
#    pa.moveTo(center.x, center.y)
#else:
#    print('assets/home2.png not found')

#move()
#if not clickph('assets/hero2.png'): exit()
#backFromGain()
#backFromHero2()
#toMap()
#toGain2()
#toHero2()

#bomber()
#scrollToBottom()

#sleepInPeriods(60,15)

#dayMode()

#allToRest()


