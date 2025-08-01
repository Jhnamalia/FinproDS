import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(layout="wide")

st.title("📊 Visualisasi EDA Review Aplikasi Google Play Store")
st.markdown("_Explore the distribution of ratings, installs, sentiment, and more._")

# Load dataset
df = pd.read_csv("data/reviews.csv")

# Pastel soft color palette
pastel_soft = ['#FFB5E8', '#B5EAD7', '#C7CEEA', '#FFDAC1', '#E2F0CB']

# Quick summary metrics
colA, colB, colC = st.columns(3)
colA.metric("Total Apps", f"{df.shape[0]:,}")
colB.metric("Avg Rating", f"{df['rating'].mean():.2f} ⭐")
colC.metric("Most Common Category", df['category'].mode()[0])

st.markdown("---")

# Tabs
tabs = st.tabs(["Distribusi Umum", "Tipe Aplikasi", "Sentimen dan Ulasan"])

# ======================= TAB 1 =======================
with tabs[0]:
    st.header("Distribusi Umum")
    st.info("📌 Sebagian besar aplikasi gratis dan memiliki rating tinggi; distribusi review & install miring ke kanan.")

    col1, col2 = st.columns(2)
    with col1:
        fig = px.histogram(df, x="rating", nbins=20, title="Distribusi Rating Aplikasi",
                           color_discrete_sequence=pastel_soft)
        fig.update_traces(marker_line_color="black", marker_line_width=1)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("🎯 Mayoritas aplikasi memiliki rating di atas 4.0, menunjukkan dominasi aplikasi yang cukup disukai pengguna.")
    with col2:
        fig = px.histogram(df, x="price", color="type", nbins=30, title="Distribusi Harga Aplikasi",
                           color_discrete_sequence=pastel_soft)
        fig.update_traces(marker_line_color="black", marker_line_width=1)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("💰 Sebagian besar aplikasi di Play Store bersifat gratis, terlihat dari banyaknya harga di angka 0.")


    col3, col4 = st.columns(2)
    with col3:
        fig = px.histogram(df, x="reviews_log", nbins=30, title="Distribusi Jumlah Review (log)",
                           color_discrete_sequence=pastel_soft)
        fig.update_traces(marker_line_color="black", marker_line_width=1)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("💬 Jumlah review sangat bervariasi, namun sebagian besar aplikasi memiliki jumlah review yang relatif rendah.")
    with col4:
        fig = px.histogram(df, x="installs_log", nbins=30, title="Distribusi Jumlah Install (log)",
                           color_discrete_sequence=pastel_soft)
        fig.update_traces(marker_line_color="black", marker_line_width=1)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("📈 Jumlah install sangat bervariasi, namun sebagian besar aplikasi memiliki jumlah install yang relatif tinggi.")


# ======================= TAB 2 =======================
with tabs[1]:
    st.header("Tipe Aplikasi (Free vs Paid)")
    st.info("📌 Mayoritas aplikasi gratis, dan gratis biasanya punya jumlah install lebih banyak.")

    # Interaktif filter
    st.subheader("🔍 Filter Interaktif")
    category_list = sorted(df['category'].dropna().unique())
    type_list = df['type'].dropna().unique().tolist()

    selected_type = st.selectbox("Pilih Tipe Aplikasi:", ["All"] + type_list)
    selected_category = st.selectbox("Pilih Kategori Aplikasi:", ["All"] + category_list)

    df_filtered = df.copy()
    if selected_type != "All":
        df_filtered = df_filtered[df_filtered["type"] == selected_type]
    if selected_category != "All":
        df_filtered = df_filtered[df_filtered["category"] == selected_category]

    st.markdown(f"✅ Menampilkan **{len(df_filtered):,}** aplikasi sesuai filter.")

    col1, col2 = st.columns(2)
    with col1:
        fig = px.histogram(df_filtered, x="type", color="type", title="Distribusi Tipe Aplikasi",
                           color_discrete_sequence=pastel_soft)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("🆓 Aplikasi gratis mendominasi jumlah keseluruhan aplikasi di Play Store.")
    with col2:
        fig = px.box(df_filtered, x="type", y="installs_log", color="type", title="Jumlah Install per Tipe Aplikasi (log)",
                     color_discrete_sequence=pastel_soft)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("📈 Aplikasi gratis cenderung memiliki jumlah instalasi lebih tinggi dibanding aplikasi berbayar.")

    col3, col4 = st.columns(2)
    with col3:
        fig = px.box(df_filtered, x="type", y="rating", color="type", title="Rating berdasarkan Tipe Aplikasi",
                     color_discrete_sequence=pastel_soft)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("🆓 Aplikasi gratis mendominasi jumlah keseluruhan aplikasi di Play Store.")
    with col4:
        top10_categories = df_filtered['category'].value_counts().nlargest(10).index
        df_top10 = df_filtered[df_filtered['category'].isin(top10_categories)]
        fig = px.histogram(df_top10, x="category", color="category", title="Jumlah Aplikasi per Kategori (Top 10)",
                           color_discrete_sequence=pastel_soft)
        fig.update_xaxes(categoryorder="total descending")
        st.plotly_chart(fig, use_container_width=True)
        st.caption("🏆 Kategori 'Tools', 'Entertainment', dan 'Productivity' menjadi yang paling banyak tersedia di Play Store.")

