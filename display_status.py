def display_status_information():
    print()
    if BL == 0:
        display_map()

    print("STRENGTH =", ST, "INTELLIGENCE =", IQ, "DEXTERITY =", DX)
    print("TREASURES =", TC, "FLARES =", FL, "GOLD PIECES =", GP)
    print("WEAPON =", W[WV], "ARMOR =", W[AV + 5], end="")
    if LF == 1:
        print("  AND A LAMP")
    else:
        print()

    WC = 0
    Q = FNE(L[FND[Z]])
