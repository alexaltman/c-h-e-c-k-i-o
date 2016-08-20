def letter_queue(commands):
    mystack = ''

    for i in commands:
        try:
            cmd, stk_item = i.split(" ")
        except:
            cmd = i

        if cmd == 'POP':
            mystack = mystack[1:]
        elif cmd == 'PUSH':
            mystack += stk_item

    return mystack
