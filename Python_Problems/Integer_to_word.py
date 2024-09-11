'''
Convert a non-negative integer num to its English words representation.
Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''

word_dict = {
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine',
    10 : 'Ten',
    11 : 'Eleven',
    12 : 'Twelve',
    13 : 'Thirteen',
    14 : 'Fourteen',
    15 : 'Fifteen',
    16 : 'Sixteen',
    17 : 'Seventeen',
    18 : 'Eighteen',
    19 : 'Ninteen',
    20 : 'Twenty',
    30 : 'Thirty',
    40 : 'Forty',
    50 : 'Fifty',
    60 : 'Sixty',
    70 : 'Seventy',
    80 : 'Eighty',
    90 : 'Ninety'
}

def int_to_word(num):

    if num == 0:
        return 'Zero'
    
    output = []
    count = 1
   
    if num in word_dict:
        return word_dict[num]
    
    while num != 0:
    
        temp = num % 1000
        match count:
            case 2:
                output.insert(0, 'Thousand')
            case 3:
                output.insert(0, 'Million')
            case 4:
                output.insert(0, 'Biilion')
        
        if temp in word_dict:
            output.insert(0, word_dict[temp])

        else:
            temp_hund_remain = temp % 100
            temp_hund = temp // 100

            if temp_hund_remain in word_dict:
                output.insert(0, word_dict[temp_hund_remain])
            else:
                temp_one = temp_hund_remain % 10
                temp_ten = (temp_hund_remain // 10) * 10
                
                if temp_one in word_dict:
                    output.insert(0, word_dict[temp_one])
                    output.insert(0, word_dict[temp_ten])

            if temp_hund in word_dict:
                output.insert(0, 'Hundred')
                output.insert(0, word_dict[temp_hund])


        num = num // 1000
        count += 1

    output = ' '.join(output)
    
    return output

num = 1234567
print(int_to_word(num))