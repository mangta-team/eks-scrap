import urllib.request
import string

# 표준 문서의 총 페이지 입력.
PAGE = 69

a = [a for a in range(0, PAGE)]
b = []

alpha = list(string.ascii_lowercase)

# 그냥 페이지 별로 파일 이름 부여하는 거임.
for i in range(1, 10):
    for j in range(0, len(alpha):
        b.append('{}{}'.format('z' * i, alpha[j]))

# 링크
# url = 'https://e-ks.kr/streamdocs/v4/documents/72059198425690698/renderings/{}?zoom=133&jpegQuality=o&renderAnnots=false&increasePrint=false'
url = 'https://e-ks.kr/streamdocs/v4/documents/72059216890408236/renderings/{}?zoom=133&jpegQuality=o&renderAnnots=false&increasePrint=false'

for idx, i in enumerate(a):
    with urllib.request.urlopen(url.format(i)) as f:
        html = f.read()
        files = open('{}.png'.format(b[idx]), 'wb')
        html = bytearray(html)
        html[0] = 0x89
        files.write(html)
        files.close()
