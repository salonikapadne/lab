import tkinter as tk
import re

d = {"name":"", "room":"", "nights":""}

def bot(m):
    m = m.lower().strip()

    if "hi" in m: return "Name?"
    if "cancel" in m:
        d.update({"name":"","room":"","nights":""})
        return "Cancelled"

    if m.startswith("update name"):
        d["name"] = m.replace("update name","").strip()
        return "Name updated"

    if m.startswith("update room"):
        d["room"] = m.replace("update room","").strip()
        return "Room updated"

    if m.startswith("update nights"):
        n = re.findall(r"\d+", m)
        if n: d["nights"] = n[0]; return "Nights updated"
        return "Invalid nights"

    if "my name is" in m:
        d["name"] = m.replace("my name is","").strip()
        return "Room?"

    if any(x in m for x in ["single","double","deluxe"]):
        d["room"] = m
        return "Nights?"

    if "night" in m:
        n = re.findall(r"\d+", m)
        if n:
            d["nights"] = n[0]
            return f"Confirm {d} (yes/no)"
        return "Enter number"

    if m == "yes": return "Booked!"
    if m == "no":
        d.update({"name":"","room":"","nights":""})
        return "Restart"

    return "Try again"


def send():
    msg = e.get()
    c.insert(tk.END, "You: "+msg+"\nBot: "+bot(msg)+"\n\n")
    e.delete(0,tk.END)

root = tk.Tk()
root.title("Hotel Bot")

c = tk.Text(root)
c.pack()

e = tk.Entry(root)
e.pack()

tk.Button(root,text="Send",command=send).pack()

root.mainloop()