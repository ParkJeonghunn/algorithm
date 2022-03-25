def changes():
    price = int(input())  # 물건값
    change = 1000 - price # 잔돈
    count500 = change // 500
    change500 = change % 500
    count100 = change500 // 100
    change100 = change500 % 100
    count50 = change100 // 50
    change50 = change100 % 50
    count10 = change50 // 10
    print(count500, count100, count50, count10)
    return count500, count100, count50, count10
changes()
