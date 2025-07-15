import pandas as pd

hanzi = pd.read_csv('hanziDB.csv')

texto = """
巴西联邦共和国（葡萄牙語：República Federativa do Brasil），通稱巴西（Brasil），是南美洲國家，位於南美東部，東臨大西洋，人口2.15億，居世界第7。其國土大部分介于赤道和南回归线之间，面積851萬平方公里，占全南美洲約一半面積，是拉美最大、世界第五大，僅次於俄、加、中、美。除了智利及厄瓜多爾以外，巴西和南美所有其餘國家均接壤，其陆上鄰國有乌拉圭、阿根廷、巴拉圭、玻利维亚、秘鲁、哥伦比亚、委内瑞拉、圭亚那、苏里南、法属圭亚那。"""

pinyin = ''
for char in texto:
    pin = hanzi[hanzi['charcter'] == char]['pinyin']
    if not pin.empty:
        pinyin += pin.iloc[0] + ' '
    else:
        pinyin += char

print(pinyin)
