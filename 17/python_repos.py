import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()
# print("Total repositoried:",response_dict['total_count'])

#探索有关仓库的信息,所有仓库
repo_dicts = response_dict["items"]
# print("Repositories returned:",len(repo_dicts))

#研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

#遍历所有仓库基本信息
# print("\nSelected information about first repository:")
# for repo_dict in repo_dicts:
#     print('\nName:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Description:', repo_dict['description'])

#处理结果
# print(response_dict.keys())


names,stars =[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化
my_style =LS('#336699',base_style = LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('python_repos.svg')