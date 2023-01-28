import PyPDF2
from pprint import pprint
import requests

pages_catch = dict()
split = dict()
result = dict()
with open("/tmp/vac.pdf", "rb") as pdf_file:
    read_pdf = PyPDF2.PdfReader(pdf_file)
    number_of_pages = len(read_pdf.pages)
    for x in range(number_of_pages):
        page = read_pdf.pages[x]
        page_content = page.extract_text()
        if page_content.find('Заоч') != -1 and page_content.find('18.03.01') != -1:
            print(x)
            pages_catch[x] = page_content
        # print(page_content)
for x in pages_catch:
    split[x] = pages_catch[x].split('\n')

hello = f"Привет, сейчас я попробую прочитать файл {open('/home/doroshenko/rhtu_vac/filename','r').readlines()[0]}"

# i=0
res = 0
for si in split:
    for x in range(len(split[si])):
        print(split[si][x])
        if split[si][x].find('18.03.01') != -1:
            result[res] = list()
            i = 0
            while i != 6:
                result[res].append(split[si][x + i])
                i += 1
            res += 1
# pprint(result)
rim_num = ["I", "II", "III", "IV", "V"]
chat_id = "*******"
TOKEN = "*********"

for x in range(len(result)):
    message = f"Курс {rim_num[x]}, количество мест: {result[x][-1][-1]}"
    url_req = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    reqs = requests.get(url_req)
    print(reqs)
