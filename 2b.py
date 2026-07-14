name = input("คุณชื่ออะไร")
age = int(input("อายุเท่าไหร่"))
height = float(input("ส่วนสูงเท่าไหร่"))
power = int(input("พละกำลังเท่าไหร่ 1-10"))
cash = int(input("เงินติดตัวเท่าไหร่"))
if (power >= 5 and cash >= 1000) :
    print(name + " ผ่าน ประธาน")
else:
    print(name + "ไม่ผ่าน")
