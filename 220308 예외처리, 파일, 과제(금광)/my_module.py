import random
def get_random_RPS():
    rps = ["가위","바위","보"]
    r = random.randint(0,3)
    return rps[r]
def is_win():
    user = input("가위, 바위, 보를 선택하세요. :")
    while user != "0": 
        com = get_random_RPS()
        print(f"컴퓨터 : {com}, 당신 : {user}")
        if com == user:
            print("비겼습니다.")
        if (user == "가위" and com =="바위") or (user =="바위" and com =="보") or(user =="보" and com =="가위"):
            print("졌습니다.")
        else:
            print("이겼습니다.")
        user = input("가위, 바위, 보를 선택하세요. :")
        
