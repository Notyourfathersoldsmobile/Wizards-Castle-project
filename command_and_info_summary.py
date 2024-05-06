def command_and_info_summary():
    # Print help message
    print(chr(27) + "E")  # Clear screen
    print("*** WIZARD'S CASTLE COMMAND AND INFORMATION SUMMARY ***")
    print()

    # Print available commands
    print("THE FOLLOWING COMMANDS ARE AVAILABLE:")
    print("H/ELP     N/ORTH    S/OUTH    E/AST     W/EST     U/P")
    print("D/OWN     DR/INK    M/AP      F/LARE    L/AMP     O/PEN")
    print("G/AZE     T/ELEPORT Q/UIT")
    print()

    # Print room contents legend
    print("THE CONTENTS OF ROOMS ARE AS FOLLOWS:")
    print(". = EMPTY ROOM      B = BOOK            C = CHEST")
    print("D = STAIRS DOWN     E = ENTRANCE/EXIT   F = FLARES")
    print("G = GOLD PIECES     M = MONSTER         O = CRYSTAL ORB")
    print("P = MAGIC POOL      S = SINKHOLE        T = TREASURE")
    print("U = STAIRS UP       V = VENDOR          W = WARP/ORB")
    print()

    # Print benefits of treasures
    print("THE BENEFITS OF HAVING TREASURES ARE:")
    print("RUBY RED - AVOID LETHARGY     PALE PEARL - AVOID LEECH")
    print("GREEN GEM - AVOID FORGETTING  OPAL EYE - CURES BLINDNESS")
    print("BLUE FLAME - DISSOLVES BOOKS  NORN STONE - NO BENEFIT")
    print("PALANTIR - NO BENEFIT         SILMARIL - NO BENEFIT")
    print()

    # Prompt to resume the game
    input("PRESS RETURN WHEN READY TO RESUME, " + R[RC] + ".")
