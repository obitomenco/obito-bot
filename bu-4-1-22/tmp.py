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