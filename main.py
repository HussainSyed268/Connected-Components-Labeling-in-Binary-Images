import cv2
import numpy as np

pos = 50
result_image = cv2.imread('cc.png')
result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2GRAY)

_, result_image = cv2.threshold(result_image, 128, 255, cv2.THRESH_BINARY)

def find(label):
    if dict[label] != label:
        dict[label] = find(dict[label])
    return dict[label]

dict = {}
for i in range(1, result_image.shape[0] - 1):
    for j in range(1, result_image.shape[1] - 1):
        if result_image[i][j] != 0:
            neighbors = [
                result_image[i - 1][j - 1], result_image[i - 1][j], result_image[i - 1][j + 1],
                result_image[i][j - 1]
            ]
            neighbors = [x for x in neighbors if x != 0]

            if not neighbors:
                result_image[i][j] = pos
                dict[pos] = pos
                pos = pos + 1
            else:
                mini = min(neighbors)
                for n in neighbors:
                    if n != mini:
                        dict[n] = mini
                result_image[i][j] = mini

for i in range(1, result_image.shape[0] - 1):
    for j in range(1, result_image.shape[1] - 1):
        if result_image[i][j] != 0:
            result_image[i][j] = find(result_image[i][j])

color_dict = {}

for i in range(1, result_image.shape[0] - 1):
    for j in range(1, result_image.shape[1] - 1):
        label = result_image[i][j]
        if label != 0 and label not in color_dict:
            color_dict[label] = np.random.randint(0, 256, 3)

colored_image = np.zeros((result_image.shape[0], result_image.shape[1], 3), dtype=np.uint8)

for i in range(1, result_image.shape[0] - 1):
    for j in range(1, result_image.shape[1] - 1):
        label = result_image[i][j]
        if label != 0:
            colored_image[i][j] = color_dict[label]

count = 0
label = []
for i in range(1, result_image.shape[0] - 1):
    for j in range(1, result_image.shape[1] - 1):
        intensity = result_image[i, j]
        if intensity != 0 and intensity not in label:
            count += 1
            label.append(intensity)
print("Number of objects : ", count)
cv2.imshow("Colored Result", colored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
