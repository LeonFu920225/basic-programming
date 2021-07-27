import string

#加密函數
def encrypt(text, encryDict):
    cipher = []
    for i in text:
        v = encryDict[i]
        cipher.append(v)
    return ''.join(cipher)
abc = string.printable[:-3]
subText = abc[-3:] + abc[:-3]
encry_dict = dict(zip(subText, abc))

#加密文件來源位置
fn = r'C:\Users\User\Desktop\password.txt'
with open(fn) as file_obj:
    msg = file_obj.read()

#加密過程
ciphertext = encrypt(msg, encry_dict)
print("原始帳密:\n"+msg.rstrip())
print("加密後:\n"+ciphertext)

#加密後文件存檔位置
fn = r'C:\Users\User\Desktop\encry.txt'
with open(fn, 'w') as file_obj1:
    file_obj1.write(ciphertext)