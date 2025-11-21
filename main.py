import pyautogui
import pyscreeze

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

dinosaur_x = 164
# region = (140, 750, 800 , 672)  # Left, Top, Width, Height
region = (400, 780, 1040 , 620)  # Left, Top, Width, Height
dino_img = './images/Dinosaur.png'
dead_img = './images/DeadDinosaur.png'
stalk_img = './images/CactiStalk.png'
ptera_img = './images/Ptera.png'

alive = True

print("Let's play!")

try:
    dinosaur_x, dinosaur_y = pyautogui.locateCenterOnScreen(dino_img, confidence=0.8, grayscale=True)
    # print(dinosaur_x, dinosaur_y)
except TypeError as e:
    print('Dinosaur missing. Is he dead?')
    try:
        dinosaur_x, dinosaur_y = pyautogui.locateCenterOnScreen(dead_img, confidence=0.8, grayscale=True)
        # print(dinosaur_x, dinosaur_y)
    except TypeError as e:
        print('Go back to the game please...')
        alive = False
    else:
        print("Found him, let's bring him back!")

while alive:
    stalk = pyautogui.locateCenterOnScreen(stalk_img, confidence=0.6, grayscale=True, region=region)
    if stalk is not None:
        stalk_x, stalk_y = stalk
        if stalk_x - dinosaur_x < 800:
            print('Jump')
            pyautogui.press('space')

    ptera = pyautogui.locateCenterOnScreen(ptera_img, confidence=0.6, region=region, grayscale=True)
    if ptera is not None:
        ptera_x, ptera_y = ptera
        if (ptera_x - dinosaur_x) < 800:
            print('Jump')
            pyautogui.press('space')
