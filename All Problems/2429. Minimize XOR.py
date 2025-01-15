class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        num2_binary = format(num2, 'b')
        num1_binary = format(num1, 'b')
        n = max(len(num2_binary), len(num1_binary))
        
        if len(num2_binary) != n:
            for i in range(0, n - len(num2_binary)):
                num2_binary = "0" + num2_binary
        if len(num1_binary) != n:
            for i in range(0, n - len(num1_binary)):
                num1_binary = "0" + num1_binary    

        count = num2_binary.count('1')

        result = ""
        temp_count = 0
        while(len(num1_binary) > 0):
            last_digit = num1_binary[-1]
            num1_binary = num1_binary[:-1]
            if last_digit == '1':
                result = "1" + result
                temp_count = temp_count + 1
            else:
                result = last_digit + result

        if temp_count < count :
            for i in range(len(result) - 1, -1, -1):
                if (temp_count == count):
                    break
                if result[i] == '0':
                    result = result[:i] + "1" + result[i+1:]
                    temp_count = temp_count + 1
        elif temp_count > count:
            for i in range(len(result) - 1, -1, -1):
                if (temp_count == count):
                    break
                if result[i] == '1':
                    result = result[:i] + "0" + result[i+1:]
                    temp_count = temp_count - 1

        return int(result, 2)
