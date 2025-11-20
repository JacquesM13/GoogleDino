import pyautogui
import time
import cv2

dinosaur_x = 164
cactus_x = None
cacti_x = None
# region = (10, 500, 1490, 200)
# region = (20, 730, 2996, 672) # Left, Top, Width, Height
region = (140, 750, 2000, 672) # Left, Top, Width, Height

try:
    dinosaur_x, dinosaur_y = pyautogui.locateCenterOnScreen('./images/Dinosaur.png', confidence=0.8, grayscale=True)
    print(dinosaur_x, dinosaur_y)
except pyautogui.ImageNotFoundException:
    # print('Dead')
    dinosaur_x, dinosaur_y = pyautogui.locateCenterOnScreen('./images/DeadDinosaur.png', confidence=0.8, grayscale=True)
    # print(dinosaur_x, dinosaur_y)

finally:
    alive = True
    while alive:
        try:
            stalk_x, stalk_y = pyautogui.locateCenterOnScreen('./images/CactiStalk.png', confidence=0.6, region=region, grayscale=True)
        except pyautogui.ImageNotFoundException:
            continue
        else:
            if (stalk_x - dinosaur_x) < 850:
                # print('Jump')
                pyautogui.press('space')
