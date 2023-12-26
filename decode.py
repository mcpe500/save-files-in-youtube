import cv2
import numpy as np

meta = {'init_image_size': (1080, 1080, 3), 'pixel_size': 126, 'dictionary_color': {'empty': [0, 0, 0], ',': [255.0, 85.0, 255.0], 'k': [0.0, 85.0, 85.0], 'j': [85.0, 255.0, 255.0], 'r': [0.0, 255.0, 170.0], 'n': [170.0, 170.0, 0.0], 'p': [170.0, 170.0, 255.0], 'l': [0.0, 170.0, 255.0], 'a': [0.0, 0.0, 255.0], 'o': [255.0, 170.0, 0.0], 'b': [0.0, 255.0, 255.0], 'i': [170.0, 255.0, 170.0], 'g': [255.0, 85.0, 170.0], 'h': [255.0, 170.0, 170.0], ':': [255.0, 255.0, 85.0], 'u': [85.0, 0.0, 170.0], ' ': [85.0, 0.0, 255.0], 'm': [0.0, 255.0, 0.0], 'd': [0.0, 170.0, 85.0], '2': [170.0, 0.0, 170.0], 's': [0.0, 85.0, 0.0], '5': [85.0, 255.0, 85.0], 'e': [170.0, 170.0, 85.0]}, 'max_random': 4}

image_path = "./output_image.png"
image = cv2.imread(image_path)
pixel_size = meta["pixel_size"]
split_images = []
xP = 0
yP = 0

while yP < meta["init_image_size"][0]:
    while xP < meta["init_image_size"][1]:
        split_images.append(image[yP:yP + pixel_size, xP:xP + pixel_size])
        xP += pixel_size
    xP = 0
    yP += pixel_size

msg = ""
for i in split_images:
    # Convert the dictionary colors to integers
    reference_colors = {key: [int(val) for val in value] for key, value in meta["dictionary_color"].items()}
    
    for letter, reference_color in reference_colors.items():
        # Check if the color of the first pixel in the split image is equal to the color in the dictionary
        if np.array_equal(i[0][0], reference_color):
            if letter != "empty":
              msg+=letter
            break  # Exit the inner loop once a matching color is found for the current split image
print(msg)