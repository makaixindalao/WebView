import pythoncom
import pyHook
import win32api


def on_keyboard_event(event):
    # 检查是否按下了CTRL和ALT键以及字母K键
    if event.Ascii == 11 and event.Alt and event.Control:
        print("CTRL + ALT + K 键被按下！")
        # 执行您的操作

    # 返回True以指示键盘事件已经处理
    return True


# 创建一个钩子管理器
manager = pyHook.HookManager()

# 注册键盘事件的回调函数
manager.KeyDown = on_keyboard_event

# 设置键盘钩子
manager.HookKeyboard()

# 让Python保持运行状态
pythoncom.PumpMessages()
