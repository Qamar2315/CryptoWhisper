## CryptoWhisper: A Simple Text Encryption Tool

**CryptoWhisper** is a Python program that allows you to encrypt and decrypt text using a unique key and permutation-based encoding algorithm. The program uses key combinations for convenience and integrates with the system clipboard for seamless copying and pasting of encoded/decoded text.

### Features:

- **Simple Encryption/Decryption:** Encodes and decodes text using a randomly generated key and permutations.
- **Key Generation:** Generates a unique 5-character key for each encoding session.
- **Clipboard Integration:** Copies the encoded/decoded text directly to the clipboard.
- **User-Friendly Interface:** Uses key combinations to initiate encoding/decoding actions.
- **Logging:** Logs all actions to a file for tracking and debugging.

### Usage:

1. **Start the App:** Press F5 to start the program.
2. **Copy Text:** Copy the text you want to encode/decode to your clipboard.
3. **Encode/Decode:**
   - Press Page Up to encode the text.
   - Press Page Down to decode the text.
4. **Paste Encoded/Decoded Text:** The encoded or decoded text will automatically be copied to your clipboard.

### Installation:

1. **Install Python:** Make sure you have Python installed on your system.
2. **Install Dependencies:** Install the required libraries by running the following command in your terminal:
   ```bash
   pip install pynput pyperclip
   ```

### Key Combinations:

- **F5:** Start the App
- **Page Up:** Encode and Copy Text
- **Page Down:** Decode and Copy Text

### Project Information:

- **Developer:** Qamar Ul Islam
- **GitHub:** [https://github.com/qamar2315](https://github.com/qamar2315)

### Disclaimer:

This program is for educational purposes only and should not be used for any sensitive or confidential data. The encryption algorithm is relatively simple and can be broken with effort.

### Future Improvements:

- Implement a more robust encryption algorithm.
- Add a user interface for easier interaction.
- Allow users to save and load their own custom keys.

### License:

This project is licensed under the MIT License.