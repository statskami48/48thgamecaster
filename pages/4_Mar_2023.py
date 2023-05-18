import streamlit as st
import pandas as pd
from streamlit_extras.image_in_tables import table_with_images


df = pd.DataFrame(
        [
            #Name Kami Oshi Cookies Likes
            ["Lookked", "1,200,333", 1155027, 34713051, 331002277],
            ["Jingjing", 60632, 790040, 3070447, 212558178],
            ["Champoo", 9536, 422931, 19852167, 145934619],
            ["Emmy", 17848, 359891, 8826585, 1379974505],
            ["Kaofrang", 9860, 178245, 1699369, 32969875],
        ],
    columns=[
            "Name",
            "Kami",
            "Oshi",
            "Cookies",
            "Likes",
        ],
)

    # Create a list named country to store all the image paths
member = [
        "https://img.bnk48cdn.net/others/cgm48-6th-single-profile-square/v2/Lookked.png",
        "https://img.bnk48cdn.net/others/cgm48-6th-single-profile-square/v2/Jingjing.png",
        "https://img.bnk48cdn.net/others/cgm48-6th-single-profile-square/v2/Champoo.png",
        "https://www.bnk48.com/data/Members/99/s/20230228042740cjnyz7.png",
        "https://www.bnk48.com/data/Members/86/s/20230228050544ahptx3.png",
    ]
    # Assigning the new list as a new column of the dataframe
df["Photo"] = member

#st.caption("Input dataframe")
#st.write(df)
df_html = table_with_images(df=df, url_columns=("Photo",))
st.caption("Output")
st.markdown(df_html, unsafe_allow_html=True)