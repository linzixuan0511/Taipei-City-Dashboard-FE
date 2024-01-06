import pandas as pd
import json

# 读取 CSV 文件
csv_file = '12.csv'
df = pd.read_csv(csv_file)

# 创建 GeoJSON 结构
features = []

for index, row in df.iterrows():
    feature = {
        "type": "Feature",
        "properties": {
            "type": row['類別'],
            "name": row['機構名稱'],
            "addr": row['地址'],
        },
        "geometry": {
            "type": "Point",
            "coordinates": [float(row['Y']), float(row['X'])]
        }
    }
    features.append(feature)

geojson_data = {
    "type": "FeatureCollection",
    "features": features
}

# 将数据保存为 GeoJSON 文件
geojson_file = 'm01.geojson'
with open(geojson_file, 'w', encoding='utf-8') as f:
    json.dump(geojson_data, f, ensure_ascii=False, indent=2)

print(f'Conversion completed. GeoJSON file saved to {geojson_file}')
