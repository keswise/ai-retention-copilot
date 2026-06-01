import streamlit as st
import pandas as pd
import plotly.express as px

from src.ai_recommender import get_recommendation

from src.content_generator import (
    generate_push,
    generate_whatsapp,
    generate_email
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Retention Copilot",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv(
    "data/segmented_users.csv"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🤖 AI Retention Copilot")

st.markdown(
    """
    Analyze customer segments, identify churn risks,
    generate AI retention strategies and create campaign content.
    """
)

st.divider()

# --------------------------------------------------
# KPIs
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Users",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "Total Revenue",
        f"₹{int(df['revenue'].sum()):,}"
    )

with col3:
    st.metric(
        "Average Revenue",
        f"₹{int(df['revenue'].mean()):,}"
    )

st.divider()

# --------------------------------------------------
# CHARTS
# --------------------------------------------------

chart1, chart2 = st.columns(2)

with chart1:

    st.subheader(
        "Customer Segment Distribution"
    )

    pie_fig = px.pie(
        df,
        names="segment_name",
        hole=0.4
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

with chart2:

    st.subheader(
        "Revenue Distribution"
    )

    revenue_fig = px.histogram(
        df,
        x="revenue",
        color="segment_name",
        nbins=30
    )

    st.plotly_chart(
        revenue_fig,
        use_container_width=True
    )

st.divider()

# --------------------------------------------------
# SEGMENT OVERVIEW
# --------------------------------------------------

st.subheader(
    "Segment Overview"
)

segment_summary = (
    df.groupby("segment_name")
      .agg(
          Users=("user_id", "count"),
          Avg_Revenue=("revenue", "mean"),
          Avg_Sessions=("sessions", "mean"),
          Avg_Last_Login_Days=("last_login_days", "mean")
      )
      .round(2)
)

st.dataframe(
    segment_summary,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# SEGMENT SELECTOR
# --------------------------------------------------

st.subheader(
    "🧠 AI Retention Strategy Generator"
)

segment = st.selectbox(
    "Select Customer Segment",
    sorted(df["segment_name"].unique())
)

# --------------------------------------------------
# STRATEGY GENERATION
# --------------------------------------------------

if st.button(
    "Generate Strategy"
):

    with st.spinner(
        "Generating strategy..."
    ):

        recommendation = get_recommendation(
            segment
        )

    st.success(
        "Strategy Generated Successfully"
    )

    st.markdown(
        recommendation
    )

st.divider()

# --------------------------------------------------
# CAMPAIGN GENERATOR
# --------------------------------------------------

st.subheader(
    "📢 AI Campaign Content Generator"
)

col1, col2, col3 = st.columns(3)

# ---------------- PUSH ----------------

with col1:

    if st.button(
        "Generate Push Notification"
    ):

        with st.spinner(
            "Generating push copy..."
        ):

            push = generate_push(
                segment
            )

        st.text_area(
            "Push Notification",
            value=push,
            height=150
        )

# ---------------- WHATSAPP ----------------

with col2:

    if st.button(
        "Generate WhatsApp Copy"
    ):

        with st.spinner(
            "Generating WhatsApp copy..."
        ):

            whatsapp = generate_whatsapp(
                segment
            )

        st.text_area(
            "WhatsApp Copy",
            value=whatsapp,
            height=250
        )

# ---------------- EMAIL ----------------

with col3:

    if st.button(
        "Generate Email Campaign"
    ):

        with st.spinner(
            "Generating email..."
        ):

            email = generate_email(
                segment
            )

        st.text_area(
            "Email Campaign",
            value=email,
            height=350
        )

st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "Built with Python, Streamlit, Machine Learning and OpenAI"
)