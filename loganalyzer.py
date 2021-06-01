# Imports System-specific parameters and functions
import sys

"""
RESOURCES FOR SOULIUTION: 
https://stackoverflow.com/questions/30392793/input-variable-from-command-line-in-python
https://wiki.python.org/moin/HandlingExceptions
https://stackoverflow.com/questions/57882946/reading-log-files-in-python (?)
"""

# list of possible options for validation
action_options = ['statistics', 'error', 'notice']

# validate input
try:
	filepath = str(sys.argv[1])  # get the first input from cmd
	file = open(filepath, 'r')  # reads the file

	print("Opened filed: "+filepath)
except Exception as e:
	print(e)  # Gives error if 

# checks if the 2nd input is matching any of the possible action_options
if(any(sys.argv[2] in option for option in action_options)):
	print("Selected option:" + str(sys.argv[2]))
	#pass
	# Or erase line 25 and set pass for an clean output
else:
	print("invalid option: "+str(sys.argv[2]))
	print("please select one of the possible options: ")
	for option in action_options:
		print(option + "  ")


# Parse the file differently depending on the input...
print("starting to analyze the file .. ")

if str(sys.argv[2]) == 'statistics':
    Notice = 0
    Error = 0

    for rad in file:
        if "error" in rad:
            Error = Error + 1
        else:
            Notice = Notice + 1

    print("errors: ", Error)
    print("notice: ", Notice)
# to execute do loganalyzer.py [file] --> log.test [action] --> statistics

# Date and Message split Error argument loop
# to execute do loganalyzer.py [file] --> log.test [action] --> error
if str(sys.argv[2]) == 'error':
        for rad in file: 
            if "error" in rad: 
                dateMessage = rad.split("[error]")
                print(dateMessage[0], dateMessage[1])
# to execute do loganalyzer.py [file] --> log.test [action] --> notice
# Date and Message split Notice argument loop
if str(sys.argv[2]) == 'notice':
    for rad in file:
        if "notice" in rad:
            dateMessage = rad.split("[notice]")
            print(dateMessage[0], dateMessage[1])


