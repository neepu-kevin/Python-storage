stocks = {
    "1": ["601398", "工商", 5.51],
    "2": ["000001", "平安", 8.94],
    "3": ["601939", "建设", 6.89],
    "4": ["601328", "交通", 5.61]
}

while True:
    no = input("请输入股票编号(1-4): ")
    
    if no in stocks:
        info = stocks[no]
        print("代码:", info[0], "名称:", info[1], "买入价:", info[2])
    else:
        print("无查询结果")
        break