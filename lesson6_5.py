#自訂funtion
def play():
    import random
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print("=======猜數字遊戲=======")
    while True:    
        key = int(input(f"猜數字的範圍{min}~{max}:"))
        count += 1
        if key >= min and key <= max:
            if(key == target):
                print(f"賓果!猜對了, 答案是:{key}")
                print(f"您總共猜了{count}次")
                break
            elif(key<target):
                print("太小")
                print(f"您已經猜了{count}次")
                min=key+1
                
            elif(key>target):
                print("太大")
                print(f"您已經猜了{count}次")
                max=key-1
            
        else:
            print("超出範圍")
        
while True:
    play()
    again = input("您還要繼續遊戲嗎?(y or n):")
    if again == 'n':
        break
    else:
        continue

print("遊戲結束")