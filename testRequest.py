from pathlib import Path
import time


p = Path(__file__).with_name('input.txt')
with p.open('w') as file:
    Lines = file.writelines("Bleak good afternoon \nA domestic, blue pig flies \nin spite of the cube")

print("written haiku to input.txt")

time.sleep(2)

p = Path(__file__).with_name('signal.txt')
with p.open('w') as file:
    Lines = file.writelines("run")

print("called for image generation")