# -*- coding:utf-8 -*-

from pyecharts import Style
from pyecharts import Geo


# city = []

# with open('quan.txt', mode = 'r', encoding = 'utf-8') as f:
# 	lines = f.readlines()
# 	for line in lines:
# 		arr = line.split(',')
# 		if len(arr) == 5:
# 			city.append(arr[2].replace('\n',''))

# def all_list(arr):
# 	result = {}
# 	for i in set(arr):
# 		result[i] = arr.count(i)
# 	return result

# data = []
# for item in all_list(city):
# 	data.append((item, all_list(city)[item]))

# 上述代码获取的地址，有些不能解析出来的干扰地址，需要去除，去除之后的显示情况
data = [('漳州', 1), ('石狮', 1), ('株洲', 1), ('晋城', 1), ('增城', 1), ('信阳', 2), ('日照', 1), ('厦门', 2), ('舟山', 1), ('福州', 1), ('湘潭', 1), ('辽阳', 2), ('龙岩', 1), ('重庆', 1), ('西安', 3), ('登封', 1), ('长春', 1), ('深圳', 1), ('昆山', 2), ('兰州', 1), ('芜湖', 1), ('许昌', 1), ('定州', 1), ('郴州', 1), ('苏州', 4), ('铜仁', 2), ('敦化', 1), ('南宁', 1), ('马鞍山', 1), ('唐山', 2), ('郑州', 14), ('青岛', 6), ('兰州', 1), ('商丘', 1), ('济宁', 1), ('海宁', 1), ('汝州', 1), ('常州', 5), ('威海', 2), ('天津', 2), ('青岛', 1), ('台州', 1), ('包头', 6), ('烟台', 8), ('银川', 1), ('三河', 1), ('宝鸡', 1), ('曲阜', 1), ('临汾', 2), ('运城', 2), ('常熟', 3), ('开封', 3), ('明光', 1), ('新洲区', 1), ('日照', 1), ('沛县', 1), ('太原', 1), ('上海', 7), ('张家口', 2), ('北京', 17), ('钦州', 1), ('太原', 2), ('湖州', 1), ('宜昌', 2), ('惠州', 2), ('绵阳', 1), ('巢湖', 1), ('张家港', 2), ('毕节', 2), ('上饶', 1), ('石家庄', 4), ('兴城', 1), ('上饶', 1), ('青州', 1), ('滕州', 1), ('日照', 1), ('沧州', 1), ('吕梁', 1), ('寿光', 1), ('南通', 3), ('乌鲁木齐', 2), ('中山', 1), ('江阴', 2), ('重庆', 5), ('成都', 10), ('东阳', 1), ('无锡', 2), ('通辽', 2), ('徐州', 4), ('扬州', 1), ('德州', 1), ('昆明', 1), ('瑞安', 1), ('武汉', 7), ('盐城', 6), ('襄阳', 1), ('营口', 2), ('大理', 1), ('瑞昌', 1), ('长治', 1), ('贵港', 1), ('盘锦', 1), ('阜新', 1), ('沈阳', 3), ('蚌埠', 1), ('辽源', 1), ('即墨', 1), ('南京', 11), ('连云港', 3), ('长沙', 5), ('广州', 4), ('贵阳', 3), ('北海', 1), ('泉州', 2), ('六安', 1), ('绍兴', 2), ('镇江', 3), ('大连', 4), ('东台', 1), ('乐山', 1), ('廊坊', 1), ('温州', 1), ('九江', 2), ('咸宁', 2), ('普宁', 1), ('呼和浩特', 2), ('宜宾', 1), ('佛山', 4), ('淮安', 2), ('新密', 1), ('顺德', 1), ('彭州', 1), ('保定', 1), ('鞍山', 3), ('潢川县', 1), ('温岭', 1), ('秦皇岛', 1), ('六盘水', 1), ('汕头', 1), ('东莞', 2), ('珠海', 1), ('哈尔滨', 4), ('杭州', 5), ('咸阳', 1), ('临沂', 4), ('泰安', 2)]

style = Style(
		title_color = '#fff',
		title_pos = 'center',
		width = 1200,
		height = 600,
		background_color = '#404a59'
		)

	
# print(data)

geo = Geo("《邪不压正》粉丝人群地理位置", "数据来源：练习Python", **style.init_style)

attr, value = geo.cast(data)

geo.add("",attr,value,visual_range=[0,20],
	visual_text_color='#fff',
	symbol_size=20,
	is_visualmap=True,
	is_piecewise=True,
	visual_split_number=4
	)

geo.render()












