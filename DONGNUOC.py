#DONGNUOC.py
# đọc dữ liệu từ file DONGNUOC.INP
with open("DONGNUOC.INP", "r") as f:
    N = int(f.read().strip())
min_steps = float("inf")
# Duyệt số lần đóng nước bằng cốc 5 từ lớn đến nhỏ
for i in range(N // 5, -1, -1):
    remainder = N - 5 * a 
    if remainder % 3 == 0:
        b = remainder // 3 
        steps = a+b
        if steps < min_steps:
            min_steps = steps

# Ghi kết quả ra file DONGNUOC.OUT
with open("DONGNUOC.OUT", "w") as f:
    if min_steps == float("inf"):
        f.write("-l/n")
    else:
        f.write(str(min_steps)+ "\n")                
