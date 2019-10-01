# python 3 

# collection of all plotting functions for data visualzation in python 




# Package imports
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import folium
from folium import plugins


# Display plots inline and change default figure size
%matplotlib inline
matplotlib.rcParams['figure.figsize'] = (10.0, 8.0)


# -----------------------------

"""
credit 
https://github.com/dennybritz/nn-from-scratch/blob/master/nn-from-scratch.ipynb
Plot the decision boundary
example 
plot_decision_boundary(lambda x: clf.predict(x))
plt.title("Logistic Regression")

# Helper function to plot a decision boundary.
# If you don't fully understand this function don't worry, it just generates the contour plot below.

"""

def plot_decision_boundary(pred_func):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole gid
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)



# -----------------------------



def plot_heatmap_lon_lat(df,map_center):
    #map_center = [50.87650,4.39723]
    print (map_center)
    heatmap = folium.Map(location=map_center, 
                         tiles='https://api.tiles.mapbox.com/v4/mapbox.light/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiZ29nb3ZhbmFwcCIsImEiOiJjaWg3MTk0ZjAwZmI5dXVraTF5aDNudTd0In0.mcuRTlI-EWoMm0IponVnVA',
                         attr='Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
                         zoom_start=11)

    # plz modify lon / lat columns here in cases for various dataset 
    heatmap_locations_list = df[['start_lat', 'start_lon']].dropna().values.tolist()
    heatmap.add_children(plugins.HeatMap(heatmap_locations_list, radius=20, blur=30))
    display(heatmap)


# -----------------------------


def plot_polygon_map(geo_json_data):
    # credit 
    # https://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/Colormaps.ipynb
    # in case you can import your own geojson data 
    # geo_json_data = json.load(open('proposal_zone.json'))
    m = folium.Map([50.85,4.35], tiles='cartodbpositron', zoom_start=12)
    # can modify map center above 
    folium.GeoJson(
    geo_json_data,
    style_function=lambda feature: {
        'color': 'black',
        'weight': 2,
        'dashArray': '5, 5'}
    ).add_to(m)
    return m



# -----------------------------

def preprocss_polygon_point_map(df):
    df_ = df[['lat','lon']].dropna().astype(float)
    df_list_ = df_.values.tolist()
    return df_list_ 


def plot_polygon_map_with_point(geo_json_data,point_list):
    # credit 
    # https://georgetsilva.github.io/posts/mapping-points-with-folium/
    # https://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/Colormaps.ipynb
    m = folium.Map([50.85,4.35], tiles='cartodbpositron', zoom_start=12)

    folium.GeoJson(
        geo_json_data,
        style_function=lambda feature: {
            
            'color': 'black',
            'weight': 2,
            'dashArray': '5, 5'
        }
    ).add_to(m)

    # get your points (lon & lat ) data as form here 
    # point_list = preprocss_polygon_point_map(df)
    for point in range(0, len(point_list)):
        folium.Marker(point_list[point]).add_to(m)

    return m



def plot_polygon_map_with_parameter_popup(geo_json_data,point_list):

    m = folium.Map([50.85,4.35], tiles='cartodbpositron', zoom_start=12)
    # plz modify the code here let it can loop over all zones within geojson and plot them and their parameters 
    for k in range(0,len(geo_json_data['features'])):
        data = geo_json_data['features'][k]
        x = folium.GeoJson(data=data)
        """
        in case you wanna remove special icon in address that make pop up still work 
        i.e.  d'Albanie -> dAlbanie
        zone_name = geo_json_data['features'][k]['properties']['name'].replace("'", "")
        x.add_child(folium.Popup('{}'.format(zone_name)))
        """
        x.add_child(folium.Popup('zone id  : {}'.format(geo_json_data['features'][k]['id'])))
        x.add_to(m)

    return m 



# -----------------------------



"""
credit 

http://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/Plugins.ipynb
https://www.kaggle.com/daveianhickey/how-to-folium-for-maps-heatmaps-time-analysis
https://github.com/python-visualization/folium/issues/441

"""

