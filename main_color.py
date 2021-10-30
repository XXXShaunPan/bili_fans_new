import PIL.Image as Image
import colorsys
import requests as rq
import os
# from spider_UP_pic import spider_pic
 

# input_pic=[196356191,32786875,9617619,390461123,437316738,17561219,1871001,479918671,505370779,15143934,359314,438880209,489412051,592560791,254040065,359423988,481470422,206932746,14182761,777536,466272,1188981217,1868902080,45912795,660127655,443275433,514241541,453106948,498581698,663142480,454349858,510598973,167945180,473048378,601599005,382731410,518888859,27977500,486310631,550505981,431685318,665891831,474477818,651719656,558125898,612820586,400613638,486717621,481805383,533622509,497280316,491240131,591798830,453981403,533337148,32187114,359314,32819897,13826696,443593223,3210592,200817734,35393135,4198849,510146862,107297669,22871593,431623653,6548616,76430484,471959769,13542382,328284808,86254673,109,382806584,6421869,388020815,32375398]


def get_dominant_color(image):
    
#颜色模式转换，以便输出rgb颜色值
    image = image.convert('RGBA')
    
#生成缩略图，减少计算量，减小cpu压力
    image.thumbnail((200, 200))
    
    max_score = 0
    dominant_color = 0
    
    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        # 跳过纯黑色
        if a == 0:
            continue
        
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]

        if((r<20)&(g<20)&(b<20)):
            continue

        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
       
        y = (y - 16.0) / (235 - 16)
        
        # 忽略高亮色
        if y > 0.9:
            continue
        
        score = (saturation + 0.1) * count

        
        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)
    
    return dominant_color
 

def trans_rgb(input_rgb):
    try:
        list=input_rgb.split(',')
        str1=list[0][4:]
        str2=list[1][1:]
        str3=list[2][1:-1]
        # hex返回的字母A~F均为小写字母a~f，根据样例输出，用upper函数把字母全部转为大写
        hex1=hex(int(str1))[2:].upper()
        hex2=hex(int(str2))[2:].upper()
        hex3=hex(int(str3))[2:].upper()
        # 十进制转16进制时会出现缺省零的情况，用rjust函数可在字符串左侧填充0
        # 同理 ljust函数可在字符串的右侧填充0
        hex1 = hex1.rjust(2, '0')
        hex2 = hex2.rjust(2, '0')
        hex3 = hex3.rjust(2, '0')
        outputstr="0x"
        outputstr=outputstr+hex1+hex2+hex3
    except:
        outputstr="0x35292D"
    return outputstr

def main(input_pic):
    result_all=[]
    root='bili_UP_pic/'
    for i in input_pic:
		try:
			pic=rq.get(f'https://api.bilibili.com/x/space/acc/info?mid={i}').json()['data']['face']
		except:
			pic="https://static.hdslb.com/images/member/noface.gif"
		with open(f'{root}{i}.jpg','wb') as f:
			f.write(rq.get(pic).content)
			print(str(i)+"——下载完成==",end="")
		input_rgb="rgb"+str(get_dominant_color(Image.open(f'{root}/{i}.jpg')))
		result_all.append(trans_rgb(input_rgb))
		print(i)
    # print('\n\ncolor,'+','.join(result_all))
    return result_all
# print(hex(255))
# print(type(hex(255)))
# print(hex(255))
