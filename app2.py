import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# タイトル
st.title("災害時に犬と一緒に避難できる避難所")

# データの読み込み
@st.cache_data
def load_data():
    data = pd.read_csv("shelters.csv")
    return data

data = load_data()

# ペットフレンドリーな避難所のフィルタリング
pet_friendly = st.checkbox("ペット同伴可のみ表示", value=True)
if pet_friendly:
    data = data[data["PetFriendly"] == "Yes"]

# 地図の作成
m = folium.Map(location=[35.6895, 139.6917], zoom_start=10)
for _, row in data.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"{row['Name']} ({row['Address']})",
        icon=folium.Icon(color="green" if row["PetFriendly"] == "Yes" else "red"),
    ).add_to(m)

# 地図を表示
st_folium(m, width=700, height=500)

# 詳細表示
st.write("避難所リスト:")
st.dataframe(data)
