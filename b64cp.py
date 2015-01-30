import sys
import base64

try:
	from Tkinter import Tk
except ImportError:
	from tkinter import Tk


def encodeToBase64(originalString):
	return base64.b64encode(originalString).encode("utf-8")

def runner():
	tk = Tk()
	tk.withdraw()
	originalString = ''
	if len(sys.argv) == 1:
		originalString = tk.selection_get(selection = "CLIPBOARD")
	else:
		originalString = sys.argv[1]
	tk.clipboard_clear()
	tk.clipboard_append(encodeToBase64(originalString))
	tk.destroy()
	
runner()