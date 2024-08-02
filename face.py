import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a blank image
image = np.zeros((500, 500, 3), dtype="uint8")
image.fill(255)  # Fill the image with white color

# Draw the face (ellipse)
cv2.ellipse(image, (250, 250), (150, 200), 0, 0, 360, (255, 220, 185), -1)

# Draw the eyes
cv2.circle(image, (200, 200), 30, (255, 255, 255), -1)  # Left eye white part
cv2.circle(image, (300, 200), 30, (255, 255, 255), -1)  # Right eye white part
cv2.circle(image, (200, 200), 15, (0, 0, 0), -1)        # Left eye pupil
cv2.circle(image, (300, 200), 15, (0, 0, 0), -1)        # Right eye pupil

# Draw the nose (polygon)
pts = np.array([[250, 230], [230, 300], [270, 300]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(image, [pts], (255, 220, 185))

# Draw the mouth (ellipse)
cv2.ellipse(image, (250, 350), (80, 40), 0, 0, 180, (0, 0, 0), 5)

# Display the image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
