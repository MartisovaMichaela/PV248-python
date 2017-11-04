#!/usr/bin/env python3

import json

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
import bokeh.palettes
from math import pi
from pprint import pprint as pp

data = open("election.json", "r")
dictlist = json.loads(data.read())

# part 1
num_parties = len(dictlist)
p1 = figure(x_range = (-1, num_parties))
shares = []
for d in dictlist:
    shares.append(d['share'])
p1.vbar(x = list(range(len(shares))),
       top = shares, width = 0.7, fill_color="#b3de69")
#show(p1)

# part 2
small_shares = []
for s in shares:
    if s < 1:
        small_shares.append(s)
p2 = figure(x_range = (-1, len(small_shares)))
p2.vbar(x = list(range(len(small_shares))),
       top = small_shares, width = 0.7, fill_color="#b3de69")
#show(p2)

# part 3
# TODO: pie chart is weird
percents = []
for i in shares:
    if i >= 5:
        percents.append(i/100)
starts = [p*2*pi for p in percents[:-1]]
ends = [p*2*pi for p in percents[1:]]

# a color for each pie piece
#colors = ["red", "green", "blue", "orange", "yellow"]
colors = bokeh.palettes.viridis(len(percents)-1)

p = figure(x_range=(-1,1), y_range=(-1,1))

p.wedge(x=0, y=0, radius=1, start_angle=starts, end_angle=ends, color=colors)

# display/save everythin
show(p)

def simple_bar_plot():
    src = ColumnDataSource(
        data = {'color': ["purple", "black"]}
    )
    p = figure( x_range = (-1,10) )
    p.vbar( x = [0, 1], top = [25, 50], width = 0.7, source = src)
    show( p )

def simple_pie_chart():
    p = figure( x_range = (-10,10) )
    p.wedge( x = 0, y = 0, radius = 5, start_angle = [ 1/4 * pi, 6/4 * pi ],
             end_angle = [ 6/4 * pi, 1/4 * pi ],
    color = ["purple", "darkblue"] )
    show( p )

def simple_with_legend():
    src = ColumnDataSource( data = {
        'start': [ 1/4 * pi, 6/4 * pi ],
        'end': [ 6/4 * pi, 1/4 * pi ],
        'color': [ "purple", "darkblue" ],
        'label': [ "mlem", "purr" ] } )

    p = figure()
    p.wedge( x = 0, y = 0, radius = 5, start_angle = 'start', end_angle = 'end',
            color = 'color', legend = 'label', source = src )
    show(p)

#simple_bar_plot()
#simple_pie_chart()
#simple_with_legend()
