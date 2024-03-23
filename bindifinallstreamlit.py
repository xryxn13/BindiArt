import streamlit as st
from PIL import Image,ImageSequence
import numpy as np
import io

def process_image(source_image, matrix_size):
    # Open GIF images
    gif1 = Image.open('BindiGifs/1.gif')
    gif2 = Image.open('BindiGifs/2.gif')
    gif3 = Image.open('BindiGifs/3.gif')
    gif4 = Image.open('BindiGifs/4.gif')
    gif5 = Image.open('BindiGifs/5.gif')

    # Open dice images
    die_one = Image.open("BindiImages/1.png")
    die_two = Image.open("BindiImages/2.png")
    die_three = Image.open("BindiImages/3.png")
    die_four = Image.open("BindiImages/4.png")
    die_five = Image.open("BindiImages/5.png")

    number_of_frames = min(gif1.n_frames, gif2.n_frames, gif3.n_frames, gif4.n_frames, gif5.n_frames)
    frames = []
    
    # Initialize counters for each color
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0

    # Convert source image to grayscale
    resized_image = source_image.resize((matrix_size, matrix_size))
    resized_image = resized_image.convert('L')
    pix_val = list(resized_image.getdata())

    # Map grayscale values to 1 to 5
    for i in range(len(pix_val)):
        if pix_val[i] < 51:
            pix_val[i] = 5
            count_5 += 1
        elif 51 <= pix_val[i] < 102:
            pix_val[i] = 4
            count_4 += 1
        elif 102 <= pix_val[i] < 153:
            pix_val[i] = 3
            count_3 += 1
        elif 153 <= pix_val[i] < 204:
            pix_val[i] = 2
            count_2 += 1
        else:
            pix_val[i] = 1
            count_1 += 1

    # Create output image
    output_image_size = (die_one.width * matrix_size, die_one.height * matrix_size)
    output_image = Image.new('RGB', output_image_size, color=(255, 255, 255))

    # Paste dice images onto output image
    for i in range(len(pix_val)):
        x_location = int((int(die_one.width) * i)) % (die_one.width * matrix_size)
        y_location = int(i / matrix_size) * die_one.height
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
    img1 = gif1.copy()
    matrix=np.array(pix_val).reshape(matrix_size, matrix_size)

    for frame_number in range(number_of_frames):
        new_image = Image.new('RGBA', (img1.width*matrix_size, img1.height*matrix_size), color= (0,0,0))
        for i in range(matrix_size):
            for j in range(matrix_size):
                if matrix[i][j] == 1:
                    gif1.seek(frame_number)
                    img1 = gif1.copy()
                    new_image.paste(img1, (j*img1.width, i*img1.height))
                elif matrix[i][j] == 2:
                    gif2.seek(frame_number)
                    img2 = gif2.copy()
                    new_image.paste(img2, (j*img1.width, i*img1.height))
                elif matrix[i][j] == 3:
                    gif3.seek(frame_number)
                    img3 = gif3.copy()
                    new_image.paste(img3, (j*img1.width, i*img1.height))
                elif matrix[i][j] == 4:
                    gif4.seek(frame_number)
                    img4 = gif4.copy()
                    new_image.paste(img4, (j*img1.width, i*img1.height))
                elif matrix[i][j] == 5:
                    gif5.seek(frame_number)
                    img5 = gif5.copy()
                    new_image.paste(img5, (j*img1.width, i*img1.height))
        frames.append(new_image)
    frames[0].save('outputGIF.gif', save_all=True, append_images=frames[1:], loop=1, duration=100)
    OutputGif = Image.open('outputGIF.gif')
    frames = [frame.copy() for frame in ImageSequence.Iterator(OutputGif)]

    # Get the last frame
    last_frame = frames[-1]

    # Create a new GIF with the last frame repeated
    repeated_frames = [last_frame.copy() for _ in range(40)]

    # Save the new GIF
    frames.extend(repeated_frames)

    frames[0].save('OutputGIF.gif', save_all=True, append_images=frames[1:], loop=1, duration=100)

    return output_image, (count_1, count_2, count_3, count_4, count_5)

def convert_image_to_bytes(img):
    # Convert PIL image to bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')
    return img_byte_arr.getvalue()

def main():
    col1, col2 = st.columns(2)
    with col1:
        st.title("Bindi Art by CCL, IIT Gandhinagar")    
    with col2:
        st.image("logo.png", width=150)
    # File uploader for selecting an image
    uploaded_image = st.file_uploader("Choose an image:", type=["png", "jpg", "jpeg"])

    # Slider for selecting matrix size
    matrix_size = st.slider("Select matrix size:", min_value=1, max_value=70, value=60)

    if uploaded_image is not None:
        # Process the image
        source_image = Image.open(uploaded_image)
        processed_image, counts = process_image(source_image, matrix_size)
        with open("outputGIF.gif", "rb") as f:
            gif_bytes = f.read()
        # Display the processed image
        # col1, col2 = st.columns(2)
        # with col1:
        st.image(processed_image, caption="Processed Image", use_column_width=True)
        st.download_button(label="Download Image", data=convert_image_to_bytes(processed_image), file_name="image1.jpg")

        # Display the second image in the second column
        # with col2:
        st.image('outputGIF.gif',caption="Bindi Art GIF",use_column_width=True)
        st.download_button(label="Download GIF", data=gif_bytes, file_name="image1.gif")

        # Display counts
        st.write("Number of Size 1's Bindis:", counts[0])
        st.write("Number of Size 2's Bindis:", counts[1])
        st.write("Number of Size 3's Bindis:", counts[2])
        st.write("Number of Size 4's Bindis:", counts[3])
        st.write("Number of Size 5's Bindis:", counts[4])

if __name__ == "__main__":
    main()
