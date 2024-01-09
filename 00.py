import pandas as pd
import json

# 读取 CSV 文件
csv_file = '0109.csv'
df = pd.read_csv(csv_file)

# 创建 GeoJSON 结构
features = []

for index, row in df.iterrows():
    feature = {
        "type": "Feature",
        "properties": {
            "main_type": row['名稱'],
            "sub_type": row['承辦單位'],
            "address": row['地址'],
            "area": row['地區'],
        },
        "geometry": {
            "type": "Point",
            "coordinates": [float(row['X']), float(row['Y'])]
        }
    }
    features.append(feature)

geojson_data = {
    "type": "FeatureCollection",
    "features": features
}

# 将数据保存为 GeoJSON 文件
geojson_file = '931.geojson'
with open(geojson_file, 'w', encoding='utf-8') as f:
    json.dump(geojson_data, f, ensure_ascii=False, indent=2)

print(f'Conversion completed. GeoJSON file saved to {geojson_file}')
