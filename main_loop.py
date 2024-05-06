# Main processing loop
def main_processing():
    global T, GP, RF, OF, BL, X, Y, Z, ST, IQ, DX, FL, WV, AV, LF, TC, WC
    
    T += 1

    # Check if player is affected by traps or obstacles
    if RF + OF > 0:
        trap_effects()
        return

    # Check if player's actions consume time or resources
    if C[0][3] > T[0]:
        T += 1
    
    if C[1][3] > T[2]:
        GP -= random.randint(1, 5)
        if GP < 0:
            GP = 0

    if C[2][3] <= T[4]:
        trap_effects()
        return

    # Update player's position
    A, B, C = X, Y, Z
    X, Y, Z = random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)
    L[FND(Z)] = L[FND(Z)] + 100

    # Check for monsters in the new room
    if L[FND(Z)] != 1:
        trap_effects()
        return

    # Check if player steps on traps or obstacles
    for Q in range(1, 4):
        C[Q][3] = -(C[Q][0] == X) * (C[Q][1] == Y) * (C[Q][2] == Z)

    # Check if player is affected by traps or obstacles
    if random.randint(1, 5) > 1:
        print("\nYOU ", end="")
        Q = random.randint(1, 7) + BL
        if Q > 7:
            Q = 4
        trap = {
            1: "STEPPED ON A FROG!",
            2: "HEAR A SCREAM!",
            3: "HEAR FOOTSTEPS!",
            4: "ENCOUNTER A WUMPUS!",
            5: "HEAR THUNDER!",
            6: "SNEEZED!",
            7: "SEE A BAT FLY BY!"
        }
        print(trap[Q])
    else:
        return
