#! /usr/bin/python3


def tower_of_hanoi(t, a, aux, target):
    counter=0
    if t == 1:
        print(f"Move {t} from {a} to {target}") 
    elif t == 2:
        print(f"Move {t-1} from {a} to {aux}")
        print(f"Move {t} from {a} to {target}")
        print(f"Move {t-1} from {aux} to {target} ")
    elif t == 3:
        print(f"Move {t-2} from {a} to {target}")
        print(f"Move {t-1} from {a} to {aux}")
        print(f"Move {t-2} from {target} to {aux} ")
        print(f"Move {t} to {target}")
        print(f"Move {t-2} from {aux} to {a}")
        print(f"Move {t-1} from {aux} to {target}")
        print(f"Move {t-2} from {a} to {target}")
    elif t==4:
        print(f"Move {t-(t-1)} to {aux}")
        print(f"Move {t-(t-2)} to {target}")
        print(f"Move {t-(t-1)} to {target}")
        print(f"Move {t-1} to {aux}")
        print(f"Move {t-(t-1)} to {a}")
        print(f"Move {t-(t-2)} to {aux}")
        print(f"Move {t-(t-1)} to {aux}")
        print(f"Move {t} to {target}")
        print(f"Move {t-(t-1)} to {target}")
        print(f"Move {t-(t-2)} to {a}")
        print(f"Move {t-(t-1)} to {a}")
        print(f"Move {t-1} to {target}")
        print(f"Move {t-(t-1)} to {aux}")
        print(f"Move {t-(t-2)} to {target}")
        print(f"Move {t-(t-1)} to {target}")



a = "tower A"    
aux = "tower B"
target = "tower C"
x = int(input("Please enter the number of towers: ")) 
tower_of_hanoi(x, a, aux, target)