from operator import itemgetter

import requests
import plotly.express as px

# api 호출하고 응답 확인
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"status code: {r.status_code}")

# 각 글의 정보를 처리
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:5]:
    # 글을 순회 하면서 api 호출
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus code: {r.status_code}")
    response_dict = r.json()

    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        print(f"KeyError for submission id {submission_id}")
        continue
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# process data
article_links, comment_counts, hover_texts = [], [], []

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
    title = submission_dict['title'][:30]
    discussion_link = submission_dict['hn_link']
    article_link = f"<a href='{discussion_link}'>{title}</a>"
    commment_count = submission_dict['comments']

    # 시각화에 필요한 데이터 준비
    article_links.append(article_link)
    comment_counts.append(commment_count)
    hover_texts.append(submission_dict['title'])

title = "Top 5 Hacker News Articles"
labels = {'x': 'Articles', 'y': 'Comment Counts'}
fig = px.bar(x=article_links, y=comment_counts, hover_name=hover_texts, title=title, labels=labels)
fig.update_layout(title_font_size=24, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()