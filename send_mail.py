import requests
import json, os

token=os.environ["GH_TOKEN"]

def run(title='通知',content='内容'):
        payload = json.dumps({"ref": "main","inputs":{
            'subject':title,"content":content,"user":"630077372@qq.com"
            }})
        header = {'Authorization': f'token {token}',
                  "Accept": "application/vnd.github.v3+json"}
        response_decoded_json = requests.post(
            f'https://api.github.com/repos/XXXShaunPan/bili_fans_new/actions/workflows/email.yml/dispatches?access_token={token}',
            data=payload, headers=header)
        print(response_decoded_json.text)
