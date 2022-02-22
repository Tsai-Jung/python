import win32api,win32con

x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
print(x)

y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
print(y)
