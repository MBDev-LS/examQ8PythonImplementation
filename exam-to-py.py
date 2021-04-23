import os
import platform


class Election(): # The election class, the basis of elections that store their data including votes and administation.
    def __init__(self): #  Sets main properties.
        self.A, self.B, self.C, self.totalVotes = 0, 0, 0, 0
        self.voting = True
        self.password = None
        self.hint = None

def passwordValidation(password): # This is used to proccess passwords when the admin enters one to be set.
    if len(password) < 4 and password != 'skip': # Validation check that the password is at least four characters.
        print('Your password must be at least four characters long.')
        return(False)
    if password == 'skip': # Handling for the 'skip' function
        print('Skipping.')
        return(False)
    else:
        return(True)

election = Election()
credDone = False
while not credDone: # Takes in and sets election admin infomation.
    passDone = False
    hintDone = False
    while not passDone: # Proccesses and sets password.
        givenPass = input("Please set the election password (enter 'skip' to skip this step): ")
        if passwordValidation(givenPass): 
            election.password = givenPass
            passDone = True
        elif givenPass == 'skip':
            passDone = True
    while not hintDone: # Proccesses and sets password hint.
        givenHint = input("Please set the election password hint (enter 'skip' to skip this step): ")
        if givenHint != 'skip':
            election.hint = givenHint
        else:
            print('Skipping.')
        hintDone = True
    credDone = True

loadQuestionDone = False
while not loadQuestionDone: # Handles the importing of elections/
    inputAnswer = input('Would you like to load a previous election? (y/n): ')
    if inputAnswer == 'n':
        loadQuestionDone = True
    elif inputAnswer == 'y':
        filePath = input("Please enter the election file path: (enter 'cancel' to cancel): ") # Takes the file path in from the user.
        if filePath == 'cancel': # Handles the 'cancel' function.
            print('Cancelling.')
            break
        try:
            loadFile = open(filePath, 'r') # Checks if the file exists by trying to import it.
        except:
            print('File not found.')
        else:
            try: # Parses the data from the file and checks that it is valid.
                fileContent = loadFile.read()
                listOfData = fileContent.split('|')
                election.A = int(listOfData[0])
                election.B = int(listOfData[1])
                election.C = int(listOfData[2])
                election.totalVotes = int(listOfData[3])
            except: #  Handles invalid files
                print('File invalid, please try again.')
            else: #Informs the user that the election has loaded and stops the importing loop.
                print('Election loaded.')
                loadQuestionDone = True
    else:
        print('Please answer y/n.')

print('STARTING ELECTION')
while election.voting == True: # The main election loop.
    voted = False
    while voted == False: # Forces a valid input
        vote = input('Enter your vote (A, B or C): ')
        if vote.upper() == 'A': # Each one of these (A, B and C) adds a vote and sets voted to true.
            election.A += 1
            election.totalVotes += 1
            voted = True
        elif vote.upper() == 'B':
            election.B += 1
            election.totalVotes += 1
            voted = True
        elif vote.upper() == 'C':
            election.C += 1
            election.totalVotes += 1
            voted = True
        elif vote == 'END': # Allows election admins to end the election using a password (if set).
            if election.password == None:
                election.voting = False
                break
            passGiven = input("Enter election password (enter 'hint' for hint): ")
            if passGiven == 'hint':
                if election.hint == None:
                    print('No hint set.')
                else:
                    print(election.hint)
                passGiven = input("Enter election password (one chances remaining): ")
                if passGiven == election.password:
                    election.voting = False
                    break
                else:
                    print('Incorrect.')
                    break
            elif passGiven == election.password:
                election.voting = False
                break
            else: # Catches any unexpected inputs
                print('Incorrect.')
                break
        else:
            print('Please enter a valid vote.')
print('ELECTION ENDED')
print('A Votes:', election.A, '\nB Votes:', election.B, '\nC Votes:', election.C, '\nTotal Votes:', election.totalVotes) # Outputs final vote tally
while True: # Allows election admins to take action once they have stopped the voting.
    nextAction = input("What would you like to do next? (Enter 'help' for a list of commands): ")
    if nextAction == 'help': # Outputs a list of commands and their descriptions.
        print('Commands:\nsave - save election results to a file.\nexport - export the election as a .txt file so you can import it later\nprint/output - output the election results again.\nclear/clr - clears your command line.\nexit - stops the program.')
    elif nextAction == 'save': # Allows users to save a copy of their election data for future reference.
        name = input('Enter file name: ')
        root, ext = os.path.splitext(name)
        if not ext:
            ext = '.txt'
        elif ext != '.txt':
            print('Error: Invalid file extention used.')
        path = root + ext
        f = open(path, 'w+')
        f.write('A Votes:'+str(election.A)+'\nB Votes:'+str(election.B)+'\nC Votes:'+str(election.C)+'\nTotal Votes:'+str(election.totalVotes))
        f.close()
        print('Saved to: '+path)
    elif nextAction == 'export': #  Allows users to export an election text file so that they can import it in the future.
        name = input('Enter file name: ')
        root, ext = os.path.splitext(name)
        if not ext:
            ext = '.txt'
        elif ext != '.txt':
            print('Error: Invalid file extention used.')
        path = root + ext
        f = open(path, 'w+')
        f.write(str(election.A)+'|'+str(election.B)+'|'+str(election.C)+'|'+str(election.totalVotes))
        f.close()
        print('Exported to: '+path)
    elif nextAction == 'print' or nextAction == 'output': # Allows the user to output the election data again.
        print('A Votes:', election.A, '\nB Votes:', election.B, '\nC Votes:', election.C, '\nTotal Votes:', election.totalVotes) # Outputs final vote tally.
    elif nextAction == 'clear' or nextAction == 'clr': # Allows users to clear their command line from within the terminal (works for Mac and Linux).
        if platform.system() == 'linux' or platform.system() == 'linux2' or platform.system() == 'Darwin': # Checks if user is using MacOS or Linux.
            os.system('clear')
        elif platform.system() == 'Windows' or platform.system() == 'win32'or platform.system() == 'win64': # Checks if the user is using Windows.
            os.system('clr')
        else:
            print('Your platform is not support for this command.')
    elif nextAction == 'exit': # Allows the user to exit the program.
        print('Stopping program.')
        break
    else:
        print('Error: Unknown command') # Handles unexpected commands.

# An implementation of a Computer Science (OCR) Paper 2 Algorithm Question
# Was in my final mock for CS.

# Created by Louis S.