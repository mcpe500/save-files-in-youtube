import numpy as np
import cv2
import math

def round_down_to_power_of_three(number):
    return int(math.ceil(number ** (1/3)))
    
def generate_color(max_random, step):
    g = np.random.randint(max_random) * step
    r = np.random.randint(max_random) * step
    b = np.random.randint(max_random) * step
    return [g, r, b]

def create_image(inp):
    unique_text = set(inp)
    pixel_size = int(1080 / (len(inp) ** 0.5))

    max_random = round_down_to_power_of_three(len(unique_text)) + 1
    step = 255 / (max_random - 1) if max_random > 1 else 255

    possible_colors = set()
    dictionary_color = {"empty": [0, 0, 0]}

    for i in unique_text:
        while True:
            generated_color = generate_color(max_random, step)
            if tuple(generated_color) not in possible_colors:
                possible_colors.add(tuple(generated_color))
                dictionary_color[i] = generated_color
                break

    empty_image = np.zeros((1080, 1080, 3), dtype=np.uint8)

    xP, yP = 0, 0
    for i in inp:
        empty_image[yP * pixel_size:(yP + 1) * pixel_size, xP * pixel_size:(xP + 1) * pixel_size] = dictionary_color[i]
        xP += 1
        if xP * pixel_size >= 1080:
            yP += 1
            xP = 0

    bigger_image = cv2.resize(empty_image, (1080, 1080))

    output_path = "output_image.png"
    cv2.imwrite(output_path, bigger_image)

    print(f"Image saved as {output_path}")

    metadata = {
        "init_image_size": (1080, 1080, 3),
        "pixel_size": pixel_size,
        "dictionary_color": dictionary_color,
        "max_random": max_random
    }
    print("METADATA")
    print(metadata)

# Add your round_down_to_power_of_three function here if not defined previously

inp = input("input: ")
create_image(inp)
