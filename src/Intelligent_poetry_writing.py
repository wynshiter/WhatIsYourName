# encoding:utf-8
import requests

# 百度智能写诗文档： https://ai.baidu.com/ai-doc/NLP/ak53wc3o3
# 清华大学 九歌：https://github.com/thunlp-aipoet

access_key = 'oFUAMvoGLKI2hYaXhVz9fxHI'
Secret_Key = 'bIdWDeeVwVSzGUAN4HxGKhiRb3PSLbM3'


# 认证机制 https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjhhu
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+access_key+'&client_secret='+Secret_Key
print(host)
response = requests.get(host)
if response:
    print(response.json())
else:
    print(response.content)