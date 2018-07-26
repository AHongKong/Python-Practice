import requests, json, time, random

def get_one_page(url):
	headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
	}

	response = requests.get(url,headers = headers)

	if response.status_code == 200:
		return response.text
	return None
# {"cmts":
# [{"approve":0,"approved":false,"avatarurl":"https://img.meituan.net/avatar/9e8050ec37a70f358bb3a30b3202174018469.jpg","cityName":"郑州","content":"波澜很小，，，","filmView":false,"id":1030868918,"isMajor":false,"juryLevel":0,"majorType":0,"movieId":248566,"nick":"刘嘚嘚哦","nickName":"刘嘚嘚哦","oppose":0,"pro":false,"reply":0,"score":2.5,"spoiler":0,"startTime":"2018-07-26 12:03:06","supportComment":true,"supportLike":true,"sureViewed":0,"tagList":{"fixed":[{"id":4,"name":"购票"}]},"time":"2018-07-26 12:03","userId":584267349,"userLevel":2,"videoDuration":0,"vipType":0}]
def parse_one_page(html):
	data = json.loads(html)['cmts']

	for item in data:
		yield{
		'comment':item['content'],
		'date':item['time'].split(' ')[0],
		'rate':item['score'],
		'city':item['cityName'],
		'nickname':item['nickName']
		}
def save_to_txt():
	for i in range(1,1001):
		# 下载数据
		url = 'http://m.maoyan.com/mmdb/comments/movie/248566.json?_v_=yes&offset=' + str(i)
		# 解析数据
		html = get_one_page(url)
		print('正在保存第%d页' % i)

		for item in parse_one_page(html):
			# 保存数据
			with open('xie_zheng.txt','a',encoding='utf-8') as f:
				f.write(item['date'] + ',' + item['nickname'] + ',' +item['city'] + ',' + str(item['rate']) + ',' + item['comment'] + '\n')
		time.sleep(5 + float(random.randint(1,100))/20)


# save_to_txt()

def xie_zheng(infile, outfile):
	infopen = open(infile, 'r', encoding = 'utf-8')
	outopen = open(outfile, 'w', encoding = 'utf-8')
	lines = infopen.readlines()
	list_1 = []

	for line  in lines:
		if line not in list_1:
			list_1.append(line)
			outopen.write(line)
	infopen.close()
	outopen.close()

# 评论去重
xie_zheng('xie_zheng.txt','quan.txt')











