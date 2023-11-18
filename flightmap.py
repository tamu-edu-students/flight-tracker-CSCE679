import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pandas import *
from plotly import *

print('here')
df = pd.read_csv("Historical_Data_With_Coordinates.csv", encoding = "ISO-8859-1")
fare1 = pd.read_csv("Historical_Data_Final_Version.csv", encoding = "ISO-8859-1")
print(df)
df.head()
print('here1')

scl = ['rgb(213,62,79)', 'rgb(244,109,67)', 'rgb(253,174,97)', \
    'rgb(254,224,139)', 'rgb(255,255,191)', 'rgb(230,245,152)', \
    'rgb(171,221,164)', 'rgb(102,194,165)', 'rgb(50,136,189)'
]
n_colors = len(scl)

userin = df[(df['city 1'] == 'Austin, Texas')]
userin2 = userin[(userin['city 2'] == 'Cleveland')]
fare2 = fare1[(fare1['city1'])]



fig = go.Figure()

fig.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    lon = userin2['city 1 longitude'],
    lat = userin2['city 1 latitude'],
    hoverinfo = 'name',
    text = userin2['city 1'],
    mode = 'markers',
    marker = dict(
        size = 4,
        color = 'rgb(255, 0, 0)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))
fig.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    lon = userin2['city 2 longitude'],
    lat = userin2['city 2 latitdue'],
    hoverinfo = 'name',
    text = userin2['city 2'],
    mode = 'markers',
    marker = dict(
        size = 4,
        color = 'rgb(255, 0, 0)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))
flight_paths = []
print(len(userin2))
#for i in range(len(userin2)):
    #print('here')
    #print(i)
    fig.add_trace(
        go.Scattergeo(
            locationmode = 'USA-states',
            lon = [userin2['city 1 longitude'], userin2['city 2 longitude']],
            lat = [userin2['city 1 latitude'], userin2['city 2 latitdue']],
            mode = 'lines',
            line = dict(width = 1,color = scl[1]),
            #opacity = float(userin2['cnt'][i]) / float(userin2['cnt'].max()),
        )
    )

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