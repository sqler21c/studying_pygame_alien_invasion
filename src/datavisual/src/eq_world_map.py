from pathlib import Path
import json
from find_dir import find_dir as fd
import plotly.express as px


# 데이터를 문자열로 읽어 JSON으로 변환
path_fd = fd(1, 'eq_data', 'eq_data_30_day_m1.geojson')
print(f"path_fd: {path_fd}")
path = Path(path_fd)
contents = path.read_text(encoding='utf-8')

all_eq_data = json.loads(contents)

# 데이터 파일을 읽기 쉬운 형태로 변환
# path_fd = fd(1, 'eq_data', 'readable_eq_data.json')
# path = Path(path_fd)
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

# 데이터 집합의 지진 데이터를 모두 읽습니다.
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))
mags, lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(title)

print(mags[:10])
print(lons[:5])
print(lats[:5])

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, title=title, 
                     color=mags, 
                     color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'}, 
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()