from pyecharts import ThemeRiver
from pyecharts import Pie

rate = []

with open('quan.txt', mode='r',encoding='utf-8') as f:
	lines = f.readlines()
	for line in lines:
		arr = line.split(',')
		if len(arr) == 5:
			rate.append(arr[3].replace('\n',''))
print(rate.count('5')+rate.count('4.5'))
print(rate.count('4')+rate.count('3.5'))
print(rate.count('3')+rate.count('2.5'))
print(rate.count('2')+rate.count('1.5'))
print(rate.count('1')+rate.count('0.5'))


attr = ['五星','四星','三星','二星','一星']
v1 = [3324,1788,1293,553,1653]
pie = Pie('饼图-星级图示例', 
	title_pos='center', 
	width=900
	)
pie.add("7-17", attr, v1, 
	center=[75,50],
	is_random=True, 
	radius=[30,75],
	rosetype='area', 
	is_legend_show=False,
	is_label_show=True
	)

pie.render()



















