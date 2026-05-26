import tkinter as tk

window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("400x300")

label = tk.Label(window, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

def check_password():
    password = entry.get()
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*()" for char in password):
        score += 1

    if score == 5:
        result_label.config(text="Strong password! 💪", fg="green")
    elif score >= 3:
        result_label.config(text="Medium password 🙂", fg="orange")
    else:
        result_label.config(text="Weak password! ❌", fg="red")

button = tk.Button(window, text="Check Strength", command=check_password)
button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()


