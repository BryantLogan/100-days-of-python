from bs4 import BeautifulSoup
import requests

# with open("Day 45 - Web Scraping/website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title) # prints <title>Angela's Personal Site</title>
# print(soup.title.name) #prints title
# print(soup.title.string) #prints Angela's Personal Site

# print(soup.prettify()) #prints HTML with indents

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.string)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)

# ---

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(class_="titleline")

article_texts = []
article_links = []
article_scores = []

for heading in articles:
    link = heading.find(name="a").get("href")
    article_links.append(link)
    text = heading.find(name="a").getText()
    article_texts.append(text)

# scores = soup.find_all(class_="score")
# for score in scores:
#     article_score = score.getText().split(" ")[0]
#     article_scores.append(article_score)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index], article_links[largest_index], largest_number)
# print(article_texts)
# print(article_links)
# print(article_upvotes)