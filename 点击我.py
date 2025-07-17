import tkinter as tk
from tkinter import Toplevel, Label

def show_custom_popup():
    # 创建一个新的顶层窗口
    popup = Toplevel(root)
    popup.title("自定义页面")
    popup.geometry("300x200")  # 设置窗口大小
    
    # 在新窗口中添加一个标签作为示例内容
    label = Label(popup, text="这是的专属页面\n欢迎来到这里！", font=("Arial", 14))
    label.pack(pady=20)  # 使用pack布局管理器放置标签
    
    # 可以添加更多控件，如按钮、输入框等

# 主窗口设置
root = tk.Tk()
root.title("主界面")
root.geometry("400x300")

# 创建一个按钮，当点击时触发show_custom_popup函数
button = tk.Button(root, text="点击我", command=show_custom_popup)
button.pack(expand=True)

# 运行应用程序
root.mainloop()