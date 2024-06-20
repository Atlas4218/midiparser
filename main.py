from mido import MidiFile, MidiTrack, Message, MetaMessage

file_name = input("File path ?")
mid_file = MidiFile(file_name)
result_file = open("result.txt", 'w')
tick_per_beat = mid_file.ticks_per_beat
tempo = 0
time = 0
for i, track in enumerate(mid_file.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        time += msg.time
        if isinstance(msg, MetaMessage):
            if msg.type == 'set_tempo':
                tempo = msg.tempo
            if (msg.type == 'end_of_track'):
                result_file.write(msg.type + "\t" + str((time * tempo) / tick_per_beat / 1000000) + "\n")    
        if (msg.type == 'note_on'):
            if (msg.velocity > 0):
                result_file.write(msg.type + "\t" + "\t" + str((time * tempo) / tick_per_beat / 1000000) + str(msg.note) + "\n")
        print(str(msg))
