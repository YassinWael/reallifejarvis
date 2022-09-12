import urllib.request

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
print( 'connected successfully' if connect() else 'no internet!' )
if connect() is False:
    from tkinter import messagebox
    messagebox.showwarning(title="Internet Error", message="No Internet Was Detected Some Services Won't work")


