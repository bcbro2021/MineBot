import pyautogui
run = True
ms = 0
s = 0
while run:
	pyautogui.keyDown("w")
	pyautogui.keyDown("ctrl")
	ms += 1
	if ms >= 1000000:
		s += 1
		ms = 0
	if s == 10:
		pyautogui.keyUp("w")
		pyautogui.keyUp("ctrl")
		pyautogui.moveTo(500, 0)
		pyautogui.mouseDown(button="right")
		pyautogui.mouseUp(button="right")
		pyautogui.moveTo(-500, 0)
		s = 0