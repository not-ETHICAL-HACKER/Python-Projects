import pyautogui as py
while True:
    print(py.position())
    x,y=py.position()
    print(py.pixel(x=x,y=y))