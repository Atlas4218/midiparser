from mido import MidiFile, MidiTrack, Message, MetaMessage
import tkinter
from tkinter import ttk, StringVar
from tkinter.filedialog import askopenfilename

class GUI:

    def __init__(self, window): 
        # 'StringVar()' is used to get the instance of input field
        self.input_text = StringVar()
        self.input_text1 = StringVar()
        self.path = ''
        self.frame = ''

        window.title("Request Notifier")
        window.resizable(0, 0) # this prevents from resizing the window
        window.geometry("700x300")

        ttk.Button(window, text = "Users File", command = lambda: self.set_path_users_field()).grid(row = 0, ipadx=5, ipady=15) # this is placed in 0 0
        ttk.Entry(window, textvariable = self.input_text, width = 70).grid( row = 0, column = 1, ipadx=1, ipady=1) # this is placed in 0 1

        ttk.Label(window, text="Frames par secondes").grid(row=1, ipadx=5, ipady=1)
        ttk.Entry(window, textvariable = self.input_text1, width = 70).grid( row = 1, column = 1, ipadx=1, ipady=1) # this is placed in 0 1

        ttk.Button(window, text = "Ok", command = lambda: self.close()).grid(row = 2, ipadx=5, ipady=15) # this is placed in 0 0

    def set_path_users_field(self):
        self.path = askopenfilename() 
        self.input_text.set(self.path)

    def set_path_Enova_field(self):
        self.frame = askopenfilename()
        self.input_text1.set(self.frame)

    def get_mid_path(self): 
        return self.path

    def get_frame_per_sec(self):
        return self.frame

    def close(self):
        self.path = self.input_text.get()
        self.frame = self.input_text1.get()
        window.destroy()


# Ouverture de la fenetre d'entree
window = tkinter.Tk()
gui = GUI(window)
window.mainloop()

# Recuperation des donnees entrees par l'utilisateur
file_name = gui.get_mid_path()
frames_per_second  = int(gui.get_frame_per_sec(), 10)

# Ouverture des fichiers d'entree/sortie
mid_file = MidiFile(file_name)
result_file = open("result.txt", 'w')

# Recuperation des donnees generales au fichier
tick_per_beat = mid_file.ticks_per_beat
tempo = 0
result_file.write('Nb frames par secondes: {}\n'.format(frames_per_second))
# Parcours des tracks
for i, track in enumerate(mid_file.tracks):
    time = 0
    print('Track {}: {}'.format(i, track.name))
    result_file.write("Type\tTime\tValue\n")
    for msg in track: # Parcours d'une track
        time += msg.time
        if isinstance(msg, MetaMessage):
            if msg.type == 'set_tempo': # changement de tempo
                tempo = msg.tempo
            if (msg.type == 'end_of_track'): # fin de track
                result_file.write('{}\t{}\n'.format(msg.type,  frames_per_second * (time * tempo) / tick_per_beat / 1000000))  
        if (msg.type == 'note_on'):
            if (msg.velocity > 0): # filtre des notes non muettes
                result_file.write('{}\t{}\t{}\n'.format(msg.type, frames_per_second * (time * tempo) / tick_per_beat / 1000000, msg.note))  
        print(str(msg))
result_file.close()


# Utilisation: renvoie une liste, parametre, nom du fichier
def get_frames(file_name):
    file = open(file_name, 'r')
    f_line = file.readline()
    word = f_line.split(' ')
    nb_frames = int(word[1])
    file.readline()
    result = []
    for line in file:
        words = line.split('\t')
        type = words[0]
        time = words[1]
        note = 0
        if (type == "note_on"):
            note = words[2]
        if (note > 0):
            result += [float(time)]
    file.close()
    return result, nb_frames