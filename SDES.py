class SDES:
    def __init__(self):
        # 初始化置换表和其他固定参数  
        self.P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]  # P10 置换表，用于密钥扩展
        self.P8 = [6, 3, 7, 4, 8, 5, 10, 9]  # P8 置换表，用于生成子密钥
        self.LS1 = [2, 3, 4, 5, 1]  # 左移 1 位的模式
        self.LS2 = [3, 4, 5, 1, 2]  # 左移 2 位的模式

        # 初始置换和逆初始置换模式  
        self.IP = [2, 6, 3, 1, 4, 8, 5, 7]  # 初始置换表
        self.IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]  # 逆初始置换表
        self.EPBox = [4, 1, 2, 3, 2, 3, 4, 1]  # 扩展置换表，用于F函数
        self.SBox1 = [[1, 0, 3, 2],  # S-Box 1
                      [3, 2, 1, 0],
                      [0, 2, 1, 3],
                      [3, 1, 0, 2]]
        self.SBox2 = [[0, 1, 2, 3],  # S-Box 2
                      [2, 3, 1, 0],
                      [3, 0, 1, 2],
                      [2, 1, 0, 3]]
        self.P4 = [2, 4, 3, 1]  # P4 置换表

    """根据给定的置换规则重新排列位"""
    def permute(self, bits, permutation):
        return [bits[i - 1] for i in permutation]  # 根据置换表返回重新排列的位

    """根据给定的顺序进行左移操作"""
    def left_shift(self, bits, shifts):
        return [bits[i - 1] for i in shifts]  # 通过索引进行左移位

    """扩展密钥，生成两个子密钥 K1 和 K2"""
    def key_expansion(self, key):
        # 使用 P10 置换密钥  
        permuted_key = self.permute(key, self.P10)

        left_part = permuted_key[:5]  # 密钥的左半部分
        right_part = permuted_key[5:]  # 密钥的右半部分
        # 左移1位  
        left_part_shifted1 = self.left_shift(left_part, self.LS1)
        right_part_shifted1 = self.left_shift(right_part, self.LS1)
        K1 = self.permute(left_part_shifted1 + right_part_shifted1, self.P8)  # 生成K1

        # 左移2位  
        left_part_shifted2 = self.left_shift(left_part, self.LS2)
        right_part_shifted2 = self.left_shift(right_part, self.LS2)
        K2 = self.permute(left_part_shifted2 + right_part_shifted2, self.P8)  # 生成K2

        return K1, K2  # 返回两个子密钥  

    """将二进制位数组转换为整数"""

    def bits_to_int(self, bits):
        return int("".join(map(str, bits)), 2)  # 将位数组逐位拼成字符串并转换为整数  

    """将整数转换为指定位数的二进制数组"""
    def int_to_bits(self, value, length):
        return [int(bit) for bit in bin(value)[2:].zfill(length)]  # 转换为二进制并填充至指定长度  

    """使用 S-Box 进行置换"""
    def s_box(self, bits, sbox):
        row = self.bits_to_int([bits[0], bits[3]])  # S-Box 行由第一个和最后一个二进制位确定  
        col = self.bits_to_int([bits[1], bits[2]])  # S-Box 列由中间两个二进制位确定  
        return self.int_to_bits(sbox[row][col], 2)  # 返回 S-Box 经过置换的结果（2位二进制）  

    """轮函数 F"""
    def f_function(self, bits, subkey):
        expanded_bits = self.permute(bits, self.EPBox)  # 扩展输入位  
        xor_result = [bit ^ key_bit for bit, key_bit in zip(expanded_bits, subkey)]  # 与子密钥进行异或操作  
        left_sbox_result = self.s_box(xor_result[:4], self.SBox1)  # 对左半部进行 S-Box 置换  
        right_sbox_result = self.s_box(xor_result[4:], self.SBox2)  # 对右半部进行 S-Box 置换  
        sbox_result = left_sbox_result + right_sbox_result  # 连接 S-Box 的结果  
        return self.permute(sbox_result, self.P4)  # 最后进行 P4 置换后返回  

    """加密函数"""
    def encrypt(self, plaintext, key):
        # 生成两个子密钥  
        K1, K2 = self.key_expansion(key)
        permuted_plaintext = self.permute(plaintext, self.IP)  # 进行初始置换  
        left_part = permuted_plaintext[:4]  # 左半部分  
        right_part = permuted_plaintext[4:]  # 右半部分  

        # 第一轮  
        f_output1 = self.f_function(right_part, K1)  # 调用 F 函数  
        left_xor_f1 = [l_bit ^ f1_bit for l_bit, f1_bit in zip(left_part, f_output1)]  # 左半部与 F 输出进行异或  
        left_part, right_part = right_part, left_xor_f1  # 交换部分  

        # 第二轮  
        f_output2 = self.f_function(right_part, K2)  # 调用 F 函数  
        left_xor_f2 = [l_bit ^ f2_bit for l_bit, f2_bit in zip(left_part, f_output2)]  # 左半部与 F 输出进行异或  
        final_bits = left_xor_f2 + right_part  # 拼接成加密后的位  

        return self.permute(final_bits, self.IP_inv)  # 进行逆初始置换，返回加密结果  

    """解密函数"""
    def decrypt(self, ciphertext, key):
        # 生成两个子密钥
        K1, K2 = self.key_expansion(key)
        permuted_ciphertext = self.permute(ciphertext, self.IP)  # 进行初始置换  
        left_part = permuted_ciphertext[:4]  # 左半部分  
        right_part = permuted_ciphertext[4:]  # 右半部分  

        # 第一轮（使用 K2）  
        f_output1 = self.f_function(right_part, K2)  # 调用 F 函数  
        left_xor_f1 = [l_bit ^ f1_bit for l_bit, f1_bit in zip(left_part, f_output1)]  # 左半部与 F 输出进行异或  
        left_part, right_part = right_part, left_xor_f1  # 交换部分  

        # 第二轮（使用 K1）  
        f_output2 = self.f_function(right_part, K1)  # 调用 F 函数  
        left_xor_f2 = [l_bit ^ f2_bit for l_bit, f2_bit in zip(left_part, f_output2)]  # 左半部与 F 输出进行异或  
        final_bits = left_xor_f2 + right_part  # 拼接成解密后的位  

        return self.permute(final_bits, self.IP_inv)  # 进行逆初始置换，返回解密结果  

    """检查输入位是否合法（合法长度和位数）"""
    @staticmethod
    def is_valid_input(bits, expected_length):
        return len(bits) == expected_length and all(bit in '01' for bit in bits)  # 确保长度正确且全为二进制位
