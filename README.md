# Page Reader


This is a simple python module that extracts the information from webpage based on
the HTML5 tags.

- Python 3.6
- Beautifulsoup


## Installation

```bash
pip install git+https://github.com/invanatech/webpage-reader
```


## Usage

```python
from webpage_reader import analyse

result = analyse(url="https://github.com/invanatech/page-reader", )
print(result)

{
  'status':'success',
  'result':{
    'title':'GitHub - invanatech/webpage-reader: Reads a webpage and extracts the information out of it, based on the HTML5 tags/classes',
    'url':'https://github.com/invanatech/page-reader',
    'website':'https://github.com',
    'links':{
      'article_links':[
        {
          'url':'https://github.com/#page-reader',
          'title':''
        }
      ],
      'header_nav_links':[
        {
          'url':'https://github.com/',
          'title':''
        },
        {
          'url':'https://github.com/features',
          'title':'Features'
        },
        {
          'url':'https://github.com/business',
          'title':'Business'
        },
        {
          'url':'https://github.com/explore',
          'title':'Explore'
        },
        {
          'url':'https://github.com/marketplace',
          'title':'Marketplace'
        },
        {
          'url':'https://github.com/pricing',
          'title':'Pricing'
        }
      ],
      'footer_nav_links':[
        {
          'url':'https://github.com/site/terms',
          'title':'Terms'
        },
        {
          'url':'https://github.com/site/privacy',
          'title':'Privacy'
        },
        {
          'url':'https://help.github.com/articles/github-security/',
          'title':'Security'
        },
        {
          'url':'https://status.github.com/',
          'title':'Status'
        },
        {
          'url':'https://help.github.com',
          'title':'Help'
        },
        {
          'url':'https://github.com',
          'title':''
        },
        {
          'url':'https://github.com/contact',
          'title':'Contact GitHub'
        },
        {
          'url':'https://developer.github.com',
          'title':'API'
        },
        {
          'url':'https://training.github.com',
          'title':'Training'
        },
        {
          'url':'https://shop.github.com',
          'title':'Shop'
        },
        {
          'url':'https://blog.github.com',
          'title':'Blog'
        },
        {
          'url':'https://github.com/about',
          'title':'About'
        }
      ],
      'all_nav_links':[
        {
          'url':'https://github.com/features',
          'title':'Features'
        },
        {
          'url':'https://github.com/business',
          'title':'Business'
        },
        {
          'url':'https://github.com/explore',
          'title':'Explore'
        },
        {
          'url':'https://github.com/marketplace',
          'title':'Marketplace'
        },
        {
          'url':'https://github.com/pricing',
          'title':'Pricing'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader',
          'title':'Code'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/issues',
          'title':'Issues\n0'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/pulls',
          'title':'Pull requests\n0'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/projects',
          'title':'Projects\n      0'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/pulse',
          'title':'Insights'
        }
      ],
      'aside_nav_links':[

      ],
      'all_links':[
        {
          'url':'https://github.com/#start-of-content',
          'title':'Skip to content'
        },
        {
          'url':'https://github.com/',
          'title':''
        },
        {
          'url':'https://github.com/features',
          'title':'Features'
        },
        {
          'url':'https://github.com/business',
          'title':'Business'
        },
        {
          'url':'https://github.com/explore',
          'title':'Explore'
        },
        {
          'url':'https://github.com/marketplace',
          'title':'Marketplace'
        },
        {
          'url':'https://github.com/pricing',
          'title':'Pricing'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader',
          'title':'This repository'
        },
        {
          'url':'https://github.com/login?return_to=%2Finvanatech%2Fwebpage-reader',
          'title':'Sign in'
        },
        {
          'url':'https://github.com/join?source=header-repo',
          'title':'Sign up'
        },
        {
          'url':'https://github.com/login?return_to=%2Finvanatech%2Fwebpage-reader',
          'title':'Watch'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/watchers',
          'title':'1'
        },
        {
          'url':'https://github.com/login?return_to=%2Finvanatech%2Fwebpage-reader',
          'title':'Star'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/stargazers',
          'title':'0'
        },
        {
          'url':'https://github.com/login?return_to=%2Finvanatech%2Fwebpage-reader',
          'title':'Fork'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/network',
          'title':'0'
        },
        {
          'url':'https://github.com/invanatech',
          'title':'invanatech'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader',
          'title':'webpage-reader'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader',
          'title':'Code'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/issues',
          'title':'Issues\n0'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/pulls',
          'title':'Pull requests\n0'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/projects',
          'title':'Projects\n      0'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/pulse',
          'title':'Insights'
        },
        {
          'url':'https://github.com/join?source=prompt-code',
          'title':'Sign up'
        },
        {
          'url':'https://github.com/topics/html-parser',
          'title':'html-parser'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/commits/master',
          'title':'8\n              \n              commits'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/branches',
          'title':'1\n            \n            branch'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/releases',
          'title':'0\n            \n            releases'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/graphs/contributors',
          'title':'1\n    \n    contributor'
        },
        {
          'url':'https://help.github.com/articles/which-remote-url-should-i-use',
          'title':''
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/archive/master.zip',
          'title':'Download ZIP'
        },
        {
          'url':'https://desktop.github.com/',
          'title':'download GitHub Desktop'
        },
        {
          'url':'https://desktop.github.com/',
          'title':'download GitHub Desktop'
        },
        {
          'url':'https://developer.apple.com/xcode/',
          'title':'download Xcode'
        },
        {
          'url':'https://visualstudio.github.com/',
          'title':'download the GitHub extension for Visual Studio'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/find/master',
          'title':'Find file'
        },
        {
          'url':'https://github.com/#',
          'title':'Branches'
        },
        {
          'url':'https://github.com/#',
          'title':'Tags'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/tree/master',
          'title':'master'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/tree/f71e9cfd80ec574e7f59d3846c8c1e3b5c92477f',
          'title':'Permalink'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/tree/master/page_reader',
          'title':'page_reader'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/commit/f71e9cfd80ec574e7f59d3846c8c1e3b5c92477f',
          'title':'making url absolute fix'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/blob/master/README.md',
          'title':'README.md'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/commit/f557d1aee8f22beb2a887458554e741e3263f68b',
          'title':'selector fixes'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/blob/master/example.py',
          'title':'example.py'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/commit/663180bfbd5f79432445813007c156359db44726',
          'title':'selector fixes'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/blob/master/requirements.txt',
          'title':'requirements.txt'
        },
        {
          'url':'https://github.com/invanatech/webpage-reader/commit/14486917574bf9190940e4edc4ec6455a32abf31',
          'title':'first commit'
        },
        {
          'url':'https://github.com/#page-reader',
          'title':''
        },
        {
          'url':'https://github.com/site/terms',
          'title':'Terms'
        },
        {
          'url':'https://github.com/site/privacy',
          'title':'Privacy'
        },
        {
          'url':'https://help.github.com/articles/github-security/',
          'title':'Security'
        },
        {
          'url':'https://status.github.com/',
          'title':'Status'
        },
        {
          'url':'https://help.github.com',
          'title':'Help'
        },
        {
          'url':'https://github.com',
          'title':''
        },
        {
          'url':'https://github.com/contact',
          'title':'Contact GitHub'
        },
        {
          'url':'https://developer.github.com',
          'title':'API'
        },
        {
          'url':'https://training.github.com',
          'title':'Training'
        },
        {
          'url':'https://shop.github.com',
          'title':'Shop'
        },
        {
          'url':'https://blog.github.com',
          'title':'Blog'
        },
        {
          'url':'https://github.com/about',
          'title':'About'
        },
        {
          'url':'https://github.com/',
          'title':'Reload'
        },
        {
          'url':'https://github.com/',
          'title':'Reload'
        }
      ]
    }
  }
}
```