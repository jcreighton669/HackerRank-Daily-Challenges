def swap_case(s):
    new_s = ""
    for el in s:
        if el.islower():
            new_s += el.upper()
        elif el.isupper():
            new_s += el.lower()
        else:
            new_s += el
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
