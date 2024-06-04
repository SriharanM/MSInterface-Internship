from tkinter import *
from tkinter import simpledialog, filedialog
from PIL import Image

def process_image(image_path, key):
    image = Image.open(image_path)
    image = image.convert("RGB")

    width, height = image.size
    for i in range(width):
        for j in range(height):
            r, g, b = image.getpixel((i, j))
            encrypted_pixel = (r ^ key, g ^ key, b ^ key)
            image.putpixel((i, j), encrypted_pixel)

    return image

def open_image(mode):
    key = simpledialog.askinteger("Input", f"Enter the key to {mode} (0-255):", minvalue=0, maxvalue=255)
    if key is None:
        return  # User cancelled the input dialog

    image_path = filedialog.askopenfilename()
    if image_path:
        result_image = process_image(image_path, key)
        result_image.show()
        save_path = filedialog.asksaveasfilename(defaultextension=".png")
        if save_path:
            result_image.save(save_path)

def encrypt_image():
    open_image('encrypt')

def decrypt_image():
    open_image('decrypt')

root = Tk()
root.title("Image Encryptor/Decryptor")

Button(root, text="Encrypt Image", command=encrypt_image).pack(pady=5)
Button(root, text="Decrypt Image", command=decrypt_image).pack(pady=5)
Button(root, text="Quit", command=root.quit).pack(pady=5)

root.mainloop()

