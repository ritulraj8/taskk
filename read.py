import cv2
import numpy as np

image_size = 600
background_color = (255, 255, 255)
image = np.full((image_size, image_size, 3), background_color, dtype=np.uint8)

dice_size = 100
positions = [
    (200, 100), 
    (100, 200), 
    (200, 200), 
    (300, 200),
    (200, 300), 
    (0, 200)  
]


colors = [
    (190, 40, 100),  
    (240, 145, 55),    
    (215, 85, 50),  
    (70, 155, 165),  
    (100, 65, 185),  
    (55, 130, 230)   
]


dot_positions = {
    1: [(0.5, 0.5)],
    2: [(0.25, 0.25), (0.75, 0.75)],
    3: [(0.25, 0.25), (0.5, 0.5), (0.75, 0.75)],
    4: [(0.25, 0.25), (0.25, 0.75), (0.75, 0.25), (0.75, 0.75)],
    5: [(0.25, 0.25), (0.25, 0.75), (0.75, 0.25), (0.75, 0.75), (0.5, 0.5)],
    6: [(0.25, 0.25), (0.5, 0.25), (0.75, 0.25), (0.25, 0.75), (0.5, 0.75), (0.75, 0.75)]
}


dice_numbers = [4, 6, 5, 1, 3, 2] 
dot_color = (220, 220, 220)  

for idx, pos in enumerate(positions):
    top_left = (pos[0], pos[1])
    bottom_right = (pos[0] + dice_size, pos[1] + dice_size)
    
    cv2.rectangle(image, top_left, bottom_right, colors[idx], -1)
    
    for dot_pos in dot_positions[dice_numbers[idx]]:
        center = (int(top_left[0] + dot_pos[0] * dice_size), int(top_left[1] + dot_pos[1] * dice_size))
        cv2.circle(image, center, 10, dot_color, -1)

cv2.putText(image,"Ritul 123CS0020",(200,490),cv2.FONT_HERSHEY_TRIPLEX,1.0,(0,0,0),2)
cv2.imwrite('dice_image.png', image)
cv2.imshow('Dice Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

