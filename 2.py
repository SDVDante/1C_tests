def brackets_check(data):
    s = []
    for sign in data:
        if sign == "(":
            s.append(sign)
        elif sign == ")":
            if len(s) == 0:
                return False
            s.pop()
    return len(s) == 0
