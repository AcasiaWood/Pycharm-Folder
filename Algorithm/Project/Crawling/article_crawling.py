from bs4 import BeautifulSoup
import urllib.request
import re

file = 'text.txt'  # text file to store news article content

url = 'article_text'  # article website address

def get_text(browser):  # crawling article
    source = urllib.request.urlopen(browser)
    soup = BeautifulSoup(source, 'lxml', from_encoding='utf-8')
    text = ''
    for data in soup.find_all('div', id='articleBodyContents'):  # copy and use the id of the div item from the Naver article HTML content.
        text = text + str(data.find_all(text=True))  # news article content crawl
    return text

def clean_text():
    text = get_text(url)
    # the re.sub code converts certain characters in the article content to spaces.
    text = re.sub('[a-zA-Z]', '', text)  # the codes [a-z] and [A-Z] refer to all characters between a and z, and all characters between A and Z, respectively.
    text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', text)  # [special characters] Code means special characters.
    return text

def main():
    # save the news article content in the text file you specified first.
    text_file = open(file, 'w')
    text = clean_text()
    text_file.write(text)
    text_file.close()

if __name__ == '__main__':  # run the code using the main function.
    main()
