import json
import requests
import json
import jsonpath
import requests


def api_response(url: str, method: str, body: any):
    if method == 'POST':
        response = requests.post(url, str(body).replace("'", '"'))
        print(url, body, response)
        return response

    if method == 'GET':
        response = requests.get(url)
        return response

    if method == 'PUT':
        response = requests.put(url, str(body).replace("'", '"'))
        return response

    if method == 'PATCH':
        response = requests.patch(url, str(body).replace("'", '"'))
        return response

    if method == 'DELETE':
        response = requests.delete(url)
        return response


def order_api():
    url = "https://oyvm2iv4xj.execute-api.ap-south-1.amazonaws.com/v1/orin/api/orders/"
    file = open('./data.json')
    json_req = json.loads(file.read())
    data = json_req['--data-raw']
    body = data.json_req['orders']
    return url, data, body
