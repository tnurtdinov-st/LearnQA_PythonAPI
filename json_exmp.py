import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)

#покрасивее через цикл
for i in obj['messages']:
    if "second" in i['message']:
        print(i['message'])
    else:
        pass

#или совсем прямой вариант
print(obj['messages'][1]['message'])
