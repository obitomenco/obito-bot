import pyautogui as pa
import time, random
#from core import bomberBis, clickph
import cv2
import win32gui, win32con
from pathlib import Path


def clickph(img):
    pa.moveTo('assets/full-screen.png')
    btn = pa.locateOnScreen(img)
    if btn:
        center = pa.center(btn)
        x,y = center
        #print(x, ', ',y)
        clickk(x,y)
    else:
        print('[{}] {} not found on screen'.format(time.strftime('%d/%m %X'), img))
        # TODO take screenshot, identify state, 
        # e.g. goBackFromMap if img= treasure hunt, goToMap is arrow up/down, 
    return btn   

def scroll1(first=0, ra=4):
    if first == 1: ra=3
    for i in range(ra):  pa.scroll(-1)

def bomberBis(order='work'):
    clickph('assets/home2.png')
    scroll1(1)
    for i in range(9): scroll1()
    #pa.locateAllOnScreen('assets/work-')
    return

def toWorkBis():
    findWin("bombcrypto")
    screenshot()
    backFromMap()
    print("[{}] -- toWork()".format(time.strftime('%d/%m %X')))
    toHero1()
    sl(3)
    # Go to the bottom
    # Decide to work/sleep based on HP
    # Option 1
        # scan last bomber ?? how
            # option 1 : last detected 'home' btn
            # option 2 :
                # AllToRest() 
                # use locateOnScreen(b15.png) -> x,y
                # get coordinates and screenshot(region=(x,y, 52, 367)) y+52px et x+ 832-465
        # extract HP and decide
            # if work, use click on last detected 'work' -> bomber will move up
                # do same for the next one
            # if rest, use last detected 'rest' -> need to move up
                # move up by detecting last - 1 ''
    # Option 2
        # allToRest()
        # for each bi.png (1=1..15)
            # b = locateOnScreen(bi.png)
            # i = 1
            # while b == None
                # scroll down 5 bombers (3 scrolls for first, 4 for next, after first on i=0 )
                # r = 5
                # if i == 1: 
                #   scroll1(1)
                #   i = 0
                #   r = 4
                # for j in range(r): scroll1()
                # b = locateOnScreen(bi.png)
            # screenshot hp region
            # extract (v/w)
            # orderBomber()
     # def orderBomber(b, v, w):
        # if b == 7 # legendary
        # else: less than fifty click 'work'

            


def sl(i):
    time.sleep(i)

def clickk(x,y):
    pa.click(x,y)# 362,187


