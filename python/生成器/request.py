import re,os.path,requests
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
response = requests.get('https://www.vmgirls.com/12985.html',headers=headers)
html = response.text
dir_name = re.findall('<h1 class=".*?">(.*?)</h1>',html)[-1]
print(dir_name)
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?" ',html)
if not os.path.exists('d:/'+dir_name):
    os.mkdir('d:/'+dir_name)
for url in urls:
    pic_name = os.path.basename(url)
    response = requests.get(url,headers=headers)
    with open('d:/'+dir_name+'/'+pic_name,'wb') as  f:
        f.write(response.content)