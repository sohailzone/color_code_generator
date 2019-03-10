# Search
def search(color, n):
    size = len(color)
    point = 0
    while point < size:
        if color[point] == n:
            return True
        point = point + 1
    return False


# Color Array
color = ["red", "green", "blue", "white", "black", "gray"]

# RGB Pattern
rgb = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
    "black": [0, 0, 0],
    "white": [255, 255, 255],
    "gray": [190, 190, 190]
}
# HEX Pattern
hex = {
    "black": "#000000",
    "white": "#FFFFF",
    "gray": "#BEBEBE",
    "blue": "#0000FF",
    "red": "#FF0000",
    "green": "#00FF00"
}
print("\nHello\nand\nWelcome to Colour Value Generator")
while True:
    print("\nYour Choices:")
    print("1. Add Color and it's Value")
    print("2. Check Color and it's Value")
    print("3. Remove Colour and it's Value")
    print("4. View Colour List")
    print("5. Exit")
    c = int(input("Enter Choice : "))
    if c == 1:
        name = input("Enter Colour Name : ")
        rgb1 = input("Enter it's RGB 1st Parameter Value : ")
        rgb2 = input("Enter it's RGB 2nd Parameter Value : ")
        rgb3 = input("Enter it's RGB 3rd Parameter Value : ")
        hex_value = input("Enter it's Hex Value followed by # TAG  : ")
        color.append(name)
        rgb[name] = [rgb1, rgb2, rgb3]
        hex[name] = hex_value
        print("***** Colour Added *****")
    elif c == 2:
        n = input("Enter colour Name : ")
        if search(color, n):
            print("Here it is.")
            print("\tRGB Value of", n, "is : ", rgb[n])
            print("\tHexadecimal Value of", n, "is : ", hex[n])
        else:
            print("Color Not Exists")
    elif c == 3:
        remove = input("Enter colour Name : ")
        color.remove(remove)
        del rgb[remove]
        del hex[remove]
        print("***** Colour Removed Successfully *****")
    elif c == 4:
        size = len(color)
        print("Here it is.")
        for i in range(size):
            print("\t", color[i])
            i = i + 1
    else:
        break
print("***** Thank You So Much *****")
