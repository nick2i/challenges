import random

def monty_hall(strategy, _iterations=1000):
    step2strat = strategy[0]
    step4strat = strategy[1]

    n_wins = 0
    for i in range(_iterations):
        doors = [0, 1, 2]
        prize = random.randint(0, 2)
        choice = step2strat()
        openable_doors = doors[:]
        openable_doors.remove(choice)
        if prize in openable_doors:
            openable_doors.remove(prize)

        open_door = random.choice(openable_doors)

        choice = step4strat(choice, open_door)
        
        if choice == prize:
            n_wins += 1

    win_pct = (n_wins / _iterations) * 100
    return win_pct


def shawn():
    def step2strat():
        return 0
    def step4strat(*args):
        return 0
    return step2strat, step4strat

def john():
    def step2strat():
        return 0
    def step4strat(choice, open_door):
        doors = [0, 1, 2]
        doors.remove(choice)
        if open_door in doors:
            doors.remove(open_door)
        return doors[0]
    return step2strat, step4strat

def jeff():
    def step2strat():
        return random.randint(0, 2)
    def step4strat(choice, open_door):
        doors = [0, 1, 2]
        doors.remove(open_door)
        return random.choice(doors)
    return step2strat, step4strat

def joel():
    def step2strat():
        return random.randint(0, 2)
    def step4strat(choice, open_door):
        return choice
    return step2strat, step4strat

def nick():
    def step2strat():
        return random.randint(0, 2)
    def step4strat(choice, open_door):
        # this is the same as john's step4strat
        doors = [0, 1, 2]
        doors.remove(choice)
        doors.remove(open_door)
        return doors[0]
    return step2strat, step4strat

def dan():
    def step2strat():
        return 0
    def step4strat(choice, open_door):
        return int(open_door == 2)
    return step2strat, step4strat

shawnh_won_last_time = False
shawnh_strats = [shawn, john]
shawnh_last_strat = shawn
def shawnh():
    global shawnh_last_strat
    if shawnh_won_last_time:
        return shawnh_last_strat()
    else:
        temp = shawnh_strats[:]
        temp.remove(shawnh_last_strat)
        shawnh_last_strat = temp[0]
        return temp[0]()

def main():
    a = monty_hall(shawn())
    b = monty_hall(john())
    c = monty_hall(jeff())
    d = monty_hall(joel())
    e = monty_hall(nick())
    f = monty_hall(dan())
    g = monty_hall(shawnh())

    print(f"shawn: {a}%")
    print(f"john: {b}%")
    print(f"jeff: {c}%")
    print(f"joel: {d}%")
    print(f"nick: {e}%")
    print(f"dan: {f}%")
    print(f"shawnh: {g}%")


if __name__ == "__main__":
    main()
