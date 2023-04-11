import requests
from bs4 import BeautifulSoup
from docx import Document
import re


url_chapters_name = "https://www.royalroad.com/fiction/21220/mother-of-learning"
page = requests.get(url_chapters_name)
soup = BeautifulSoup(page.content, "html.parser")
chaptersName = []
names = soup.find('tbody').text
clean_text = re.sub(r'\s+\d+\s*years\s*ago\s*', ' ', names.strip())
enhanced_names = re.sub(r"\d+", "\n\\g<0>", clean_text)
# for name in names:
print(enhanced_names)
# chapterName = names[1].find('tr', {"class", "chapter-row"})
# print(len(names))

url_story = "https://www.royalroad.com/fiction/21220/mother-of-learning/chapter/301778/1-good-morning-brother"
page = requests.get(url_story)
soup = BeautifulSoup(page.content, "html.parser")
chapter_content = soup.find(
    "div", {'class': 'chapter-inner chapter-content'}).text.strip()
button = soup.find(
    "div", {'class': 'col-xs-6 col-md-4 col-md-offset-4 col-lg-3 col-lg-offset-6'}).text.strip()
# doc = Document()
# length = len(button)
# print(button)
# doc.add_paragraph(chapter_content)
# doc.save('story.docx')
# print(chapter_content)
