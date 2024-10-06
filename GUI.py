import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from SDES import SDES

class SDESApp:
    def __init__(self, root):
        # 初始化SDES算法和Tkinter窗口
        self.sdes = SDES()
        self.root = root
        self.root.title("SDES 加密和解密")
        self.root.geometry("450x500")  # 设置窗口大小
        self.root.configure(bg="#f2f2f2")

        # 添加并调整背景图像
        self.bg_image = ImageTk.PhotoImage(Image.open("bg_image.jpg").resize((450, 450), Image.LANCZOS))
        background_label = tk.Label(root, image=self.bg_image)  # 创建一个标签来显示背景图像
        background_label.place(relwidth=1, relheight=1)  # 使背景图像覆盖整个窗口

        # 添加标题标签
        title_label = tk.Label(root, text="S-SED", font=("Helvetica Neue", 28, "bold"), bg="#f2f2f2", fg="#303F9F")
        title_label.pack(pady=(10, 5))  # 添加上下边距

        # 创建Notebook组件用于分隔不同页面
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=1, fill="both", padx=20, pady=20)

        # 加密标签页
        self.encrypt_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.encrypt_frame, text="加密")  # 添加加密页面
        self.setup_encrypt_tab()  # 设置加密页面的内容

        # 解密标签页
        self.decrypt_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.decrypt_frame, text="解密")  # 添加解密页面
        self.setup_decrypt_tab()  # 设置解密页面的内容

    def setup_encrypt_tab(self):
        # 加密页面的UI设置
        ttk.Label(self.encrypt_frame, text="输入10位二进制密钥:", font=("Helvetica Neue", 14, "bold"), background="#f2f2f2").pack(pady=(15, 5))
        self.key_entry = ttk.Entry(self.encrypt_frame, width=40, font=("Helvetica Neue", 14), justify='center', show='*')  # 输入密钥框
        self.key_entry.pack(pady=10)

        ttk.Label(self.encrypt_frame, text="输入8位明文:", font=("Helvetica Neue", 14, "bold"), background="#f2f2f2").pack(pady=(10, 5))
        self.plaintext_entry = ttk.Entry(self.encrypt_frame, width=40, font=("Helvetica Neue", 14), justify='center', show='*')  # 输入明文框
        self.plaintext_entry.pack(pady=10)

        # 创建按钮框并添加加密和清空按钮
        button_frame = tk.Frame(self.encrypt_frame, bg="#f2f2f2")
        button_frame.pack(pady=20)

        # 加密按钮
        encrypt_button = tk.Button(button_frame, text="🔒 加密", command=self.encrypt_action,
                                   font=("Helvetica Neue", 14, "bold"), bg="#4CAF50", fg="white",
                                   relief="raised", width=10, bd=0, highlightthickness=0)
        encrypt_button.pack(side=tk.LEFT, padx=(20, 5), pady=10)

        # 清空按钮
        clear_button = tk.Button(button_frame, text="🔄", command=self.clear_encrypt_fields,
                                 font=("Helvetica Neue", 14, "bold"), bg="#e0e0e0", fg="black",
                                 relief="raised", width=3, bd=0, highlightthickness=0)
        clear_button.pack(side=tk.LEFT)

        # 用于显示加密结果的标签
        self.result_label_encrypt = ttk.Label(self.encrypt_frame, text="", foreground="red",
                                              font=("Helvetica Neue", 14), background="#f2f2f2")
        self.result_label_encrypt.pack(pady=(10, 20))

    def setup_decrypt_tab(self):
        # 解密页面的UI设置
        ttk.Label(self.decrypt_frame, text="输入10位二进制密钥:", font=("Helvetica Neue", 14, "bold"), background="#f2f2f2").pack(pady=(15, 5))
        self.key_decrypt_entry = ttk.Entry(self.decrypt_frame, width=40, font=("Helvetica Neue", 14), justify='center', show='*')
        self.key_decrypt_entry.pack(pady=10)

        ttk.Label(self.decrypt_frame, text="输入8位密文:", font=("Helvetica Neue", 14, "bold"), background="#f2f2f2").pack(pady=(10, 5))
        self.ciphertext_entry = ttk.Entry(self.decrypt_frame, width=40, font=("Helvetica Neue", 14), justify='center', show='*')
        self.ciphertext_entry.pack(pady=10)

        # 创建按钮框并添加解密和清空按钮
        button_frame = tk.Frame(self.decrypt_frame, bg="#f2f2f2")
        button_frame.pack(pady=20)

        # 解密按钮
        decrypt_button = tk.Button(button_frame, text="🔓 解密", command=self.decrypt_action,
                                   font=("Helvetica Neue", 14, "bold"), bg="#f44336", fg="white",
                                   relief="raised", width=10, bd=0, highlightthickness=0)
        decrypt_button.pack(side=tk.LEFT, padx=(20, 5), pady=10)

        # 清空按钮
        clear_button = tk.Button(button_frame, text="🔄", command=self.clear_decrypt_fields,
                                 font=("Helvetica Neue", 14, "bold"), bg="#e0e0e0", fg="black",
                                 relief="raised", width=3, bd=0, highlightthickness=0)
        clear_button.pack(side=tk.LEFT)

        # 用于显示解密结果的标签
        self.result_label_decrypt = ttk.Label(self.decrypt_frame, text="", foreground="red",
                                              font=("Helvetica Neue", 14), background="#f2f2f2")
        self.result_label_decrypt.pack(pady=(10, 20))

    def encrypt_action(self):
        # 处理加密按钮的操作
        key_input = self.key_entry.get()  # 获取密钥输入
        plaintext_input = self.plaintext_entry.get()  # 获取明文输入

        # 验证输入有效性
        if self.sdes.is_valid_input(key_input, 10) and self.sdes.is_valid_input(plaintext_input, 8):
            key = [int(bit) for bit in key_input]  # 将密钥转换为整型列表
            plaintext = [int(bit) for bit in plaintext_input]  # 将明文转换为整型列表
            encrypted_text = self.sdes.encrypt(plaintext, key)  # 执行加密操作
            self.result_label_encrypt.config(text=f"加密结果: {''.join(map(str, encrypted_text))}")  # 显示加密结果
        else:
            # 如果输入无效，清空输入框并弹出错误消息
            self.key_entry.delete(0, tk.END)
            self.plaintext_entry.delete(0, tk.END)
            messagebox.showerror("Error", "无效输入，请确保密钥为10位，明文为8位二进制数。")

    def decrypt_action(self):
        # 处理解密按钮的操作
        key_input = self.key_decrypt_entry.get()
        ciphertext_input = self.ciphertext_entry.get()

        # 验证输入有效性
        if self.sdes.is_valid_input(key_input, 10) and self.sdes.is_valid_input(ciphertext_input, 8):
            key = [int(bit) for bit in key_input]  # 将密钥转换为整型列表
            ciphertext = [int(bit) for bit in ciphertext_input]  # 将密文转换为整型列表
            decrypted_text = self.sdes.decrypt(ciphertext, key)  # 执行解密操作
            self.result_label_decrypt.config(text=f"解密结果: {''.join(map(str, decrypted_text))}")  # 显示解密结果
        else:
            # 如果输入无效，清空输入框并弹出错误消息
            self.key_decrypt_entry.delete(0, tk.END)
            self.ciphertext_entry.delete(0, tk.END)
            messagebox.showerror("Error", "无效输入，请确保密钥为10位，密文为8位二进制数。")

    def clear_encrypt_fields(self):
        # 清空加密页面的输入框和结果标签
        self.key_entry.delete(0, tk.END)
        self.plaintext_entry.delete(0, tk.END)
        self.result_label_encrypt.config(text="")

    def clear_decrypt_fields(self):
        # 清空解密页面的输入框和结果标签
        self.key_decrypt_entry.delete(0, tk.END)
        self.ciphertext_entry.delete(0, tk.END)
        self.result_label_decrypt.config(text="")

# 主程序入口
if __name__ == "__main__":
    root = tk.Tk()  # 创建Tkinter窗口
    app = SDESApp(root)  # 实例化SDESApp类
    root.mainloop()  # 启动主循环，等待事件