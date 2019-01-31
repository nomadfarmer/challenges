def stack(instructions):
    """ instructions is a list with the following types of entries:
    push x      (add n to the list)
    pop         (pop the last item off the list)
    inc n x     (increment the first n items by x)
    after processing each instruction, display the last item on the list

    """
    s = []
    incs = {}
    for i in instructions:
        op, *n = i.split(' ')
        if op == 'push':
            s.append(int(n[0]))
        elif op == 'pop':
            s.pop()
            inc_keys = sorted(incs.keys())
            if len(inc_keys) >= 2 and inc_keys[-2] > len(s):
                incs.pop(inc_keys[-1])
        elif op == 'inc':
            n, x = n
            for k in incs.keys():
                if k < n:
                    incs[k] += x
            if n in incs.keys():
                incs[n] += x
            else:
                incs[n] = x
        # display the last item on the stack
        mi = max(incs.keys())
        if mi > len(s):
            inc_v = incs[mi]
        else:
            inc_v = 0
        print(s[-1] + inc_v)


        f'abc{inc_v}'
        
