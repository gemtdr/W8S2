while True:

    try:
        
        fileName = input('Enter the name of a file to open ==> ')
        print()
        inFile = open(fileName)
        break

    except NameError: #Error 1

        print('File not found. Please try again.')

with open(fileName) as inFile:

    lines = inFile.read() #Error 2 

    linesCopy = lines[:]

    for i in range(len(linesCopy)): #This for loop isn't bugged, but bonus points if you know what it does.

        lines[i] = lines[i][:-1]

    choiceList = []
    choiceList2 = []

    print('Round 1')
    print()
    
    for i in range(0,9): #Error 3
        print()
        print(f'{lines[i]} or {lines[i+1]}?')
        choice = input('Enter your choice ==> ')
        
        choiceList.append(choice)
        
        print()

    print('Round 2')
    while True:


        try:

            for i in range(0,5,2):

                print(f'{choiceList[i]} or {choiceList[i+1]}?')
                choice2 = input('Enter your choice ==> ')
        
                choiceList2.append(choice2)
        
                print()


        except IndexError: 

            #Error 4

    print('Round 3')
    print()

    print(f'{choiceList2[0]} or {choiceList[-1]}?')

    choice2 = input('Enter your choice ==> ') #Error 5

    if choice3 == choiceList2[0]:

        print(f'{choiceList2[0]} or {choiceList[1]}?')
        choice4 = input('Enter your choice ==> ')

        print()

        print(f'Your winner is {choice4}.')

    else:

        print(f'{choiceList[-1]} or {choiceList2[1]}?')
        choice4 = input('Enter your choice ==> ')

        print()

        print(f'Your winner is {choice4}.')

