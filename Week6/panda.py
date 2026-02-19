import pandas as pd
path = r":\\Python\\MyOwnPractices\\python\\Week6\\ano.csv"

with open(path, "r", encoding="latin1") as f:
    for i, line in enumerate(f, start=1):
        if i == 6:
            print("LINE 6:", repr(line))
            break