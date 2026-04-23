import tkinter as tk

# ---------------- DATA STORE ----------------
bookings = []

# ---------------- CORE OPERATIONS ----------------
def add_booking():
    name = e_name.get().strip()
    room = e_room.get().strip()
    nights = e_nights.get().strip()

    if not (name and room and nights):
        status.config(text="Fill all fields")
        return

    bookings.append({"name": name, "room": room, "nights": nights})
    status.config(text="Booking added")
    clear_inputs()

def update_booking():
    name = e_name.get().strip()
    for b in bookings:
        if b["name"] == name:
            b["room"] = e_room.get().strip()
            b["nights"] = e_nights.get().strip()
            status.config(text="Booking updated")
            return
    status.config(text="Booking not found")

def cancel_booking():
    global bookings
    name = e_name.get().strip()
    bookings = [b for b in bookings if b["name"] != name]
    status.config(text="Booking cancelled (if existed)")

# ---------------- VIEW (MODULAR OUTPUT) ----------------
def view_bookings():
    view_box.delete("1.0", tk.END)   # clears old output ONLY here

    if not bookings:
        view_box.insert(tk.END, "No bookings available\n")
        return

    view_box.insert(tk.END, "--- CURRENT BOOKINGS ---\n\n")
    for b in bookings:
        view_box.insert(tk.END, f"Name: {b['name']}\n")
        view_box.insert(tk.END, f"Room: {b['room']}\n")
        view_box.insert(tk.END, f"Nights: {b['nights']}\n")
        view_box.insert(tk.END, "----------------------\n")

# ---------------- HELPERS ----------------
def clear_inputs():
    e_name.delete(0, tk.END)
    e_room.delete(0, tk.END)
    e_nights.delete(0, tk.END)

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Hotel Information Management System")

tk.Label(root, text="Name").pack()
e_name = tk.Entry(root)
e_name.pack()

tk.Label(root, text="Room").pack()
e_room = tk.Entry(root)
e_room.pack()

tk.Label(root, text="Nights").pack()
e_nights = tk.Entry(root)
e_nights.pack()

tk.Button(root, text="Add Booking", command=add_booking).pack()
tk.Button(root, text="Update Booking", command=update_booking).pack()
tk.Button(root, text="Cancel Booking", command=cancel_booking).pack()
tk.Button(root, text="View Bookings", command=view_bookings).pack()

status = tk.Label(root, text="", fg="blue")
status.pack()

view_box = tk.Text(root, height=15)
view_box.pack()

root.mainloop()