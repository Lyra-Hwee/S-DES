import time
from SDES import SDES

class BruteForce:
    def __init__(self):
        self.sdes = SDES()

    def find_valid_keys(self, pairs):
        valid_keys = []  # 用于存储有效密钥

        for key_candidate in range(1024):  # 1024 = 2^10
            key_bits = self.sdes.int_to_bits(key_candidate, 10)  # 将密钥转换为10位二进制列表
            matches = True  # 假设密钥是有效的

            # 检查所有的明密文对
            for plaintext, ciphertext in pairs:
                encrypted_result = self.sdes.encrypt(plaintext, key_bits)
                # 如果任何一个加密结果不匹配，设置为 False
                if encrypted_result != ciphertext:
                    matches = False
                    break

            if matches:  # 如果所有明密文对都匹配
                valid_keys.append(key_bits)  # 添加到有效密钥列表

        return valid_keys


if __name__ == "__main__":
    brute_force = BruteForce()

    while True:  # 循环以允许多次输入
        pairs = []  # 用于保存明密文对

        # 读取用户的明密文对
        while True:
            pair_input = input("请输入明密文对 (格式：明文 密文，如 10110011 11001100)，或输入 'end' 结束输入: ")
            if pair_input.lower() == 'end':
                break  # 用户输入结束，停止接收
            try:
                plaintext, ciphertext = pair_input.split()
                # 检查输入的长度是否正确
                if len(plaintext) != 8 or len(ciphertext) != 8:
                    raise ValueError("明文和密文必须为8位二进制数。")
                plaintext = [int(bit) for bit in plaintext]  # 转为二进制列表
                ciphertext = [int(bit) for bit in ciphertext]  # 转为二进制列表
                pairs.append((plaintext, ciphertext))  # 添加到列表中
            except ValueError as e:
                print(f"输入错误: {e}. 请重新输入。")  # 提示用户输入错误

        # 记录开始时间
        start_time = time.time()
        found_keys = brute_force.find_valid_keys(pairs)  # 进行暴力破解
        # 记录结束时间
        end_time = time.time()

        # 输出找到的密钥
        if found_keys:
            print("找到的密钥:")
            for key in found_keys:
                print(f"{''.join(map(str, key))}")  # 打印每一个找到的密钥
        else:
            print("未找到符合条件的有效密钥。")

        # 计算并输出所用时间
        elapsed_time = end_time - start_time
        print(f"花费的时间: {elapsed_time:.4f} 秒")

        # 询问用户是否继续
        continue_choice = input("是否继续输入明密文对？(y/n): ").strip().lower()
        if continue_choice != 'y':
            print("退出程序。")
            break