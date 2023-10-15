import os

while True:
    while True:
        try:
            user_choice =int(input('\nWould you like to read or write? (1,2,3)\n1. Read\n2. Write\n3. Quit\n'))
            break
        except ValueError: print('Invalid Input')
        
    if user_choice ==2:
        os.system('cls' if os.name =='nt' else 'clear')
        print('\033[4mWriting to File\033[0m')
        
        words =[]
            
        while True:
            try:
                number_of_words =int(input('How many words would you like to write?: '))
                break
            except ValueError: print('Invalid Input')

        for word_index in range(number_of_words):
            words.append(input(f'Enter the {word_index+1} word: '))
            
        with open("words.txt", "w") as file:
            for word in words:
                file.write(f'{word} ')
            file.close()
            
    elif user_choice ==1:
        os.system('cls' if os.name =='nt' else 'clear')
        try:file =open("words.txt", "r")
        except FileNotFoundError:
            print('File does not exist, please write first')
            continue
        
        print('\033[4mReading from File\033[0m')
        file_output =file.read()
        
        print(f'Number of words in the file: {len(file_output.split())}')
        print(f'The longest word in the file: {max(file_output.split(), key=len)}')  
        print(f'The average length of words in the file: {round(sum(len(word) for word in file_output.split()) / len(file_output.split()))}')      
        print(f'File output:\n{file_output}')

        file.close()
    
    elif user_choice ==3: break