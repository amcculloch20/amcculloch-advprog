pb = {}
pbr = {}
x = 1
# pb[key] = value

def main():
    while x == 1:
        print "What you want to do?"
        choose = raw_input("enter a new contact(entry), find someone by name (name), find someone by number (number)")
        if choose == "entry": entry()
        if choose == "name": name()
        if choose == "number": number()

def entry():
    while x == 1:
        name = raw_input("Whats their name?    when done adding contacts, say done")
        if name == "done":
            break
        number = raw_input("Whats their number?")
        pb[name] = number
        pbr[number] = name

def name():
    check = raw_input("Whose number would you like to find?")
    if check in pb: print pb[check]
    else: print "sorry you dont have that contact"


def number():
    check = raw_input("What name would you like to find? (by number)")
    print pbr[check]

main()
