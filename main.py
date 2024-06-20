from mido import MidiFile, MidiTrack, Message, MetaMessage

file_name = ""
mid_file = MidiFile(file_name)
result_file = open("result.txt", 'w')
tick_per_beat = mid_file.ticks_per_beat
tempo = 0
for i, track in enumerate(mid_file.tracks):
    time = 0
    print('Track {}: {}'.format(i, track.name))
    result_file.write("Type\tTime\tValue\n")
    for msg in track:
        time += msg.time
        if isinstance(msg, MetaMessage):
            if msg.type == 'set_tempo':
                tempo = msg.tempo
            if (msg.type == 'end_of_track'):
                result_file.write('{}\t{}\n'.format(msg.type, (time * tempo) / tick_per_beat / 1000000))  
        if (msg.type == 'note_on'):
            if (msg.velocity > 0):
                result_file.write('{}\t{}\t{}\n'.format(msg.type, (time * tempo) / tick_per_beat / 1000000, msg.note))  
        print(str(msg))
