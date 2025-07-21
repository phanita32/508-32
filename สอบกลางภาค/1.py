hour = int(input("ป้อนจำนวนชั่วโมง: "))
minute = int(input("ป้อนจำนวนนาที: "))

if hour < 0 or minute < 0:
    print("โปรดใส่ข้อมูลที่ไม่ติดลบ")
else:
    
    if minute > 0:
        hour += 1

    hour -= 1
    
    if hour < 0:
        hour = 0

    free = hour * 30

    print("ค่าจอดรถคือ", fee, "บาท")