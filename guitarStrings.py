
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
    
    def getSixStringScale(self, fretboard):
        # cordas soltas da guitarra de seis cordas, na afinação padrão

        strings = {"E1":1, "A":1, "D":2, "G":2, "B":2, "E":3}
        valor = 1
        real_notes_fretboard = []

        for i in range(len(fretboard)):
            v = []
            
            for j in range(len(fretboard[i])):                
                if j == 0:
                    if i == 0:
                        simple_note = fretboard[i][j] + str(i + 1)
                    else:
                        simple_note = fretboard[i][j]
                    
                    valor = strings.get(simple_note)                    

                else:
                    simple_note = fretboard[i][j]

                    if simple_note == "C":
                        valor += 1
                
                real_note = "./sounds/" + fretboard[i][j] + str(valor) + ".mp3"
                v.append(real_note)
            
            real_notes_fretboard.append(v)

        return real_notes_fretboard

    def getSevenStringScale(self, fretboard):
        # cordas soltas da guitarra de sete cordas, na afinação padrão

        strings = {"B0":0, "E1":1, "A":1, "D":2, "G":2, "B":2, "E":3}        
        valor = 1
        real_notes_fretboard = []

        for i in range(len(fretboard)):
            v = []
            
            for j in range(len(fretboard[i])):                
                # i == 0 and j == 0 representa 'primeira' corda solta
                if j == 0:
                    if i == 0 or i == 1:
                        # representa a 'primeira' ou a 'segunda' corda solta (B ou E)
                        simple_note = fretboard[i][j] + str(i)
                    
                    valor = strings.get(simple_note)            

                else:
                    simple_note = fretboard[i][j]

                    if simple_note == "C":
                        
                        if valor is not None:
                            valor += 1
                
                real_note = "./sounds/" + fretboard[i][j] + str(valor) + ".mp3"
                v.append(real_note)
            
            real_notes_fretboard.append(v)

        return real_notes_fretboard

    def getOctaStringScale(self, fretboard):
            # cordas soltas da guitarra de sete cordas, na afinação padrão

            strings = {"F#0":0, "B0":0, "E1":1, "A":1, "D":2, "G":2, "B":2, "E":3}
            valor = 1
            real_notes_fretboard = []

            for i in range(len(fretboard)):
                v = []
                
                for j in range(len(fretboard[i])):
                    # i == 0 and j == 0 representa 'primeira' corda solta
                    if j == 0:
                        if i == 0:
                            # representa a 'primeira' corda solta (F#)
                            simple_note = fretboard[i][j] + str(i)
                        elif i == 1 or i == 2:
                            # representa a 'segunda' ou a 'terceira' corda solta (B ou E)
                            simple_note = fretboard[i][j] + str(i-1)
                        
                        valor = strings.get(simple_note)

                    else:
                        simple_note = fretboard[i][j]

                        if simple_note == "C":
                            
                            if valor is not None:
                                valor += 1
                    
                    real_note = "./sounds/" + fretboard[i][j] + str(valor) + ".mp3"
                    v.append(real_note)
                
                real_notes_fretboard.append(v)

            return real_notes_fretboard