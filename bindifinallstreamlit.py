import streamlit as st
from PIL import Image,ImageSequence
import numpy as np
import io

def process_image(source_image, matrix_size,selected_color):
    REDgif1 = Image.open('BindiGifs/RED/1.gif')
    REDgif2 = Image.open('BindiGifs/RED/2.gif')
    REDgif3 = Image.open('BindiGifs/RED/3.gif')
    REDgif4 = Image.open('BindiGifs/RED/4.gif')
    REDgif5 = Image.open('BindiGifs/RED/5.gif')
    RED1 = Image.open("BindiImages/RED/1.png")
    RED2 = Image.open("BindiImages/RED/2.png")
    RED3 = Image.open("BindiImages/RED/3.png")
    RED4 = Image.open("BindiImages/RED/4.png")
    RED5 = Image.open("BindiImages/RED/5.png")
    PINKgif1 = Image.open('BindiGifs/PINK/1.gif')
    PINKgif2 = Image.open('BindiGifs/PINK/2.gif')
    PINKgif3 = Image.open('BindiGifs/PINK/3.gif')
    PINKgif4 = Image.open('BindiGifs/PINK/4.gif')
    PINKgif5 = Image.open('BindiGifs/PINK/5.gif')
    PINK1 = Image.open("BindiImages/PINK/1.png")
    PINK2 = Image.open("BindiImages/PINK/2.png")
    PINK3 = Image.open("BindiImages/PINK/3.png")
    PINK4 = Image.open("BindiImages/PINK/4.png")
    PINK5 = Image.open("BindiImages/PINK/5.png")
    BLUEgif1 = Image.open('BindiGifs/BLUE/1.gif')
    BLUEgif2 = Image.open('BindiGifs/BLUE/2.gif')
    BLUEgif3 = Image.open('BindiGifs/BLUE/3.gif')
    BLUEgif4 = Image.open('BindiGifs/BLUE/4.gif')
    BLUEgif5 = Image.open('BindiGifs/BLUE/5.gif')
    BLUE1 = Image.open("BindiImages/BLUE/1.png")
    BLUE2 = Image.open("BindiImages/BLUE/2.png")
    BLUE3 = Image.open("BindiImages/BLUE/3.png")
    BLUE4 = Image.open("BindiImages/BLUE/4.png")
    BLUE5 = Image.open("BindiImages/BLUE/5.png")
    BLACKgif1 = Image.open('BindiGifs/BLACK/1.gif')
    BLACKgif2 = Image.open('BindiGifs/BLACK/2.gif')
    BLACKgif3 = Image.open('BindiGifs/BLACK/3.gif')
    BLACKgif4 = Image.open('BindiGifs/BLACK/4.gif')
    BLACKgif5 = Image.open('BindiGifs/BLACK/5.gif')
    BLACK1 = Image.open("BindiImages/BLACK/1.png")
    BLACK2 = Image.open("BindiImages/BLACK/2.png")
    BLACK3 = Image.open("BindiImages/BLACK/3.png")
    BLACK4 = Image.open("BindiImages/BLACK/4.png")
    BLACK5 = Image.open("BindiImages/BLACK/5.png")
    ORANGEgif1 = Image.open('BindiGifs/ORANGE/1.gif')
    ORANGEgif2 = Image.open('BindiGifs/ORANGE/2.gif')
    ORANGEgif3 = Image.open('BindiGifs/ORANGE/3.gif')
    ORANGEgif4 = Image.open('BindiGifs/ORANGE/4.gif')
    ORANGEgif5 = Image.open('BindiGifs/ORANGE/5.gif')
    ORANGE1 = Image.open("BindiImages/ORANGE/1.png")
    ORANGE2 = Image.open("BindiImages/ORANGE/2.png")
    ORANGE3 = Image.open("BindiImages/ORANGE/3.png")
    ORANGE4 = Image.open("BindiImages/ORANGE/4.png")
    ORANGE5 = Image.open("BindiImages/ORANGE/5.png")
    GREENgif1 = Image.open('BindiGifs/GREEN/1.gif')
    GREENgif2 = Image.open('BindiGifs/GREEN/2.gif')
    GREENgif3 = Image.open('BindiGifs/GREEN/3.gif')
    GREENgif4 = Image.open('BindiGifs/GREEN/4.gif')
    GREENgif5 = Image.open('BindiGifs/GREEN/5.gif')
    GREEN1 = Image.open("BindiImages/GREEN/1.png")
    GREEN2 = Image.open("BindiImages/GREEN/2.png")
    GREEN3 = Image.open("BindiImages/GREEN/3.png")
    GREEN4 = Image.open("BindiImages/GREEN/4.png")
    GREEN5 = Image.open("BindiImages/GREEN/5.png")
    if selected_color=='Red':
        gif1 = REDgif1
        gif2 = REDgif2
        gif3 = REDgif3
        gif4 = REDgif4
        gif5 = REDgif5

        die_one = RED1
        die_two = RED2
        die_three = RED3
        die_four = RED4
        die_five = RED5
    
    if selected_color=='black':
        gif1 = BLACKgif1
        gif2 = BLACKgif2
        gif3 = BLACKgif3
        gif4 = BLACKgif4
        gif5 = BLACKgif5

        die_one = BLACK1
        die_two = BLACK2
        die_three = BLACK3
        die_four = BLACK4
        die_five = BLACK5
    if selected_color=='blue':
        gif1 = BLUEgif1
        gif2 = BLUEgif2
        gif3 = BLUEgif3
        gif4 = BLUEgif4
        gif5 = BLUEgif5

        die_one = BLUE1
        die_two = BLUE2
        die_three = BLUE3
        die_four = BLUE4
        die_five = BLUE5
    if selected_color=='green':
        gif1 = GREENgif1
        gif2 = GREENgif2
        gif3 = GREENgif3
        gif4 = GREENgif4
        gif5 = GREENgif5

        die_one = GREEN1
        die_two = GREEN2
        die_three = GREEN3
        die_four = GREEN4
        die_five = GREEN5
    if selected_color=='orange':
        gif1 = ORANGEgif1
        gif2 = ORANGEgif2
        gif3 = ORANGEgif3
        gif4 = ORANGEgif4
        gif5 = ORANGEgif5

        die_one = ORANGE1
        die_two = ORANGE2
        die_three = ORANGE3
        die_four = ORANGE4
        die_five = ORANGE5
    if selected_color=='pink':
        gif1 = PINKgif1
        gif2 = PINKgif2
        gif3 = PINKgif3
        gif4 = PINKgif4
        gif5 = PINKgif5

        die_one = PINK1
        die_two = PINK2
        die_three = PINK3
        die_four = PINK4
        die_five = PINK5

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
    repeated_frames = [last_frame.copy() for _ in range(200)]

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
    colors = {"Black": "black", "Blue": "blue", "Green": "green",
          "Pink": "pink", "Red": "red", "Orange": "orange"}
    col1, col2 = st.columns(2)
    with col1:
        st.title("Bindi Art by CCL, IIT Gandhinagar")    
    with col2:
        st.image("logo.png", width=150)
    # File uploader for selecting an image
    uploaded_image = st.file_uploader("Choose an image:", type=["png", "jpg", "jpeg"])

    # Slider for selecting matrix size
    matrix_size = st.slider("Select matrix size:", min_value=1, max_value=70, value=60)
    selected_color = st.selectbox("Choose a Color", list(colors.keys()))
    color_hex = colors[selected_color]

    if uploaded_image is not None:
        # Process the image
        source_image = Image.open(uploaded_image)
        processed_image, counts = process_image(source_image, matrix_size,color_hex)
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
