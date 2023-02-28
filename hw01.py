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
#二進位轉換十六進位
length = len(binary_list)
hexadecimal_list = [0, 0]

hexadecimal_1 = 0
hexadecimal_2 = 0
total_1 = 0
total_2 = 0
#將經過二進位轉換後的list切分成前後兩段
binary_list_1 =  binary_list[0:length//2]
binary_list_2 =  binary_list[length//2:len(binary_list)]

#第一段數字加總
binary_list_1.reverse()
for i in range(len(binary_list_1)):
    total_1 += binary_list_1[i] * (2**i)
#第二段數字加總
binary_list_2.reverse()
for i in range(len(binary_list_2)):
    total_2 += binary_list_2[i] * (2**i)

#將加總數字對應到十六進位的轉換表
hexadecimal_dict = {'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,
                    '10': 'A', '11': 'B', '12':'C', '13':'D', '14': 'E', '15': 'F', '16': 'G'}
#輸出十六進位答案
print("This is your hexadecimal number:",str(hexadecimal_dict[str(total_1)])+str(hexadecimal_dict[str(total_2)]))