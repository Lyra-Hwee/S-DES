from SDES import SDES

def main():
    # 获取用户输入的密钥
    key = input("请输入密钥 (10 位二进制数): ")

    # 确保输入格式正确
    if not SDES.is_valid_input(key, 10):
        print("错误: 密钥必须是 10 位二进制数")
        return

    # 获取用户输入的选择
    choice = input("请选择操作 (1. 加密, 2. 解密): ")

    # 获取用户输入的明文或密文
    if choice == '1':
        plaintext = input("请输入明文 (ASCII 字符串): ")
        input_data = plaintext
    elif choice == '2':
        ciphertext = input("请输入密文 (ASCII 字符串): ")
        input_data = ciphertext
    else:
        print("错误: 无效的选择")
        return

    # 将输入数据转换为二进制位列表
    bits = [bit for char in input_data for bit in SDES().int_to_bits(ord(char), 8)]

    if choice == '1':
        # 加密
        ciphertext_bits = []
        for i in range(0, len(bits), 8):
            block = bits[i:i+8]
            encrypted_block = SDES().encrypt(block, [int(bit) for bit in key])
            ciphertext_bits.extend(encrypted_block)

        # 输出加密结果
        ciphertext_chars = [chr(SDES().bits_to_int(ciphertext_bits[i:i+8])) for i in range(0, len(ciphertext_bits), 8)]
        ciphertext = ''.join(ciphertext_chars)
        print("加密结果:", ciphertext)

    elif choice == '2':
        # 解密
        decrypted_bits = []
        for i in range(0, len(bits), 8):
            block = bits[i:i+8]
            decrypted_block = SDES().decrypt(block, [int(bit) for bit in key])
            decrypted_bits.extend(decrypted_block)

        # 输出解密结果
        decrypted_text = ''.join(chr(SDES().bits_to_int(decrypted_bits[i:i+8])) for i in range(0, len(decrypted_bits), 8))
        print("解密结果:", decrypted_text)

if __name__ == "__main__":
    main()