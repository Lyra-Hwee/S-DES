import time
from SDES import SDES
import tkinter as tk
from tkinter import ttk, messagebox

class BruteForceBUI:
    def __init__(self, master):
        self.master = master
        master.title("SDES 暴力破解")
        master.geometry("600x450")
        master.configure(bg="#f2f2f2")

        self.sdes = SDES()

        # 设置样式
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TLabel', font=('Arial', 12), padding=5)
        self.style.configure('TEntry', font=('Arial', 12), padding=5)
        self.style.configure('TButton', font=('Arial', 12), padding=5)
        self.style.configure('TFrame', background='#f0f0f0')

        # 创建输入区域
        self.input_frame = ttk.Frame(master)
        self.input_frame.pack(padx=20, pady=20)

        # 添加标题标签
        self.title_label = ttk.Label(self.input_frame, text="S-DES 暴力破解", font=('Arial', 14, 'bold'))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))  # 在输入框上方添加标题

        self.plaintext_label = ttk.Label(self.input_frame, text="明文 (8位):")
        self.plaintext_label.grid(row=1, column=0, sticky="e")
        self.plaintext_entry = ttk.Entry(self.input_frame, width=20)
        self.plaintext_entry.grid(row=1, column=1)

        self.ciphertext_label = ttk.Label(self.input_frame, text="密文 (8位):")
        self.ciphertext_label.grid(row=2, column=0, sticky="e")
        self.ciphertext_entry = ttk.Entry(self.input_frame, width=20)
        self.ciphertext_entry.grid(row=2, column=1)

        # 将添加和清空按钮放在同一行
        self.button_frame = ttk.Frame(self.input_frame)
        self.button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.add_button = ttk.Button(self.button_frame, text="添加", command=self.add_pair)
        self.add_button.pack(side=tk.LEFT, padx=(0, 10))

        self.clear_button = ttk.Button(self.button_frame, text="清空", command=self.clear_all)
        self.clear_button.pack(side=tk.LEFT)

        # 创建显示区域并减小高度
        self.output_frame = ttk.LabelFrame(master, text="结果", padding=(10, 10))
        self.output_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.key_label = ttk.Label(self.output_frame, text="找到的密钥:")
        self.key_label.grid(row=0, column=0, sticky="w")

        self.key_text = tk.Text(self.output_frame, width=50, height=6, font=('Arial', 12), wrap=tk.WORD)  # 改为高度6
        self.key_text.grid(row=1, column=0, pady=(10, 5))

        self.time_label = ttk.Label(self.output_frame, text="用时:")
        self.time_label.grid(row=2, column=0, sticky="w")

        self.time_text = ttk.Label(self.output_frame, text="")
        self.time_text.grid(row=2, column=1)

        self.pairs = []

    def add_pair(self):
        """添加明文和密文对并开始暴力破解。"""
        try:
            plaintext = [int(bit) for bit in self.plaintext_entry.get().strip()]
            ciphertext = [int(bit) for bit in self.ciphertext_entry.get().strip()]
            if len(plaintext) != 8 or len(ciphertext) != 8:
                raise ValueError("明文和密文必须为8位二进制数。")
            self.pairs.append((plaintext, ciphertext))
            self.plaintext_entry.delete(0, tk.END)
            self.ciphertext_entry.delete(0, tk.END)
            self.start_brute_force()
        except ValueError as e:
            self.show_error(str(e))

    def find_valid_keys(self):
        """寻找符合条件的密钥。"""
        valid_keys = []  # 用于存储有效密钥

        for key_candidate in range(1024):  # 1024 = 2^10
            key_bits = self.sdes.int_to_bits(key_candidate, 10)  # 将密钥转换为10位二进制列表
            matches = True  # 假设密钥是有效的

            for plaintext, ciphertext in self.pairs:
                encrypted_result = self.sdes.encrypt(plaintext, key_bits)
                if encrypted_result != ciphertext:
                    matches = False
                    break

            if matches:  # 如果所有明密文对都匹配
                valid_keys.append(key_bits)  # 添加到有效密钥列表

        return valid_keys

    def show_error(self, message):
        """显示错误提示消息框。"""
        messagebox.showerror("错误", message)

    def start_brute_force(self):
        """开始暴力破解。"""
        if not self.pairs:
            self.show_error("请先输入明密文对。")
            return

        start_time = time.time()
        found_keys = self.find_valid_keys()
        end_time = time.time()

        self.key_text.delete("1.0", tk.END)
        if found_keys:
            for key in found_keys:
                self.key_text.insert(tk.END, "".join(map(str, key)) + "\n")
        else:
            self.key_text.insert(tk.END, "未找到符合条件的有效密钥。")

        elapsed_time = end_time - start_time
        self.time_text.configure(text=f"{elapsed_time:.4f} 秒")

    def clear_all(self):
        """清空输入和结果。"""
        self.pairs.clear()
        self.key_text.delete("1.0", tk.END)
        self.time_text.configure(text="")
        self.plaintext_entry.delete(0, tk.END)
        self.ciphertext_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = BruteForceBUI(root)
    root.mainloop()