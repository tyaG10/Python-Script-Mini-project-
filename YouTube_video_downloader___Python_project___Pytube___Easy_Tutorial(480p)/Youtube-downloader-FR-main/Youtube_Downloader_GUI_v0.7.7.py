'''
Auteur: La mouche
https://github.com/lamouchedu94/Youtube-downloader-FR
Permet de télécharger des vidéos Youtube avec une interface.
'''

from pytube import YouTube
import pytube, string,time,os,subprocess, threading, json,shutil
#from tkinter import Tk, Entry, Frame, Label, END, Button, ACTIVE, Checkbutton, IntVar, Listbox, Menu, LEFT, BOTTOM,HO RIGHT, TOP, GROOVE, SOLID, X, Y, YES
from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *
from pytube.contrib.playlist import Playlist

try :                               #essaye d'importer la librairie ffmpeg
    import ffmpeg
    ffmpeg_install = "False"        
except :
    print("ffmpeg ne peut pas être importé.")
    showwarning("ffmpeg Warning", "ffmeg-python n'est pas installé ! vous pourez seulement choisir entre la 360p et la 720p !")
    ffmpeg_install = "True"


def initialisation():
    '''
    Cette fonction regarde si le fichier de config est correct 
    '''
    
    try :
        os.stat("./config_Yt.json")
        with open('./config_Yt.json', 'r') as fichier:
            data = json.load(fichier)
            if data["mp3_file"] == "False" or data["mp3_file"] == "True"  :
                pass
            else :
                data["mp3_file"] = "False"
            if data["history"] == "False" or data["history"] == "True" :
                pass
            else :
                data["history"] = "False"
        with open('./config_Yt.json', 'w') as fichier:
            json.dump(data, fichier, sort_keys=False, indent=5,ensure_ascii=False) 
            fichier.close()
        if data["directory"] == "" :
            changement_repertoire_telechargement_GUI()             
    except: 
        with open("config_Yt.json","a", encoding='utf8') as file :
            file.close

def check_ffmpeg():                                             #execute commande ffmpeg -version pour voir si ffmpeg est installé 
    test_ffmpeg = os.system("ffmpeg -version")
    print("\n")
    if test_ffmpeg == 1 :
        print("Attention ! ffmpeg n'étant pas installé, les définitions proposées seront seulment : 360p et 720p.")
        showwarning("ffmpeg Warning", "ffmpeg n'étant pas installé, les définitions proposées seront seulment : 360p et 720p !")
        ffmpeg_not_installed = "True"
    else :
        ffmpeg_not_installed = "False"
    return ffmpeg_not_installed
check_ffmpeg()

def video_title(url) :
    yt = YouTube(url)
    titre = yt.title
    for i in range(32) :
        titre_modifie = titre.replace(string.punctuation[i], " ")
        titre = titre_modifie
    return titre_modifie

