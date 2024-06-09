with open(r'Python_Tips\Sample_Truncate.txt', 'w') as f:
    f.write("<<HELLO WORLD>>")
    # truncate will trim the data upto the length of 10 and will write only first 10 bytes of data
    f.truncate(10) 