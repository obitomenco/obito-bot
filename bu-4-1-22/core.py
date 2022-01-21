from PIL.ImageOps import grayscale
from numpy import e
import pyautogui as pa
import time, random
import cv2, pyperclip
import win32gui, win32con
from pathlib import Path
import subprocess, os

BOMBERS = 15
PERIOD = 20


STATE= None

pa.FAILSAFE = False
NAVI = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe' 

def findOnScreen(img):
    return pa.locateOnScreen(img, confidence=0.9)

def clickOnScreen(img):
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
    #print('[{}] state = {}'.format(time.strftime('%d/%m %X'), STATE))
    try:
        btn = clickOnScreen(img)
        if not btn:
            print('[{}] {} not found-1'.format(time.strftime('%d/%m %X'), img))
            screenshot()
            sl(3)
            if not findWin("sponsored session", True):
                print('[{}] not teamviewer'.format(time.strftime('%d/%m %X')))
                if not clickOnScreen('assets/new-map.png'):
                    onStart()
            dayMode(PERIOD)
            # TODO take screenshot, identify state, 
            # e.g. goBackFromMap if img= treasure hunt, goToMap is arrow up/down, 
    except TypeError or pa.ImageNotFoundException:
        print('[{}] {} not found - wrong webpage? disconnec? new map?'.format(time.strftime('%d/%m %X'), img))       
        screenshot()
        sl(3)
        if not findWin("sponsored session", True):
            print('[{}] not teamviewer'.format(time.strftime('%d/%m %X')))
            if not clickOnScreen('assets/new-map.png'):
                onStart()
        dayMode(PERIOD)

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

def scroll15(dir=-1):
    scroll1(1,dir)
    for ii in range(BOMBERS-5-1): scroll1(0, dir)

def startBrowser():
    print("[{}] start new - wrong windows".format(time.strftime('%d/%m %X')))
    subprocess.Popen(["taskkill","/f","/im","chrome.exe"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    sl(2)
    subprocess.Popen([NAVI,"app.bombcrypto.io"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    sl(2)
    nav_found = findWin("bombcrypto - google chrome")
    while(not nav_found): nav_found = findWin("bombcrypto - google chrome")    

    sl(6) # wait for metamask notification to disapear
    pa.click('assets/metamask.png')
    sl(4)
    secretshit='M.d0hh0n1m'
    print("[{}] metamask password".format(time.strftime('%d/%m %X')))
    for c in secretshit:
        pa.press(c)
   # pyperclip.copy(secretshit)
   # pa.hotkey('ctrl', 'v', interval=0.1)
    #print('copy psd')
    screenshot()
    #pa.typewrite(, interval)

    sl(1)
    pa.press('enter')
    sl(3)
    pa.press('f5')
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
    STATE='toMap'
    clickph('assets/treasure-hunt.png')
    sl(3)
def toGain1():
    STATE='toGain1'
    #clickk(1523,232)
    clickph('assets/gain1.png')
    sl(3)
def toGain2():
    STATE='toGain2'
    #clickk(1523,232)
    clickph('assets/gain2.png')
    sl(3)    
def toHero1():
    STATE='toHero1'
    clickph('assets/hero1.png')
    #clickk(1490,850) # from main
    sl(3)
    #screenshot()
def toHero2():
    STATE='toHero2'
    clickph('assets/up-arrow.png')
    #clickk(975,918) # white arrow
    sl(3)
    clickph('assets/hero2.png')
    #clickk(973,884) # hero
    sl(5)             # load
    #screenshot()

def backFromMap():
    STATE='backFromMap'
    clickph('assets/back-from-map.png')
    #clickk(430,229) # green arrow
    sl(2)
def backFromGain():
    STATE='backFromGain'
    clickph('assets/back-from-gain.png')
    #clickk(1306,334) # gain red cross
    sl(3)  
def backFromHero1():
    STATE='backFromHero1'
    clickph('assets/back-from-hero.png')
    sl(1)     
def backFromHero2():
    STATE='backFromHero2'
    clickph('assets/back-from-hero.png')
    sl(1)
    clickph('assets/down-arrow.png')
    #clickk(1047,329) # hero red cross
    sl(3)

def move():
    print("[{}] move()".format(time.strftime('%d/%m %X')))
    #clickk(1360,385) # click inside map
    backFromMap()
    toMap()
    if not findOnScreen('assets/gain2.png'):
        onStart()    

def bomberBis(order='work'):
    clickph('assets/home2.png')
    scroll1(1)
    for i in range(9): scroll1()
    #pa.locateAllOnScreen('assets/work-')
    return

def bomber(nb = 0, order='work', delay=4, offset=0):
    dy = 88
    dx = 0
    if order == 'rest': dx= 73

    clickk(872+dx, 430+nb*dy+offset)
    sl(delay)

def screenshot():
    sl(2)
    sc = pa.screenshot()
    scdir = str(Path(__file__).parent)#.replace('\\','\\')
    scdir += "\\screen\\{}.png".format(time.strftime('%d-%m__%H-%M-%S'))
    #print('[{}] screenshot()'.format(time.strftime('%d/%m %X')))
    sc.save(scdir)


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

def bomberState():
    print("[{}] bomberstate()".format(time.strftime('%d/%m %X')))
    backFromMap()
    toHero1()
    clickph('assets/home2.png')
    screenshot()
    for i in range(2):
        scroll5()
        screenshot()
    backFromHero1()
    toMap()

def sleepInPeriods(d, p=15, e=0):
    print("[{}] -- sleepInPeriods()".format(time.strftime('%d/%m %X')))
    assert p*d != 0 
    if d < p: 
        d = p 
    count = int(d/p)

    for i in range(int(d/p)):
        for i in range(3): 
            found = findWin("bombcrypto - google chrome")
        
        bomberState()
        #e = random.randint(-1,1)
        assert(p+e > 0)
        print("[{}] sleep {} min - ({}x / {} min)".format(time.strftime('%d/%m %X'), e+p, count,d))
        count -= 1
        sl((p+e)*60)

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
    scroll15()
    sl(1)
    for i in range(BOMBERS):
        bomber(4,'work', 3, offset) # TODO locate work botton
    if not legendary:
        for ii in range(2): scroll1(0,1)
        clickOnScreen('assets/rest-off.png') # first rest (off) on screen
    backFromHero1()
    toMap()

def dayMode(p=15):
    count=0
    while(True):
    
        for i in range(2): findWin("bombcrypto - google chrome")
        if not findOnScreen('assets/gain2.png'):
            toMap()

        count += 1
        print("[{}] cycle {}".format(time.strftime('%d/%m %X'), count))

        toWork()
       
        d = 40*3 #(60 + random.randint(-5,5))
        p = 40
        assert(p>0)
        assert(d>0)
        sleepInPeriods(d,p)
        #sleepInPeriods(2,1)


sl(2)
dayMode(PERIOD)
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
#scroll15()

#sleepInPeriods(60,15)

#dayMode()

#allToRest()


#sl(2)
#toWork()
#bomber(2)


"""
while not btn:
    print(btn)
    backFromMap()
    toHero1()
    btn =  pa.locateOnScreen('assets/home2.png', grayscale=True) # add
    backFromHero2()
    toMap()
print(btn)
"""