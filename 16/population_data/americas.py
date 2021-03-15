import pygal
from pygal_maps_world.maps import World

wm = World()
wm.title = 'North,Central,and South American'
wm.add('North American',['ca','mx','us'])
wm.add('Central American',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South American',['ar','bo','br','ci','co','ec','gf','gy','pe','py','sr','uy','ve'])

wm.render_to_file('American.svg')
