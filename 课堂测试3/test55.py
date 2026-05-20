def check():
    while True:
        shuru = input("请输入数字（输入no退出）：")
        
        if shuru.lower() == "no":
            break
            
        if shuru.isdigit():
            shuzi = int(shuru)
            if shuzi % 2 == 0:
                print("结果：偶数")
            else:
                print("结果：奇数")
        
        elif shuru.isalpha():
            print("异常提示：你输入的是字符/字母，请重新输入数字！")
        else:
            print("异常提示：你输入的是特殊符号或混合内容，请重新输入数字！")

check()