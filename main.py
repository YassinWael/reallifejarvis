try:
    print("hello git")
    from os import startfile
    startfile('internet_connection.py')
    import cv2
    from cvzone.HandTrackingModule import HandDetector

    try:
        from playsound import playsound
        if __name__ == '__main__':
            from threading import Thread
            t1 = Thread(target=lambda:playsound("sounds\\ready.wav"))
            t1.start()
        from pyttsx3 import init
        from random import choice
        from speech_recognition import Recognizer, Microphone
        from datetime import datetime
        from pyautogui import hotkey,leftClick,press
        from time import sleep
        from webbrowser import open
        from threading import Timer
        from sys import setrecursionlimit,exit
       
        
        setrecursionlimit(999999999)
        import win32process
        import ctypes
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()      
        if hwnd != 0:      
            ctypes.windll.user32.ShowWindow(hwnd, 0)      
            ctypes.windll.kernel32.CloseHandle(hwnd)
            _, pid = win32process.GetWindowThreadProcessId(hwnd)

        from kivy.app import App
        from kivy.uix.boxlayout import BoxLayout
        from kivy.lang import Builder
        from kivy.uix.widget import Widget
        from kivy.config import Config
        Config.set('graphics', 'resizable', False)
        


    except Exception as e:
        from pyttsx3 import init
        print(e)
        engine = init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)


        def speak(s): 

            engine.say(s)
            engine.runAndWait()


        speak(f"in imports{e}")
    today_date = datetime.now()

    hwnd = ctypes.windll.kernel32.GetConsoleWindow()      

    Builder.load_file("main.kv")



    engine = init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)


    def speak(s):  # the function that speaks

        engine.say(s)
        engine.runAndWait()


    def get_audio(printorno=True):  # function that recognizes speech

        r = Recognizer()
        with Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=6)
            if printorno is True:
                update_text(text_to_update="Talk Now Please")
                playsound("sounds\\Siri.mp3")
            else:
                update_text(text_to_update="Talk Now Please")

            try:

                audio = r.listen(source, timeout=5)
            except Exception:
                pass

            said = ""
            try:

                said = r.recognize_google(audio)
                said = said.lower()

            
            except Exception as Error:
                pass

        return said



    day = today_date.strftime("%A")


    def get_song_by_lyrics():
        from clipboard import paste
        from urllib.request import Request, urlopen
        from bs4 import BeautifulSoup
        from pyautogui import write,press
        speak('please say a part of the lyrics')
        lyrics = get_audio(printorno=True)
        open('https://songsear.ch')
        sleep(5)
        leftClick(x=568, y=270)
        sleep(1)
        write(lyrics)
        press('enter')
        leftClick(x=608, y=52)
        hotkey('ctrl', 'c')
        website = paste()

        req = Request(website)
        html_page = urlopen(req)

        soup = BeautifulSoup(html_page, "lxml")

        links = []
        for link in soup.findAll('a'):
            links.append(link.get('href'))
        full_link = str(links[3])
        split_link = full_link.split('/')
        
        speak(f'The song is called {split_link[3]}')
        speak(f'and the author is called {split_link[2]}')



    


    def dictionary():
        from PyDictionary import PyDictionary
        split_mean = text.split('does')[1]
        word1 = str(split_mean.split('mean')[0])
        
        global dc
        dc = PyDictionary()
        meaning = dc.meaning(word1)
        speak(meaning)
        

    main_volume = 30

    playing = True
    def random_music():
        
        from vlc import MediaPlayer
        from tkinter import Tk, Button, Label, BOTTOM, TOP,Entry
        from mutagen.mp3 import MP3
        from random import choice
        from os import listdir
        global musicplayer
        def music_player(song):
            try:
                global musical
                musical = MediaPlayer(song)
                global main_volume
                musical.audio_set_volume(main_volume)
                musical.play()

            except Exception as e:
                print(e)

        global path, d
        path = "musicfiles"
        files = listdir(path)
    
    
        i = 0
        while True:
            try:
                i += 1
                d = choice(files)
                if len(files) == 1:
                    path = "musicfiles"
                    files = listdir(path)
                

                else:
                    files.remove(d)
                    

                def get_song_length():
                    audio = MP3(f"{path}//{d}")
                    global song_length
                    song_length = int(audio.info.length)
                

                def quit2():
                    global playing
                    playing = False
                    musical.pause()
                    Timer(1.0,checker).start()
                    root.destroy()
                    quit()
                    
                def change_volume():
                    global main_volume
                    main_volume = int(tkinter_input.get())
                    
                    musical.audio_set_volume(main_volume)
                    volume_level = Label(root, text=f"volume is {tkinter_input.get()}", bg='green')
                    volume_level.pack()

                def destroyer():
                    root.destroy()

                    
                root = Tk()    

                get_song_length()
                
                
                root.geometry('600x600')
                root.title('Music Player')
                root.iconbitmap("Photos\\jarvis.png")
                root.config(bg='blue')

                button = Button(root, text="Next!", command=destroyer, bg='cyan')
                button.config(height=50, width=5)
                button.pack(side='left')

                button = Button(root, text='Click me to play!', command=lambda: musical.play(), bg='green')
                button.config(height=7, width=80)
                button.pack(side=BOTTOM)

                button = Button(root, text='Click me to stop!', command=lambda: musical.set_pause(1), bg='red')
                button.config(height=7, width=80)
                button.pack(side=TOP)

                button = Button(root, text='quit', command=quit2, bg='pink' )
                button.config(height=100, width=5)
                button.pack(side='right')

                tkinter_input = Entry(root, width=3, bg='white', fg='black')
                tkinter_input.pack()
                print("hi")
                

                button = Button(root, text='go',command=change_volume)
                button.pack()

                
                label1 = Label(text=f'playing {d}', bg='yellow')
                label1.config(height=10, width=30)
                label1.pack()
                root_sleep = song_length * 1000
                
            
                music_player(f"{path}//{d}")
                root.after(root_sleep,destroyer)
                root.mainloop()
                musical.stop()
                
            

            except Exception as e:
                print(e)
                


    

  
    def searchmodule():
        from pywhatkit import search
        if "search" in text:
            splitted_text = text.split('search')
        elif "sir" in text:
            splitted_text = text.split('sir')
        elif "share" in text:
            splitted_text = text.split('share')
        else:
            splitted_text = ''
        
        try:
            search(splitted_text[1])
            sleep(10)

        except ValueError:
            speak("couldn't find what to search")





    def get_input(*args):
        global text
        text = get_audio().lower()

    paused = False

    
    i=0
    greetings = ["hello","hi","what's up", "how's everything going?" , "how are things?",  "how's life?","good morning"]
    def checker(*args):

            stopped = False
            
            while True: 
                while not stopped:
                 
                    get_input()
                    global text
                    Refresher()
                    global i
                    if i ==5:
                        stopped = True
                    if len(text)!=0:
                        for phrase in greetings:
                            if phrase in text:
                                greeting = True
                                break
                            else:
                                greeting = False
                    global paused
                    if paused is True:
                        stopped = True 
                        speak('stopped')
                    if len(text)==0:
                        playsound("sounds\\no_input.mp3")
                        i+=1
                    
                    elif greeting is True:
                        update_status('greeting')
                        reply = ['morning','how is it going','whats up','how are you','good to see you','hello']
                        speak(f'{choice(reply)} sir')
                
                    elif 'timer' in text:
                        split = text.split(" ")
                        print(split)
                        found = False
                        for x in split:
                            try:
                                integer = int(x)
                                print(integer)
                                found = True
                            except Exception as e:
                                print("this is not an int number")
                                found = False
                            if found is True:
                                speak(f"creating a timer for {integer}")
                                if "minute" in text or  "minutes" in text:
                                    sleep(integer * 60)
                                    print(integer * 60)
                                    open("https://www.youtube.com/watch?v=NgM_CjqpWQY&ab_channel=GoMusically")
                                    open("https://www.youtube.com/watch?v=NgM_CjqpWQY&ab_channel=GoMusically")
                                    open("https://www.youtube.com/watch?v=NgM_CjqpWQY&ab_channel=GoMusically")
                                    startfile("musicfiles\\Fight Back.mp3")
                                elif "hour" in text or "hours":
                                    sleep(integer * 3660)
                                    print(integer * 3660)
                                    open("https://www.youtube.com/watch?v=NgM_CjqpWQY&ab_channel=GoMusically")
                                    open("https://www.youtube.com/watch?v=NgM_CjqpWQY&ab_channel=GoMusically")
                                    open("https://www.youtube.com/watch?v=NgM_CjqpWQY&ab_channel=GoMusically")
                                    startfile("musicfiles\\Fight Back.mp3")
                                else:
                                    sleep(integer)
                                    open("https://www.youtube.com/watch?v=NgM_CjqpWQY&ab_channel=GoMusically")
                                    
                                    open("https://www.youtube.com/watch?v=NgM_CjqpWQY&ab_channel=GoMusically")
                                    open("https://www.youtube.com/watch?v=NgM_CjqpWQY&ab_channel=GoMusically")
                                    startfile("musicfiles\\Fight Back.mp3")
                                

                    elif 'stop' in text or 'top' in text:

                        stopped = True
                        playsound("sounds\\jarvis_listen.mp3",block=False)
                        update_status('Stopped')
                        break
                    
                    elif 'lyrics' in text or 'song' and 'called' in text:
                        get_song_by_lyrics()
                    

                    elif 'read' in text:
                        from clipboard import paste
                    
                        speak('reading...')
                        sleep(2)
                        hotkey('ctrl', 'c')

                        hotkey('ctrl', 'c')
                        
                        text_to_read = paste()
                    
                        speak(text_to_read)

                    elif 'recycle' in text or 'empty' in text:
                        from winshell import recycle_bin
                        speak('recycling bin')
                        recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                    elif 'mean' in text:
                        dictionary()
                    elif 'shut down' in text or 'shutdown' in text:
                        from os import system
                        hotkey('alt', 'f4')
                        hotkey('alt', 'f4')
                        hotkey('alt', 'f4')
                        system("shutdown /s /t 5")

                    elif 'phone' in text:
                        speak('calling the phone')
                        open('https://myaccount.google.com/find-your-phone?continue=https://myaccount.google.com/?utm_source'
                            '%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%26pli%3D1')
                        sleep(13)
                        leftClick(601, 446)
                        sleep(2)
                        leftClick(225, 415)
                        speak('called')
                    elif "search" in text or "sir" in text or "share" in text:
                        searchmodule()
                    elif "music" in text:
                        update_status("Playing music")
                        random_music()
                    elif 'minecraft' in text or 'game' in text:
                        from os import startfile
                        
                        try:
                            speak('opening minecraft')
                            startfile(r'C:\\Users\\Dr.Wael\\AppData\\Roaming\\.tlauncher\\mcl\\Minecraft\\TL.exe')
                            sleep(52)
                            leftClick(x=658, y=444)
                        except Exception as e:
                            pass
                    elif "month" in text:
                        month = today_date.strftime("%B")
                        speak(month)
                    
                    elif "year" in text:
                        year = today_date.strftime("%Y")
                        speak(year)
                    
                    elif "day" in text:
                        day = today_date.strftime("%A")
                        speak(day)
                    
                    elif 'time' in text:
                        hour = today_date.strftime("%I")
                        minutes = today_date.strftime("%M")
                        speak(hour + minutes)

                    elif "name" in text:
                        speak("hi my name is jarvis")

                    elif 'Khan' in text or 'academy' in text or 'Academy' in text or 'khan' in text:
                        open("https://www.khanacademy.org/profile/me/courses")

                    elif 'youtube' in text:
                        open('https://www.youtube.com')

                    elif 'facebook' in text:
                        open('https://www.facebook.com')

                    elif 'whatsapp' in text:
                        open('https://web.whatsapp.com')
                    elif 'discord' in text:
                        open('https://discord.com/channels/@me')
                        
                    elif 'fiverr' in text:
                        open('https://fiverr.com')
                    elif 'gmail' in text or 'mail' in text:
                        open('https://gmail.com')
                    elif 'messenger' in text:
                        open('https://messenger.com')
                    
                    
                    

                    elif 'code' in text:
                        from os import startfile
                        startfile(r'code.lnk')
                        speak('Time to start coding!')
                    
                    else:
                        speak("unknown command")
                    
                q = False
                while stopped is True:
                    update_status('stopped')
                    
                    text = get_audio(printorno=False)
                    Refresher()

                    
                    def hi():
                        print('finger shown')
                        global fing
                        fing = cv2.imread("fingers\\0.jpg")
                        global gesture
                        gesture =True
                    
                        
                       
                    detector = HandDetector(maxHands=1, detectionCon=0.8)
                    video = cv2.VideoCapture(0)
                    finger = 0
                    while True:
                        _, img = video.read()
                        img = cv2.flip(img, 1)
                        hand = detector.findHands(img, draw=False)
                        fing = cv2.imread("fingers\\0.jpg")
                        if hand:
                            lmlist = hand[0]
                            if lmlist:
                                fingerup = detector.fingersUp(lmlist)
                                if fingerup == [0, 1, 0, 0, 0] or fingerup == [0, 0, 0, 0, 1] :
                                    hi()
                                    q = True
                        fing = cv2.resize(fing, (220, 280))
                        img[50:330, 20:240] = fing
                        cv2.imshow("Video", img)

                        print(f'This is {q}')
                        if q is True:
                            print('q is True')
                            break
                        
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                        if q is True:
                            print('q is True')
                            break
                            
                    video.release()
                    cv2.destroyAllWindows()


                    if 'listen' in text or 'jarvis' in text or "wake" in text or gesture is True:
                        playsound("sounds\\ready.mp3",block = False)
                        update_status('listening')
                        stopped = False
                        paused = False
                        print('listen or jarvis')
                    
                    



    class TestWidget(BoxLayout,Widget):
        def Terminate(*args,reboot = False):
            from os import startfile
            if reboot is True:
                Timer(25,lambda:startfile(r"TaskKill.lnk")).start()
                exit()
            else:
                Timer(6,lambda:startfile(r"TaskKill.lnk")).start()
                exit()
            

        def Reboot(*args):
            from os import startfile
            startfile('runner.py')
            TestWidget().Terminate(reboot=True)
            

        def Stop(*args):
            global paused
            paused = True
            
        def __init__(self, **args):
            super(TestWidget, self).__init__(**args)
        
            global Refresher
            def Refresher(*args):
                self.ids.label.text = text
            
            global update_text
            def update_text(text_to_update,*args):
                self.ids.label.text=text_to_update

            global update_status
            def update_status(status_text,*args):
                self.ids.status.text=f"status : {status_text}"


        
    class Jarvis(App):

        def build(self):
            
            self.title = "J.A.R.V.I.S"
            
            
            Timer(0.8,checker).start()
            return TestWidget()
            
    if __name__ == "__main__":
        t1.join()
        
        Jarvis().run()
except Exception as e:
        from tkinter import messagebox
        messagebox.showwarning(title="Fatal Error", message=e)

