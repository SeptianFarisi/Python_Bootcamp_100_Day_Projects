#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", "r") as guess:
    for invited in guess.readlines():
        letter = open("Input/Letters/starting_letter.txt")
        new_invited = invited.strip("\n")
        new_letter = letter.read()
        with open(f"Output/ReadyToSend/invited_{new_invited}.txt", "x") as send:
            send_letter = new_letter.replace("[name]", new_invited)
            send.write(send_letter)
    letter.close()