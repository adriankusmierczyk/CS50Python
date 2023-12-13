def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# 2-6 znakow
# dwa pierwsze znaki to litery
# bez . ! ' '
#nie moze byc cyfry w srodku
#pierwsza cyfra to nie moze byc 0



def is_valid(s):
    if s.isalnum()==False:
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    i = 0
    while i < len(s):
        if s[i].isalpha()==False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    return True


main()