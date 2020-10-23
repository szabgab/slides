import random
# Originally Created by Anna Uzonyi as a project for the course

true_values = ["T", "t", "True", "TRUE", "true", "1"]
false_values = ["F", "f", "False", "FALSE", "false", "0"]
tt = True
ff = False
good = ["Good job!", "Correct answer!", "You're a smartie.", "Nice!", "You're the next Bill Gates.", "You're the best programmer ever!", "On a scale of 1 to 10, you're an 11!"]
bad = ["Nope.", "Wrong answer.", "You should listen to the video again.", "Did you listen to the videos double speed? Bad idea.", "Seriosly?", "Where did you get that idea?"]

def runchap(chapter):
    #questions, answers = chapter["q"], chapter["a"]
    quizzes = chapter["quiz"]
    counter=0
    for ix, quiz in enumerate(quizzes):
        print("\nQuestion {}".format(ix+1))
        inp = input(quiz["q"])
        answer = quiz["a"]
        ok = False
        if answer is True and inp in true_values:
            ok = True
        if answer is False and inp in false_values:
            ok = True
        if answer not in [True, False] and inp in answer:
            ok = True
        if ok:
            counter+=1
            print(random.choice(good))
        else:
            print(random.choice(bad))

    print("You gave " + str(counter) + " correct answers out of 3")

### define questions and answers as dictionary
import json
content = {
"1":{
    "title": "First steps",
    "q":['What is the output of the following code?\na = "19"\nb = "23"\nc = a + b\n',
                    'What is the output of the following code?\na = 19\nb = 23\nc = a + b\n',
                    'How many of the following statements are correct?\n23 is an int\n"word" is a str\nNone is a bool\n'],
    "a": [["1923"], ["42"], ["2"]]},
"2":{
    "title": "Second steps",
    "q":['Is it true or false?\nThe recommendation for indentation is a tab.\nT or F: ', 'In which python version is the following code correct?\nprint "Foo", "Bar"\n2 or 3: ', 'Which word is used to implement a function?\nfun\nfunction\ndef\n'],
    "a":[ff,["2"],["def"]]},
"3":{
    "title": "Numbers",
    "q":['What is the result of 10%3?\n', 'Is it true or FALSE?\nrandom.random generates a random number between 1 and 100.\nT or F: ', 'Which of the following is used to sleect an element of a list?\nrandom.choice\nrandom.choose\nrandom.select\n'],
    "a":[["1"], ff, ["random.choice"]]},
"4":{
    "title": "Comparision and boolean",
    "q":['True or False is:\n T/F: ', 'Which of the following expresses not equal?\n-=\n!!\n!=\nn=\n', 'Is it true or FALSE?\n"2"<="11"\nT or F: '],
    "a":[tt, ["!="], ff]},
"5":{
    "title": "String",
    "q":["What is the output of this code?\ntext = 'abcd'\ntext = text[:2] + 'Y' + text[3:]\nprint(text)')\n", "What is the output of this code?\na = 'xYzA'\nprint(a.lower())\n", 'What is the output of this code?\ntext = "The black cat climbed the green tree."\nprint(text.index("The"))\n'],
    "a":[["abYd"], ["xyza"], ["0"]]},
"6":{
    "title": "Loop",
    "q":["How many numbers are included in range(3,7)?\n", "Is it true or FALSE?\nbreak will stop your program no matter where you call it\nT or F: ", 'Is it true or FALSE?\ncontinue will stop the current iteration of the current "while" or "for" loop\nT or F: '],
    "a":[["4"], ff, tt]},
"7":{
    "title": "Formatted printing",
    "q":["print("'{:>12}'".format(txt)) will align to left\nT/F: ", "print("'{:^12}'".format(txt)) will align to the center\nT/F: ", 'What is formating command of hexadecimal type?\nh/x/e: '],
    "a":[ff,tt,["x"]]},
"8":{
    "title": "Lists",
    "q":["Is it true or FALSE?\nIt is possible to have a list as an element of a list.\nT or F: ", "Which element of a list would .pop() remove?\nfirst/last: ", 'Sorted mutates a string to its sorted version.\nT/F: '],
    "a":[tt, ["last"], ff]},
"9":{
    "title": "Files",
    "q":["What is the name of the package that deals with excel files in python?\n", 'line = line.rstrip("\n") will a new line at the end of each row\nT/F: ', "It is not recommended to read a file using with\nT/F: "],
    "a":[["openpyxl"], ff, ff]},
"10":{
    "title": "Dictionary",
    "q":["If fname is a key in user dictionary, the code print('fname' in user) will return\na True\nb False\nc the value that belongs to this key\na/b/c", "Dictionary keys are returned in alphabetical order.\nT/F: ", "Deleting a key also removes the connected value.\nT/F: "],
    "a":[["a"], ff,tt]},
"11":{
    "title": "Set",
    "q":["Set operations are used to change the settings of the computer.\nT/F: ", "Which of the following is not a set operation?\na union\nb intersection\nc sum\na/b/c: ", "Which of the following is the parenthesis used to define sets?\na ()\nb {}\nc ([])\na/b/c: "],
    "a":[ff, ["c"], ["c"]]},
"12":{
    "title": "Functions",
    "q":["def add(x, y):\nz = x * y\nreturn z\na = add(2, 3)\nprint(a)\nWhat is the output of the above code?\n", "def mysum(*numbers):\nThe star denotes that the function can receive any number or character to be executed on.\nT/F: ", "Function documentation should be included in three pairs of double parenthesis.\nT/F: "],
    "a":[["6"], ff, tt]},
"13":{
    "title": "Modules",
    "q":["Which command is used to add a module to use?\nadd\nload\nimport\n", "Which is not used to search and specify module path?\nos\nsys\npath\n", "If you import a function in duplicate, from different modules, python will use the one imported first.\nT/F: "],
    "a":[["import"],["path"], tt]},
"14":{
    "title": "Regex",
    "q":["Regular expressions are only used in python programming language.\nT/F: ", "Which command returns lines that have the specified string in them?\ncatch\ngrep\nfind\n", "\d matches\na a digit\nb a number\nc a line\na/b/c: "],
    "a":[ff, ["grep"], ["a"]]},
"15":{
    "title": "Python standard modules",
    "q":["Which standard package deals with regular expression?\n", "To wait until a defined amount of time passes, you should use\na time.pass\nbtime.sleep\nc time.time\n a/b/c: ", "Which module can you use to list files with a given extension?\n"],
    "a":[["re"], ["b"], ["glob"]]},
"16":{
    "title": "Testing",
    "q":["With testing you can be sure that your code is bug-free./nT/F: ", "Which of the following is not a testing tool?\na doctest\nb pytest\c codetest\na/b/c: ", "Which command runs unittest?\n"],
    "a":[ff, ["c"], ["pytest"]]},
"17":{
    "title": "Python for science",
    "q":["Which of the following is used to handle n-dimensional arrays?\na NumPy\b BioPython\nc Keras\na/b/c: ", "Which of the following is used to work with FASTA files?\na NumPy\b BioPython\nc Keras\na/b/c: ", "Matplotlib is a library in Matlab.\nT/F: "],
    "a":[["a"], ["b"], ff]},
"18":{
    "title": "GUI",
    "q":["Which of the following is not a GUI toolkit?\na Tk\b Gkit\nc GTK\na/b/c: ", "You can pick multiple radio buttons at the same time.\nT/F: ", 'label.config(fg="#0000FF") defines the\nsize\ncolor\nposition of the label.\n'],
    "a":[["b"], ff, ["color"]]},}

