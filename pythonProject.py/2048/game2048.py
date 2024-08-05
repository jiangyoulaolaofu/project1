import msvcrt
import os
import random
import sys
import time

from PyQt5.QtWidgets import QApplication
from matplotlib.backends.backend_qt import MainWindow
from tabulate import tabulate


# 接口函数
def start():
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


class Run2048:

    # 初始化图表
    def __init__(self):
        self.debug = 'PYCHARM_HOSTED' in os.environ
        self.matrix = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 4, 0, 0],
            [0, 0, 0, 0],
        ]
        self.grade = 0

    # 找到列表里的0
    def find0(self):
        """
        判断matrix列表里元素是否为0，找下标，存入新列表

        """
        temp = []
        for x in range(4):
            for y in range(4):
                if self.matrix[x][y] == 0:
                    temp.append([x, y])
        # print(temp)
        return temp

    # 新增两个方块  赋值2或4
    def new_brick(self):
        """
        随机先找两个下标，通过下标找到值 赋值2或4
        :return: NANO

        """
        # 判断temp列表长度
        temp = self.find0()
        long = len(temp)
        if long > 1:
            temp1 = random.sample(temp, 2)
        elif long == 1:
            temp1 = random.sample(temp, 1)
        else:
            return
            # 从新列表随机选择2个下标.
        for x, y in temp1:
            if random.randint(0, 100) < 89:
                self.matrix[x][y] = 2
            else:
                self.matrix[x][y] = 4

    # 输出图表
    def print_inter(self):
        """
        打印出图标
        """
        if not self.debug:
            os.system("cls")
        print('当前分数是：', self.grade)
        print(tabulate(self.matrix, tablefmt='gird'))
        if self.success():
            return True
        else:
            print("按w(向上)a(向左)s(向下)d(向右)合并方块，按q(退出)")

    # 转置函数
    def transpose(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for x in range(4):
            for y in range(4):
                new_matrix[x][y] = self.matrix[y][x]
        return new_matrix

    # 对转置后函数进行反转
    def reverse(self):
        for i in range(4):
            self.matrix[i].reverse()

    # 判断游戏是否结束
    def failure(self):
        """
        :return: 布尔 当前游戏是否结束
        """
        if len(self.find0()) > 0:
            return False
        else:
            for i in range(4):
                for j in range(3):
                    if self.matrix[i][j] == self.matrix[i][j + 1]:
                        return False
                    elif i < 3 and self.matrix[i][j] == self.matrix[i + 1][j]:
                        return False
        return True

    # 控制列表每行数字左移，先移除列表中的所有0，放入一个新列表中,得到原有列表
    def lift_move(self):
        new_matrix = []  # 用于存储处理后的所有行
        for row in self.matrix:
            # 收集不为0的元素
            no_0 = [y for y in row if y != 0]
            # 计算需要多少个0来填充
            yes_0 = [0] * (4 - len(no_0))
            new_row = no_0 + yes_0
            new_matrix.append(new_row)
        return new_matrix

    # 比较与前者是否相同,合并,加分
    def add_left(self):
        self.matrix = self.lift_move()
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.grade += self.matrix[i][j]
                    self.matrix[i][j + 1] = 0
        self.matrix = self.lift_move()

    # 判断游戏是否成功
    def success(self):
        for i in self.matrix:
            for j in i:
                # 为方便测试，在此设置当合成数字出现16时，游戏成功并结束，如有需要，可以更改
                if j == 16:
                    return True
        return False

    # 控制键盘输入，四个方向位移
    def kooking(self, char1):
        if char1 == 'w':
            self.matrix = self.transpose()
            self.add_left()
            self.matrix = self.transpose()
        elif char1 == 'a':
            self.add_left()
        elif char1 == 's':
            self.matrix = self.transpose()
            self.reverse()
            self.add_left()
            self.reverse()
            self.matrix = self.transpose()
        elif char1 == 'd':
            self.reverse()
            self.add_left()
            self.reverse()

    # 等待输入控制命令
    def wait(self):
        if self.debug:
            char = input("")
        else:
            char = msvcrt.getch().decode('utf-8', errors='ignore')
            time.sleep(0.2)
        # 判断输入char是什么
        if char == 'q':
            sys.exit('游戏结束')
        else:
            self.kooking(char)

    def run(self):
        while True:
            self.new_brick()
            self.print_inter()
            if self.success():
                print('恭喜你，游戏成功')
                sys.exit('游戏结束')
            if self.failure():
                print("已经无法继续游戏了。\n是否重新开始(点击y重新开始）")
                if self.debug:
                    char = input("")
                else:
                    char = msvcrt.getch().decode('utf-8', errors='ignore')
                if char.lower() == 'y':
                    self.__init__()
                else:
                    exit()
            else:
                self.wait()


if __name__ == "__main__":
    Run2048().run()
