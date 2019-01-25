def NDaysOfChristmas(gifts):
    for i in range(1, len(gifts) + 2):
        if i == 1:
            th = "st"
            conj = "A"
        elif i == 2:
            th = "nd"
            conj = "and a"
        elif i == 3:
            th = "rd"
            conj = "and a"
        else:
            th = "th"
            conj = "and a"

        print(f"On the {i}{th} day of Christmas, my true love gave to me,")

        for j in range(i, 1, -1):
            print(f"{j} {gifts[j - 2]}")

        print(f"{conj} partridge in a pear tree")


gifts = ["turtle doves", "French hens", "calling birds", "golden rings", "geese a-laying", "swans a-swimming",
         "maid a-milking", "ladies dancing", "lords a-leaping", "pipers piping", "drummers drumming"]
NDaysOfChristmas(gifts)
