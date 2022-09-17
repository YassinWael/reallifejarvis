


from time import sleep


main_volume = 30
music_stopped = False
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

                def pause_music():

                    musical.set_pause(1)
                    global music_stopped
                    music_stopped = True
                    print(music_stopped)
                
                def play_music():
                    musical.play()
                    global music_stopped
                    music_stopped = False

                    print(music_stopped)
                if music_stopped is False:
                    root = Tk()   
                    root.geometry('600x600')
                    root.title('Music Player')
                    root.iconbitmap("Photos\\jarvis.png")
                    root.config(bg='blue') 

                get_song_length()
                
                
                

                button = Button(root, text="Next!", command=destroyer, bg='cyan')
                button.config(height=50, width=5)
                button.pack(side='left')

                button = Button(root, text='Click me to play!', command=play_music, bg='green')
                button.config(height=7, width=80)
                button.pack(side=BOTTOM)

                button = Button(root, text='Click me to stop!', command=pause_music, bg='red')
                button.config(height=7, width=80)
                button.pack(side=TOP)

                button = Button(root, text='Quit', command=quit2, bg='pink' )
                button.config(height=100, width=5)
                button.pack(side='right')

                tkinter_input = Entry(root, width=3, bg='white', fg='black')
                tkinter_input.pack()
           
                

                button = Button(root, text='go',command=change_volume)
                button.pack()

                
                label1 = Label(text=f'playing {d}', bg='yellow')
                label1.config(height=10, width=30)
                label1.pack()
                root_sleep = song_length * 1000
                
                music_player(f"{path}//{d}")
                if music_stopped is False:
                    root.after(root_sleep,destroyer)
                    root.mainloop()
                    
                    print("its ws here")
                    sleep(0.2)
                else:
                    
                    print("it is True")
                    
                musical.stop()
                
                   
                        
                    

            except Exception as e:
                print(e)
random_music()