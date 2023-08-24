# Work in progress
import ctypes
import win32con
import win32gui

GWL_STYLE = -16
WS_VISIBLE = 0x10000000
SWP_HIDEWINDOW = 0x0080

def get_window_long(hwnd, index):
    return ctypes.windll.user32.GetWindowLongW(hwnd, index)

def set_window_long(hwnd, index, new_long):
    return ctypes.windll.user32.SetWindowLongW(hwnd, index, new_long)

def set_window_pos(hwnd, hwnd_insert_after, x, y, cx, cy, flags):
    return ctypes.windll.user32.SetWindowPos(hwnd, hwnd_insert_after, x, y, cx, cy, flags)

def main():
    handle = win32gui.GetForegroundWindow()  # Get the current foreground window handle
    style = get_window_long(handle, GWL_STYLE)
    set_window_long(handle, GWL_STYLE, style & ~WS_VISIBLE)
    set_window_pos(handle, 0, 0, 0, 0, 0, SWP_HIDEWINDOW)

    print("lol")
    input()

if __name__ == "__main__":
    main()
