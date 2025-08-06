import streamlit as st
from PIL import Image, ImageFont
import handright

# Load the font
FONT_PATH = "Grandrainbowdemo-BWpWd.otf"
font = ImageFont.truetype(FONT_PATH, 32)

# Create template (no padding parameter used)
background = Image.new("RGB", (800, 600), "white")
template = handright.Template(
    background=background,
    font=font,
    line_spacing=50,
    fill=0,
    word_spacing=1.2,
    line_spacing_sigma=1.0,
    word_spacing_sigma=0.1,
    perturb_x_sigma=2,
    perturb_y_sigma=2,
    perturb_theta_sigma=0.01
)

# Streamlit app
st.title("🖋️ Typed to Handwritten Text Generator")
text = st.text_area("Enter your text")

if st.button("Generate"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        images = handright.handwrite(text, template)
        for img in images:
            st.image(img)
