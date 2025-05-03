import pygame

# This class controls the color grading




# This function takes an image(Surface), and returns a greyscaled image
def convert_to_black_and_white(image):
    bw_image = pygame.Surface(image.get_size()).convert()
    arr = pygame.surfarray.pixels3d(image)
    
    # Iterate over each pixel
    for y in range(image.get_height()):
        for x in range(image.get_width()):
            avg = (int(arr[x][y][0]) + int(arr[x][y][1]) + int(arr[x][y][2])) // 3
            avg = min(max(avg, 0), 255)  # Ensure the value is within the range [0, 255]
            arr[x][y] = [avg, avg, avg]
    
    return image

# This function takes an image(Surface), and returns an imaage with the removedColor
# Buth replacement_color and target_color are RGB values(R,G,B)
def remove_color(image, target_color, replacement_color=(0,0,0), acceptedRange= 100) -> pygame.Surface:
    
    def color_distance(c1, c2):
        return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5


    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel_color = image.get_at((x,y))[:3]
            if color_distance(pixel_color, target_color) <= acceptedRange:
                image.set_at((x,y), replacement_color)
    
    return image

# This function removes the red channel (SHOULD NOT BE USED WHEN CHANNEL HAS BEEN X REMOVED MORE THAN ONCE)
def remove_red_channel(image) -> pygame.Surface:
    image = image.copy()

    for x in range(image.get_width()):
        for y in range(image.get_height()):
            r,g,b, *a = image.get_at((x,y))
            alpha = a[0] if a else 255
            image.set_at((x,y), (0,g,b,alpha))

    return image

# This function removes the green channel (SHOULD NOT BE USED WHEN CHANNEL HAS BEEN X REMOVED MORE THAN ONCE)
def remove_green_channel(image) -> pygame.Surface:
    image = image.copy()

    for x in range(image.get_width()):
        for y in range(image.get_height()):
            r,g,b, *a = image.get_at((x,y))
            alpha = a[0] if a else 255
            image.set_at((x,y), (r, 0, b, alpha))
    return image

# This function removes the green channel (SHOULD NOT BE USED WHEN CHANNEL HAS BEEN X REMOVED MORE THAN ONCE)
def remove_blue_channel(image) -> pygame.Surface:
    image = image.copy()

    for x in range(image.get_width()):
        for y in range(image.get_height()):
            r,g,b, *a = image.get_at((x,y))
            alpha = a[0] if a else 255
            image.set_at((x,y), (r, g, 0, alpha))

    return image