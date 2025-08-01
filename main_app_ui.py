import tkinter as tk
from tkinter import scrolledtext
import requests

API_KEY = "AIzaSyD5m64cIJR4FZe6ibpLVAbAVXxsN2GymIM"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def call_google_ai(prompt):
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        try:
            text = result['candidates'][0]['content']['parts'][0]['text']
            return text
        except (KeyError, IndexError):
            return "Error: Unexpected response format"
    else:
        return f"Error: {response.status_code} - {response.text}"

def on_ask():
    prompt = entry.get()
    if prompt.strip() == "":
        return
    btn_ask.config(state='disabled')
    txt_output.delete(1.0, tk.END)
    txt_output.insert(tk.END, "Generating...\n")
    root.update()

    result = call_google_ai(prompt)
    txt_output.delete(1.0, tk.END)
    txt_output.insert(tk.END, result)
    btn_ask.config(state='normal')

root = tk.Tk()
root.title("Google AI Chat")

tk.Label(root, text="Ask something:").pack(pady=5)
entry = tk.Entry(root, width=60)
entry.pack(padx=10)

btn_ask = tk.Button(root, text="Generating", command=on_ask)
btn_ask.pack(pady=10)

tk.Label(root, text="Generating:").pack()
txt_output = scrolledtext.ScrolledText(root, width=70, height=15)
txt_output.pack(padx=10, pady=5)

root.mainloop()
