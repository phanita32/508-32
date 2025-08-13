import tkinter as tk

def update_label():
    my_label.config(
        text="ชื่อ: น.ส.ภณิตา พึ่งใจ\nชั้น: 5/8\nเลขที่: 32",
        fg="red"
    )

root = tk.Tk()
root.title("EPT - Event Label Example")

# เมื่อกดปุ่ม Label จะเปลี่ยนข้อความ
my_label = tk.Label(root, text="กดปุ่มเพื่อแสดงข้อมูล", fg="green")
my_label.pack()

my_button = tk.Button(root, text="กดที่นี่", command=update_label)
my_button.pack()

root.mainloop()