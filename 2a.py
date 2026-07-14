quantity = int(input("จำนวนปืนที่รับมาขาย : "))
cost = int(input("ต้นทุนปืนที่รับมาขาย : "))
sell = int(input("ราคาที่นำไปขายต่อ : "))
team_members = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน : "))

#ส่วนที่คำนวณออก output
sumstart = (quantity * cost) #ต้นทุน
sumsell = (sell * quantity) #เงินที่ได้จากกาารขาย
profit = (sumsell - sumstart) #กำไร
InBoss = (profit * 0.20) #เข้าบอส
net_profit = (profit - InBoss) #กำไรสุทธิ

#เงื่อนไขคนที่ไปทำงาน
if team_members > 0:
    team_members = net_profit / team_members
else:
    team_members = 0
print(f"ต้นทุนทั้งหมด : {sumstart} บาท")
print(f"รายรับทั้งหมด : {sumsell} บาท")
print(f"กำไรสุทธิ : {profit} บาท")
print(f"จำนวนเงินที่หักไปให้บอส : {InBoss} บาท")
print(f"จำนวนเงินที่ลูกน้องแต่ละคนได้ : {team_members} บาท")