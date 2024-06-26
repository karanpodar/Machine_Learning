import pandas as pd

inp = input('What do you want to search?\n')
df = pd.read_csv('Barc_search.csv')

hold = set(inp.lower().split(' '))
df_co = df.shape[0]
count_buck = [[] for _ in range(len(hold)+1)]

for i in range(df_co):

    count = 0

    for j in hold:

        if j in df.iloc[i, 1]:
            count += 1
    
    if count > 0:
        count_buck[count].append(df.iloc[i, 0])

#print(count_buck)

for k in range(len(count_buck)-1, 0, -1):
    if len(count_buck[k]) == 0:
        continue
    else:
        print('\n'.join(map(str, count_buck[k])))
