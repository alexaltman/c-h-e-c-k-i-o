def digit_stack(commands):
    possible = [ 'push', 'pop', 'peek' ]
    mycommands= []
    mystack = []
    mysum = 0
    mypop = ''
    digit = ''
    for i in commands:
        i = i.lower()
        try:
            command, digit = i.split(' ')
        except ValueError:
            command = i
        if command not in possible:
            return 0

        if command == 'push':
            mystack.append(digit)
        elif command == 'pop':
            if len(mystack) > 0:
                mypop = mystack.pop()
                mysum += int(mypop)
        elif command == 'peek':
            if len(mystack) >= 1:
                mysum += int(mystack[-1])
    return mysum
