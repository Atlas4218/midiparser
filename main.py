from mido import MidiFile, MidiTrack, Message, MetaMessage
import tkinter
from GUI import *


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
    #print('Track {}: {}'.format(i, track.name))
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
                result_file.write('{}\t{}\t{}\n'.format(msg.type, frames_per_second * ((time * tempo) / tick_per_beat / 1000000), msg.note))  
        #print(str(msg))
result_file.close()



# Utilisation: renvoie nombre de frames/secondes et listes de frames, parametre, nom du fichier, appel "nb_frames, list_frames = get_frames(filename)"
def get_frames(file_name):
    file = open(file_name, 'r')
    f_line = file.readline()
    word = f_line.split(':')
    nb_frames = int(word[1])
    file.readline()
    result = []
    for line in file:
        words = line.split('\t')
        type = words[0]
        time = words[1]
        note = 0
        if (type == "note_on"):
            note = int(words[2])
        if (note > 0):
            result += [float(time)]
    file.close()
    return result, nb_frames

#exemple
list, nb_frames = get_frames("result.txt")
print(list)