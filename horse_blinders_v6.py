#horse-blinders.py
#Python command-line experimental coding utility
#
#Useful for inputting experimental coding values while only dealing with one data point at a time
#
#
#Project: NPI/Negation Corpus study with Francis Blanchette and Cynthia Lukyanenko
#Author: Benjamin Hunt 
#Date: 12/02/2021

#procedure:

#Open and read outputfile
#determine last coded line
#open inputfile
#grab N lines starting from last coded + 1 (N = sys.argv[3])
#create instance of entry class for each line
#print formatted line to stdout
#take user coding input for each factor
#output (append) the formatted entry instance to the outputfile

#Things to add (based on meeting 12/10/21)
#   -Display item metadata along with sentence at top
#   -Highlight target negative word (reference target index to differentiate multiple targets)
#   -Add input options  
#       -Notes: ?______ = "review: _____"
#       -TC bounds: #,x = here to end of the line 
#   -
#   -
#   -
#   -

import os
import sys
from colorama import init

init(autoreset=True)

class entry:
    def __init__(self, line, numLines, i, codedBy):
        line = line.split("\t")
        self.full_line = line
        self.corpus = line[0]
        self.subcorpus = line[1]
        self.filename = line[2]
        self.lineNumber = line[3]
        self.citationID = line[4]
        self.sentID = line[5]
        self.speaker = line[6]
        self.utterance = line[7]
        self.sentence = line[8]
        self.targetWord = line[9]
        self.targetIndex = line[10]
        self.synCat = line[11]
        self.type = line[12]
        self.synRole = line[13]
        self.sentNum = i
        self.totalSent = numLines
        self.tensedClause = self.markTensedClause()  # new function
        self.verb = self.markVerb() #new function
        self.notes = self.takeNotes()  # new function
        self.resolved = line[17]
        self.assignedto = line[18].strip()
        self.codedby = codedBy

    def __str__(self):
        return f"""{self.corpus}\t{self.subcorpus}\t{self.filename}\t{self.lineNumber}\t{self.citationID}\t{self.sentID}\t{self.speaker}\t{self.utterance}\t{self.sentence}\t{self.targetWord}\t{self.targetIndex}\t{self.synCat}\t{self.type}\t{self.synRole}\t{self.tensedClause}\t{self.verb}\t{self.notes}\t{self.resolved}\t{self.assignedto}\t{self.codedby}"""

    def printFormat(self, index, outstring):
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.sentNum+1 == self.totalSent:
            print("\033[32m> " + "Progress: \033[32m{0}\033[32m/{1}\n".format(self.sentNum+1, self.totalSent))
        else:
            print("\033[32m> " + "Progress: \033[31m{0}\033[32m/{1}\n".format(self.sentNum+1, self.totalSent))

        #color target word
        which = int(self.targetIndex)-1

        outstring[which] = "\033[31m" + outstring[which] + "\033[0m"
        interList = index + outstring
        interList[::2] = index
        interList[1::2] = outstring

        print(f"""
    +---------------------+
    |    \033[35mTarget Entry\033[0m     |
    +---------------------+
        """)
        print(f"""
> Corpus: {self.corpus}
> Subcorpus: {self.subcorpus}
> Filename: {self.filename}
> Line: {self.lineNumber}
> Speaker: {self.speaker}
        """)
        print("> " + " ".join(outstring) + "\n")

        term_size = os.get_terminal_size()
        print('_' * term_size.columns + "\n\n\n\n")
        print("> " + "".join(item.center(12, " ") for item in interList))
        print("\n\n\n" + '_' * term_size.columns)
        #Spacing
        print("\n")


        #function for delineating the tensed clause boundaries:
        #print sentence with word boundaries numbered
        #take user input (start, end)
        #slice sentence with new boundaries and store in self.tensedClause

    def printPrep(self, offset):
        sentence = self.sentence.split()
        index = [item for item in range(0, len(sentence)+offset)]
        index = ["\033[32m" + str(item) + "\033[0m" for item in index]
        self.printFormat(index, sentence)
        return sentence

    def markTensedClause(self):
        sentence = self.printPrep(1)

        #print options and handle user input
        inputOpts = "> Input options:\t\033[36m#,#\033[0m = Clause range (start_index, end_index)\n\t\t\t\033[36m#,x\033[0m = Clause range (start_index, end of sentence)\n\t\t\t\033[36ma\033[0m = full line\n\t\t\t\033[36mx\033[0m = incomplete\n\t\t\t\033[36m^C\033[0m = Exit\n"
        print("\n" + inputOpts)
        while True:
            try:
                clauseInput = input("> Tensed Clause boundaries: \033[36m")
                #"a" = full sentence
                if clauseInput == "a":
                    return self.sentence
                #"x" or "X" = incomplete
                elif clauseInput == "X" or clauseInput == "x":
                    return "X"
                #tuple
                elif "," in clauseInput:
                    bounds = clauseInput.split(",")
                    #case for "#,x" = # to end of sentence
                    if clauseInput[-1] == "x":
                        return " ".join(sentence[int(bounds[0]):])
                    #case for "#,#" = start,end
                    else:
                        return " ".join(sentence[int(bounds[0]):int(bounds[1])])
                else:
                    print("\n \033[31m!Invalid input\n")
            except ValueError:
                print("\n \033[31m!This input is not in range.\n")

    def markVerb(self):
        self.printPrep(0)

        #print options and handle user input
        inputOpts = "> Input options:\t\033[36m____\033[0m = verb as written\n\t\t\t\033[36mMV\033[0m = missing verb\n\t\t\t\033[36mx\033[0m = incomplete\n\t\t\t\033[36m^C\033[0m = Exit\n"
        print("\n" + inputOpts)
        verbInput = input("> Verb: \033[36m")
        return verbInput

    def takeNotes(self):
        self.printPrep(0)

        inputOpts = "> Input options:\t\033[36m____\033[0m = Custom note\n\t\t\t\033[36mnf\033[0m = \"Not a full sentence\"\n\t\t\t\033[36m?____\033[0m = \"Review:\" ____\n\t\t\t\033[36m?\033[0m = \"unsure/unclear\"\n\t\t\t\033[36mnt\033[0m = \"No target word\"\n\t\t\t\033[36m^C\033[0m = Exit\n"
        print("\n" + inputOpts)
        notesInput = input("> Notes: \033[36m")
        if notesInput == "nf":
            return "Not a full sentence"
        elif notesInput == "nt":
            return "No target word"
        elif notesInput == "?":
            return "unsure/unclear"
        elif notesInput[0] == "?" and len(notesInput) > 1:
            return "Review: " + notesInput[1:]
        else:
            return notesInput
    
