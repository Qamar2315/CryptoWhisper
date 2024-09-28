import pyperclip
from pynput.keyboard import Listener, Key
import logging
import encoder
import decoder
from utils import is_alphanumeric_with_spaces

# Project Name
PROJECT_NAME = "CryptoWhisper"

# Developer Information
DEVELOPER_NAME = "Qamar Ul Islam"
GITHUB_LINK = "https://github.com/qamar2315"

# Set up logging
logging.basicConfig(filename=f"{PROJECT_NAME}.log", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define your key combinations
COPY_KEY = Key.f1  # Copy key combo
ENCODE_KEY = Key.page_up # Encode key combo
DECODE_KEY = Key.page_down # Decode key combo
PASTE_KEY = Key.f4  # Paste key combo
START_KEY = Key.f5  # Start the program key combo

# Define the states for your app
running = False
# copied_text = "hi"

# Your existing coding and decoding functions
def encode(text):
    encoded_text = encoder.toString(text)
    return encoded_text

def decode(text):
    decoded_text = decoder.toString(text)
    return decoded_text

def on_press(key):
    global running
    try:
        if key == START_KEY:
            running = True
            print("App started! Waiting for key combinations...")
            logging.info("App started")

        if running:
            if key == ENCODE_KEY:
                if not is_alphanumeric_with_spaces(pyperclip.paste()):
                    print("Text contains non-alphanumeric characters. Please copy a valid text.")
                    logging.warning("Text contains non-alphanumeric characters. Please copy a valid text.")
                else:
                    text = pyperclip.paste()
                    encoded_text = encode(text)
                    pyperclip.copy(encoded_text)
                    logging.info("Text encoded and copied to clipboard")

            elif key == DECODE_KEY:
                if is_alphanumeric_with_spaces(pyperclip.paste()):
                    print("Text contains only alphanumeric characters. Please copy an encoded text.")
                    logging.warning("Text contains only alphanumeric characters. Please copy an encoded text.")
                else:
                    text = pyperclip.paste()
                    decoded_text = decode(text)
                    pyperclip.copy(decoded_text)
                    logging.info("Text decoded and copied to clipboard")

    except AttributeError:
        print("Special key pressed!")

def main():
    global running

    # Print Project Name in a more visually appealing way
    print("\n" + "="*40)
    print(f"  {'_'*10} WELCOME TO {'_'*10}")
    print(f"     *** {PROJECT_NAME} ***")
    print("="*40)
    print(f"  Developed by: {DEVELOPER_NAME}")
    print(f"  GitHub: {GITHUB_LINK}")
    print("="*40)
    
    print("\nAvailable Keys:")
    print("  PageUp - Encode and Copy Text")
    print("  PageDown - Decode and Copy Text")
    print("  F5 - Start the App")

    # Start listening to key events
    print("\nPress F5 to start the app.")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
