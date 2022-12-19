import requests


response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

red_count = int(len(response.history))
print("Число редиректов: " + str(red_count))

final_response = response.history[red_count - 1]
print("Конечный URL: " + final_response.url)


