
class myScale():
    def __init__(self, fretboard:list, scale_type, scale_pitch:str, sysNotes:list):
        
        self.majorNaturalFormula = [0, 2, 4, 5, 7, 9, 11]        
        self.minorNaturalFormula = [0, 2, 3, 5, 7, 8, 10]
        self.minorHarmonicFormula = [0, 2, 3, 5, 7, 8, 11]
        self.majorPentatonicFormula = [0, 2, 4, 7, 9]
        self.minorPentatonicFormula = [0, 3, 5, 7, 10]
        self.scale_pitch = scale_pitch
        self.scale_type = scale_type
        self.fretboard = fretboard
        self.sysNotes = sysNotes
        self.notesQtt = 12

        self.dict_scale_type = {"Maior Natural":self.majorNaturalFormula,
                                "Menor Natural":self.minorNaturalFormula,
                                "Menor Harmônica":self.minorHarmonicFormula,
                                "Pentatônica Maior":self.majorPentatonicFormula,
                                "Pentatônica Menor":self.minorPentatonicFormula}

    def buildScale(self):
        
        scale, scale_formula, scale_twelve_notes, scale_string = [], [], [], []
        
        # obtém a fórmula da escala escolhida pelo usuário
        for key, value in self.dict_scale_type.items():            
            if self.scale_type == key:
                scale_formula = value.copy()
                break
        
        # obtém as notas efetivas da escala, a partir da fórmula obtida no passo anterior
        pos_main = self.sysNotes.index(self.scale_pitch)
        
        # número de notas no sistema temperado, incluindo semitons 12        
        [scale_twelve_notes.append(self.sysNotes[n]) for n in range(pos_main, pos_main + self.notesQtt)]

        # retorna a escala efetiva, baseada na tônica escolhida
        [scale.append(scale_twelve_notes[i]) for i in scale_formula]

        # construir a escala, para cada corda do fretboard da guitarra
        for i in range(len(self.fretboard)):
            yes_or_no = []
         
            for j in range(len(self.fretboard[i])):
                note = self.fretboard[i][j]
                yes_or_no.append(1) if note in scale else yes_or_no.append(0)

            scale_string.append(yes_or_no)
        
        return scale_string