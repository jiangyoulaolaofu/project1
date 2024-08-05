import requests
import os

# 定义目录路径
directory_path = '../pythonProject.py/教程练习/爬虫练习/img/'

# 使用os.makedirs()创建目录，如果目录已存在则不会引发错误
os.makedirs(directory_path, exist_ok=True)

# 接下来，你可以继续你的文件写入操作

www = requests.get("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt=zh-CN").json()
url0 = www["images"]

for i in url0:
    url = "https://cn.bing.com" + i["url"]
    title = "./img/" + i['title'] + ".jpg"
    img_file = requests.get(url)
    # 检查文件是否已经存在
    if os.path.isfile(title):
        print(f'{title}文件已存在，跳过下载。')
        continue
    with open(title, "wb") as f:
        f.write(img_file.content)
    print(f"文件{title}下载完成。")

