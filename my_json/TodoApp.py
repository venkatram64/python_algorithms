import json
import requests

def processTodos():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(response.text)
    mtodos = json.dumps(todos, indent=2)
    print(mtodos)


if __name__ == '__main__':
    processTodos()