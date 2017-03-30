class Note:
    def __init__(self, time, pitch, velocity, duration):
        self.time = time
        self.pitch = pitch
        self.velocity = velocity
        self.duration = duration
        
    def get_note_array(self):
        return [self.time, self.pitch, self.velocity, self.duration]


class Melody:
    def __init__(self, notes: Note):
        self.notes = notes
        
    @property
    def pitch(self):
        return [x.pitch for x in self.notes]

    @property
    def duration(self):
        return [x.duration for x in self.notes]
    
    def return_midi_array(self):
        return [x.get_note_array() for x in self.notes]
