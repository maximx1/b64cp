import sys
import base64
import os
from threading import Thread

try:
	from Tkinter import Tk
except ImportError:
	from tkinter import Tk
	
def encodeToBase64(originalString):
	return base64.b64encode(bytes(originalString, "utf-8")).decode("utf-8")

def unicornMethod(cp, b64string):
	cp.clipboard_clear()
	cp.clipboard_append(b64string)
	cp.destroy()
	
def windowsSpecificAlternative(b64string):
	os.system("echo " + b64string + " | clip")
	
def unicornMethod():
	cp = Tk()
	cp.withdraw()
	originalString = ""
	if len(sys.argv) == 1:
		originalString = cp.selection_get(selection = "CLIPBOARD")
	else:
		originalString = sys.argv[1]
	b64string = encodeToBase64(originalString)
	windowsSpecificAlternative(b64string)

unicornMethod()