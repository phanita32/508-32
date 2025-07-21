numbers = []

while True:
    try:
        num = float(input("ป้อนจำนวนจริงบวก: "))
        if num <= 0:
            break
        numbers.append(num) 
    except:
        break 

if numbers:
    print("ค่าน้อยที่สุดคือ:", min(numbers))
else:
    print("ไม่มีจำนวนจริงบวกที่รับเข้ามา")