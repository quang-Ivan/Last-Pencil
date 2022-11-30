# when pencil left == 1 mod 4 you will lose
import random

while True:
    pencils = input("How many pencils would you like to use:")
    if pencils.isdigit():
        pencils = int(pencils)
        if pencils > 0:
            break
        elif pencils == 0:
            print("The number of pencils should be positive")
            continue
    print("The number of pencils should be numeric")

while True:
    fst = input("Who will be the first (John, Jack):")
    if fst not in ["John", "Jack"]:
        print("Choose between John and Jack")
    else:
        break
print("|" * pencils)
names = ["John", "Jack"]
count = names.index(fst)
while pencils > 0:
    if names[count % 2] == "Jack":
        print(f"{names[count % 2]}'s turn")
        if not pencils % 4 == 1:
            for i in range(1,4):
                if (pencils - i) % 4 == 1:
                    use = i
                    break
        else:
            use = random.randrange(1,min((pencils + 1,4)))
        print(use)
    else:
        while True:
            use = input(f"{names[count % 2]}'s turn")
            if use.isdigit():
                use = int(use)
                if int(use) not in range(1, 4):
                    print("Possible values: '1', '2' or '3'")
                    continue
                elif int(use) > pencils:
                    print("Too many pencils were taken")
                    continue
                else:
                    break
            else:
                print("Possible values: '1', '2' or '3'")
                continue
    pencils -= use
    print("|" * pencils)
    count += 1
print(f"{names[count % 2]} won!")
