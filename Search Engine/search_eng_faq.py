import pandas as pd
import time

inp = input('What do you want to search?\n')

start = time.process_time()

df = pd.read_csv('Barclays_FAQs.csv', encoding='cp1252')

hold = set(inp.lower().split(' '))
# print(hold)
df_co = df.shape[1]    #count of FAQs Titles
count_dict = {}

for i in range(df_co):
    # print(df.iloc[i, 1])  
    count = 0

    for j in hold:
        # print(j)
        if j in df.iloc[i, 1]:
            count += 1
    
    if count > 0:
        count_dict[df.iloc[i, 3]] = count

end = time.process_time()

print(count_dict)
print('time', end - start)