def splashScreen(inputFileName, outputFileName):
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('mode 132,40')
    print(f"""
                                        ++-------------------------------------------------++
                                        ||                            .''                  ||
                                        ||                  ._.-.___.' (\033[41m`\ \033[0m                ||
                                        ||                 //(        ( `'                 ||
                                        ||                '/ )\ ).__. )                    ||
                                        ||                ' <' `\ ._/'\                    ||
                                        ||                   `   \     \                   ||
                                        ||                                                 ||
                                        ||                 \033[32mHorse-Blinders\033[0m                  ||
                                        ||              Manual Coding Utility              ||
                                        ||                   Version 0.6                   ||
                                        ||                  Benjamin Hunt                  ||
                                        ||                    1/28/2022                    ||
                                        ++-------------------------------------------------++


                                                    Welcome to \033[32;1mHorse-Blinders\033[0m! 

                                    This tool can be used to speed up experimental coding procedures 
                                    when manual coding is necessary. Essentially, this utility provides 
                                    a way to reduce the coder's on-screen distractions and facilitate 
                                    rapid input of coding values.

                                    Type ^C to exit the program at any time.



                                    Here are the files you are working with currently:

                                    Input File: \033[34;1m{inputFileName}\033[0m
                                    Output File: \033[34;1m{outputFileName}\033[0m
                                    """ + '\n\n')
                        
    numLines = input(" "*36 + "How many lines would you like to manually code? \033[36m")
    return int(numLines)

#find last line of the file and return the line number
def last_line(outfile):
    lineNum = 0
    last = outfile[-1]
    #get SentID
    last = last.split("\t")
    lineNum = last[5]
    #check if there is anything there
    return lineNum

def celebrate():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"""
    +=========================================+
    |  You have reached the end of the file!  |
    +=========================================+""")
    quit()

def main():

    if len(sys.argv) != 3:
        print(f"""Usage:\tpython3 {sys.argv[0]} inputfile.txt outputfile.txt""", file=sys.stderr, flush=True)
    else:
        try:
            with open(sys.argv[2], "a+") as outputFile:
                numLines = splashScreen(sys.argv[1], sys.argv[2])
                codedBy = input(" "*36 + "Enter your initials: \033[36m")
                #handle initial coding session (no/blank outputfile)
                if outputFile.tell() == 0:
                    outputFile.write("Corpus"+"\t"+"Subcorpus"+"\t"+"Filename"+"\t"+"LineNumber"+"\t"+"CitationID"+"\t"+"SentID"+"\t"+"Speaker"+"\t"+"Utterance"+"\t"+"Sentence"+"\t"+"targetWord"+"\t"+"targetIndex"+"\t"+"synCat"+"\t"+"type"+"\t"+"synRole"+"\t"+"tensedClause"+"\t"+"verb"+"\t"+"notes"+"\t"+"resolved"+"\t"+"assignedto"+"\t"+"codedby"+"\n")
                    lastCoded = ""
                    with open(sys.argv[1], encoding="unicode_escape") as f:
                        text = f.readlines()
                        lines = text[1:numLines+1]
                        for i, line in enumerate(lines):
                            if line:
                                # do output stuff
                                outputFile.write(
                                    str(entry(line, numLines, i, codedBy)) + "\n")
                            else:
                                pass
                    outputFile.seek(0) #rewind for later use

                #all other coding sessions
                else:
                    outputFile.seek(0)
                    out = [line for line in outputFile]
                    #find last line in output file
                    lastCoded = last_line(out)
                    with open(sys.argv[1], encoding="unicode_escape") as f:
                        text = f.readlines()                    
                        #find last coded line in input file; 
                        for i, line in enumerate(text):
                            temp = line.split("\t")
                            if temp[5] == lastCoded:
                                lastCodedIndex = i
                                break
                        #get n lines from input file after lastLine
                        lines = text[lastCodedIndex+1:lastCodedIndex+numLines+1]
                        #check if end of the file reached
                        if lastCodedIndex+1 == len(text):
                            celebrate()
                        #otherwise, iterate through extracted files
                        for i, line in enumerate(lines):
                            tracker = lastCodedIndex+2+i
                            if line:
                                outputFile.write(str(entry(line, numLines, i, codedBy)) + "\n")
                            else:
                                pass
                            #check if end of the file reached
                            if tracker == len(text):
                                celebrate()
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Exiting program...")


if __name__ == "__main__":
    main()
