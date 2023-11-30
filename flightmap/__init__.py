import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pandas import *
from plotly import *
import numpy as np
import random
#read file
df = pd.read_csv("dataset/Historical Data_With_Coordinates_Final_Version.csv", encoding = "ISO-8859-1")
df.head()

#color library
scl = ['rgb(213,62,79)', 'rgb(244,109,67)', 'rgb(253,174,97)', \
    'rgb(254,224,139)', 'rgb(255,255,191)', 'rgb(230,245,152)', \
    'rgb(171,221,164)', 'rgb(102,194,165)', 'rgb(50,136,189)'
]
scl.reverse()
n_colors = len(scl)

#New Data Frames filtered from user input




# REPLACE THE CLEVELAND AND DENVER WITH WHATEVER THE USER PUTS IN
userin = df[(df['city1'] == 'Cleveland')]
userin2 = userin[(userin['city2'] == 'Denver')]

lat1 = userin2['city 1 latitude'].iloc[1]
lat2 = userin2['city 2 latitude'].iloc[1]
lon1 = userin2['city 1 longitude'].iloc[1]
lon2 = userin2['city 2 longitude'].iloc[1]
userin3 = userin2[(userin2['quarter'] == 1)]


print(userin3)




#!!!!!!!!!!!!!!!!

#THIS IS WHERE TO ADD THE DATAFRAME FROM THE API
#Replace userin3 with dataframe from api

# fpaths = userin3[['airline','fare','airport1','airport2','time'], ['airline','fare','airport1','airport2','time']]
# fpaths = fpaths.sort_values(by=['fare'])


def generate_map_html(processed_flight_data):    
    #!!!!!!!!!!!!!!!!
    #MAP
    fpaths = processed_flight_data
    fpaths.head()
    print('!!!!!!!!!')
    print(fpaths)
    print('!!!!fpaths length!!!!!')
    print(len(fpaths))
    fig = go.Figure()

    flight_paths = []
    for i in range(len(fpaths)):
        print('!!!!!!!!!')
        var = 10-(float(fpaths['fare'].iloc[i])/100)
        if fpaths['fare'].iloc[i] >= 1000:
            var = 10-(float(fpaths['fare'].iloc[i])/1000)

        clr = scl[i]
        if fpaths['fare'].iloc[i] == fpaths['fare'].min():
            var = 20
            clr = 'rgb(0,255,0)'
        if fpaths['fare'].iloc[i] == fpaths['fare'].max():
            clr = 'rgb(255,0,0)'
        if len(fpaths) == 1:
            clr = 'rgb(0,255,0)'
        
        fig.add_trace(
            go.Scattergeo(
                locationmode = 'USA-states',
                lat = [lat1+(i), lat2+(i)],
                lon = [lon1, lon2],
                hoverinfo = 'text',
                text = fpaths['fare'].iloc[i]+ ' , '  + fpaths['airlines'].iloc[i] + ' , '  + fpaths['city1'].iloc[i] + ' to ' + fpaths['city2'].iloc[i] + ', Time of flight:' + fpaths['time'].iloc[i],
                hoverlabel = dict(bgcolor=clr,font_color='black'),
                mode = 'lines',
                line = dict(width = var,color = clr),
                opacity = 1.0
            )
        )
    for i in range(len(fpaths)):
        clr = scl[i]
        if fpaths['fare'].iloc[i] == fpaths['fare'].min():
            clr = 'rgb(0,255,0)'
        if fpaths['fare'].iloc[i] == fpaths['fare'].max():
            clr = 'rgb(255,0,0)'
        if len(fpaths) == 1:
            clr = 'rgb(0,255,0)'
        fig.add_trace(
            go.Scattergeo(
                locationmode = 'USA-states',
                lat = [lat1+(i), lat2+(i)],
                lon = [lon1, lon2],
                hoverinfo = 'text',
                text = fpaths['fare'].iloc[i]+ ' , ' + fpaths['airlines'].iloc[i] + ' , '  + fpaths['city1'].iloc[i] + ' to ' + fpaths['city2'].iloc[i] + ', Time of flight:' + fpaths['time'].iloc[i],
                hoverlabel = dict(bgcolor=clr,font_color='black'),
                mode = 'markers',
                marker = dict(
                    size = 10,
                    line = dict(width = 10,color = clr),
                    opacity = 1.0 
                
            )
        ))
    print('did it get here !!!!!!!!!!!')

    #city one markers
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = userin2['city 1 longitude'],
        lat = userin2['city 1 latitude'],
        hoverinfo = 'text',
        text = userin2['city1'],
        mode = 'markers',
        marker = dict(
            size = 1,
            color = 'rgb(255, 0, 0)',
            line = dict(
                width = 3,
                color = 'rgba(68, 68, 68, 0)'
            )
        )))

    #city two markers
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = userin2['city 2 longitude'],
        lat = userin2['city 2 latitude'],
        hoverinfo = 'text',
        text = userin2['city2'],
        mode = 'markers',
        marker = dict(
            size = 1,
            color = 'rgb(255, 0, 0)',
            line = dict(
                width = 3,
                color = 'rgba(68, 68, 68, 0)'
            )
        )))


    print('here')
    fig.update_layout(

        showlegend = False,
        geo = dict(
            scope = 'north america',
            projection_type = 'azimuthal equal area',
            showland = True,
            landcolor = 'rgb(243, 243, 243)',
            countrycolor = 'rgb(204, 204, 204)',
        ),
    )
    dir_path = "./html_generated"
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print('File count:', count)
    html_path = str(dir_path+str("/html"+str(count+1)))
    fig.write_html(html_path)
    return html_path