def plot_dynamic_heatmap_lon_lat(df):

    m = folium.Map(
        location=[35.68159659061569, 139.76451516151428],
        zoom_start=16
    )

    # Lon, Lat order.
    """
    to fix here 

    lines_ = [{'coordinates': json.loads(json.dumps(df_[df_.booking_start_day == k][['start_lat','start_lon']].values.tolist())),
          'dates': json.loads(json.dumps(df_[df_.booking_start_day == k][['booking_start_date']].values.tolist())),
          'color': 'red' } for k in set(df_.booking_start_day) 
        ]
    """

    lines = [
        {
            'coordinates': [
                [139.76451516151428, 35.68159659061569],
                [139.75964426994324, 35.682590062684206],
            ],
            'dates': [
                '2017-06-02T00:00:00',
                '2017-06-02T00:10:00'
            ],
            'color': 'red'
        },
        {
            'coordinates': [
                [139.75964426994324, 35.682590062684206],
                [139.7575843334198, 35.679505030038506],
            ],
            'dates': [
                '2017-06-02T00:10:00',
                '2017-06-02T00:20:00'
            ],
            'color': 'blue'
        },
        {
            'coordinates': [
                [139.7575843334198, 35.679505030038506],
                [139.76337790489197, 35.678040905014065],
            ],
            'dates': [
                '2017-06-02T00:20:00',
                '2017-06-02T00:30:00'
            ],
            'color': 'green',
            'weight': 15,
        },
        {
            'coordinates': [
                [139.76337790489197, 35.678040905014065],
                [139.76451516151428, 35.68159659061569],
            ],
            'dates': [
                '2017-06-02T00:30:00',
                '2017-06-02T00:40:00'
            ],
            'color': '#FFFFFF',
        },
    ]


    features = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'LineString',
                'coordinates': line['coordinates'],
            },
            'properties': {
                'times': line['dates'],
                'style': {
                    'color': line['color'],
                    'weight': line['weight'] if 'weight' in line else 5
                }
            }
        }
        for line in lines
        
    ]


    plugins.TimestampedGeoJson({
        'type': 'FeatureCollection',
        'features': features,
    }, period='PT1M', add_last_point=True).add_to(m)


    #m.save(os.path.join('results', 'Plugins_5.html'))

    m 






# ref : https://www.kaggle.com/poonaml/last-cab-to-new-york-animated-heatmap-trips-folium

"""
1) dynamic map 

#co-ordinates
LaGuardia = {
    "minLat": 40.76,
    "maxLat": 40.78,
    "minLong": -73.895,
    "maxLong": -73.855
}
train['pickup_datetime'] = pd.to_datetime(train.pickup_datetime)
train['dropoff_datetime'] = pd.to_datetime(train.dropoff_datetime)

LaGuardiaData = train[(train['pickup_longitude'].apply(lambda x: (x >=LaGuardia["minLong"]) & (x <= LaGuardia["maxLong"])))]
LaGuardiaData = train[(train['pickup_latitude'].apply(lambda x: (x >=LaGuardia["minLat"]) & (x <= LaGuardia["maxLat"])))]
LaGuardiaData = train[(train['dropoff_longitude'].apply(lambda x: (x >=LaGuardia["minLong"]) & (x <= LaGuardia["maxLong"])))]
LaGuardiaData = train[(train['dropoff_latitude'].apply(lambda x: (x >=LaGuardia["minLat"]) & (x <= LaGuardia["maxLat"])))]

m = folium.Map(
    location=[40.7769, -73.8740],
    zoom_start=12
)
folium.Marker(location=[40.7769, -73.8740],icon=folium.Icon(color='black') ,popup='LA Guardia International Airport').add_to(m)

shortTripsDF=LaGuardiaData[LaGuardiaData.trip_duration==900]

lines = [
    {
        'coordinates': [
            [shortTripsDF.pickup_longitude.iloc[index], shortTripsDF.pickup_latitude.iloc[index]],
            [shortTripsDF.dropoff_longitude.iloc[index], shortTripsDF.dropoff_latitude.iloc[index]],
        ],
        'dates': [
        str(shortTripsDF.pickup_datetime.iloc[index]),
        str(shortTripsDF.dropoff_datetime.iloc[index])
        ],
        'color': 'gold'
    }
    for index in range(100)
]
features = [
    {
        'type': 'Feature',
        'geometry': {
            'type': 'LineString',
            'coordinates': line['coordinates'],
        },
        'properties': {
            'times': line['dates'],
            'style': {
                'color': line['color'],
                'weight': line['weight'] if 'weight' in line else 10
            }
        }
    }
    for line in lines
]


plugins.TimestampedGeoJson({
    'type': 'FeatureCollection',
    'features': features,
}, period='PT24H', add_last_point=True).add_to(m)
m


"""

"""
2) dynamic heatmap



newyork_on_heatmap = folium.Map(location=[40.767937,-73.982155 ],tiles= "Stamen Terrain",
                    zoom_start = 13) 

# List comprehension to make out list of lists
heat_data = [[[row['dropoff_latitude'],row['dropoff_longitude']] 
                for index, row in heat_df[heat_df['Weight'] == i].iterrows()] 
                 for i in range(0,6)]

# Plot it on the map
hm = plugins.HeatMapWithTime(heat_data,auto_play=True,max_opacity=0.8)
hm.add_to(newyork_on_heatmap)

# Display the map
newyork_on_heatmap


"""