class Download_merge :
    def __init__(self) :
        pass
    
    def download_low_def(self, url,resol,chemin,titre) :                        #Télécharger en 360p et 720p uniquement (les autres def n'ont pas d'audio)
        format = get_gpu()
        if format == "False" :
            youtube = pytube.YouTube(url)
            video = youtube.streams.filter(res=resol).first()
            video.download(chemin,filename= video_title(url)+ ".mp4")
        else :
            chemin_audio = chemin + "\\audio_only"
            youtube = pytube.YouTube(url)
            t=youtube.streams.filter(only_audio=True).all()
            t[0].download(chemin_audio, filename= titre + ".mp3")
            
            try :
                os.remove(chemin + "\\" +titre + ".mp3")
            except :
                pass
            shutil.move(chemin_audio,chemin)
    def merge_video_audio(self, titre, chemin, resol) :                   #Utilise ffmpeg pour coller piste audio/vidéo         
            
            format = get_gpu()
            chemin_sans_backslash = chemin.replace("\\","/")

            if format == "False" :
                input_video = ffmpeg.input(chemin_sans_backslash+'/video_only/video.mp4')
                input_audio = ffmpeg.input(chemin_sans_backslash+'/audio_only/audio.mp3')
                ffmpeg.output(input_video, input_audio, chemin_sans_backslash + "/" + titre + '.mp4', codec='copy').run()
            else :
                input_audio = chemin_sans_backslash+'/audio_only/audio.mp3'
                #input_audio = input_audio.replace("/","\\")
                shutil.move(input_audio,chemin)
                try :
                    os.remove(chemin + "\\" +titre + ".mp3")
                except :
                    pass
                os.rename(chemin + "\\audio.mp3", chemin + "\\" +titre + ".mp3")

    def download_high_def(self, url, resol, chemin,titre) :               #Télécharger dans toutes les définitions sauf 360p et 720p avec audio
        chemin_audio = chemin + "\\audio_only"
        chemin_video = chemin + "\\video_only"
        format = get_gpu()
        youtube = pytube.YouTube(url)
        video = youtube.streams.filter(res=resol).first()
        try :
            if format == "False" :
                video.download(chemin_video, filename= "video.mp4")
        except  :
            if format == "False" :
                print("Erreur : Essayez de changer la définition.")
                showerror("Erreur", "la définition demandé n'existe pas pour cette vidéo. La définition choisie par défaut est 144p.")
                video = youtube.streams.filter(res="144p").first()
                video.download(chemin_video, filename= "video.mp4")

        youtube = pytube.YouTube(url)
        t=youtube.streams.filter(only_audio=True).all()
        t[0].download(chemin_audio, filename= "audio.mp3")

        print("début de l'assemblage des pistes.")
        time.sleep(2)
        #merge_video_audio(titre, chemin, resol)

def hist(cochee) :
    #cochee a deux valeurs
    # 0 = False
    # 1 = True 
    with open('./config_Yt.json', 'r') as fichier:
        data = json.load(fichier)
    if cochee == 1 :
        data["history"] = "True"
    if cochee == 0 :
        data["history"] = "False"
    
    with open('./config_Yt.json', 'w') as fichier:
            json.dump(data, fichier, sort_keys=False, indent=5,
              ensure_ascii=False)    

def checkbutton_mp3(cochee):
    with open('./config_Yt.json', 'r') as fichier:
        data = json.load(fichier)
    if cochee == 1 :
        data["mp3_file"] = "True"
    if cochee == 0 :
        data["mp3_file"] = "False"
    with open('./config_Yt.json', 'w') as fichier:
        json.dump(data, fichier, sort_keys=False, indent=5,
          ensure_ascii=False)    

def json_config() :

    with open('./config_Yt.json', 'r') as fichier:
        data = json.load(fichier)
        fichier.close
    return data

def get_gpu() :
    data = json_config()
    file_extention = data["mp3_file"]
    return file_extention
def get_history() :
    data = json_config()
    history = data["history"]
    return history
def get_path() :
    data = json_config()
    path = data["directory"]
    return path

def low_download(url, video_title, resol):
    chemin = get_path()
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(res=resol).first()
    video.download(chemin,filename= video_title(url))

def high_download(url, resol):
    chemin = get_path()
    chemin_audio = chemin + "\\audio_only"
    chemin_video = chemin + "\\video_only"
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(res=resol).first()
    try :
        video.download(chemin_video, filename= "video.mp4")
    except  :
        print("Erreur : Essayez de changer la définition.")
        showerror("Erreur", "la définition demandé n'existe pas pour cette vidéo. La définition choisie par défaut est 144p.")
        video = youtube.streams.filter(res="144p").first()
        video.download(chemin_video, filename= "video.mp4")
    youtube = pytube.YouTube(url)
    t=youtube.streams.filter(only_audio=True).all()
    t[0].download(chemin_audio, filename= "audio.mp3")

def changement_repertoire(user_path) :                          #permet de changer de répertoire après validation sur l'interface graphique
    try :
        os.stat(user_path)
        with open('./config_Yt.json', "r") as fichier :
            data = json.load(fichier)
            print(user_path)
            data["directory"] = user_path
        with open('./config_Yt.json', 'w') as fichier:
            json.dump(data, fichier, sort_keys=False, indent=5,ensure_ascii=False)   
            fichier.close()
        showinfo("info", "Le répertoire à bien été définit.")
        return user_path
    except :
        showerror("Erreur", "Le répertoire de téléchargement n'existe pas ! Merci de changer le répertoire dans : fichier > changer répertoire téléchargement.")
        return 1


