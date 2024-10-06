import tkinter as tk
from tkinter import ttk
from BIT_GUI import SDESApp
from Bruteforce_GUI import BruteForceBUI
from ASCII_GUI import SDES_ASCIIApp
from PIL import Image, ImageTk

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("S-DES")
        self.master.geometry("450x470")
        self.master.configure(bg="#f2f2f2")

        self.setup_background()  # 设置背景图
        self.setup_window()
        self.create_buttons()

    def setup_background(self):
        """加载并设置背景图像"""
        self.bg_image = Image.open("bg_image.jpg")  # 替换为您的图片文件名
        self.bg_image = self.bg_image.resize((500, 400), Image.LANCZOS)  # 调整图像大小
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)  # 创建PhotoImage对象

        # 创建标签用于显示背景图像
        background_label = tk.Label(self.master, image=self.bg_photo)
        background_label.place(relwidth=1, relheight=1)  # 使背景图像充满整个窗口

    def setup_window(self):
        """设置主窗口的样式和按钮框"""
        # 设置样式
        style = ttk.Style()
        style.theme_use('clam')
        # 为不同颜色的按钮创建样式，保持相同的大小
        style.configure('Green.TButton', font=('Arial', 12, 'bold'), padding=5, background="#4CAF50",
                        foreground="white", width=15)  # 调整宽度和内填充
        style.configure('Blue.TButton', font=('Arial', 12, 'bold'), padding=5, background="#2196F3",
                        foreground="white", width=15)  # 调整宽度和内填充
        style.configure('Red.TButton', font=('Arial', 12, 'bold'), padding=5, background="#F44336",
                        foreground="white", width=15)  # 调整宽度和内填充

    def create_buttons(self):
        """创建功能按钮"""
        buttons = [
            ("二进制加解密", self.open_encrypt_decrypt, 'Green.TButton'),
            ("ASCII加解密", self.open_ascii_app, 'Blue.TButton'),
            ("暴力破解", self.open_brute_force, 'Red.TButton')
        ]

        for text, command, style in buttons:
            button = ttk.Button(self.master, text=text, command=command, style=style)
            button.pack(pady=2, padx=5, expand=True, fill='x')

    def open_encrypt_decrypt(self):
        """打开加密和解密界面"""
        self.open_new_window(SDESApp)

    def open_ascii_app(self):
        """打开ASCII加解密界面"""
        self.open_new_window(SDES_ASCIIApp)

    def open_brute_force(self):
        """打开暴力破解界面"""
        self.open_new_window(BruteForceBUI)

    def open_new_window(self, app_class):
        """打开新窗口并加载相应的应用程序"""
        self.new_window = tk.Toplevel(self.master)
        app_class(self.new_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()