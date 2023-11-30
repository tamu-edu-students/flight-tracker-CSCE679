import pandas as pd
from matplotlib import pyplot as plt
import os

def generate_linegraph(city1, city2):
    df = pd.read_csv("dataset/Historical Data_3.csv",encoding='cp1252')
    df['year_quarter'] = df['Year'].map(str) +" "+ df['quarter'].map(str) +"Q"

    df_example = df[(df['city1']==city1) & (df['city2']==city2)]

    df_example[['Year','quarter','city1','city2','fare','fare_lg','fare_low', 'year_quarter']]

    df_sorted = df_example.sort_values(['year_quarter'])

    plt.plot(df_sorted['year_quarter'], df_sorted['fare'], label="Fare_average", color='black',linewidth = 2)

    plt.xlabel('Year Quarter')
    plt.ylabel('Fare')
    plt.xticks(rotation=45)
    plt.legend()
    dir_path = "./images_generated"
    # plt.show()
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print('File count:', count)
    save_path = str(dir_path+str("/temp"+str(count+1)))
    plt.savefig(save_path)
    return save_path

