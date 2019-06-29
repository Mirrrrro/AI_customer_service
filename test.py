import chat_robot

print("你好，我是聊天机器人，请输入任意内容进行聊天")
while True:
    question = input()
    if question == "退出":
        break
    print(chat_robot.get_robot_reply(question))