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

url="https://github.com/invanatech/webpage-reader"
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
        {
          'url':'https://moz.com/community/users/143993',
          'title':'Paddy Moogan'
        },
        {
          'url':'https://moz.com/blog/category/link-building',
          'title':'Link Building'
        },
        {
          'url':'https://moz.com/blog/category/whiteboard-friday',
          'title':'Whiteboard Friday'
        },
        {
          'url':'https://moz.com/blog/category/content',
          'title':'Content'
        },
        {
          'url':'http://d2v4zi8pl64nxt.cloudfront.net/sustainable-link-building/5acf9e2fe6ee71.49569665.jpg',
          'title':''
        },
        {
          'url':'http://www.linkbuildingbook.com/',
          'title':'may have read my link building book'
        },
        {
          'url':'http://www.speechpad.com/page/video-transcription/',
          'title':'Video transcription'
        },
        {
          'url':'http://www.speechpad.com/',
          'title':'Speechpad.com'
        },
        {
          'url':'http://www.aira.net',
          'title':'Aira'
        },
        {
          'url':'http://www.linkbuildingbook.com',
          'title':'The Link Building Book'
        },
        {
          'url':'http://twitter.com/paddymoogan',
          'title':'Twitter'
        },
        {
          'url':'https://plus.google.com/104334957300160196129?rel=author',
          'title':'Google+'
        },
        {
          'url':'http://www.paddymoogan.com/blog',
          'title':'personal blog'
        },
        {
          'url':'https://moz.com/blog/mobile-first-index-link-graph',
          'title':'How Mobile-First Indexing Disrupts the Link Graph'
        },
        {
          'url':'https://moz.com/blog/clickbait-linkbait-viral-content-seo-campaigns',
          'title':'Where Clickbait, Linkbait, and Viral Content Fit in SEO Campaigns - Whiteboard Friday'
        },
        {
          'url':'https://moz.com/blog/links-from-low-ranking-domains',
          'title':"Why It Can Pay to Get Links from Domains that Don't Always Rank Highly - Whiteboard Friday"
        }
      ],
      'header_nav_links':[
        {
          'url':'https://moz.com',
          'title':''
        },
        {
          'url':'https://moz.com/products',
          'title':'Products'
        },
        {
          'url':'https://moz.com/blog',
          'title':'Blog'
        },
        {
          'url':'https://moz.com/about',
          'title':'About'
        },
        {
          'url':'https://moz.com/pages/search_results',
          'title':''
        },
        {
          'url':'https://moz.com/learn/seo',
          'title':'Learn SEO'
        },
        {
          'url':'https://moz.com/products/pro',
          'title':'Moz Pro'
        },
        {
          'url':'https://moz.com/products/local',
          'title':'Moz Local'
        },
        {
          'url':'https://moz.com/tools',
          'title':'Free SEO Tools'
        },
        {
          'url':'https://moz.com/login',
          'title':'Log in'
        },
        {
          'url':'https://moz.com/community/users/143993',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/143993',
          'title':'Paddy Moogan'
        },
        {
          'url':'https://moz.com/blog/category/link-building',
          'title':'Link Building'
        },
        {
          'url':'https://moz.com/blog/category/whiteboard-friday',
          'title':'Whiteboard Friday'
        },
        {
          'url':'https://moz.com/blog/category/content',
          'title':'Content'
        },
        {
          'url':'https://moz.com/community/users/4002371',
          'title':'Zack Reboletti'
        },
        {
          'url':'https://moz.com/community/users/11395477',
          'title':'Nikola  Roza'
        },
        {
          'url':'https://moz.com/community/users/11239555',
          'title':'Jonathan Diaz'
        },
        {
          'url':'https://moz.com/community/users/547397',
          'title':'Aaron Henry'
        },
        {
          'url':'https://moz.com/community/users/52887',
          'title':'Donna Duncan'
        },
        {
          'url':'https://moz.com/community/users/11417783',
          'title':'royjones_q2'
        },
        {
          'url':'https://moz.com/community/users/11417909',
          'title':'efemichael'
        },
        {
          'url':'https://moz.com/community/users/332674',
          'title':'Joe Robison'
        },
        {
          'url':'https://moz.com/community/users/11395477',
          'title':'Nikola  Roza'
        },
        {
          'url':'https://moz.com/community/users/11385293',
          'title':'WIlliamPolson'
        },
        {
          'url':'https://moz.com/community/users/3852691',
          'title':'Stereo90 Letras'
        },
        {
          'url':'https://moz.com/community/users/4771850',
          'title':'Tayeeb Khan'
        },
        {
          'url':'https://moz.com/community/users/10661537',
          'title':'Toni_Amarres'
        },
        {
          'url':'https://moz.com/community/users/11277241',
          'title':'Catie-B'
        },
        {
          'url':'https://moz.com/community/users/11163827',
          'title':'Zohaib Khan'
        },
        {
          'url':'https://moz.com/community/users/361809',
          'title':'Steven Brown'
        }
      ],
      'footer_nav_links':[
        {
          'url':'https://moz.com',
          'title':''
        },
        {
          'url':'https://moz.com/about/contact',
          'title':'Contact'
        },
        {
          'url':'https://moz.com/products',
          'title':'Products'
        },
        {
          'url':'https://moz.com/products/api',
          'title':'API'
        },
        {
          'url':'https://moz.com/terms-privacy',
          'title':'Terms & Privacy'
        },
        {
          'url':'https://moz.com/about/jobs',
          'title':'Jobs'
        },
        {
          'url':'https://moz.com/help',
          'title':'Help'
        },
        {
          'url':'https://moz.com/explorer',
          'title':'Keyword Research'
        },
        {
          'url':'https://moz.com/products/pro/site-crawl',
          'title':'SEO Audit & Crawl'
        },
        {
          'url':'https://moz.com/researchtools/ose/',
          'title':'Backlink Research'
        },
        {
          'url':'https://moz.com/products/pro/rank-tracking',
          'title':'Rank Tracking'
        },
        {
          'url':'https://moz.com/products/pro/seo-toolbar',
          'title':'SEO Toolbar'
        },
        {
          'url':'https://moz.com/local/search',
          'title':'Business Listings Audit'
        },
        {
          'url':'https://moz.com/products/local/citation-cleanup-whitepaper',
          'title':'Citation Cleanup'
        },
        {
          'url':'https://moz.com/local-search-ranking-factors',
          'title':'Local Ranking Factors'
        },
        {
          'url':'https://moz.com/products/local/enterprise',
          'title':'Local For Enterprise'
        },
        {
          'url':'https://moz.com/blog',
          'title':'Moz Blog'
        },
        {
          'url':'https://moz.com/beginners-guide-to-seo',
          'title':'Beginner’s Guide To SEO'
        },
        {
          'url':'https://moz.com/community/q',
          'title':'Community Q&A'
        },
        {
          'url':'https://moz.com/training',
          'title':'Workshops & Training'
        },
        {
          'url':'https://moz.com/rand/recommended-list-seo-consultants/',
          'title':'Recommended SEO Companies'
        }
      ],
      'all_nav_links':[
        {
          'url':'https://moz.com/products',
          'title':'Products'
        },
        {
          'url':'https://moz.com/blog',
          'title':'Blog'
        },
        {
          'url':'https://moz.com/about',
          'title':'About'
        }
      ],
      'aside_nav_links':[
        {
          'url':'https://moz.com/blog/mobile-first-index-link-graph',
          'title':'How Mobile-First Indexing Disrupts the Link Graph'
        },
        {
          'url':'https://moz.com/blog/clickbait-linkbait-viral-content-seo-campaigns',
          'title':'Where Clickbait, Linkbait, and Viral Content Fit in SEO Campaigns - Whiteboard Friday'
        },
        {
          'url':'https://moz.com/blog/links-from-low-ranking-domains',
          'title':"Why It Can Pay to Get Links from Domains that Don't Always Rank Highly - Whiteboard Friday"
        },
        {
          'url':'https://moz.com/products/pro',
          'title':'Learn More About Moz Pro'
        },
        {
          'url':'https://moz.com/products/pro',
          'title':'Learn More About Moz Pro'
        }
      ],
      'all_links':[
        {
          'url':'https://moz.com',
          'title':''
        },
        {
          'url':'https://moz.com/products',
          'title':'Products'
        },
        {
          'url':'https://moz.com/blog',
          'title':'Blog'
        },
        {
          'url':'https://moz.com/about',
          'title':'About'
        },
        {
          'url':'https://moz.com/pages/search_results',
          'title':''
        },
        {
          'url':'https://moz.com/learn/seo',
          'title':'Learn SEO'
        },
        {
          'url':'https://moz.com/products/pro',
          'title':'Moz Pro'
        },
        {
          'url':'https://moz.com/products/local',
          'title':'Moz Local'
        },
        {
          'url':'https://moz.com/tools',
          'title':'Free SEO Tools'
        },
        {
          'url':'https://moz.com/login',
          'title':'Log in'
        },
        {
          'url':'https://moz.com/community/users/143993',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/143993',
          'title':'Paddy Moogan'
        },
        {
          'url':'https://moz.com/blog/category/link-building',
          'title':'Link Building'
        },
        {
          'url':'https://moz.com/blog/category/whiteboard-friday',
          'title':'Whiteboard Friday'
        },
        {
          'url':'https://moz.com/blog/category/content',
          'title':'Content'
        },
        {
          'url':'http://d2v4zi8pl64nxt.cloudfront.net/sustainable-link-building/5acf9e2fe6ee71.49569665.jpg',
          'title':''
        },
        {
          'url':'http://www.linkbuildingbook.com/',
          'title':'may have read my link building book'
        },
        {
          'url':'http://www.speechpad.com/page/video-transcription/',
          'title':'Video transcription'
        },
        {
          'url':'http://www.speechpad.com/',
          'title':'Speechpad.com'
        },
        {
          'url':'http://www.aira.net',
          'title':'Aira'
        },
        {
          'url':'http://www.linkbuildingbook.com',
          'title':'The Link Building Book'
        },
        {
          'url':'http://twitter.com/paddymoogan',
          'title':'Twitter'
        },
        {
          'url':'https://plus.google.com/104334957300160196129?rel=author',
          'title':'Google+'
        },
        {
          'url':'http://www.paddymoogan.com/blog',
          'title':'personal blog'
        },
        {
          'url':'https://moz.com/blog/mobile-first-index-link-graph',
          'title':'How Mobile-First Indexing Disrupts the Link Graph'
        },
        {
          'url':'https://moz.com/blog/clickbait-linkbait-viral-content-seo-campaigns',
          'title':'Where Clickbait, Linkbait, and Viral Content Fit in SEO Campaigns - Whiteboard Friday'
        },
        {
          'url':'https://moz.com/blog/links-from-low-ranking-domains',
          'title':"Why It Can Pay to Get Links from Domains that Don't Always Rank Highly - Whiteboard Friday"
        },
        {
          'url':'https://moz.com/products/pro',
          'title':'Learn More About Moz Pro'
        },
        {
          'url':'https://moz.com/community/blog-disclaimer',
          'title':'community etiquette'
        },
        {
          'url':'https://moz.com/community/users/4002371',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/4002371',
          'title':'Zack Reboletti'
        },
        {
          'url':'https://moz.com/community/users/11395477',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/11395477',
          'title':'Nikola  Roza'
        },
        {
          'url':'https://moz.com/community/users/11239555',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/11239555',
          'title':'Jonathan Diaz'
        },
        {
          'url':'https://moz.com/community/users/547397',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/547397',
          'title':'Aaron Henry'
        },
        {
          'url':'https://moz.com/community/users/52887',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/52887',
          'title':'Donna Duncan'
        },
        {
          'url':'https://moz.com/community/users/11417783',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/11417783',
          'title':'royjones_q2'
        },
        {
          'url':'https://moz.com/community/users/11417909',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/11417909',
          'title':'efemichael'
        },
        {
          'url':'https://moz.com/community/users/332674',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/332674',
          'title':'Joe Robison'
        },
        {
          'url':'https://moz.com/community/users/11395477',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/11395477',
          'title':'Nikola  Roza'
        },
        {
          'url':'https://moz.com/community/users/11385293',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/11385293',
          'title':'WIlliamPolson'
        },
        {
          'url':'https://moz.com/community/users/3852691',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/3852691',
          'title':'Stereo90 Letras'
        },
        {
          'url':'https://moz.com/community/users/4771850',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/4771850',
          'title':'Tayeeb Khan'
        },
        {
          'url':'https://moz.com/community/users/10661537',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/10661537',
          'title':'Toni_Amarres'
        },
        {
          'url':'https://moz.com/community/users/11277241',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/11277241',
          'title':'Catie-B'
        },
        {
          'url':'https://moz.com/community/users/11163827',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/11163827',
          'title':'Zohaib Khan'
        },
        {
          'url':'https://moz.com/community/users/361809',
          'title':''
        },
        {
          'url':'https://moz.com/community/users/361809',
          'title':'Steven Brown'
        },
        {
          'url':'https://moz.com/blog/sustainable-link-building/stats',
          'title':'Post Analytics'
        },
        {
          'url':'https://moz.com/products/pro',
          'title':'Learn More About Moz Pro'
        },
        {
          'url':'https://moz.com/lost-password',
          'title':'Forgot Password'
        },
        {
          'url':'https://moz.com/community/join?source=blog&redirect=/blog/sustainable-link-building',
          'title':'Sign Up'
        },
        {
          'url':'https://moz.com',
          'title':''
        },
        {
          'url':'https://moz.com/about/contact',
          'title':'Contact'
        },
        {
          'url':'https://moz.com/products',
          'title':'Products'
        },
        {
          'url':'https://moz.com/products/api',
          'title':'API'
        },
        {
          'url':'https://moz.com/terms-privacy',
          'title':'Terms & Privacy'
        },
        {
          'url':'https://moz.com/about/jobs',
          'title':'Jobs'
        },
        {
          'url':'https://moz.com/help',
          'title':'Help'
        },
        {
          'url':'https://moz.com/explorer',
          'title':'Keyword Research'
        },
        {
          'url':'https://moz.com/products/pro/site-crawl',
          'title':'SEO Audit & Crawl'
        },
        {
          'url':'https://moz.com/researchtools/ose/',
          'title':'Backlink Research'
        },
        {
          'url':'https://moz.com/products/pro/rank-tracking',
          'title':'Rank Tracking'
        },
        {
          'url':'https://moz.com/products/pro/seo-toolbar',
          'title':'SEO Toolbar'
        },
        {
          'url':'https://moz.com/local/search',
          'title':'Business Listings Audit'
        },
        {
          'url':'https://moz.com/products/local/citation-cleanup-whitepaper',
          'title':'Citation Cleanup'
        },
        {
          'url':'https://moz.com/local-search-ranking-factors',
          'title':'Local Ranking Factors'
        },
        {
          'url':'https://moz.com/products/local/enterprise',
          'title':'Local For Enterprise'
        },
        {
          'url':'https://moz.com/blog',
          'title':'Moz Blog'
        },
        {
          'url':'https://moz.com/beginners-guide-to-seo',
          'title':'Beginner’s Guide To SEO'
        },
        {
          'url':'https://moz.com/community/q',
          'title':'Community Q&A'
        },
        {
          'url':'https://moz.com/training',
          'title':'Workshops & Training'
        },
        {
          'url':'https://moz.com/rand/recommended-list-seo-consultants/',
          'title':'Recommended SEO Companies'
        }
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