import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import pyperclip
import pyttsx3

def translate_text():
    src = src_lang.get()
    tgt = tgt_lang.get()
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return
    try:
        translator = Translator()
        translated = translator.translate(text, src=src, dest=tgt)
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
        output_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

def copy_output():
    result = output_text.get("1.0", tk.END).strip()
    pyperclip.copy(result)
    messagebox.showinfo("Copied!", "Translated text was copied to clipboard.")

def text_to_speech():
    result = output_text.get("1.0", tk.END).strip()
    if result:
        engine = pyttsx3.init()
        engine.say(result)
        engine.runAndWait()
    else:
        messagebox.showwarning("No Text", "No translated text to speak.")

# GUI Setup
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("480x390")

# Language dropdown values
langs = list(LANGUAGES.keys())
lang_names = [LANGUAGES[lang].title() for lang in langs]
lang_map = dict(zip(lang_names, langs))

# Source language dropdown
src_lang = tk.StringVar(value="en")
ttk.Label(root, text="Source Language:").pack(pady=4)
src_combo = ttk.Combobox(root, values=lang_names, state="readonly")
src_combo.set("English")
src_combo.pack()
src_combo.bind('<<ComboboxSelected>>', lambda e: src_lang.set(lang_map[src_combo.get()]))

# Target language dropdown
tgt_lang = tk.StringVar(value="fr")
ttk.Label(root, text="Target Language:").pack(pady=4)
tgt_combo = ttk.Combobox(root, values=lang_names, state="readonly")
tgt_combo.set("French")
tgt_combo.pack()
tgt_combo.bind('<<ComboboxSelected>>', lambda e: tgt_lang.set(lang_map[tgt_combo.get()]))

# Text input box
ttk.Label(root, text="Enter text:").pack(pady=4)
input_text = tk.Text(root, height=4)
input_text.pack(padx=8, pady=3)

# Translate button
ttk.Button(root, text="Translate", command=translate_text).pack(pady=9)

# Output box
ttk.Label(root, text="Translated text:").pack()
output_text = tk.Text(root, height=4, state=tk.DISABLED)
output_text.pack(padx=8, pady=3)

# Copy and Text-to-Speech buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=8)
ttk.Button(btn_frame, text="Copy Output", command=copy_output).pack(side=tk.LEFT, padx=5)
ttk.Button(btn_frame, text="Speak Output", command=text_to_speech).pack(side=tk.LEFT, padx=5)

root.mainloop()
