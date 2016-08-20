def check_command(pattern, command):

    pattern = bin(pattern)
    pattern = pattern[2:]
    pattern = pattern.zfill(len(command))

    if len(pattern) != len(command):
        return False

    #convert command to L or D
    cvt_cmd = ''
    for i in command:
        if i.isdigit():
            cvt_cmd += 'D'
        elif i.isalpha():
            cvt_cmd += 'L'

    #compare d/l w/ string 0/1
    for x, y in zip(pattern, cvt_cmd):
        if x == '0' and y == 'D':
            continue
        elif x == '1' and y == 'L':
            continue
        else:
            print(x, y)
            return False
    return True
