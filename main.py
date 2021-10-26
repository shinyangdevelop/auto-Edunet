import pyautogui

# print(pyautogui.pixelMatchesColor(1224, 334, (236, 240, 241)))
# print(pyautogui.pixelMatchesColor(1210, 337, (255, 255, 255)))

while True:
    if pyautogui.locateOnScreen("images/x_button.png") is not None:
        pyautogui.click(pyautogui.locateOnScreen("images/x_button.png"))
    if pyautogui.pixelMatchesColor(1224, 334, (236, 240, 241)) and pyautogui.pixelMatchesColor(1210, 337, (255, 255, 255)):
        pyautogui.click(1224, 334)
        break