def changement_repertoire_telechargement_GUI() :            #Fenetre pour chnager le répertoire 
    def intermediaire() : 
        repertoire = entry2.get()
        if changement_repertoire(repertoire) != 1:
            fenetre2.destroy()
            return repertoire
    path3 = get_path()
    path3 = str(path3)
    print(path3)
    
    fenetre2 = Tk()
    fenetre2.title("Répertoire téléchargement")
    fenetre2.geometry('480x250')
    fenetre2.minsize(480, 250)
    fenetre2.config(background= '#f9f7f7')
    frame2 = Frame(fenetre2, bg = '#f9f7f7', borderwidth=0)
    label_title1 = Label(frame2, text= "Chemin actuel :", font=("Arial", 15), bg = '#f9f7f7', fg ='#000000')
    label_title1.pack(expand = YES )
    entry3 = Entry(frame2, text= "", font=("Arial", 14), bg = '#ececec', fg ='#000000', relief = SOLID)                                         #25 = taille police , bg = background texte ,  fg = front ground couleur texte.    On peut soit afficher dans la fenêtre soit dans la frame
    entry3.pack(expand = YES,fill=X)
    entry3.delete(0,END)
    entry3.insert(0, path3)
    entry3.config(bg = "#f9f7f7")
    entry3.config(state=DISABLED)
    label_title = Label(frame2, text= "Entrez le répertoire de téléchargement :", font=("Arial", 15), bg = '#f9f7f7', fg ='#000000')
    label_title.pack(expand = YES)
    entry2 = Entry(frame2, text= "", font=("Arial", 14), bg = '#ececec', fg ='#000000', relief = SOLID)                                         #25 = taille police , bg = background texte ,  fg = front ground couleur texte.    On peut soit afficher dans la fenêtre soit dans la frame
    entry2.pack(expand = YES,fill=X)

    button_confirmation = Button(frame2, text = "Confirmer", font=("Arial", 20),bg = "#a8a8a8", borderwidth=0, fg ='#000000',activebackground = "#f7f7f7",highlightcolor = "#00aeff" ,command = intermediaire)                       #après command = mettre fonction
    button_confirmation.pack(fill = X, padx=20, pady=40)

    
    frame2.pack(expand = YES, padx=0, pady=0)
    fenetre2.mainloop()

def hist_GUI(entry_url) :
    with open("history_Yt.txt", "r") as file :
        long_hist = file.readlines()
        file.close
    fenetre3 = Tk()
    fenetre3.title("Historique")
    fenetre3.geometry("875x400")
    fenetre3.minsize(300, 200)
    fenetre3.maxsize(1500, 1500)
    fenetre3.config(background= '#f9f7f7')
    frame3 = Frame(fenetre3, bg = '#f9f7f7', borderwidth=0)
    
    label_title1 = Label(frame3, text= "Voici l'historique :", font=("Arial", 20), bg = '#f9f7f7', fg ='#000000')          #25 = taille police , bg = background texte ,  fg = front ground couleur texte.    On peut soit afficher dans la fenêtre soit dans la frame
    label_title1.pack(padx=0, pady=10)
    nbligne = (len(long_hist)-1) / 2
    nbligne = int(nbligne)
    liste1 = Listbox(frame3,selectbackground = "#a7a7a7",bg = "#f9f7f7", width = 95, font=("Arial", 13),borderwidth=0, height = nbligne)
    ligne = 1
    button = Button(frame3, text = "Télécharger", font=("Arial", 20),bg = "#a8a8a8", borderwidth=0, fg ='#000000',activebackground = "#f7f7f7",highlightcolor = "#00aeff",command=(lambda *args:(hist_download(liste1.get(ACTIVE), fenetre3, entry_url, long_hist))))                       #après command = mettre fonction
    
    try :
        for i in range(len(long_hist)) :
            liste1.insert(i, long_hist[ligne])
            ligne += 2
    except :
        pass
    
    liste1.pack(expand = YES)
    button.pack(fill = X)
    frame3.pack(expand = YES)

