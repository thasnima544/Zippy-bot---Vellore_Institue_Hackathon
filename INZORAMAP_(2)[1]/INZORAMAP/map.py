import folium

# Define map center (latitude, longitude)
map_center = [28.6139, 77.2090]  # Example: New Delhi coordinates

# Create a map object
m = folium.Map(location=map_center, zoom_start=12)

# Add green dot for normal area
normal_areas = [
    [28.615, 77.210],  # Example location 1
    [28.620, 77.215],  # Example location 2
]

for loc in normal_areas:
    folium.CircleMarker(
        location=loc,
        radius=8,
        color='green',
        fill=True,
        fill_color='green',
        fill_opacity=0.7,
        popup='Normal Area'
    ).add_to(m)

# Add red dot for victim location
victim_locations = [
    [28.610, 77.200],  # Example victim location
]

for loc in victim_locations:
    folium.CircleMarker(
        location=loc,
        radius=10,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.9,
        popup='Victim Location'
    ).add_to(m)

# Save map to an HTML file
m.save("map_with_victims.html")

print("Map saved! Open map_with_victims.html in your browser.")
