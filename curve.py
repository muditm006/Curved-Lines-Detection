import numpy as np
import cv2
from collections import defaultdict
import argparse

configuration = argparse.ArgumentParser()
configuration.add_argument("-i", "--image", required=True, help="Path to the image")
config = vars(configuration.parse_args())
image = config["image"]
img = cv2.imread(image)
product = img.copy()

blur = cv2.medianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 5)
edges = cv2.Canny(blur, 100, 200)
bin_img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

lines = cv2.HoughLines(bin_img, 2, np.pi / 180, 350)


def seg(lns, k, **dic):
    default_criteria_type = cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER
    pts = np.array([[np.cos(2 * angle), np.sin(2 * angle)] for angle in np.array([line[0][1] for line in lns])],
                   dtype=np.float32)
    labels, centers = cv2.kmeans(pts, k, None, dic.get('Thing_One', (default_criteria_type, 10, 1.0)),
                                 dic.get('Thing_Three', 10), dic.get('Thing_Two', cv2.KMEANS_RANDOM_CENTERS))[1:]
    labels = labels.reshape(-1)
    mented = defaultdict(list)
    for iterator, line in zip(range(len(lns)), lns):
        mented[labels[iterator]].append(line)
    mented = list(mented.values())
    return mented


segmented = seg(lines, 2)
intersections = []
for i, group in enumerate(segmented[:-1]):
    for next_group in segmented[i + 1:]:
        for line1 in group:
            for line2 in next_group:
                rho1, theta1 = line1[0]
                rho2, theta2 = line2[0]
                a = np.array([[np.cos(theta1), np.sin(theta1)], [np.cos(theta2), np.sin(theta2)]])
                b = np.array([[rho1], [rho2]])
                x0, y0 = np.linalg.solve(a, b)
                x0, y0 = int(np.round(x0)), int(np.round(y0))
                intersections.append([[x0, y0]])

x_points = []
y_points = []
for point in intersections:
    pt = (point[0][0], point[0][1])
    x_points.append(point[0][0])
    y_points.append(point[0][1])

average_x = int(sum(x_points) / len(x_points))
average_y = int(sum(y_points) / len(y_points))
height, width, channels = img.shape
if width // 2 >= average_x:
    cv2.arrowedLine(product, (average_x, average_y + 4 * average_y), (average_x, average_y), (148, 0, 211), 1)
    cv2.arrowedLine(product, (average_x, average_y), (width, average_y), (218, 165, 32), 1)
else:
    cv2.arrowedLine(product, (average_x, average_y + 4 * average_y), (average_x, average_y), (148, 0, 211), 1)
    cv2.arrowedLine(product, (average_x, average_y), (0, average_y), (218, 165, 32), 1)

cv2.imshow("Product", product)
cv2.waitKey()
