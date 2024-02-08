import pandas

data = pandas.read_excel('output.xlsx')
print(data)
for elemet in data.iterrows():
    print(elemet)
