import winsound
import time

frequency = 730
unit_time = 100

dot = (frequency, unit_time)
dash = (frequency, unit_time * 3)
space = (0, unit_time / 1000)
space_3 = (0, unit_time * 3 / 1000)
space_7 = (0, unit_time * 7 / 1000)

morse_code_dict = {
    'a': [dot, space, dash],
    'b': [dash, space, dot, space, dot, space, dot],
    'c': [dash, space, dot, space, dash, space, dot],
    'd': [dash, space, dot, space, dot],
    'e': [dot],
    'f': [dot, space, dot, space, dash, space, dot],
    'g': [dash, space, dash, space, dot],
    'h': [dot, space, dot, space, dot, space, dot],
    'i': [dot, space, dot],
    'j': [dot, space, dash, space, dash, space, dash],
    'k': [dash, space, dot, space, dash],
    'l': [dot, space, dash, space, dot, space, dot],
    'm': [dash, space, dash],
    'n': [dash, space, dot],
    'o': [dash, space, dash, space, dash],
    'p': [dot, space, dash, space, dash, space, dot],
    'q': [dash, space, dash, space, dot, space, dash],
    'r': [dot, space, dash, space, dot],
    's': [dot, space, dot, space, dot],
    't': [dash],
    'u': [dot, space, dot, space, dash],
    'v': [dot, space, dot, space, dot, space, dash],
    'w': [dot, space, dash, space, dash],
    'x': [dash, space, dot, space, dot, space, dash],
    'y': [dash, space, dot, space, dash, space, dash],
    'z': [dash, space, dash, space, dot, space, dot],
    ' ': [space_7],
    '1': [dot, space, dash, space, dash, space, dash, space, dash],
    '2': [dot, space, dot, space, dash, space, dash, space, dash],
    '3': [dot, space, dot, space, dot, space, dash, space, dash],
    '4': [dot, space, dot, space, dot, space, dot, space, dash],
    '5': [dot, space, dot, space, dot, space, dot, space, dot],
    '6': [dash, space, dot, space, dot, space, dot, space, dot],
    '7': [dash, space, dash, space, dot, space, dot, space, dot],
    '8': [dash, space, dash, space, dash, space, dot, space, dot],
    '9': [dash, space, dash, space, dash, space, dash, space, dot],
    '0': [dash, space, dash, space, dash, space, dash, space, dash],
    '?': [dot, space, dot, space, dash, space, dash, space, dot, space, dot],
    '!': [dash, space, dot, space, dash, space, dot, space, dash, space, dash],
    '.': [dot, space, dash, space, dot, space, dash, space, dot, space, dash],
    ',': [dash, space, dash, space, dot, space, dot, space, dash, space, dash],
    ';': [dash, space, dot, space, dash, space, dot, space, dash, space, dot],
    ':': [dash, space, dash, space, dash, space, dot, space, dot, space, dot],
    '+': [dot, space, dash, space, dot, space, dash, space, dot],
    '-': [dash, space, dot, space, dot, space, dot, space, dot, space, dash],
    '/': [dash, space, dot, space, dot, space, dash, space, dot],
    '=': [dash, space, dot, space, dot, space, dot, space, dash]

}

text = input('Enter a standard text to convert to Morse Code:\n').lower()
split_text = [*text]
print(split_text)

morse_seq = []
for char in split_text:
    var = morse_code_dict[char]
    var.append(space_3)
    morse_seq.extend(var)

for seq1, seq2 in morse_seq:
    try:
        winsound.Beep(seq1, seq2)
    except TypeError:
        time.sleep(seq2)
