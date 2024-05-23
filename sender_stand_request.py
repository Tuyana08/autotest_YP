import requests

import configuration

import data


def create_order(body):
    req = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        json=body)
    return req


def get_order_info():
    params = data.params.copy()
    params["t"] = create_order(data.body).json()["track"]
    req = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO_PATH,
                       params=params)

    return req
