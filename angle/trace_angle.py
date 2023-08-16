import json
import glob
import calc_angle_points
import pandas as pd
import csv

# 모든 json 파일 list로 가져오기
path = '../data/output'
json_file_list = glob.glob(path + '/*.json')

print(json_file_list)

DataFrame = []

# json 파일 읽어오기
for json_file in json_file_list:
    with open(json_file) as f:
        DataFrame.append(json.load(f))

# print(DataFrame)

angles_list = []

# json 파일에서 각도 계산하기
for data in DataFrame:
    angles = calc_angle_points.calc_angles(data['tooltips'])
    # print(angles)
    angles_list.append(angles)

# print(angles_list)

angles_dict = dict()

for i, data in enumerate(DataFrame):
    angles = calc_angle_points.calc_angles(data['tooltips'])
    angles_dict[i] = angles

# csv DataFrame 만들기
df = pd.DataFrame(columns=angles_list[0].keys())
for i, d in enumerate(angles_list):
    df.loc[i] = d.values()

print(df)
df.to_excel('./data_angle/angles.xlsx')

# csv 쓰기
# with open('angles.csv', 'w', newline='') as f:
    # using csv.writer method from CSV package
#     write = csv.writer(f)
#     write.writerows(angles_list)

# json 파일 쓰기
with open('./data_angle/angles.json', 'w') as f:
    json.dump(angles_dict, f)