profit = float(input("请输入今年的利润："))
    
if profit <= 100000:
    reward = profit * 0.1
elif 100000 < profit <= 200000:
    reward = 100000 * 0.1 + (profit - 100000) * 0.075
elif 200000 < profit <= 400000:
    reward = 100000 * 0.1 + 100000 * 0.075 + (profit - 200000) * 0.05
elif 400000 < profit <= 600000:
    reward = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (profit - 400000) * 0.03
elif 600000 < profit <= 1000000:
    reward = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (profit - 600000) * 0.015
else:
    reward = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (profit - 1000000) * 0.01
    
print("应该发放的奖金总数是：", reward, sep='')