import win32api, win32con
import time
from selenium import webdriver

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

initX = 220
initY = 885
interval = 110

driver = webdriver.Chrome()
driver.fullscreen_window()
driver.get("https:chess.com/vision")

start_btn = driver.find_element_by_class_name("settings-start-button")
start_btn.click()
time.sleep(3)
square = driver.find_element_by_class_name("target-label-white")

while True:
    file = square.text[0]
    rank = square.text[1]
    xCoord = (ord(file)-97)*interval+initX
    yCoord = (ord(rank)-49)*(-interval)+initY
    click(xCoord, yCoord)

# first (a1):   220:885
# interval:     110 px