unconfirmed_users = ['alice', 'brian', 'candace', 'ben', 'mike']
confirmed_users = []
while True:
    name = input("输入参会人的名字：")
    if name.lower() == 'all':
        break
    found = False
    for user in unconfirmed_users:
        if user.lower() == name.lower():
            unconfirmed_users.remove(user)
            confirmed_users.append(user)
            found = True
            break       
    if not found:
        print("名单中没有此人或已确认过。")
print("\n确认参会：", confirmed_users)
print("没有确认参会：", unconfirmed_users)