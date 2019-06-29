'''
文件描述：基于微信公众号实现AI客服
作者：Mirrrrro
邮箱：13006185248@163.com

'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import urllib.request
import urllib.parse


def get_robot_reply(question):
    '''
    函数功能：对于特定问题进行特定回复，对于其他非特定问题进行智能回复
    
    参数描述：
    question 聊天内容或问题

    返回值：str，回复内容
    '''

    if "你叫什么名字" in question:
        answer = "我是poiu"
    elif "我还有多少钱" in question:
        answer = "88888888$"
    elif "你多少岁" in question:
        answer = "3"
    elif "你是GG还是MM" in question:
        answer = "你猜呢"
    else:
        try:
        # 调用NLP接口实现智能回复
            params = urllib.parse.urlencode({'msg': question}).encode()  # 接口参数需要进行URL编码 
            req = urllib.request.Request("http://api.itmojun.com/chat_robot", params, method = "POST")  # 创建请求对象
            answer = urllib.request.urlopen(req).read().decode()  # 调用接口(即向目标服务器发出HTTP请求，并获取服务器的响应数据)
            if answer == "":
                answer = "AI机器人看不懂你在说什么。。。"
        except Exception as e:
            answer = "AI机器人出现故障！(原因: %s)" % e

    return answer

if __name__ == "__main__":
    while True:
        question = input("\n我说：")
        answer = get_robot_reply(question)
        print("\n小魔仙说：%s" % answer)