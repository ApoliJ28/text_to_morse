#Diccionario de codigo morse, clave -> letters, number o signo, valor-> codigo morse

dict_morse={
'A':'.-',
'B':'-...',
'C':'-.-.',
'@':'----',
'D':'-..',
'E':'.',
'F':'..-.',
'G':'--.',
'H':'....',
'I':'..',
'J':'.---',
'K':'-.-',
'J':'.-..',
'L':'.-..',
'M':'--',
'N':'-.',
'Ñ':'--.--',
'O':'---',
'P':'.--.',
'Q':'--.-',
'R':'.-.',
'S':'...',
'T':'-',
'U':'..-',
'V':'...-',
'W':'.--',
'X':'-..-',
'Y':'-.--',
'Z':'--..',
'0':'-----',
'1':'.----',
'2':'..---',
'3':'...--',
'4':'....-',
'5':'.....',
'6':'-....',
'7':'--...',
'8':'---..',
'9':'----.',
'.':'.-.-.-',
',':'--..--',
'?':'..--..',
'"':'.-..-.',
'/':'-..-.',
' ': ' '
}

def convert_to_morse(msg) -> str:
    msg_to_morse=''
    for i in range(0, len(msg)):
        msg_to_morse += dict_morse[msg[i]]
    return msg_to_morse

# Inicio del programa

# se pide el mensaje por consola...

msg = input('Mensaje a codigo morse: ').upper()

msg = msg.replace('CH','@')

print(f'El mensaje "{msg}" a codigo morse es: {convert_to_morse(msg)}')
