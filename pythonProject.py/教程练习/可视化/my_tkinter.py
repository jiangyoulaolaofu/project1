import tkinter as tk


def dianji(x):
    global fuhaoanxia, shu, fuhao, result_num
    if x == '=':
        jisuan()
    elif x == 'AC':
        result_num.set('')
        shu = ''
        fuhao = ''
        fuhaoanxia = False
    elif x == '⬅':
        result_num.set(result_num.get()[:-1] if result_num.get() else '')
    elif x in ["+", "-", "*", "/"]:
        if shu is None and not result_num.get() == '':
            jisuan()
        fuhaoanxia = True
        fuhao = x
    else:
        if fuhaoanxia:
            shu = result_num.get()
            result_num.set("")
            fuhaoanxia = False
        result_num.set(result_num.get() + x)


def jisuan():
    global fuhaoanxia, shu, fuhao, result_num
    try:
        current_result = result_num.get()  # 获取当前显示的结果
        if current_result == '':  # 如果当前结果是空字符串，直接返回
            result_num.set("Error: No input")
            return
        # 将当前结果显示的字符串转换为浮点数
        current_result = float(current_result)
        if fuhao == '+':
            result_num.set(float(shu) + current_result)
        elif fuhao == '-':
            result_num.set(float(shu) - current_result)
        elif fuhao == '*':
            result_num.set(float(shu) * current_result)
        elif fuhao == '/':
            if current_result == 0:
                result_num.set("Error: Division by zero")
            else:
                result_num.set(float(shu) / current_result)
        elif fuhao == '%':
            if shu == 0:
                result_num.set("Error: Division by zero")
            else:
                result_num.set(shu * 0.01)  # 注意这里 shu 应该已经是一个浮点数
        # 格式化结果，保留两位小数，并去掉末尾的零
        result_num.set(format(float(result_num.get()), '.2f').rstrip('0').rstrip('.'))

        shu = float(result_num.get())
        fuhao = ''
        fuhaoanxia = False

    except ValueError:
        result_num.set("Error: Invalid input")


shu = ''
fuhao = ''
fuhaoanxia = ''
root = tk.Tk()
root.title('我的计算器')
root.attributes('-alpha', 0.9)
font = ('宋体', 20)
font_16 = ('宋体', 16)
root.geometry('295x280+100+100')
root.config(bg='black')

result_num = tk.StringVar()
result_num.set(" ")
operation = ''

tk.Label(root,
         textvariable=result_num,
         height=2,
         width=20,
         justify=tk.LEFT,
         anchor=tk.SE,
         font=font
         ).grid(row=0, column=0, columnspan=4)
buttons = [
    ("AC", False, 1, 0, False),
    ("⬅", False, 1, 1, False),
    ("%", False, 1, 2, False),
    ("*", False, 1, 3, False),
    ("7", True, 2, 0, False),
    ("8", True, 2, 1, False),
    ("9", True, 2, 2, False),
    ("/", False, 2, 3, False),
    ("4", True, 3, 0, False),
    ("5", True, 3, 1, False),
    ("6", True, 3, 2, False),
    ("-", False, 3, 3, False),
    ("1", True, 4, 0, False),
    ("2", True, 4, 1, False),
    ("3", True, 4, 2, False),
    ("+", False, 4, 3, False),
    ("0", True, 5, 0, True),
    (".", False, 5, 2, False),
    ("=", False, 5, 3, False),
]
for text, color, row, column, iszore in buttons:
    if iszore:
        button = tk.Button(master=root, text=text, width=12, font=font_16, relief=tk.FLAT, bg='orange')
        button.grid(row=row, column=column, padx=4, pady=4, columnspan=2)
        if text == '=':
            button.config(command=jisuan)
        else:
            pass
    elif color:
        button = tk.Button(master=root, text=text, width=5, font=font_16, relief=tk.FLAT, bg='orange')
        button.grid(row=row, column=column, padx=4, pady=4)
    else:
        button = tk.Button(master=root, text=text, width=5, font=font_16, relief=tk.FLAT, bg='grey')
        button.grid(row=row, column=column, padx=4, pady=4)
    button.config(command=lambda txt=text: dianji(txt))

root.mainloop()
