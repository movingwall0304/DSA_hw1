#<<資料結構與演算法>>作業一 
#將十進位數字轉換成二進位與16進位

#請使用者想要轉換的十進位數字
decimal_number = float(input("Please enter a decimal number between 0 to 255.\n"))

#確保使用者輸入的數字在0-255間，若不符合條件則提醒使用者
if decimal_number > 255 or decimal_number < 0:
    raise ValueError("Your number is not in a specific range.")
    
#十進位轉換二進位
binary_ori = decimal_number
binary_list = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(binary_list)-1,-1,-1):
    if binary_ori < 2**i:
        binary_list[len(binary_list) - (i + 1)] = 0
    else:
        binary_list[len(binary_list) - (i + 1)] = 1
        binary_ori = binary_ori - 2**i
print("This is your binary number:",*binary_list)
#十六進位轉換