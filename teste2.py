import cv2
import matplotlib.pyplot as plt


img = cv2.imread('AI_Engineer.png', cv2.IMREAD_COLOR)
# Primeira maneira
"""img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()"""

# Segunda maneira
while True:
    cv2.imshow('figura1', img)
    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break
cv2.destroyAllWindows()
