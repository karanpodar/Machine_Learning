import pandas as pd

inp = input('What do you want to search?\n')
df = pd.read_csv('Barc_search.csv')

hold = set(inp.lower().split(' '))
# print(hold)
df_co = df.shape[0]
count_dict = {}

for i in range(df_co):
    # print(df.iloc[i, 1])  
    count = 0

    for j in hold:
        # print(j)
        if j in df.iloc[i, 1]:
            count += 1
    
    if count > 0:
        count_dict[df.iloc[i, 0]] = count

print(count_dict)