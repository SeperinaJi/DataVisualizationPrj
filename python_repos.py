import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

response_dict = r.json()
print(response_dict.keys())

repo_dicts = response_dict['items']
print('Total Repositories: ', response_dict['total_count'])

print('\nSelected information about each repositories:')
for repo_dict in repo_dicts:
    print('\nName: ', repo_dict['name'])
    print('Owner: ', repo_dict['owner']['login'])
    print('Stars: ', repo_dict['stargazers_count'])
    print('Repositories: ', repo_dict['html_url'])
    print('Description: ', repo_dict['description'])

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    #stars.append(repo_dict['stargazers_count'])
    description = repo_dict['description']
    if not description:
        description = 'Not provided'
    plot_dict = {
                'value': repo_dict['stargazers_count'],
                'label': description,
                'xlink': repo_dict['html_url'],
                }
    plot_dicts.append(plot_dict)

print(plot_dicts)

my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_reposw.svg')


