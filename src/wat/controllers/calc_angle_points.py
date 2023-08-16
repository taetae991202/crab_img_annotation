import math

epsilon = 2e-8

# 3점 사이의 각도 구하기
def calc_angle(p1, p2, p3):
    o1 = math.atan((p1['y']-p2['y'])/(p1['x']-p2['x']+epsilon))
    o2 = math.atan((p3['y'] - p2['y']) / (p3['x'] - p2['x']+epsilon))

    angle = math.fabs((o1-o2) * 180/math.pi)
    return angle


# 여러 points 입력 받아서 각도 구하기
def calc_angles(points):
    length = len(points)
    angle_dict = dict()

    for i in range(length - 2):
        # 각도 계산
        angle = calc_angle(points[i], points[i + 1], points[i + 2])
        # {점 : 각도} 딕셔너리
        angle_dict[i+1]  = angle

    return angle_dict