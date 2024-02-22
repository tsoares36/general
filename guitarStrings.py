
class myGuitar():
    def __init__(self, str_quantity, frets_quantity):
        # 12 notas, na extensão de 3 oitavas para cada nota
        self.tempered_sys_notes = [
            "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", 
            "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",
            "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", 
            "C", "C#", "D", "D#", "E"
        ]
        self.str_quantity, self.frets_quantity = str_quantity, frets_quantity
            
    def sixString(self):
        strings = ["E", "A", "D", "G", "B", "E"]
        fretboard = []

        for st in strings:
            notes = []
            st_range = self.tempered_sys_notes.index(st)
            end_range = st_range + self.frets_quantity + 1

            for i in range(st_range, end_range):
                notes.append(self.tempered_sys_notes[i])
            
            fretboard.append(notes)

        return fretboard
    
    def sevenString(self):
        strings = ["B", "E", "A", "D", "G", "B", "E"]
        fretboard = []
        
        for st in strings:
            notes = []
            st_range = self.tempered_sys_notes.index(st)
            end_range = st_range + self.frets_quantity + 1

            for i in range(st_range, end_range):
                notes.append(self.tempered_sys_notes[i])
            
            fretboard.append(notes)

        return fretboard

    def octaString(self):
        strings = ["F#", "B", "E", "A", "D", "G", "B", "E"]
        fretboard = []
        
        for st in strings:
            notes = []
            st_range = self.tempered_sys_notes.index(st)
            end_range = st_range + self.frets_quantity + 1

            for i in range(st_range, end_range):
                notes.append(self.tempered_sys_notes[i])
            
            fretboard.append(notes)

        return fretboard

    def getTemperedSysNotes(self):
        return self.tempered_sys_notes
    
    # incluir os padrões Drop D e Drop C
