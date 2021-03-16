import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

my_style = LS('#336699',base_style = LCS)
chart = pygal.Bar(style = my_style,x_label_rotarion = 45,show_legend =False)

chart.titie = 'Python Projects'
chart.x_labels =['https','django','flask']

plot_dicts = [
    {'value':16101,'label':'Description of httpie'},
    {'value':15028,'label':'Description of Diango'},
    {'value':12323,'label':'Description of flask'},
]
chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')

