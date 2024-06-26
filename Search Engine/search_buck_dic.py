import pandas as pd

inp = input('What do you want to search?\n')
df = pd.read_csv('Barc_search.csv')

hold = set(inp.lower().split(' '))
df_co = df.shape[0]
count_buck = {}

for i in range(df_co):

    count = 0

    for j in hold:

        if j in df.iloc[i, 1]:
            count += 1
    
    if count > 0:
        
        if count in count_buck:
            count_buck[count].append(df.iloc[i, 0])
        else:
            count_buck[count] = []
            count_buck[count].append(df.iloc[i, 0])

# print(sorted(count_buck, reverse = True))

for key,value in sorted(count_buck.items(),reverse=True):
    print('\n'.join(map(str, value)))
