import os

def read_raw_pixel_data(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

def create_ppm(width, height, pixel_data):
    with open('output.ppm', 'wb') as f:
        f.write(b'P6\n') 
        f.write(f"{width} {height}\n".encode()) 
        f.write(b'255\n')  
        f.write(pixel_data)

file_path = 'challenge4' 
pixel_data = read_raw_pixel_data(file_path)

width = 768  
height = 576  

create_ppm(width, height, pixel_data)