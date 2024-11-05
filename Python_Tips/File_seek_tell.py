with open(r'Python_Tips\Python_linter.txt', 'r') as f:
    
    # Start reading the data from 5th position of the file -    
    f.seek(5)

    # read next 5 bytes
    data = f.read(5)
    print(data)


    # tell function tells the current position of the cursor since we seeked 5 bytes and read 5 bytes tell will give an output of 10
    print(f.tell())
