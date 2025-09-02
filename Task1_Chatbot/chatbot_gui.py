import tkinter as tk
from tkinter import scrolledtext
import time
from utils import get_response

# Send message function
def send_message():
    user_msg = entry.get().strip()
    if user_msg:
        # Show user message
        chat_log.insert(tk.END, f"You 🧑 ({time.strftime('%H:%M')}): {user_msg}\n", "user")

        # Get bot response
        response = get_response(user_msg)
        chat_log.insert(tk.END, f"Bot 🤖 ({time.strftime('%H:%M')}): {response}\n\n", "bot")

        entry.delete(0, tk.END)
        chat_log.yview(tk.END)

# GUI Setup
root = tk.Tk()
root.title("CodSoft Chatbot 🤖")
root.geometry("500x600")
root.configure(bg="#2C3E50")

# Chat window with scrollbar
chat_log = scrolledtext.ScrolledText(root, bg="#1E272E", fg="white", font=("Segoe UI", 12), wrap=tk.WORD)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Styling tags
chat_log.tag_config("user", foreground="#00FFFF", font=("Segoe UI", 11, "bold"))
chat_log.tag_config("bot", foreground="#2ECC71", font=("Segoe UI", 11))

# Entry frame
entry_frame = tk.Frame(root, bg="#2C3E50")
entry_frame.pack(fill=tk.X, padx=10, pady=10)

# Entry box
entry = tk.Entry(entry_frame, font=("Segoe UI", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

# Send button
send_btn = tk.Button(entry_frame, text="Send", command=send_message,
                     bg="#27AE60", fg="white", font=("Segoe UI", 11, "bold"))
send_btn.pack(side=tk.RIGHT)

root.mainloop()
