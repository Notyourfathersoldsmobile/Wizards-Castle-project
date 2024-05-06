def display_map_and_adjacent_rooms():
    if BL != 1:
        print()
        print("** YOU CAN'T SEE ANYTHING, YOU DUMB", R[RC], "!")
        return

    # Display map of the current castle level
    print()
    A, B = X, Y  # Save current position
    for X in range(1, 9):
        for Y in range(1, 9):
            Q = L[FND[Z]]
            if Q > 99:
                Q = 34  # Let Q=Q-100 to show rooms
            if X == A and Y == B:
                print("<", I[Q], ">  ", end="")
            else:
                print(" ", I[Q], "   ", end="")
        print()
        print()

    X, Y = A, B  # Restore current position

    # Display adjacent room contents with a flare
    if FL != 0:
        print()
        FL -= 1  # Reduce flare count
        A, B = X, Y
        for Q1 in range(A - 1, A + 2):
            X = FNB(Q1)
            for Q2 in range(B - 1, B + 2):
                Y = FNB(Q2)
                Q = FNE(L[FND[Z]])
                L[FND[Z]] = Q
                print(" ", I[Q], "   ", end="")
            print()
            print()

        X, Y = A, B  # Restore current position

    # Call subroutine to update status information
    update_status_info()
