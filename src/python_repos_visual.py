import requests
import plotly.express as px

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

# 전체 결과 를 처리
response_dict = r.json()
print(f"Complete result : {not response_dict['incomplete_results']}")

# 저장소 정보를 처리
repo_dicts = response_dict['items']
# repo_names, stars, hover_texts = [], [], []
repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    # repo_names.append(repo_dict['name'])
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a heref='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    # print('repo_link : '+repo_link)
    stars.append(repo_dict['stargazers_count'])

    # make tooltip text`
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 시각화
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, 
             hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
# fig = px.bar(x=repo_names, y=stars)
fig.show()