def findWin(w,fg=True):
    def myHandler(hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    top_windows = []
    win32gui.EnumWindows(myHandler, top_windows)
    for i in top_windows:
        if w in i[1].lower():
            #print(i)
            win32gui.ShowWindow(i[0],win32con.SW_SHOW)
            if fg: 
                pa.press('alt')
                win32gui.SetForegroundWindow(i[0])
            break
    sl(2)

def scroll15():
    for i in range(50): pa.scroll(-100)

def onStart():
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;    findWin("bombcrypto")
    sl(2)
    pa.press('f5')
    sl(7)
    clickph('assets/connect-wallet.png') # connect wallet
    sl(5)
    print("--Trying to access MetaMask")
    findWin("metamask")
    clickph('assets/sign.png')         # sign metamask
    sl(10)                              # loading

def toMap():
    clickk(985,555) # treasure hunt
    sl(3)
def toGain():
    clickk(1523,232)
    sl(3)
def toHero1():
    clickk(1490,850) # from main
    sl(3)
    screenshot()
def toHero2():
    clickk(975,918) # white arrow
    sl(3)
    clickk(973,884) # hero
    sl(5)             # load
    screenshot()

def backFromMap():
    clickk(430,229) # green arrow
    sl(3)
def backFromGain():
    clickk(1306,334) # gain red cross
    sl(3)
def backFromHero1():
    clickk(1047,329) # hero red cross
    sl(3)
def backFromHero2():
    clickk(1047,331) # hero red cross
    sl(3)
    clickk(974,805) # high white arrow
    sl(3)

def move():
    print("[{}] move()".format(time.strftime('%d/%m %X')))
    clickk(1360,385) # click inside map
    backFromMap()
    toMap()

def bomber(nb = 0, order='work', delay=3, offset=0):
    dy = 88
    dx = 0
    if order == 'rest': dx= 73

    clickk(872+dx, 430+nb*dy+offset)
    sl(delay)

def screenshot(): # TODO upload to drive

    sl(2)
    sc = pa.screenshot()
    scdir = str(Path(__file__).parent)#.replace('\\','\\')
    scdir += "\\screen\\{}.png".format(time.strftime('%d-%m__%H-%M-%S'))
    #print('[{}] screenshot()'.format(time.strftime('%d/%m %X')))
    sc.save(scdir)

#all except Legendary
def toWork(ra=15):
    offset=30 # px 
    findWin("bombcrypto")
    screenshot()
    print("[{}] -- toWork()".format(time.strftime('%d/%m %X')))
    toHero2()
    sl(3)
    bomber(0, 'rest') # TODO click of first bomber icon
    scroll15()
    sl(1)
    r=4
    for i in range(ra):
        if i==6:
            r=3
        bomber(r,'work', 3, offset) # TODO locate work botton
    backFromHero2()
        
def allToWork():
    findWin("bombcrypto")
    screenshot()
    print("[{}] -- AllToWork()".format(time.strftime('%d/%m %X')))
    toHero2()
    sl(3)
    for i in range(15): 
        pa.scroll()
        bomber(4)
    backFromHero2()

def allToRest(ra=5):
    findWin("bombcrypto")
    screenshot()
    print("[{}] -- AllToRest()".format(time.strftime('%d/%m %X')))
    toHero2()
    sl(3)
    for i in range(ra): bomber(0, 'rest') 
    backFromHero2()

def sleepInPeriods(d, p=13):
    e = 0
    assert p*d != 0 
    if d < p: d = p 
    #print("[{}] sleep {} min in periods of +-{} min - ({})".format(time.strftime('%d/%m %X'), d, p, int(d/p)))
    for i in range(int(d/p)):
        screenshot()
        e = 0   #random.randint(-1,1)
        assert(p+e > 0)
        print("[{}] sleep {} min - ({})".format(time.strftime('%d/%m %X'), e+p, int(d/p)))
        sl((p+e)*60)
        for i in range(3): 
            findWin('bombcrypto')
        move()

def nightMode():
    while(True):
        sl(3)
        toMap()
        allToRest()
        toWork()
        s = (60 + random.randint(-5,5))
        #sleepInPeriods(s,p)
        # work for 30 minutes - except legendary and rare - (sleep 30 min)
        # sleep 2h again  etc etc

def dayMode(p=15):
    while(True):
        for i in range(3): 
            findWin('bombcrypto')
        toMap()
        allToRest()
        toWork()
        s = (60 + random.randint(-5,5))
        sleepInPeriods(s,p)
        #print("[{}] sleep for {} min - ({} min period)".format(time.strftime('%d/%m %X'),s,p))
        #allToRest()
        #sleepInPeriods(r,p)
        
sl(2)

#bomberBis()


#img='assets/home2.png'
#img='assets/b5.png'
#clickph(img)
#g = pa.locateAllOnScreen(img, confidence=0.95)
#print(sum(1 for _ in g))
#pa.click('assets/up-arrow.png') # OK
#onStart()
#for i in range(4): pa.scroll(-1)
"""       
def allToWork():
    findWin("bombcrypto")
    screenshot()
    print("[{}] -- AllToWork()".format(time.strftime('%d/%m %X')))
    toHero2()
    sl(3)
    for i in range(15): 
        pa.scroll()
        bomber(4)
    backFromHero2()
"""