def getInput(day:int)->str:
    with open(f'{day}.in') as file:
        res = file.read()
    return res