def hist_download(nom, fenetre3, entry_url, long_hist) :
    nb_ligne = len(long_hist)
    for i in range(nb_ligne) :
        if nom == long_hist[i] :
            url_voulue = long_hist[i + 1]
            break

    entry_url.delete(0, END)
    entry_url.insert(0,url_voulue)
    print(nom)
    fenetre3.destroy() 
    pass

def open_explorer() :
    path = get_path()

    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

    def explore(path):
        # explorer would choke on forward slashes
        path = os.path.normpath(path)

        if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])
        elif os.path.isfile(path):
            subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])
    explore(str(path))

def alerte_chemin_deja_existant(): 
    result = askquestion("Warning","Un fichier ayant le même nom est déjà présent dans le répertoire de téléchargement. Continuer quand même ?", icon = "warning")
    if result == "yes" :
        return("True")
    else :
        return("False")

def playlist(url, resol, entry1, progress, fenetre_principale) :
    Download_m = Download_merge()
    p = Playlist(url)
    showinfo("Début","Il y a "+ str(len(p)) + " vidéo dans la playlist")
    chemin = chemin_for_GUI()
    a = 0
    for i in range(len(p)) :
        url = p[i]
        titre = video_title(url)
        try :
            chemin_video = chemin+"\\"+titre+".mp4"
            os.stat(chemin_video)
            result = alerte_chemin_deja_existant()
            if result == "True" :
                os.remove(chemin_video)
            if result == "False" :
                break
        except :
            pass
        t3 = threading.Thread(target=size, args=(url,resol, entry1, progress, fenetre_principale, titre))
        t3.start()
        if resol == "144p" or resol == "240p" or resol == "480p" or resol == "1080p" or resol == "1440p" or resol == "2160p" or resol == "4320p" :
            try :
                os.remove(chemin + "\\audio_only\\audio.mp3")
                if resol == "1440p" or resol == "2160p" or resol == '4320p' :
                    os.remove(chemin + "\\video_only\\video.mp4")
                else :
                    os.remove(chemin + "\\video_only\\video.mp4")
            except :
                pass
            Download_m.download_high_def(url, resol, chemin, titre)
            Download_m.merge_video_audio(titre, chemin, resol)
            try :
                os.remove(chemin + "\\audio_only\\audio.mp3")
            except : 
                pass
            if resol == "1440p" or resol == "2160p" or resol == '4320p' :
                os.remove(chemin + "\\video_only\\video.mp4")
            else :
                try :
                    os.remove(chemin + "\\video_only\\video.mp4")
                except :
                    pass
        if resol == "360p" or resol == "720p" :
            Download_m.download_low_def(url, resol, chemin, titre)
        entry1.delete(0, END)
        history_Yt_txt(url, titre)
    showinfo("fin", "vidéo téléchargée")
    entry1.delete(0, END)

def history_Yt_txt(url, titre) :
    check = get_history()
    if check[1] == "history = True\n" :
        with open("history_Yt.txt", "r") as file : 
            history = file.readlines()
            provisoire = len(history)
            file.close()
        with open("history_Yt.txt", "w", encoding='utf8') as file : 
            try :
                for i in range(len(history)) :
                    file.write(history[i])
            except :
                pass
            file.write("\n"+titre +"\n"+ url )

