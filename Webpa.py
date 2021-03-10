import webbrowser
import requests


url = 'http://www.grandtech.info'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得网页成功")
else:
    print("取得内容失败")

print(htmlfile.text)