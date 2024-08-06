from PIL import Image

# 加载图片并转换为灰度图
img = Image.open("D:\py\图片转字符串\“甜蜜的”穹顶.jpg").convert('L')

# 调整图片大小
img = img.resize((130, 80))
# 创建字符映射表
characters = list("@%#*+=-:. ")
# 根据图片的最大亮度值确定分段的阈值
thresholds = [i * 255 // len(characters) for i in range(1, len(characters))]
# 遍历像素
asclis = ''
for y in range(img.height):
    for x in range(img.width):
        hui_num = img.getpixel((x, y))
        # 非线性映射
        for i, threshold in enumerate(thresholds):
            if hui_num < threshold:
                idx = i
                break

        asclis += characters[idx]

    asclis += "\n"

# 输出
print(asclis)