def definition_user_choice_and_download(url, resol, entry1, progress, fenetre_principale):                      #appel toutes les fonctions
    Download_m = Download_merge()
    while True :                                                             #Récupérer le choix de l'utulisateur dans la liste.
        if url == "" :
            break
        
        f = "playlist"
        if f in url :
            print("playlist")
            playlist(url, resol, entry1, progress, fenetre_principale)
            break
        else :
            print("pas playlist")
        
        titre = video_title(url)
        chemin = chemin_for_GUI()
        
        try :
            chemin_video = chemin+"\\"+titre+".mp4"
            os.stat(chemin_video)
            result = alerte_chemin_deja_existant()
            if result == "True" :
                os.remove(chemin_video)
            if result == "False" :
                break
        except :
            pass
        try :
            chemin_audio = chemin+"\\"+titre+".mp3"
            os.stat(chemin_audio)
            result = alerte_chemin_deja_existant()
            if result == "True" :
                os.remove(chemin_audio)
            if result == "False" :
                break
        except :
            pass
        t3 = threading.Thread(target=size, args=(url,resol, entry1, progress, fenetre_principale,titre))
        t3.start()
        

        if resol == "144p" or resol == "240p" or resol == "480p" or resol == "1080p" or resol == "1440p" or resol == "2160p" or resol == "4320p" :
            try :
                os.remove(chemin + "\\audio_only\\audio.mp3")
                if resol == "1440p" or resol == "2160p" or resol == '4320p' :
                    os.remove(chemin + "\\video_only\\video.mp4")
                else :
                    os.remove(chemin + "\\video_only\\video.mp4")
            except :
                pass
            Download_m.download_high_def(url, resol, chemin, titre)
            Download_m.merge_video_audio(titre, chemin, resol)
            try : 
                os.remove(chemin + "\\audio_only\\audio.mp3")
            except :
                pass
            if resol == "1440p" or resol == "2160p" or resol == '4320p' :
                os.remove(chemin + "\\video_only\\video.mp4")
            else :
                try :
                    os.remove(chemin + "\\video_only\\video.mp4")
                except :
                    pass
        if resol == "360p" or resol == "720p" :
            Download_m.download_low_def(url, resol, chemin, titre)
        history_Yt_txt(url, titre)
        showinfo("fin", "vidéo téléchargée")
        entry1.delete(0, END)
        break

def wait(url, resol, entry1, progress, fenetre_principale) :
    t2 = threading.Thread(target=definition_user_choice_and_download, args=(url,resol, entry1, progress, fenetre_principale))
    t2.start()

def chemin_for_GUI() :                                          #Regarde si le répertoire de téléchagement existe
    chemin = get_path()
    try :
        if chemin == "" :
            showerror("Erreur", "Le répertoire de téléchargement n'existe pas ! Merci de changer le répertoire dans : fichier > changer répertoire téléchargement.")
            return("False")
    except :
        pass
    try :
        os.stat(chemin)
    except :
        print("le chemin définit n'existe pas !!!")
        showerror("Erreur", "Le répertoire de téléchargement n'existe pas ! Merci de changer le répertoire dans : fichier > changer répertoire téléchargement.")
        return("False")
    try :
        os.mkdir(chemin+ "\\audio_only")
        os.mkdir(chemin+ "\\video_only")
    except :
        pass
    return chemin

def size_playlist(url,resol,progress,fenetre_principale,titre):
    for i in range(1):
        try:
            youtube = Playlist(url)
        except:
            pass
        for i in range(len(youtube)):
            video = youtube[i].streams.filter(res=resol).first()
            taille = video.filesize
            chemin = chemin_for_GUI()

          

def size(url, resol, entry1, progress, fenetre_principale,titre) :
    for i in range(1) :
        try :
            youtube = pytube.YouTube(url)
        except :
            break
        video = youtube.streams.filter(res=resol).first()
        taille = video.filesize
        chemin = chemin_for_GUI()
        count = 0
        while True :
            try :
                time.sleep(0.5)
                if resol == "360p" or resol == "720p" :
                    en_cours = os.stat(chemin + "\\" + titre + ".mp4").st_size
                else :
                    try :
                        en_cours = os.stat(chemin + "\\video_only\\video.mp4").st_size
                    except :
                        en_cours = os.stat(chemin + "\\video_only\\video.mp4").st_size
                pourcentage = (en_cours/taille)*100
                pourcentage = round(pourcentage,1)
                progress['value']= pourcentage
                fenetre_principale.update_idletasks()
                
                if pourcentage == 0 :
                    count += 1
                if count >= 10 :
                    print("le téléchargement à planté !")
                entry1.delete(0, END)
                entry1.insert(0, str(pourcentage) + "%")
                entry1.config(bg ='#ececec')
                print(str(pourcentage)+ "%")
                
                if pourcentage >= 100 :
                    pourcentage = 0
                    progress['value']= pourcentage
                    entry1.delete(0, END)
                    entry1.insert(0, "Merci de patienter")
                    entry1.config(bg = '#f9f7f7', fg ='#000000',borderwidth=0)
                    break
            except :
                entry1.delete(0, END)
                entry1.insert(0, "none")


