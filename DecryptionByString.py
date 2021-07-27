import string

#解密函數
def decrypt(text, decryDict):
    not_cipher = []
    for i in text:
        r = decryDict[i]
        not_cipher.append(r)
    return ''.join(not_cipher)
abc = string.printable[:-3]
subText = abc[-3:] + abc[:-3]
decry_dict = dict(zip(abc, subText))

#文件解密來源位置
fn1 = r'C:\Users\User\Desktop\encry.txt'
with open(fn1) as file_obj:
    encry_msg = file_obj.read()

#解密過程
not_ciphertext = decrypt(encry_msg, decry_dict)
print("解密後:\n"+not_ciphertext)

#文件解密後存放位置
fn2 = r'C:\Users\User\Desktop\decry.txt'
with open(fn2, 'w') as file_obj:
    decry_msg = file_obj.write(not_ciphertext)
