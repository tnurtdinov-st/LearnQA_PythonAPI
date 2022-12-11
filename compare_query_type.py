import requests

#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("1: " + response.text)

#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("2: " + response.text)

#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print("3: " + response.text)


#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
# И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением
# параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
params = ("GET", "POST", "PUT", "DELETE")
for i in params:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": i})
    print("4GET " + i+ ": " + response.text)
    if "GET" not in i:
        if "success" in response.text:
            print("warning!!! incorrect response for GET and " + i)


for i in params:
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
    print("4POST " + i+ ": " + response.text)
    if "POST" not in i:
        if "success" in response.text:
            print("warning!!! incorrect response for POST and " + i)

for i in params:
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
    print("4PUT " + i+ ": " + response.text)
    if "PUT" not in i:
        if "success" in response.text:
            print("warning!!! incorrect response for PUT and " + i)

for i in params:
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
    print("4DELETE " + i+ ": " + response.text)
    if "DELETE" not in i:
        if "success" in response.text:
            print("warning!!! incorrect response for DELETE and " + i)