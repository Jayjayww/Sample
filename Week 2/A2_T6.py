#Write a Python program which asks user to insert hex color. 
#In this case hex color is expected to be the 7 character representation starting with # and followed by 6 0-F characters to represent RGB colors. 
#More about hex colors at https://en.wikipedia.org/wiki/Web_colors

#Slice the amount of red, green and blue from that inserted color and display each color as shown below.

print("Program starting.\n")
hex_color = input("Insert hex color (format: #RRGGBB):")
if len(hex_color) != 7 or not hex_color.startswith("#"):
    print("Invalid hex color format. Please ensure it starts with '#' and is 7 characters long.")
    print("Program ending.")
    exit()
    
red_hex = hex_color[1:3]
green_hex = hex_color[3:5]
blue_hex = hex_color[5:7]
print("\nColors")
print(f"-Red {red_hex}")
print(f"-Green {green_hex}")
print(f"-Blue {blue_hex}\n")
print("Program ending.")
