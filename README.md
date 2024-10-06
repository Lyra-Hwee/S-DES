# S-DES测试结果

<img width="335" alt="图片1" src="https://github.com/user-attachments/assets/606704aa-5f06-48cc-a68b-95b19e20afa0">

## 第一关：基本测试
加密操作：
输入10bit密钥和8bit明文

密钥：1010101010
明文：10101010

<img width="331" alt="图片2" src="https://github.com/user-attachments/assets/8ab0368b-8945-47cd-a591-9ca8de172354">

获取加密结果

<img width="336" alt="图片3" src="https://github.com/user-attachments/assets/0d2cbd6a-5d79-4f5c-9b71-518994fad443">

解密操作：
输入10bit密钥和8bit密文

密钥：1010101010
密文：10001111

<img width="335" alt="图片4" src="https://github.com/user-attachments/assets/67df9c6e-3a6e-48fc-8cad-b1bdfdea3ad7">

获取解密结果

<img width="332" alt="图片5" src="https://github.com/user-attachments/assets/d8fc229e-87cf-4643-8761-4572f836149a">

## 第二关：交叉测试
我们与黄涛组的同学进行了二进制和ASCII的加密解密交叉测试，得出结果如下

二进制加密

二进制明文和密钥相同时，加密所得密文也相同

<img width="337" alt="图片6" src="https://github.com/user-attachments/assets/5dde3ec0-95f0-424a-8207-427a9d134082">

