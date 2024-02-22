import flet as ft
from guitarStrings import myGuitar as mg
from myScales import myScale as ms

# --------------------------------------------------------------------------------------------------------------------

def main(page: ft.Page):
    
    def k(fretboard, highlights=[]):
        
        guitar_obj_text, guitar_obj_row = [], []
        
        if len(highlights) > 0:
            for i in range(len(fretboard)):
                guitar_obj_text = []

                for j in range(len(fretboard[i])):
                    if highlights[i][j] == 1:
                        # TextFields
                        # guitar_obj_text.append(ft.TextField(value=fretboard[i][j],
                        #                       text_align=ft.TextAlign.CENTER, width=50, bgcolor=ft.colors.BLUE_GREY_200))
                        guitar_obj_text.append(ft.Container(padding=0, border_radius=10, bgcolor=ft.colors.GREY_50, 
                        content=(
                            ft.TextButton(width=51, height=50, 
                                content=ft.Container(
                                ft.Text(value=fretboard[i][j], size=13))))))

                    else:
                        # guitar_obj_text.append(ft.TextField(value=fretboard[i][j],
                        #                       text_align=ft.TextAlign.CENTER, width=50))

                        guitar_obj_text.append(ft.TextButton(width=51, height=50, content=ft.Container(
                            ft.Text(value=fretboard[i][j], size=13))))
                    
                my_row = ft.Row(guitar_obj_text, alignment=ft.MainAxisAlignment.CENTER)
                guitar_obj_row.append(my_row)
            
                page.add(my_row)
        
        else:
            for i in range(len(fretboard)):
                guitar_obj_text = []

                #[guitar_obj_text.append(ft.TextField(value=fretboard[i][j],
                #                        text_align=ft.TextAlign.CENTER, width=50)) for j in range(len(fretboard[i]))]

                [guitar_obj_text.append(ft.TextButton(width=51, height=50, content=ft.Container(
                    ft.Text(value=fretboard[i][j], size=13)))) for j in range(len(fretboard[i]))]
            
                my_row = ft.Row(guitar_obj_text, alignment=ft.MainAxisAlignment.CENTER)
                guitar_obj_row.append(my_row)
                
                page.add(my_row)

        return guitar_obj_row
    
    def show_instructions():
        dict_modes = {"guitar_type":guitar_dropdown.value, 
                      "frets_number":frets_dropdown.value,
                      "pitch":pitch_dropdown.value,
                      "scale_shape":scale_dropdown.value
                     }
        
        dict_modes_alerts = {"guitar_type":"Escolha um modelo de guitarra",
                             "frets_number":"Escolha uma quantidade de trastes (22 a 24)",
                             "pitch":"Escolha uma tonalidade para a escala",
                             "scale_shape":"Escolha um tipo de escala"
                            }

        items = []

        i = 0
        for key, value in dict_modes.items():
            if value is None:
                items.append(ft.Text(value=dict_modes_alerts[key]))
                page.add(items[i])
                i += 1

        return items
        
        
    def clicked(e):
        fretboard, highlights = [], []

        instructions = show_instructions()
        [page.controls.remove(instructions[i]) for i in range(len(instructions))]

        frets = 24 if frets_dropdown.value is None else int(frets_dropdown.value)

        if guitar_dropdown.value == "Six Strings":
            newGuitar = mg(6, frets)
            fretboard = newGuitar.sixString()
        
        elif guitar_dropdown.value == "Seven Strings":
            newGuitar = mg(7, frets)
            fretboard = newGuitar.sevenString()
        
        else:
            newGuitar = mg(8, frets)
            fretboard = newGuitar.octaString()
        
        scale_type = scale_dropdown.value        
        if pitch_dropdown.value is not None and scale_dropdown.value is not None:
            highlights = ms(fretboard=fretboard, scale_type=scale_type, 
                            scale_pitch=pitch_dropdown.value, sysNotes=newGuitar.getTemperedSysNotes()).buildScale()
        
        # remover rows do fretboard
        list_fret_rows = k(fretboard, highlights)
        [page.controls.remove(list_fret_rows[i]) for i in range(len(list_fret_rows))]
                
        return
    
    page.padding = 0

    msg = ft.Text(value="Fretboard", size=20)
    page.add(msg)   # o mesmo que 'page.controls.append(msg)'
    
    # mínimo de cordas 6; máximo 7
    # mínimo de 'frets' 22; máximo 24

    guitar_type = ft.Text(value="Tipo de Guitarra", width=200)
    guitar_dropdown = ft.Dropdown(width=200,     
    options=[
        ft.dropdown.Option("Six Strings"),
        ft.dropdown.Option("Seven Strings"),
        ft.dropdown.Option("Eight Strings")
    ])

    number_of_frets = ft.Text(value="Trastes", width=75)
    frets_dropdown = ft.Dropdown(width=75,
    options=[
        ft.dropdown.Option(22),
        ft.dropdown.Option(23),
        ft.dropdown.Option(24)
    ])

    # notas no sistema temperado
    pitch = ft.Text(value="Tonalidade", width=100)
    pitch_dropdown = ft.Dropdown(width=100,
    options=[
        ft.dropdown.Option("C"),
        ft.dropdown.Option("C#"),
        ft.dropdown.Option("D"),
        ft.dropdown.Option("D#"),
        ft.dropdown.Option("E"),
        ft.dropdown.Option("F"),
        ft.dropdown.Option("F#"),
        ft.dropdown.Option("G"),
        ft.dropdown.Option("G#"),
        ft.dropdown.Option("A"),
        ft.dropdown.Option("A#"),
        ft.dropdown.Option("B")        
    ])
    
    scale_type = ft.Text(value="Escala/Modo", width=200)
    scale_dropdown = ft.Dropdown(width=200,
    options=[
        ft.dropdown.Option("Maior Natural"),
        ft.dropdown.Option("Menor Natural"),
        ft.dropdown.Option("Menor Harmônica"),
        ft.dropdown.Option("Pentatônica Maior"),
        ft.dropdown.Option("Pentatônica Menor"),
    ])
    
    submit_btn = ft.ElevatedButton(text="GO", on_click=clicked)

    page.add(ft.Row([guitar_type, number_of_frets, pitch, scale_type], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row([guitar_dropdown, frets_dropdown, pitch_dropdown, scale_dropdown, submit_btn], 
                    alignment=ft.MainAxisAlignment.CENTER))

    page.update()

ft.app(target=main)