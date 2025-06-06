import time
import os

# --- Helper Functions for UI ---

def clear_screen():
    """Clears the console screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (os.name is 'posix')
    else:
        _ = os.system('clear')

def animated_text(text):
    """Prints text with a typewriter effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

# ANSI color codes for a more vibrant UI
class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# --- Core Cipher Logic ---

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts a given text using the Caesar Cipher.

    Args:
        text (str): The input string to be processed.
        shift (int): The number of positions to shift the letters.
        mode (str): The operation to perform, 'encrypt' or 'decrypt'.

    Returns:
        str: The processed (encrypted or decrypted) text.
    """
    result = ""
    
    # To decrypt, we shift in the opposite direction
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            # Calculate the shifted position with wrap-around
            shifted_pos = (ord(char) - start + shift) % 26
            # Convert back to a character
            result += chr(start + shifted_pos)
        else:
            # Keep non-alphabetic characters (spaces, punctuation) unchanged
            result += char
            
    return result

# --- Main Program Execution ---

if __name__ == "__main__":
    clear_screen()
    # Displaying a cool ASCII art header
    print(Colors.HEADER + Colors.BOLD)
    print("      .--.")
    print("     /.-. '----------.")
    print("     \\'-' .--\"--\"\"-\"-'")
    print("      '--'")
    print("\n--- CAESAR CIPHER ---\n" + Colors.ENDC)
    time.sleep(1)

    while True:
        # Get user's choice for operation
        choice_prompt = f"{Colors.YELLOW}What is your choice? ({Colors.BOLD}E{Colors.ENDC}{Colors.YELLOW}ncrypt / {Colors.BOLD}D{Colors.ENDC}{Colors.YELLOW}ecrypt): {Colors.ENDC}"
        choice = input(choice_prompt).lower()

        if choice.startswith('e'):
            mode = 'encrypt'
            action_text = "ENCRYPTING"
        elif choice.startswith('d'):
            mode = 'decrypt'
            action_text = "DECRYPTING"
        else:
            print(f"{Colors.RED}Invalid choice. Please choose 'E' or 'D'.{Colors.ENDC}\n")
            continue

        # Get user's message and shift key
        message = input(f"{Colors.CYAN}Enter your message: {Colors.ENDC}")
        while True:
            try:
                key = int(input(f"{Colors.CYAN}Enter the secret key (a whole number): {Colors.ENDC}"))
                break
            except ValueError:
                print(f"{Colors.RED}Invalid key. A number is required for this operation.{Colors.ENDC}")

        # Add a dynamic "processing" animation
        print(f"\n{Colors.GREEN}{action_text} TRANSMISSION", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print(f" COMPLETE!{Colors.ENDC}\n")
        time.sleep(0.5)

        # Get the result from the cipher function
        processed_message = caesar_cipher(message, key, mode)

        # Display the result in a formatted output
        animated_text(f"Your {mode}ed message is:")
        print(Colors.GREEN + Colors.BOLD + "----------------------------------------" + Colors.ENDC)
        print(f" {processed_message}")
        print(Colors.GREEN + Colors.BOLD + "----------------------------------------" + Colors.ENDC)
        
        # Ask to continue
        another_round = input(f"\n{Colors.YELLOW}Another task? (yes/no): {Colors.ENDC}").lower()
        if another_round != 'yes' and another_round != 'y':
            print(f"\n{Colors.HEADER}Turning off the machine.{Colors.ENDC}")
            break
        
        clear_screen()
        print(Colors.HEADER + "--- Ready for a new task? ---\n" + Colors.ENDC)