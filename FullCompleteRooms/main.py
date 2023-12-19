from distutils.core import setup
from turtle import goto
import pyautogui as py
import time
import winsound
from datetime import datetime

ordernumberBoxLoc = (0,0)
fullButtLoc = (0,0)

fullButtClick = r'images/eCompBtn.png'
searchOrderNo = r'images/eOrderNo.png'
orderCompletedSuccessfully = r'images/eFullComp.png'
undoButt = r'images/eUndoButt.png'
okButt = r'images/eOkBtn.png'
py.FAILSAFE=True

print('Running...')
time.sleep(3)

ordernumberBoxLoc = py.locateOnScreen(searchOrderNo, confidence=.8)
fullButtLoc = py.locateOnScreen(fullButtClick, confidence=.6)   
compSuccLoc = py.locateOnScreen(orderCompletedSuccessfully, confidence=.8)
undoButtLoc = py.locateOnScreen(undoButt, confidence=.6)
daFile = open('OrderNumberList.txt', 'r') 

"""print(ordernumberBoxLoc)
print("__")
print(fullButtLoc)"""


def goToOrderBox(daOrderNo):
    #first check for new location since it can change
    ordernumberBoxLoc = py.locateOnScreen(searchOrderNo, confidence=.8)
    #barely hits corner
    py.moveTo(ordernumberBoxLoc[0]+100,ordernumberBoxLoc[1]+10, duration=.65)
    time.sleep(.1)
    
    py.click()
    py.hotkey('ctrl','a')
    #put in orderNo now 
    py.typewrite(daOrderNo,.1)
    py.press('enter')
    print('OrderNo Searched:   ' + daOrderNo)

def checkIfFound():
    if (py.locateOnScreen(undoButt,confidence=.8)):
        print('true hit')
        return True
    return False


while(True):
    line = daFile.readline()
    if not line:
        print('Not line hit')
        break
    goToOrderBox(line)
    time.sleep(5)
    py.moveTo(fullButtLoc,duration=.65)
    time.sleep(5)
    
    if(checkIfFound()):
        #if found dont click and add it to the new completed list
        winsound.Beep(3000,100)
        winsound.Beep(800,100)
        time.sleep(.1)
        
    else:
         #if fine then add orderno to another file
        
        with open('completedOrderNoList.txt','a') as file:
            file.write(line)
        print('Moving to CLick butt')
        py.moveTo(fullButtLoc,duration=.65)     #this line is for worst case scenario slow load time
        time.sleep(.3)
        py.click()
        time.sleep(.2)
        okLoc = py.locateOnScreen(okButt, confidence=.7)
        py.moveTo(okLoc, duration=.65)
        py.click()
        #time sleeping is time i am writing the orderno down
        time.sleep(3)
