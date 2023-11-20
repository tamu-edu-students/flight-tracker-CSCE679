import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pandas import *
from plotly import *

#read file
df = pd.read_csv("Historical Data_With_Coordinates_Final_Version.csv", encoding = "ISO-8859-1")
df.head()

#color library
scl = ['rgb(213,62,79)', 'rgb(244,109,67)', 'rgb(253,174,97)', \
    'rgb(254,224,139)', 'rgb(255,255,191)', 'rgb(230,245,152)', \
    'rgb(171,221,164)', 'rgb(102,194,165)', 'rgb(50,136,189)'
]
n_colors = len(scl)

#New Data Frames filtered from user input
userin = df[(df['city1'] == 'Allentown, Pennsylvania')]
userin2 = userin[(userin['city2'] == 'Tampa, Florida')]
userin3 = userin2[(userin2['quarter'] == 1)]


#MAP
fig = go.Figure()


#flight lines
#var = float(userin3['fare']) / 100
#print(var)
opac = float(1.0)

lons = []
lats = []
import numpy as np
lons = np.empty(3 * len(userin3))
lons[::3] = userin3['city 1 longitude']
lons[1::3] = userin3['city 2 longitude']
lons[2::3] = None
lats = np.empty(3 * len(userin3))
lats[::3] = userin3['city 1 latitude']
lats[1::3] = userin3['city 2 latitude']
lats[2::3] = None

fig.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    lon = lons,
    lat = lats,
    #hoverinfo = 'text',
    #text = userin3['fare'],
    mode = 'lines',
    opacity = opac,
    line = dict(
        width = float(userin3['fare']) / 100,
        color = 'rgb(255, 0, 0)')
        
    )
)



#city one markers
fig.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    lon = userin3['city 1 longitude'],
    lat = userin3['city 1 latitude'],
    hoverinfo = 'text',
    text = userin2['city1'],
    mode = 'markers',
    marker = dict(
        size = 4,
        color = 'rgb(255, 0, 0)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))

#city two markers
fig.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    lon = userin3['city 2 longitude'],
    lat = userin3['city 2 latitude'],
    hoverinfo = 'text',
    text = userin2['city2'],
    mode = 'markers',
    marker = dict(
        size = 4,
        color = 'rgb(255, 0, 0)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))


print('here')
fig.update_layout(
    #title_text = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
    showlegend = False,
    geo = dict(
        scope = 'north america',
        projection_type = 'azimuthal equal area',
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
)

fig.show()