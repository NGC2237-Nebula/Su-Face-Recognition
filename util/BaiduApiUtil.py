# -*- coding: utf-8 -*-
import os
import json
import base64
import requests
from configparser import ConfigParser


def network_connect_judge():
    """
    联网判断
    :return: 是否联网
    """
    ret = os.system("ping baidu.com -n 1")
    return True if ret == 0 else False


def get_access_token():
    """
    获取访问令牌
    :return: 访问令牌
    """
    conf = ConfigParser()
    path = os.path.join(os.path.dirname(__file__))
    conf.read(path[:path.rindex('util')] + "conf\\setting.conf", encoding='gbk')

    API_KEY = conf.get('baidu_config', 'app_id')
    SECRET_KEY = conf.get('baidu_config', 'secret_key')

    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


def face_api_invoke(path):
    """
    人脸 API 调用
    :param path: 待检测的图片路径
    :return: 是否通过静默人脸识别
    """
    with open(path, 'rb') as f:
        img_data = f.read()
        base64_data = base64.b64encode(img_data)
        base64_str = base64_data.decode('utf-8')
    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceverify?access_token=" + get_access_token()
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps(([{
        "image": base64_str,
        "image_type": "BASE64"
    }]))
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)
    result = json.loads(response.text)
    if result["error_msg"] == "SUCCESS":
        frr_1e_4 = result["result"]["thresholds"]["frr_1e-4"]
        frr_1e_3 = result["result"]["thresholds"]["frr_1e-3"]
        frr_1e_2 = result["result"]["thresholds"]["frr_1e-2"]
        face_liveness = result["result"]["face_liveness"]

        if face_liveness >= frr_1e_2:
            return True
        elif frr_1e_3 <= face_liveness <= frr_1e_2:
            return True
        elif face_liveness <= frr_1e_4:
            return False
