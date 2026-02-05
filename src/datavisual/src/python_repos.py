import requests

# API를 호출하고 응답을 확인
url = 'https://api.github.com/search/repositories' # URL 메인
url += '?q=language:python+sort:stars+stars:>10000' # 쿼리 문자열

headers = {"Accept": "application/vnd.github.v3+json"} # 버전3 api를 명시적으로 지정, 결과는 json으로 반환 하라는 해더 정의
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

# 응답 객체를 dictionary로 변환
response_dict = r.json()
# print(response_dict.keys()) # 응답 객체의 키 출력
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# 저장소 정보를 탐색
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# 첫번째 저장소를 분석
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)
# print("\nSelected information about first repoository:")
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository URL: {repo_dict['html_url']}")
# print(f"Created at: {repo_dict['created_at']}") 
# print(f"Updated at: {repo_dict['updated_at']}")
# print(f"Description: {repo_dict['description']}")

print("\nSelected information about each repoository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository URL: {repo_dict['html_url']}")
    print(f"Created at: {repo_dict['created_at']}") 
    print(f"Updated at: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
    print("-" * 80)                                                                                    