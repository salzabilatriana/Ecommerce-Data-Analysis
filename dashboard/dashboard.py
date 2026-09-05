import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

st.set_page_config(page_title="E-Commerce Public Dataset Dashboard", layout="wide")


@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]
    for c in date_cols:
        df[c] = pd.to_datetime(df[c], errors="coerce")
    return df


main_df = load_data()

st.title("📊 E-Commerce Public Dataset Dashboard")
st.markdown(
    "Dashboard interaktif untuk menjawab dua pertanyaan bisnis utama: "
    "**tren order & kategori produk terbaik**, serta "
    "**pengaruh keterlambatan pengiriman terhadap kepuasan pelanggan**."
)

# ---------------- Sidebar filters ----------------
st.sidebar.header("Filter Data")

valid_months = sorted(
    m for m in main_df["order_purchase_month"].dropna().unique()
    if "2016" not in m and m != "2018-09"
)
month_range = st.sidebar.select_slider(
    "Rentang Bulan (Jan 2017 - Agu 2018)",
    options=valid_months,
    value=(valid_months[0], valid_months[-1]),
)

states = sorted(main_df["customer_state"].dropna().unique())
selected_states = st.sidebar.multiselect(
    "Wilayah Pelanggan (State)", options=states, default=[]
)

categories = sorted(main_df["product_category"].dropna().unique())
selected_categories = st.sidebar.multiselect(
    "Kategori Produk", options=categories, default=[]
)

# ---------------- Apply filters ----------------
df = main_df[
    (main_df["order_purchase_month"] >= month_range[0])
    & (main_df["order_purchase_month"] <= month_range[1])
]
if selected_states:
    df = df[df["customer_state"].isin(selected_states)]
if selected_categories:
    df = df[df["product_category"].isin(selected_categories)]

# ---------------- Top-level metrics ----------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Jumlah Order", f"{df['order_id'].nunique():,}")
col2.metric("Total Revenue (BRL)", f"{df['revenue'].sum():,.0f}")

delivered = df[df["order_status"] == "delivered"].drop_duplicates("order_id")
late_pct = 100 * delivered["is_late"].mean() if len(delivered) else 0
col3.metric("% Pesanan Terlambat", f"{late_pct:.1f}%")

avg_review = delivered["review_score"].mean() if len(delivered) else float("nan")
col4.metric("Rata-rata Review Score", f"{avg_review:.2f}" if pd.notna(avg_review) else "N/A")

st.divider()

# ---------------- Question 1 ----------------
st.header("1️⃣ Tren Order Bulanan & Kategori Produk Teratas")

c1, c2 = st.columns(2)

with c1:
    monthly_orders = (
        df.drop_duplicates("order_id")
        .groupby("order_purchase_month")["order_id"]
        .nunique()
        .sort_index()
    )
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(monthly_orders.index, monthly_orders.values, marker="o", color="#2E86AB")
    ax.set_title("Tren Jumlah Order Bulanan")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Order")
    plt.xticks(rotation=60)
    plt.tight_layout()
    st.pyplot(fig)

with c2:
    top_categories = (
        df.groupby("product_category")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )
    fig2, ax2 = plt.subplots(figsize=(7, 4.5))
    colors = ["#2E86AB" if i == 0 else "#A9C7DD" for i in range(len(top_categories))]
    sns.barplot(
        x=top_categories.values,
        y=top_categories.index,
        hue=top_categories.index,
        palette=colors,
        legend=False,
        ax=ax2,
    )
    ax2.set_title("Top 5 Kategori Produk Berdasarkan Revenue")
    ax2.set_xlabel("Total Revenue (BRL)")
    ax2.set_ylabel("Kategori Produk")
    plt.tight_layout()
    st.pyplot(fig2)

st.info(
    "**Insight:** Order tumbuh signifikan sepanjang 2017 dengan lonjakan musiman "
    "di November, lalu stabil tinggi sepanjang 2018. Kategori `health_beauty`, "
    "`watches_gifts`, `bed_bath_table`, `sports_leisure`, dan `computers_accessories` "
    "menyumbang revenue terbesar."
)

st.divider()

# ---------------- Question 2 ----------------
st.header("2️⃣ Keterlambatan Pengiriman vs Kepuasan Pelanggan")

c3, c4 = st.columns([1, 1])

with c3:
    if len(delivered):
        delay_summary = delivered.groupby("is_late")["review_score"].mean()
        labels = ["Tepat Waktu", "Terlambat"]
        values = [
            delay_summary.get(False, 0),
            delay_summary.get(True, 0),
        ]
        fig3, ax3 = plt.subplots(figsize=(6, 4.5))
        bars = ax3.bar(labels, values, color=["#2E86AB", "#E63946"])
        ax3.set_title("Rata-rata Review Score: Tepat Waktu vs Terlambat")
        ax3.set_ylabel("Rata-rata Review Score")
        ax3.set_ylim(0, 5)
        for bar, val in zip(bars, values):
            ax3.text(
                bar.get_x() + bar.get_width() / 2,
                val + 0.05,
                f"{val:.2f}",
                ha="center",
                fontweight="bold",
            )
        plt.tight_layout()
        st.pyplot(fig3)
    else:
        st.warning("Tidak ada data pesanan 'delivered' pada filter saat ini.")

with c4:
    if len(delivered):
        delay_by_state = (
            delivered[delivered["is_late"]]
            .groupby("customer_state")["order_id"]
            .count()
            .sort_values(ascending=False)
            .head(10)
        )
        fig4, ax4 = plt.subplots(figsize=(6, 4.5))
        sns.barplot(
            x=delay_by_state.values,
            y=delay_by_state.index,
            hue=delay_by_state.index,
            palette="Reds_r",
            legend=False,
            ax=ax4,
        )
        ax4.set_title("Top 10 State dengan Pesanan Terlambat Terbanyak")
        ax4.set_xlabel("Jumlah Pesanan Terlambat")
        ax4.set_ylabel("State")
        plt.tight_layout()
        st.pyplot(fig4)

st.info(
    "**Insight:** Pesanan yang terlambat memiliki rata-rata review score jauh lebih "
    "rendah dibandingkan pesanan tepat waktu, menunjukkan keterlambatan pengiriman "
    "berdampak besar terhadap kepuasan pelanggan."
)

st.divider()
st.caption(
    "Sumber data: E-Commerce Public Dataset (Olist). Dibuat untuk proyek analisis data. @salzabilatrianasaid"
)
