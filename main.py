from mido import MidiFile, MidiTrack, Message, MetaMessage

file_name = input("File path ?")
mid_file = MidiFile(file_name)
result_file = open("result.txt", 'w')
tick_per_beat = mid_file.ticks_per_beat
tempo = 0

for i, track in enumerate(mid_file.tracks):
    print('Track {}: {}'.format(i, track.name))
    result_file.write(str(msg) + "\n")
    for msg in track:
        if isinstance(msg, MetaMessage):
            if msg.type == 'set_tempo':
                tempo = msg.tempo
                

        result_file.write(str(msg) + "\n")
        print(str(msg))
