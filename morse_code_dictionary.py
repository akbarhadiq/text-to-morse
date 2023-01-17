morse_code_chart = {
    # Alphabet
    "A" : ".-",
    "B" : "-..",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",

    # Numerical
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",

    # Punctuation
    " " : "/",
    "." : ".-.-.-",
    "," : "--..--",
    ":" : "---...",
    "?" : "..--..",
    "`" : ".----.",
    "-" : "-....-",
    "/" : "-..-.",
    "(" : "-.--.",
    ")" : "-.--.-"
    
}

def print_morse_chart():
    for key in morse_code_chart:
        print(f"{key} : {morse_code_chart[key]}")