![图片7](https://github.com/user-attachments/assets/4c944aa3-ad79-4a2e-8226-bae401cd68f3)


二进制解密

二进制密文和密钥相同时，解密所得明文也相同

<img width="329" alt="图片8" src="https://github.com/user-attachments/assets/aaff017a-08d0-4fa6-bbc5-7b49bf15912b">

![图片9](https://github.com/user-attachments/assets/42dd4d8b-9a96-4990-96a7-b4c10c793bed)


ASCII加密

ASCII明文和密钥相同时，加密所得密文也相同

<img width="333" alt="图片10" src="https://github.com/user-attachments/assets/59a85911-4a5e-45b3-bea6-6c2a03b7b1ef">

![图片11](https://github.com/user-attachments/assets/c76b56d7-a993-496a-9b4f-b12fd8b06638)

ASCII解密

ASCII密文和密钥相同时，解密所得明文也相同

<img width="331" alt="图片12" src="https://github.com/user-attachments/assets/f805ee2f-1eb1-4ff9-a102-e21fab584175">

![图片13](https://github.com/user-attachments/assets/33c3aff9-999b-49b6-bc05-22bcf22fdce9)



## 第三关：扩展功能
对ASCII字符串进行加密

密钥：1010101010
明文：cat12345

<img width="334" alt="图片14" src="https://github.com/user-attachments/assets/45d75d1e-ba49-4176-a810-30f35f1bfdf5">

对ASCII字符串进行解密

密文：sparking
密钥：1111111111

<img width="331" alt="图片15" src="https://github.com/user-attachments/assets/b200fbbe-06d2-48cd-aefb-80456dfd0440">

## 第四关：暴力破解
输入明密文对

<img width="443" alt="图片16" src="https://github.com/user-attachments/assets/85f1d25f-ac02-4cb7-8751-6599b5b3546e">

开始破解

<img width="446" alt="图片17" src="https://github.com/user-attachments/assets/df63a74e-ed7e-4b7c-8741-8843a48a525a">

## 第五关：封闭测试
我们的暴力破解函数：

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
    
我们的破解函数能找到一对明密文之间的所有可能密钥，例如：
明文：10110011
密文：11001100

<img width="446" alt="图片18" src="https://github.com/user-attachments/assets/a03e8738-a806-4fd6-9401-e4283053069f">

发现该明密文之间有四把不同的密钥，破解花费时间为0.0239秒

# 用户指南 - S-DES系统
## 1.系统简介
S-DES系统是一款结合DES加解密算法，专为用户设计的工具，旨在为您提供高效的加密与解密以及破解密码服务，使用界面简单直观，即使是小白也能快速上手。
## 2.环境配置
### 2.1安装Python
请确保您的计算机上已经安装了Python。您可以通过访问Python的官方网站来下载并安装。
### 2.2安装Pycharm
为了能顺利使用该工具，您需要借助Pycharm来运行项目。您可以通过访问Pycharm的官方网站来下载并安装。
## 3.启动系统
运行Pycharm,打开我们的S-DES项目，运行项目文件。
## 4.功能介绍
系统的功能主要分为：

二进制加密：用户可以对二进制8bit明文进行加密。

二进制解密：用户可以对二进制8bit密文进行解密。

ASCII加密：用户可以对ASCII字符进行加密。

ASCII解密：用户可以对ASCII字符进行解密。

暴力破解：如果您忘记了密钥，可以使用这个功能获取密钥，并且系统能生成可能的所有密钥。

## 5.使用说明
### 5.18位二进制数加密
1.在主界面中点击二进制加解密，定位到“加密”按钮

2.在提供的输入框中，输入10bit二进制密钥和8bit二进制明文

3.点击下方加密按钮

4.在下方，您会看到将该明文加密得到的密文结果

5.可点击刷新按钮，重新输入
### 5.28位二进制数解密
1.在主界面中点击二进制加解密，定位到“解密”按钮

2.在提供的输入框中，输入10bit二进制密钥和8bit二进制密文

3.点击下方解密按钮

4.在下方，您会看到将该密文解密得到的明文结果

5.可点击刷新按钮，重新输入
### 5.3ASCII加密
1.在主界面中点击ASCII加解密，定位到“加密”按钮

2.在提供的输入框中，输入10bit二进制密钥和ASCII明文

3.点击下方加密按钮

4.在下方，您会看到将该明文加密得到的密文结果

5.可点击刷新按钮，重新输入
### 5.4ASCII解密
1.在主界面中点击ASCII加解密，定位到“解密”按钮

2.在提供的输入框中，输入10bit二进制密钥和ASCII密文

3.点击下方解密按钮

4.在下方，您会看到将该密文解密得到的明文结果

5.可点击刷新按钮，重新输入
### 5.5暴力破解
1.在主界面中点击暴力破解，输入明密文对

2.得到可能的密钥和破解时间
# 开发手册
## 1.引言
在现代信息安全中，加密技术是保护数据隐私的重要手段。AES（高级加密标准）和DES（数据加密标准）是最广泛使用的对称加密算法。本开发手册旨在为开发人员提供基于Python开发的S-DES加密算法应用程序的接口说明，适用于需要对S-DES加密算法进行集成或二次开发的开发人员。
## 2.技术栈
加密算法：S-DES加密算法
数据库：无（简单的文件存储）
编程语言：Python
## 3.主要函数
#初始化置换表和其他固定参数 
def __init__(self):

#根据给定的置换规则重新排列位
def permute(self, bits, permutation):

#根据给定的顺序进行左移操作
def left_shift(self, bits, shifts):

#扩展密钥，生成两个子密钥 K1 和 K2
def key_expansion(self, key):

#将二进制位数组转换为整数
def bits_to_int(self, bits):

#将整数转换为指定位数的二进制数组
def int_to_bits(self, value, length):

#使用 S-Box 进行置换
def s_box(self, bits, sbox):

#轮函数 F
def f_function(self, bits, subkey):

#加密函数
def encrypt(self, plaintext, key):

#解密函数
def decrypt(self, ciphertext, key):

#检查输入位是否合法（合法长度和位数）
def is_valid_input(bits, expected_length):

#加密页面的UI设置
def setup_encrypt_tab(self)

#解密页面的UI设置
def setup_decrypt_tab(self):

#处理加密按钮的操作
def encrypt_action(self):

#处理解密按钮的操作
def decrypt_action(self):

#清空加密页面的输入框和结果标签
def clear_encrypt_fields(self):

#清空解密页面的输入框和结果标签
def clear_decrypt_fields(self):

#找到有效密钥
def find_valid_keys(self, pairs):

#添加明文和密文对并开始暴力破解
def add_pair(self):

#显示错误提示消息框
def show_error(self, message):

#开始暴力破解
def start_brute_force(self):

#清空输入和结果。
def clear_all(self):

#加载并设置背景图像
def setup_background(self):

#设置主窗口的样式和按钮框
def setup_window(self):

#创建功能按钮
def create_buttons(self):

#打开加密和解密界面
def open_encrypt_decrypt(self):

#打开ASCII加解密界面
def open_ascii_app(self):

#打开暴力破解界面
def open_brute_force(self):

#打开新窗口并加载相应的应用程序
def open_new_window(self, app_class):

## 4.功能实现
### 暴力破解

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

### 加解密算法实现

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
    
    left_part_shifted2 = self.left_shift(left_part_shifted1, self.LS2)
    
    right_part_shifted2 = self.left_shift(right_part_shifted1, self.LS2)
    
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
    
## 5.性能优化
1.可以考虑使用更高效的算法或数据结构来实现置换、S 盒替换等操作，以提高加密和解密的速度。

2.对于暴力破解功能，可以考虑使用更优化的搜索算法，以减少破解时间。
## 6.安全考虑
1.S-DES 是一种相对简单的加密算法，安全性有限。不建议在对安全性要求较高的场景中单独使用。

2.在使用暴力破解功能时，应注意其计算复杂度可能较高，尤其是对于较长的明文和密文。

3.虽然使用了加密算法，但在实际应用中，应注意保护密钥的安全，避免在网络传输中泄露。

4.对于暴力破解功能，应考虑限制其使用频率，以防止恶意攻击。













