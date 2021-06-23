import os
import subprocess
import time
import cv2
import ctypes
import threading
import pyautogui

os.chdir(f"C:\\Users\\{os.environ['USERNAME']}")
def camera():
    sayac = 1
    for i in range(1):
        camera = cv2.VideoCapture(0)
        return_value,image = camera.read()
        cv2.imwrite(f'image{sayac}.png',image)
        image_path_address = f"image{sayac}.png"
        sayac +=1
        camera.release()
        cv2.destroyAllWindows()
        path = os.path.join(os.getcwd(),image_path_address)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
        time.sleep(1)
        os.remove(path)

def openCall():
    for i in range(1):
        os.system("calc.exe")

def openPaint():
    for i in range(1):
        os.system("mspaint.exe")

def openSystem():
    for i in range(1):
        os.system("appwiz.cpl")

def openWordPad():
    for i in range(1):
        os.system("write.exe")


def writeHacklendin():
    metin1 = "---------------HACKLENDİN------------\n"

    for i in range(1):
        subprocess.Popen("notepad.exe")
        for j in range(10):
            time.sleep(0.2)
            pyautogui.write(str(metin1))

def write_SytemInfo():
    metin = subprocess.check_output("systeminfo", shell=True)
    for i in range(1):
        subprocess.Popen("notepad.exe")
        time.sleep(0.2)
        pyautogui.write(str(metin))


if __name__ == "__main__":
    walpaper = threading.Thread(target=camera(),args=())
    walpaper.start()
    #----
    cal = threading.Thread(target=openCall(),args=())
    cal.start()
    #--
    point = threading.Thread(target=openPaint(), args=())
    point.start()
    #----
    sysr = threading.Thread(target=openSystem(), args=())
    sysr.start()
    #--
    word = threading.Thread(target=openWordPad(), args=())
    word.start()
    #--
    sys_info = threading.Thread(target=write_SytemInfo(), args=())
    sys_info.start()
    #--
    w_hack = threading.Thread(target=writeHacklendin(), args=())
    w_hack.start()

