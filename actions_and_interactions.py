def actions_and_interactions():
    # Take a drink from a pool
    if L[FND[Z]] == 5:
        print()
        print("** IF YOU WANT A DRINK, FIND A POOL!")
        return

    Q = FNA(8)  # Randomly determine the effect of the drink
    print()
    print("YOU TAKE A DRINK AND ", end="")
    if Q < 7:
        print("FEEL ", end="")

    # Apply the effect of the drink based on the random outcome
    if Q == 1:
        ST = FNC(ST + FNA(3))  # Increase strength
        print("STRONGER.")
    elif Q == 2:
        ST = ST - FNA(3)  # Decrease strength
        print("WEAKER.")
        if ST < 1:
            ST = 1  # Ensure strength doesn't become negative
            print("WEAK TO THE POINT OF EXHAUSTION.")
    elif Q == 3:
        IQ = FNC(IQ + FNA(3))  # Increase intelligence
        print("SMARTER.")
    elif Q == 4:
        IQ = IQ - FNA(3)  # Decrease intelligence
        print("DUMBER.")
        if IQ < 1:
            IQ = 1  # Ensure intelligence doesn't become negative
            print("TOO DUMB TO REMEMBER YOUR NAME.")
    elif Q == 5:
        DX = FNC(DX + FNA(3))  # Increase dexterity
        print("NIMBLER.")
    elif Q == 6:
        DX = DX - FNA(3)  # Decrease dexterity
        print("CLUMSIER.")
        if DX < 1:
            DX = 1  # Ensure dexterity doesn't become negative
            print("SO CLUMSY YOU CAN'T TIE YOUR SHOES.")
    elif Q == 7:
        RC = FNA(4)  # Change character race
        if RC != R:
            print("BECOME A", R[RC] + ".")
        else:
            print("CHANGE RACE, BUT REMAIN THE SAME.")
    elif Q == 8:
        SX = 1 - SX  # Toggle character sex
        print("TURN INTO A", end=" ")
        if SX == 0:
            print("FEMALE", end="")
        else:
            print("MALE", end="")
        print(" " + R[RC] + "!")

    # Handle specific actions related to opening a chest or a book
    if L[FND[Z]] == 6:
        print()
        print("YOU OPEN THE CHEST AND")
    elif L[FND[Z]] == 12:
        print()
        print("YOU OPEN THE BOOK AND")

    # Handle specific outcomes based on the content of the chest or the book
    if L[FND[Z]] == 6 or L[FND[Z]] == 12:
        outcome = FNA(6)
        if outcome == 1:
            print("FLASH! OH NO! YOU ARE NOW A BLIND", R[RC], "!")
            BL = 1
        elif outcome == 2:
            print("IT'S ANOTHER VOLUME OF ZOT'S POETRY! - YECH!!")
        elif outcome == 3:
            print("IT'S AN OLD COPY OF PLAY", R[FNA(4)], "!")
        elif outcome == 4:
            print("IT'S A MANUAL OF DEXTERITY!")
            DX = 18
        elif outcome == 5:
            print("IT'S A MANUAL OF STRENGTH!")
            ST = 18
        elif outcome == 6:
            print("THE BOOK STICKS TO YOUR HANDS -")
            print("NOW YOU ARE UNABLE TO DRAW YOUR WEAPON!")
            BF = 1
        L[FND[Z]] = 1

    # Handle specific outcomes based on a trap or treasure found
    if L[FND[Z]] == 11:
        print()
        print("IT'S HARD TO GAZE WITHOUT AN ORB!")
    elif L[FND[Z]] == 10:
        print()
        print("YOU SEE ", end="")
        outcome = FNA(6)
        if outcome == 1:
            print("YOURSELF IN A BLOODY HEAP!")
            ST = ST - FNA(2)
            if ST < 1:
                ST = 1
        elif outcome == 2:
            print("YOURSELF DRINKING FROM A POOL AND BECOMING", C[12 + FNA(13)], "!")
        elif outcome == 3:
            print(C[12 + FNA(13)], "GAZING BACK AT YOU!")
        elif outcome == 4:
            A, B, C = FNA(8), FNA(8), FNA(8)
            if FNA(8) < 4:
                A, B, C = O[1], O[2], O[3]
            print("***THE ORB OF ZOT*** AT (", A, ",", B, ") LEVEL", C, "!")
        elif outcome == 5:
            print("A SOAP OPERA RERUN!")

    # Handle teleportation with the runestaff
    if RF == 0:
        print()
        print("** YOU CAN'T TELEPORT WITHOUT THE RUNESTAFF!")
        return

    # Teleportation coordinates input
    z_coordinate_input("X-COORDINATE")
    X = Q
    z_coordinate_input("Y-COORDINATE")
    Y = Q
