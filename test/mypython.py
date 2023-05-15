import json

json_data = '{"destination":"U270261b658b25b75161552c150a94035","events":[{"type":"message","message":{"type":"text","id":"18108195351535","text":"Test"},"webhookEventId":"01GZVE39D64EWP67ET4P8YSJ6K","deliveryContext":{"isRedelivery":false},"timestamp":1683474195371,"source":{"type":"user","userId":"U48f90a8bc210739c762ab7e25ec5e662"},"replyToken":"ae00916ddbd14617b937ac63d20d41f7","mode":"active"}]}'

data = json.loads(json_data) # 將 JSON 字符串轉換為 Python 對象
print('')
print(data)
print('')

# if 'type' in data.values():
#     print('type 存在')
# else:
#     print('type 不存在')

# print(data['events'][0])


print(data.values()) #沒有顯示的兩個值是keys
print('')
print(list(data.values())[0]) #這是第一個key值的value key=destination value=U270261b658b25b75161552c150a94035
print('')
print(list(data.values())[1][0]['message']) #這是第二個key值的value且取出message的值 key=events value=[]整個陣列內容，因為有指定message，所以print出message的值
print('')
print(list(data.values())[1][0]['webhookEventId'])
print('')


print(list(data.values())[1][0]['message']['text']) #取得更裡面的value OK!