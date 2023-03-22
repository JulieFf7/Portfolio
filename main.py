import PySimpleGUI as sg

layout = [[sg.Text("F or C ?")],
          [sg.Input(key='-INPUT-')],
          [sg.Button('F'), sg.Button('C')],
          [sg.Button('Ok')],
          [sg.Text(size=(40,1), key='-OUTPUT-')]]

window = sg.Window("Convert", layout)


while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Ok'):
        break
    elif  event == 'F':
        f = float(values['-INPUT-'])
        c = (f - 32) * 5 / 9
        window['-OUTPUT-'].update(c)
    elif event == 'C':
        c = float(values['-INPUT-'])
        f =  (c * 9 / 5 ) + 32
        print(f)
    else:    print("what")

window.close()
