#Bryan Gomez Encoder and Main Function

#Encode function
def encode(string):
    #Create an empty list to store the changed values
    encoded_string = []
    #
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

#Main function        
if __name__ == "__main__":
    cont = True
    #While loop to keep menu running as long as the user doesn't select option 3
    while cont:
        choice = int(input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: "))
        #Option 1 prompts the user for their password and stores it in the password variable
        if choice == 1:
            password = input ("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
        #Option 2 displays the encoded password and the original password
        elif choice == 2:
            print(f"The encoded password is {encode(password)}, and the original password is {decode(encode(password))}.\n")
        #Option 3 breaks the while loop by switching the cont variable to false
        elif choice == 3:
            cont = False
    
