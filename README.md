# Page Reader


Reads a webpage and extracts the information like SEO tags, headings,
urls based on HTML5 tags and standard styling frameworks

- Python 3.6
- Beautifulsoup


## Installation

```bash
pip install git+https://github.com/invanatech/webpage-reader#egg=webpage_reader
```


## Usage

```python

from webpage_reader import analyse, read_page

url="https://moz.com/blog/sustainable-link-building"
headers = {}
page_text = read_page(url=url, headers=headers)
result = analyse(page_text=page_text, url=url)
print(result)


{
  'status':'success',
  'result':{
    'title':'How to Increase Your Chances of Getting Links Over Time - Moz',
    'url':'https://moz.com/blog/sustainable-link-building',
    'website':'https://moz.com',
    'links':{
      'article_links':[
        {
          'url':'https://moz.com/community/users/143993',
          'title':''
        },
        ...
      ],
      'header_nav_links':[
        {
          'url':'https://moz.com',
          'title':''
        },
        ...
      ],
      'footer_nav_links':[
        {
          'url':'https://moz.com',
          'title':''
        },
       ...
      ],
      'all_nav_links':[
        {
          'url':'https://moz.com/products',
          'title':'Products'
        },
        ...
      ],
      'aside_nav_links':[
        {
          'url':'https://moz.com/blog/mobile-first-index-link-graph',
          'title':'How Mobile-First Indexing Disrupts the Link Graph'
        },
        ...
      ],
      'all_links':[
        {
          'url':'https://moz.com',
          'title':''
        },
        ...
      ]
    },
    'meta':{
      'twitter':{
        'account_id':'15651700',
        'title':'Sustainable Link Building: Increasing Your Chances of Getting Links - Whiteboard Friday',
        'description':"Link building campaigns shouldn't have a start-and-stop date—they should be ongoing, continuing to earn you links over time. Join our guest host Paddy Moogan as he shares strategies to achieve sustainable link building and milk your content efforts for all they're worth.",
        'card':'summary_large_image',
        'image':{
          'src':'https://d1avok0lzls2w.cloudfront.net/uploads/twitter_image/5acffa7092f837.61207865.jpg'
        },
        'creator':'@paddymoogan'
      },
      'fb':{
        'page_id':'8489236245',
        'admins':'22408537'
      },
      'og':{
        'image':'https://d1avok0lzls2w.cloudfront.net/uploads/og_image/5acffa719e8453.64724814.jpg',
        'title':'Sustainable Link Building: Increasing Your Chances of Getting Links - Whiteboard Friday',
        'description':"Link building campaigns shouldn't have a start-and-stop date—they should be ongoing, continuing to earn you links over time. Join our guest host Paddy Moogan as he shares strategies to achieve sustainable link building and milk your content efforts for all they're worth.",
        'type':'article',
        'site_name':'Moz',
        'url':'https://moz.com/blog/sustainable-link-building'
      }
    },
    'headings':{
      'h1':[

      ],
      'h2':[
        'Sustainable Link Building: Increasing Your Chances of Getting Links - Whiteboard&nbspFriday;',
        'Video Transcription',
        'Problems',
        'Solutions',
        'Comments                           16',
        'Log in to Moz'
      ],
      'h3':[
        'I. Content-driven link building is risky.',
        'II. A great content idea may not be a great content idea that gets links.',
        "III. It's a big investment of time and budget.",
        'IV. Think of link building as campaign-led: it starts & stops.',
        "I. Don't tie content to specific dates or events",
        'II. Look for datasets which give you multiple angles for outreach',
        'III. Build up a bank of link-worthy content',
        'IV. Learn what content formats work for you',
        'Popular posts like this',
        'Get fresh SEO data, insights, and tracking',
        'Get fresh SEO data, insights, and tracking',
        "Don't have an account?",
        'Get the Moz Top\xa010'
      ],
      'h4':[

      ],
      'h5':[

      ],
      'h6':[

      ],
      'h7':[

      ]
    }
  }
}
```