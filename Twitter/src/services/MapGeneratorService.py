import folium as folium

map = folium.Map(location=[45, 0], zoom_start=2, tiles='cartodbdark_matter')

map.save("../../data/tweets_map.html")
