from webpage_reader import analyse, read_page

url = "https://moz.com/blog/sustainable-link-building"
headers = {}
page_text = read_page(url=url, headers=headers)
result = analyse(page_text=page_text, url=url)
print(result)

