# E-Commerce Public Dataset — Data Analysis Project

A data analysis project using the **E-Commerce Public Dataset (Olist Brazilian E-Commerce)**. This project covers the complete data analysis process (data wrangling, EDA, visualization, through to conclusions & recommendations) as well as an interactive dashboard built with **Streamlit**.

## Directory Structure

```
submission
├───dashboard
│   ├───main_data.csv       # cleaned & merged data, used by the dashboard
│   └───dashboard.py        # Streamlit application
├───data                    # raw dataset (raw CSV)
│   ├───customers_dataset.csv
│   ├───order_items_dataset.csv
│   ├───order_payments_dataset.csv
│   ├───order_reviews_dataset.csv
│   ├───orders_dataset.csv
│   ├───product_category_name_translation.csv
│   ├───products_dataset.csv
│   └───sellers_dataset.csv
├───notebook.ipynb          # complete data analysis notebook (already executed)
├───README.md
├───requirements.txt
└───url.txt
```

## Business Questions

1. What is the monthly order trend from January 2017 to August 2018, and which 5 product categories contributed the highest revenue during that period?
2. What is the difference in average review score between orders that were delivered late versus orders that were delivered on time?

The complete answers along with the analysis process can be found in `notebook.ipynb`.

## Environment Setup

It is recommended to use a virtual environment first.

**Using venv (pip):**
```
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Using Anaconda:**
```
conda create --name ecommerce-analysis python=3.11
conda activate ecommerce-analysis
pip install -r requirements.txt
```

## Running the Notebook

```
jupyter notebook notebook.ipynb
```
The notebook reads the raw dataset from the `data/` folder (relative path `data/`), so run Jupyter from inside the `submission/` folder.

## Running the Dashboard (Streamlit)

The dashboard reads the cleaned `main_data.csv` (produced by the notebook process), so run it from inside the `dashboard/` folder:

```
cd dashboard
streamlit run dashboard.py
```

Once running, open your browser to the address shown in the terminal (default: `http://localhost:8501`).

### Dashboard Features
- Interactive filters: month range, customer region (state), and product category.
- Key metrics summary: number of orders, total revenue, percentage of late orders, average review score.
- Visualization of monthly order trends & top 5 product categories by revenue.
- Visualization comparing review scores for on-time vs. late orders, plus the top 10 regions with the most late orders.

## Data Source

E-Commerce Public Dataset (Olist Brazilian E-Commerce), uploaded for a data analysis project submission.

