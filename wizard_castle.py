# wizard_castle.py

# Import necessary modules
import initialization_setup as init_setup
import main_processing_loop as main_loop

# Main function to start the game
def main():
    # Initialize the game
    init_setup.initialize_game()
    
    # Start the main processing loop
    main_loop.start_main_loop()

# Entry point of the program
if __name__ == "__main__":
    main()
