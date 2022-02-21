import requests
import json

def run(title='通知',content='内容'):
        payload = json.dumps({"ref": "main","inputs":{
            'subject':title,"content":content,"user":"630077372@qq.com"
            }})
        header = {'Authorization': 'token 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',
                  "Accept": "application/vnd.github.v3+json"}
        response_decoded_json = requests.post(
            f'https://api.github.com/repos/XXXShaunPan/bili_fans_new/actions/workflows/email.yml/dispatches?access_token=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',
            data=payload, headers=header)
        print(response_decoded_json.text)
