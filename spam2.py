
import pyautogui
import pyperclip
import random
import time
import os

os.system('cls')
print("Tool Spam 2.0 By Văn Quai ")
msg = input("Nhập nội dung cần spam: ").split(" || ")
n = int(input("Nhập số lần Spam: "))
m = float(input("Nhập thời gian delay: "))

print("Chuẩn bị")
# Đếm ngược 5 giây
for i in range(5, 0, -1):
    print(i, end="...", flush=True)
    time.sleep(1)
print("Bắt đầu")

# SPAM và in số dòng và số thứ tự trên mỗi tin nhắn
line_count = 0
for i in range(n):
    # Tạo số thứ tự và dòng chữ tương ứng
    message_with_number = f"{i+1}. {random.choice(msg)}"
    pyperclip.copy(message_with_number)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(m)  # Delay
    
    lines = pyperclip.paste().split('\n')
    line_count += len(lines)
    print("Số dòng tin nhắn", i+1, ": ", len(lines))

# In tổng số dòng đã spam
print("Tổng số dòng đã spam: ", line_count)