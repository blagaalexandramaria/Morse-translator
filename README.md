# Morse-translator
A beginner-friendly Python app that converts text ↔ Morse code using a simple Tkinter GUI.
Runs locally, no internet, no external packages.
1) Features:
-Encode: Text → Morse
-Decode: Morse → Text
-Supports letters (A–Z), digits (0–9), and punctuation: .,?/-()
-Unknown characters are replaced with ?
-Minimal, easy-to-use interface
2) Requirements:
-Python 3.8+
-Uses the built-in tkinter module (no extra installs)
-On some Linux distros you may need: sudo apt install python3-tk
3) Run locally
Save the script as morse_translator.py.
Run:
python morse_translator.py
4) How it works
Type plain text or Morse code in the top box.
Click:
Encode (Text → Morse), or
Decode (Morse → Text)
See the result in the bottom box.
5) Morse conventions used
Between letters: single space
Example: .... . .-.. .-.. ---
Between words: / (slash with spaces)
Example: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Examples:
HELLO WORLD → .... . .-.. .-.. --- / .-- --- .-. .-.. -..
... --- ... → SOS
6) Internals (short)
Two dictionaries:
MORSE_TO_TEXT (Morse → Text)
TEXT_TO_MORSE generated from the first + " " -> "/" for word gaps
Core functions:
encode_text(text) converts characters to Morse

decode_sentence(morse) splits words by / and letters by spaces

Tkinter GUI with input/output Text widgets and two Buttons
