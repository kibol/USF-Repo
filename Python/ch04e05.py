def function_a():
    print "function_a was called..."

def function_b():
    print "function_b was called..."

def function_c():
    print "function_c was called..."

def dispatch (choice):
    if choice == 'a':
        function_a()
    elif choice == 'b':
        function_b()
    elif choice == 'c':
        function_c()
    else:
        print "Invalid choice."


ch = raw_input (" Please enter a,b or c: ")

dispatch (ch)
