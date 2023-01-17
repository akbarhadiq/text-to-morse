from morse_code_dictionary import morse_code_chart, print_morse_chart
# Text based - text (string) to morse code

app_run = True
while app_run:
    morse_list = []

    # accept user input of a string text
    print("Morse Code Chart")
    print_morse_chart()
    print("\n")
    text_to_convert = input("Please input text you want to convert : ")

    # split the text into a list of characters
    split_text = [character for character in text_to_convert]

    # make the letters capital
    for x in range(len(split_text)):
        split_text[x] = split_text[x].upper()
    


    for character in split_text:
        try:
            morse_list.append(morse_code_chart[character])
        except KeyError:
            print("KeyError, morse chart does NOT contain the character you are trying to use")
    
    print(morse_list)

    def ask_run():
        keep_running_app = input("Do you want to do another text? (y/n) : ").lower()
        return keep_running_app

    while True:
        answer = ask_run()

        if answer not in ('y', 'n'):
            print("Wrong character input!")
            continue

        else:
            if answer == "y":
                app_run = True

            elif answer == "n":
                app_run = False

            break