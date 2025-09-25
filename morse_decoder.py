import tkinter as tk

# Morse dictionary (Morse → Text)
MORSE_TO_TEXT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
    '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/',
    '-....-': '-', '-.--.': '(', '-.--.-': ')'
}

# Text → Morse dictionary
TEXT_TO_MORSE = {value: key for key, value in MORSE_TO_TEXT.items()}
TEXT_TO_MORSE[" "] = "/"   
def decode_word(morse_word):
    letters = morse_word.split(" ")
    decoded = ""
    for code in letters:
        decoded += MORSE_TO_TEXT.get(code, "?")
    return decoded
def decode_sentence(morse_sentence):
    words = morse_sentence.split(" / ")
    decoded_sentence = ""
    for word in words:
        decoded_sentence += decode_word(word) + " "
    return decoded_sentence.strip()

# Encode text → Morse
def encode_text(text):
    text = text.upper()
    encoded = []
    for char in text:
        encoded.append(TEXT_TO_MORSE.get(char, "?"))
    return " ".join(encoded)


# GUI
def create_gui():
    def encode_action():
        text = entry_text.get("1.0", tk.END).strip()
        result = encode_text(text)
        output.delete("1.0", tk.END)
        output.insert(tk.END, result)

    def decode_action():
        morse = entry_text.get("1.0", tk.END).strip()
        result = decode_sentence(morse)
        output.delete("1.0", tk.END)
        output.insert(tk.END, result)

    root = tk.Tk()
    root.title("Morse Code Translator")
    tk.Label(root, text="Enter text or Morse code:").pack()
    entry_text = tk.Text(root, height=5, width=50)
    entry_text.pack()
    tk.Button(root, text="Encode (Text → Morse)", command=encode_action).pack(pady=5)
    tk.Button(root, text="Decode (Morse → Text)", command=decode_action).pack(pady=5)
    tk.Label(root, text="Result:").pack()
    output = tk.Text(root, height=5, width=50)
    output.pack()
    root.mainloop()

create_gui()