#Bryan Gomez Encoder and Main Function

def encode(string):
    encoded_string = []
    for x in range(0, len(string)):
        current_num = int(string[x])
        if current_num <= 6:
            new_num = str(current_num + 3)
        elif current_num == 7:
            new_num = '0'
        elif current_num == 8:
            new_num = '1'
        elif current_num == 9:
            new_num = '2'
        encoded_string.append(new_num)
    return ''.join(encoded_string)
    
#Decoder here
def decode(encoded_pass):
    decoded_pass = ""
    for digit in encoded_pass:
        original_digit = int(digit) - 3
        # If the new digit is less than 0, add 10 to the digit
        if original_digit < 0:
            original_digit += 10
        decoded_pass += str(original_digit)
    return decoded_pass

        
if __name__ == "__main__":
    cont = True
    while cont:
        choice = int(input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: "))
        if choice == 1:
            password = input ("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            print(f"The encoded password is {encode(password)}, and the original password is {decode(encode(password))}.\n")
        elif choice == 3:
            cont = False
    