# ======================= TAB 3 =======================
with tabs[2]:
    st.header("Sentimen dan Ulasan Pengguna")
    st.info("📌 Sentimen positif mendominasi, dan rating lebih tinggi umumnya muncul pada review positif.")

    st.subheader("🔍 Filter Sentimen (Opsional)")
    sentiment_options = df['sentiment'].dropna().unique().tolist()
    selected_sentiment = st.selectbox("Pilih Sentimen:", ["All"] + sentiment_options)

    df_sentiment = df.copy()
    if selected_sentiment != "All":
        df_sentiment = df[df["sentiment"] == selected_sentiment]

    st.markdown(f"✅ Menampilkan **{len(df_sentiment):,}** review dengan sentimen {selected_sentiment if selected_sentiment != 'All' else 'apapun'}.")

    col1, col2 = st.columns(2)
    with col1:
        fig = px.histogram(df_sentiment, x="sentiment", color="sentiment", title="Distribusi Sentimen Pengguna",
                           category_orders={"sentiment": ["Negative", "Neutral", "Positive"]},
                           color_discrete_sequence=pastel_soft)
        fig.update_traces(marker_line_color="black", marker_line_width=1)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("😊 Sentimen pengguna terhadap aplikasi didominasi oleh sentimen positif, menunjukkan tingkat kepuasan yang cukup tinggi.")
    with col2:
        fig = px.box(df_sentiment, x="sentiment", y="rating", color="sentiment", title="Rating berdasarkan Sentimen",
                     color_discrete_sequence=pastel_soft)
        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        fig = px.histogram(df_sentiment, x="sentiment_polarity", color="sentiment", nbins=30,
                           title="Distribusi Sentiment Polarity",
                           color_discrete_sequence=pastel_soft)
        fig.update_traces(marker_line_color="black", marker_line_width=1)
        st.plotly_chart(fig, use_container_width=True)
    with col4:
        fig = px.histogram(df_sentiment, x="sentiment_subjectivity", color="sentiment", nbins=30,
                           title="Distribusi Sentiment Subjectivity",
                           color_discrete_sequence=pastel_soft)
        fig.update_traces(marker_line_color="black", marker_line_width=1)
        st.plotly_chart(fig, use_container_width=True)

    col5, col6 = st.columns(2)
    with col5:
        fig = px.scatter(df_sentiment, x="sentiment_polarity", y="rating", color="sentiment",
                         title="Polarity vs Rating", color_discrete_sequence=pastel_soft,
                         hover_data=["app", "sentiment_subjectivity"])
        st.plotly_chart(fig, use_container_width=True)
        st.caption("📊 Semakin tinggi polaritas ulasan, cenderung berkorelasi dengan rating aplikasi yang lebih tinggi.")
    with col6:
        fig = px.scatter(df_sentiment, x="reviews_log", y="rating", color="sentiment",
                         title="Jumlah Review vs Rating", color_discrete_sequence=pastel_soft,
                         hover_data=["app", "sentiment_polarity"])
        st.plotly_chart(fig, use_container_width=True)
        st.caption("🔁 Aplikasi dengan rating tinggi tidak selalu memiliki jumlah review yang banyak, menunjukkan popularitas tidak selalu berbanding lurus dengan kualitas.")

st.markdown("---")
st.caption("Made by Jihan Amalia")