for idx in content.keys():
    questions = content[idx].pop('q')
    answers = content[idx].pop('a')
    content[idx]["quiz"] = []
    for q, a in zip(questions, answers):
        content[idx]["quiz"].append({
            "q": q,
            "a": a,
        })



# with open('content.txt', 'w') as outfile:
#     json.dump(content, outfile)

# with open('content.txt') as json_file:
#     content = json.load(json_file)

while True:
    print(" \n**********************************************************************************")
    print("From which chapter do you want to be tested?")
    for idx in sorted(content.keys(), key=int):
        print(f"{idx} {content[idx]['title']}")
    print("If you want to exit, press'x'.\nSelect a number: ")
    chapter = input()
    if chapter == "x":
        break
    elif chapter in content.keys():
        print("Selected chapter: " + chapter)
        runchap(content[chapter])
        continue
    else:
        print("wrong, choose only from ", [key for key in content.keys()]+["x"])

## old
#while True:
#    chapter = input(" \n**********************************************************************************\nFrom which chapter do you want to be tested?\n1 First steps\n2 Second steps\n3 Numbers\n4 Comparision and boolean\n5 String\n6 Loop\n7 Formatted printing\n8 Lists\n9 Files\n10 Dictionary\n11 Set\n12 Functions\n13 Modules\n14 Regex\n15 Python standard modules\n16 Testing\n17 Python for science\n18 GUI\nIf you want to exit, press'x'.\nSelect a number: ")
#    if chapter == "1":
#        questions = ['What is the output of the following code?\na = "19"\nb = "23"\nc = a + b\n',
#                    'What is the output of the following code?\na = 19\nb = 23\nc = a + b\n',
#                    'How many of the following statements are correct?\n23 is an int\n"word" is a str\nNone is a bool\n']
#        answers = [["1923"], ["42"], ["2"]]
#        print("Selected chapter: " + chapter)
#        runchap(questions, answers)
#        continue
#    elif chapter=="x":
#        break
#
#    else:
#        print("wrong")