def fenetre_principale() :
    
    fenetre_principale = Tk()
    fenetre_principale.title("Youtube downloader")
    fenetre_principale.geometry('500x240')
    fenetre_principale.minsize(500, 240)
    fenetre_principale.config(background= '#f9f7f7')

    frame_p = Frame(fenetre_principale,bg = '#f9f7f7')
    menubar = Menu(fenetre_principale)
    menu1 = Menu(menubar, tearoff=0)

    menu1.add_command(label="Changer répertoire téléchargement", command = changement_repertoire_telechargement_GUI)
    menu1.add_command(label="Consulter historique", command = (lambda *args: (hist_GUI(entry_url) )))
    menu1.add_separator()
    menu1.add_command(label="Emplacement vidéo", command = open_explorer)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=fenetre_principale.quit)
    menubar.add_cascade(label="Fichier", menu=menu1)
    
    label_title = Label(frame_p, text = "Entrez l'url et choisissez la définition voulue :",font=("Arial", 18), bg = '#f9f7f7', fg ='#000000')
    label_title.pack(fill = X)

    entry_url = Entry(frame_p, font=("Arial", 11),width = 60,bg = '#ececec', fg ='#000000', relief = SOLID )
    entry_url.pack()

    if get_gpu() == 'False' :
        cochee = IntVar(value= 0)
    else :
        cochee = IntVar(value= 1)

    if check_ffmpeg() == "True":
        liste = Listbox(frame_p,selectbackground = "#a7a7a7",bg = "#f9f7f7", width = 6, font=("Arial", 13),borderwidth=0, height = 2)
        liste.insert(1, "360p")
        liste.insert(2, "720p")
        liste.pack(side = LEFT)
    else :
        liste = Listbox(frame_p,selectbackground = "#a7a7a7",bg = "#f9f7f7", width = 6, font=("Arial", 13),borderwidth=0, height = 9)
        liste.insert(1, "144p")
        liste.insert(2, "240p")
        liste.insert(3, "360p")
        liste.insert(4, "480p")
        liste.insert(5, "720p")
        liste.insert(6, "1080p")
        liste.insert(7, "1440p")
        liste.insert(8, "2160p")
        liste.insert(9, "4320p")   #NE SUPORTE PAS LE REENCODAGE EN 8K provisoirement enlevée. Cette config de ffmpeg ne surporte pas la 8k 
        
        case = Checkbutton(frame_p, text= "Fichier mp3",font=("Arial", 13),bg = '#f9f7f7',activebackground = '#f9f7f7', onvalue=1, offvalue=0, variable = cochee, command = (lambda *args:(checkbutton_mp3(cochee.get()))))
        liste.pack(side = LEFT)
        case.pack()
    
    if get_history() == "False" :
        cochee_hist = IntVar(value = 0)
    else : 
        cochee_hist = IntVar(value = 1) 
    
    case2 = Checkbutton(frame_p, text= "Historique",font=("Arial", 13),bg = '#f9f7f7',activebackground = '#f9f7f7', onvalue=1, offvalue=0, variable = cochee_hist, command =(lambda *args:(hist(cochee_hist.get()))))
    case2.pack()

    button = Button(frame_p, text = "Télécharger", font=("Arial", 20),bg = "#a8a8a8", borderwidth=0, fg ='#000000',activebackground = "#f7f7f7",highlightcolor = "#00aeff",command=(lambda *args: (wait(entry_url.get(),liste.get(ACTIVE), entry1, progress, fenetre_principale ))))                       #après command = mettre fonction
    button.pack(fill = X, padx=20, pady=15)
    
    progress=Progressbar(frame_p,orient=HORIZONTAL,length=425,mode='determinate')
    progress.pack()

    entry1 = Entry(frame_p, text= "", font=("Arial", 15), bg = '#f9f7f7', fg ='#000000',width= 35, borderwidth=0)                                         #25 = taille police , bg = background texte ,  fg = front ground couleur texte.    On peut soit afficher dans la fenêtre soit dans la frame
    entry1.pack(side = TOP)
    
    fenetre_principale.config(menu=menubar)
    frame_p.pack(expand = YES, padx=0, pady=0)
    fenetre_principale.mainloop()
initialisation()
fenetre_principale()
t1 = threading.Thread(target=fenetre_principale())
t1.start()