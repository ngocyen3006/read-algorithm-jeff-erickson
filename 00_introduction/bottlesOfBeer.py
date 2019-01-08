def bottlesOfBeer(n):
    for i in range(n, 0, -1):
        if i - 1 > 1:
            b = "bottles"
            p = str(i - 1) + " bottles"
        elif i - 1 == 1:
            b = "bottles"
            p = "1 bottle"
        else:
            b = "bottle"
            p = "no more bottles"

        print(f"{i} {b} of beer on the wall, {i} {b} of beer,")
        print(f"Take one down and pass it around, {p} of beer on the wall.")

    print("No more bottles of beer on the wall, no more bottles of beer,")
    print(f"Go to the store and buy some more, {n} bottles of beer on the wall.")


bottlesOfBeer(5)
