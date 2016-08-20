def rotate(state, pipe_numbers):
    variations = []
    count = 0
    starting = [ state[i] for i in pipe_numbers ]
    if 1 == all(starting):
        variations.append(count)

    end = len(state) - 1
    while count != end:
        count += 1
        test_pipes = []
        state = state[-1:] + state[:(len(state)- 1)]
        test_pipes = [ state[i] for i in pipe_numbers ]
        if 1 == all(test_pipes):
            variations.append(count)
    return variations
