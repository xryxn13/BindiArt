import streamlit as st
import numpy as np
from PIL import Image,ImageSequence
import io

def convert_image_to_bytes(img):
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')
    return img_byte_arr.getvalue()
# Load the dice images and GIFs
die_one = Image.open("BindiImages/1.png")
die_two = Image.open("BindiImages/2.png")
die_three = Image.open("BindiImages/3.png")
die_four = Image.open("BindiImages/4.png")
die_five = Image.open("BindiImages/5.png")
die_six = Image.open("BindiImages/6.png")
gif1 = Image.open('BindiGifs/1.gif')
gif2 = Image.open('BindiGifs/2.gif')
gif3 = Image.open('BindiGifs/3.gif')
gif4 = Image.open('BindiGifs/4.gif')
gif5 = Image.open('BindiGifs/5.gif')
gif6 = Image.open('BindiGifs/6.gif')
number_of_frames = min(gif1.n_frames, gif2.n_frames, gif3.n_frames, gif4.n_frames, gif5.n_frames, gif6.n_frames)

col1, col2 = st.columns(2)
with col1:
    st.title("Dice Mosaic Generator by CCL, IIT Gandhinagar")    
with col2:
    st.image("logo.png", width=150)
    
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    matrix_size = st.slider("Select matrix size", min_value=10, max_value=100, value=40)
    source_image = Image.open(uploaded_image)

    dice_image_width, dice_image_height = die_one.size
    resized_image = source_image.resize((matrix_size, matrix_size))
    resized_image = resized_image.convert('L')
    pix_val = list(resized_image.getdata())

    for i in range(len(pix_val)):
        if pix_val[i] < 42:
            pix_val[i] = 1
        elif 42 <= pix_val[i] < 84:
            pix_val[i] = 2
        elif 84 <= pix_val[i] < 126:
            pix_val[i] = 3
        elif 126 <= pix_val[i] < 168:
            pix_val[i] = 4
        elif 168 <= pix_val[i] < 210:
            pix_val[i] = 5
        else:
            pix_val[i] = 6

    output_image_size = (dice_image_width * matrix_size, dice_image_height * matrix_size)
    output_image = Image.new('L', output_image_size, color=0)

    for i in range(len(pix_val)):
        x_location = int((int(dice_image_width) * i)) % (dice_image_width * matrix_size)
        y_location = int(i / matrix_size) * dice_image_height
        if pix_val[i] == 1:
            output_image.paste(die_one, (x_location, y_location))
        elif pix_val[i] == 2:
            output_image.paste(die_two, (x_location, y_location))
        elif pix_val[i] == 3:
            output_image.paste(die_three, (x_location, y_location))
        elif pix_val[i] == 4:
            output_image.paste(die_four, (x_location, y_location))
        elif pix_val[i] == 5:
            output_image.paste(die_five, (x_location, y_location))
        else:
            output_image.paste(die_six, (x_location, y_location))

    output_image.save('OutputOfDicePortrait.png')

    elements = pix_val
    matrix = np.array(elements).reshape(matrix_size, matrix_size)
    frames = []
    for frame_number in range(1, number_of_frames, 2):
        new_image = Image.new('RGBA', (gif1.width * matrix_size, gif1.height * matrix_size), color=(0, 0, 0))
        for i in range(matrix_size):
            for j in range(matrix_size):
                if matrix[i][j] == 1:
                    gif1.seek(frame_number)
                    img = gif1.copy()
                elif matrix[i][j] == 2:
                    gif2.seek(frame_number)
                    img = gif2.copy()
                elif matrix[i][j] == 3:
                    gif3.seek(frame_number)
                    img = gif3.copy()
                elif matrix[i][j] == 4:
                    gif4.seek(frame_number)
                    img = gif4.copy()
                elif matrix[i][j] == 5:
                    gif5.seek(frame_number)
                    img = gif5.copy()
                else:
                    gif6.seek(frame_number)
                    img = gif6.copy()
                new_image.paste(img, (j * img.width, i * img.height))
        frames.append(new_image)
    frames[0].save('OutputGIF.gif', save_all=True, append_images=frames[1:], loop=1, duration=100)
    OutputGif = Image.open('OutputGIF.gif')
    frames = [frame.copy() for frame in ImageSequence.Iterator(OutputGif)]

    # Get the last frame
    last_frame = frames[-1]

    # Create a new GIF with the last frame repeated
    repeated_frames = [last_frame.copy() for _ in range(200)]

    # Save the new GIF
    frames.extend(repeated_frames)

    frames[0].save('OutputGIF.gif', save_all=True, append_images=frames[1:], loop=1, duration=100)

    num_of_frame = min(OutputGif.n_frames,OutputGif.n_frames)
    print(num_of_frame)
    with open("OutputGIF.gif", "rb") as f:
        gif_bytes = f.read()

    st.image('OutputGIF.gif', caption="Dice Mosaic GIF", use_column_width=True)
    st.download_button(label="Download GIF", data=gif_bytes, file_name="image1.gif")

    st.image(output_image, caption='Output Image', use_column_width=True)
    st.download_button(label="Download Image", data=convert_image_to_bytes(output_image), file_name="image1.jpg")
