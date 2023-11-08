import requests
from bs4 import BeautifulSoup

import requests
from selenium import webdriver



driver = webdriver.Chrome()
url = 'https://math25.aparsclassroom.com/Math25/Cycle-1/Paper-1/Chapter-7'
driver.get(url)
driver.add_cookie({
    '_ga': 'GA1.1.52809324.1691312809',
    'g_state': '{"i_p":1691320423005,"i_l":1}',
    'sign': 'M3Y3MmF1bmdhdW5nb28=',
    'uid': '6fBl3dQDHmdnCAgbS5KypulhZM62',
    'fpestid': 'DAfhPFnlHTadM5o9YQv0vbEAPQj9Zd93JXqAaHGHfDsvRskmTJSZIWEh3vvDn9HQZyCwVQ',
    '_cc_id': '8261becee7d2d86e985314cc03c06bf2',
    '_ga_YPR10DM6R6': 'GS1.1.1692774774.1.1.1692776043.0.0.0',
    '_ga_2PGS95QWE3': 'GS1.1.1693027159.1.1.1693027192.0.0.0',
    'ajs_user_id': 'XGtqAKFDspg0KKzE4QKYFhRJbzT2',
    'ajs_anonymous_id': '33984ee8-d72e-45a0-a33a-65e3cf2be2b8',
    '_fbp': 'fb.1.1699422478624.357971698',
    '_clck': 'grtgvx|2|fgj|0|1313',
    'ip': '103.197.153.59',
    '_ga_7R4CMSFEBN': 'GS1.1.1699422478.20.0.1699422480.0.0.0',
    '_ga_X9C9RQ709R': 'GS1.1.1699422440.66.1.1699422654.0.0.0',
    'returnURL': 'https://aparsclassroom.com/shop/chem25/Cycle-1/',
    '_ga_P18HXDWK2Y': 'GS1.1.1699422479.22.1.1699422951.0.0.0',
    '_ga_F7G6MJYRTN': 'GS1.1.1699423026.54.1.1699423162.0.0.0',
    '_ga_E4F0M76F4H': 'GS1.1.1699427152.47.1.1699427859.0.0.0',
    '_clsk': 'bp1rm1|1699436018845|1|1|o.clarity.ms/collect',
    '_ga_Q3216FEVST': 'GS1.1.1699436014.101.1.1699436076.0.0.0',
})
html = driver.page_source


print(html)
