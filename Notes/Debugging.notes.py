#Alishya Xavier, Debugging Notes
import trace
import sys

def trace_calls(frame, event, arg):
    if event == 'call': #when the function is called
        print(f'Calling function: {frame.f_code.co_name}')
    elif event == 'line':#new line of code happens
        print(f'Executing line {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return': #checks when we return stuff
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception': #when there is an exception
        print(f'Exception in {frame.f_code.co_name}: {arg}')

    return trace_calls

sys.settrace(trace_calls)
tracer = trace.Trace(count=False, trace=True)

#What is tracing?
#----------------------------------------------
#Tracings skips everything else and see what is disrupting our program
def sub(numone, numtwo):
    return numone - numtwo

def add(num1, num2):
    print(sub(num1, num2))
    return num1+num2

print(add(5,2))

tracer.run('add(8,9)')
#Basic Tracing command
    #python -m trace --trace Notes\Debugging.notes.py

'''
    --trace (displays lines as executed)
    --count (displays number of time executed)
    --listfuncs (displays functions used in the program)
    --trackcalls (displays the relationships between functions)
'''
#What are some ways we can debug by tracing?
#------------------------------------------------
#We use this to observe what the code is doing without disrupting our program

#How do you access the debugger in VS Code?
#----------------------------------------------------
# You can click the debug button on the left
# You can also click F5
# You can also click on the dropdown on the left and click debug

#What is testing?
#-----------------------------------------------
#running your code multiple times to make sure it works as required(trying to break it)

#What are boundary conditions?
#--------------------------------------------------
#the conditions that are prescribed at different types 
#of boundaries in order to approximate the behavior of a system.(Checking the ones most likely to be wrong)

#How do you handle when users give strange inputs?
#-----------------------------------------
# You could use basic conditionals and loops