import calc_angle_points
import json
import glob

path = '../../data/output'
json_file_list = glob.glob(path + '/*.json')

with open(json_file_list[0]) as f:
    data = json.load(f)

print(data['tooltips'])
an = calc_angle_points.calc_angles(data['tooltips'])
print(an)

