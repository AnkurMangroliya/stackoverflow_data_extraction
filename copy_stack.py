import requests
from bs4 import BeautifulSoup
import pandas as pd




inpu = int(input("Enter page number that you want to extract :"))
stackoverflow=[]

for hj in range(inpu):
    url = f'https://stackoverflow.com/users?page={hj}&tab=reputation&filter=week'

    # url='https://stackoverflow.com/users'
    base_url='https://stackoverflow.com'

    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')

    s = soup.find_all('div',class_="user-details")



    for i in s:
        u = i.find('a')
        location = i.find('span').text
        reputation = i.find('span',class_="reputation-score").text
        sd = i.find('div',class_="fs-caption")
        username = u.text
        U = u.get('href')

        userlink = base_url+U

        
        w = requests.get(userlink)
        sou = BeautifulSoup(w.content,'html.parser')
        

        reputation_num = sou.find('div',class_="fs-body3 fc-dark").text.strip()

        active_form = sou.find('div',class_="d-flex gs4 gsx ai-center").text.strip()
        
        answer_lates = sou.find('a',class_="answer-hyperlink d-table tl-fixed w100 m0 ow-break-word").text

        article_lates = sou.find('a',class_="question-hyperlink d-table tl-fixed w100 m0 ow-break-word js-gps-track").text.strip()
        
        top_meta_pos = sou.find('a',class_="question-hyperlink d-table tl-fixed w100 m0 ow-break-word js-gps-track").text.strip()

        # collectives = sou.find('div',class_="s-card bar-md p0").text.strip()

        # communities = sou.find('div',class_="s-card bar-md").text.strip()
        
        # try:
        #     articlecount_link = userlink+'?tab=articles'
        #     articlecount_w = requests.get(articlecount_link)
        #     articlecount_soup = BeautifulSoup(articlecount_w.content,'html.parser')

        #     article_count = articlecount_soup.find('div',class_="d-flex fd-column").text.strip()
        # except:
        #     article_count='None'

    
        stackoverflow_data={
            'Name':username.strip(),
            'url':userlink,
            'Location':location,
            'Summary Reputation':reputation_num,
            'Active From':active_form,
            'Answers':answer_lates,
            'Top Meta Posts':top_meta_pos,
            # 'Articles Count':article_count,
            # 'Communities':communities.strip()
        }
        stackoverflow.append(stackoverflow_data)


df = pd.DataFrame(stackoverflow)

df.to_csv('stack_overflow_data.csv')





# https://stackoverflow.com/users/115145/commonsware?tab=articles

# https://stackoverflow.com/users/115145/commonsware
