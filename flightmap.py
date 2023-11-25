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
userin = df[(df['city1'] == 'Cleveland')]
userin2 = userin[(userin['city2'] == 'Denver')]
userin3 = userin2[(userin2['quarter'] == 1)]
print(userin3)




#!!!!! PROBLEM AREA !!!!!!


fpaths = userin3[['city 1 longitude','city 2 longitude','city 1 latitude','city 2 latitude', 'fare']]
#fpaths.columns = ['city 1 longitude','city 2 longitude']
#MAP
fpaths.head()
print('!!!!!!!!!')
print(fpaths)
fig = go.Figure()

flight_paths = []
for i in range(len(fpaths)):
    fig.add_trace(
        go.Scattergeo(
            locationmode = 'USA-states',
            lon = [fpaths['city 1 longitude'][i], fpaths['city 2 longitude'][i]],
            lat = [fpaths['city 1 latitude'][i], fpaths['city 2 latitude'][i]],
            mode = 'lines',
            line = dict(width = float(fpaths['fare'][i]) / 100.0,color = 'red'),
            opacity = 1.0,
        )
    )
print('did it get here !!!!!!!!!!!')










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