import requests
from bs4 import BeautifulSoup
import pyperclip

# URLを指定
url = 'https://finance.logmi.jp/378217'

# URLからHTMLを取得
response = requests.get(url)

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(response.text, 'html.parser')

# 'article-body'クラスの要素を抽出
article_body = soup.find(class_='article-body')

# PDFのリンクを除去
for pdf_link in article_body.find_all('a', href=True):
    if '.pdf' in pdf_link['href']:
        pdf_link.decompose()

# 抽出したテキストを取得
text = article_body.get_text()

# テキストを3000文字ごとに分割
chunks = [text[i:i+3000] for i in range(0, len(text), 3000)]

# 各チャンクをクリップボードにコピー
for i, chunk in enumerate(chunks, start=1):
    print(f'--- Chunk {i} ---')
    print(chunk)
    input('Press enter to copy this chunk to the clipboard.')
    pyperclip.copy(chunk)

