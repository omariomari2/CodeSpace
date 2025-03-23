def check_parenthesis(S):
    S = S.strip()
    diction = {'(':')', '[':']', '{':'}'}
    meh = []
    for i in S:
        if i in diction.keys():
            meh.append(i)
        elif i in diction.values():
            if not meh:
                return False
            top = meh.pop()
            if diction[top] != i:
                return False
                
    return not meh
        
sample = ' )(( )){([( )])}'
print(check_parenthesis(sample))