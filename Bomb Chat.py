import pyautogui as pyg
import time
a = input("Masukkan teks anda :")
b = int(input("Masukkan berapa kali pesannya dikirim"))
c= int(input("masukkan jeda"))
for i in range(b):
    time.sleep(c)
    pyg.write(a)
    time.sleep(c)
    pyg.press("enter")

    
