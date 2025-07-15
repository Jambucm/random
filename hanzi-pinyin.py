import pandas as pd

hanzi = pd.read_csv('hanziDB.csv')

text = """

INSERT CHARACTER(S) HERE

"""

pinyin = ''
for char in text:
    pin = hanzi[hanzi['charcter'] == char]['pinyin']
    if not pin.empty:
        pinyin += pin.iloc[0] + ' '
    else:
        pinyin += char

print(pinyin)
