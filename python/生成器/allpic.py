import re,os.path,requests
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
response = requests.get('https://www.vmgirls.com/sitemap.shtml',headers=headers)
html = response.text
urls = re.findall('<a href="(.*?)" title=".*?" target=".*?">',html)
for url in urls:
    response1 = requests.get(url,headers=headers)
    html1 = response1.text
    dir_name = re.findall('<h1 class=".*?">(.*?)</h1>',html1)[-1]
    urls1 = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html1)
    if not os.path.exists('d:/'+dir_name):
        os.mkdir('d:/'+dir_name)
    for url1 in urls1:
        response2 = requests.get(url1,headers=headers)
        pic_name = os.path.basename(url1)
        # print(url1)
        with open('d:/'+dir_name+'/'+pic_name,'wb') as f:
            f.write(response2.content)