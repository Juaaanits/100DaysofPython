from art import logo

def ceaser_cipher(message, shift_number, answer):
    for character in message:
        if character.isalpha():
            ascii = ord(character)
            if answer == "encode":
                ascii += shift_number
                if ascii > 122:
                    ascii -= 26
                print(chr(ascii), end="")
            elif answer == "decode":
                ascii -= shift_number
                # since the ascii for lower case letters are from 97 to 122
                # if the ascii value is greater than 122, for example is z with shift value of 3, we need to subtract 26
                if ascii < 97:
                    ascii += 26
                print(chr(ascii), end="")
        else:
            print(character, end="")

play =  True
while play:
    print(logo)
    answer = input("Enter 'decode' to decrypt or 'encode' to encrypt': ")
    message = input("Enter your message: ").lower()
    shift_number = int(input("Enter the shift number: "))

    ceaser_cipher(message, shift_number, answer)
    print("\nDo you want to play again?")
    play_again = input("Enter 'yes' or 'no': ") 
    if play_again == "no":
        play = False
        print("Goodbye!")
    else:
        play = True