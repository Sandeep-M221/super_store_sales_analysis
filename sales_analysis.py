"""
Superstore Sales Data Analysis
Project by: Sandeep Molleti
Date: February 2026

This project analyzes retail sales data to uncover insights about:
- Sales performance by category and region
- Customer segments
- Time-based trends
- Product performance
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("="*60)
print("SUPERSTORE SALES DATA ANALYSIS")
print("="*60)
print()

# ============================================================================
# STEP 1: LOAD THE DATA
# ============================================================================
print("Step 1: Loading data...")
df = pd.read_csv('/mnt/user-data/uploads/1772112186394_train.csv')
print(f"✓ Data loaded successfully: {len(df)} rows, {len(df.columns)} columns")
print()

# ============================================================================
# STEP 2: INITIAL EXPLORATION
# ============================================================================
print("Step 2: Initial Data Exploration")
print("-" * 60)
print("First few rows:")
print(df.head())
print()

print("Dataset Info:")
print(df.info())
print()

print("Statistical Summary:")
print(df.describe())
print()

# ============================================================================
# STEP 3: DATA CLEANING
# ============================================================================
print("Step 3: Data Cleaning")
print("-" * 60)

# Check for missing values
print("Missing values per column:")
missing = df.isnull().sum()
print(missing[missing > 0] if missing.sum() > 0 else "No missing values found!")
print()

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"Duplicate rows: {duplicates}")
if duplicates > 0:
    df = df.drop_duplicates()
    print(f"✓ Removed {duplicates} duplicate rows")
print()

# Convert date columns to datetime
print("Converting date columns to datetime format...")
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')
print("✓ Date conversion complete")
print()

# Create additional time-based columns for analysis
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Quarter'] = df['Order Date'].dt.quarter
print("✓ Created Year, Month, Quarter columns")
print()

# ============================================================================
# STEP 4: DATA ANALYSIS
# ============================================================================
print("Step 4: Data Analysis")
print("-" * 60)

# Analysis 1: Sales by Category
print("\n1. Total Sales by Category:")
sales_by_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(sales_by_category)
print()

# Analysis 2: Sales by Region
print("2. Total Sales by Region:")
sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(sales_by_region)
print()

# Analysis 3: Sales by Customer Segment
print("3. Total Sales by Customer Segment:")
sales_by_segment = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)
print(sales_by_segment)
print()

# Analysis 4: Top 10 Products by Sales
print("4. Top 10 Products by Sales:")
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products)
print()

# Analysis 5: Sales Trends Over Time
print("5. Sales by Year:")
sales_by_year = df.groupby('Year')['Sales'].sum()
print(sales_by_year)
print()

# Analysis 6: Average Order Value
avg_order_value = df.groupby('Order ID')['Sales'].sum().mean()
print(f"6. Average Order Value: ${avg_order_value:.2f}")
print()

# Analysis 7: Best performing Sub-Categories
print("7. Top 10 Sub-Categories by Sales:")
top_subcategories = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_subcategories)
print()

# ============================================================================
# STEP 5: VISUALIZATIONS
# ============================================================================
print("Step 5: Creating Visualizations")
print("-" * 60)

# Visualization 1: Sales by Category
plt.figure(figsize=(10, 6))
sales_by_category.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title('Total Sales by Category', fontsize=16, fontweight='bold')
plt.xlabel('Category', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('/home/claude/sales_by_category.png', dpi=300, bbox_inches='tight')
print("✓ Created: sales_by_category.png")

# Visualization 2: Sales by Region
plt.figure(figsize=(10, 6))
sales_by_region.plot(kind='bar', color=['#d62728', '#9467bd', '#8c564b', '#e377c2'])
plt.title('Total Sales by Region', fontsize=16, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/home/claude/sales_by_region.png', dpi=300, bbox_inches='tight')
print("✓ Created: sales_by_region.png")

# Visualization 3: Sales Trend Over Time (Monthly)
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
plt.figure(figsize=(14, 6))
monthly_sales.plot(kind='line', marker='o', linewidth=2, markersize=4)
plt.title('Monthly Sales Trend', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/home/claude/sales_trend.png', dpi=300, bbox_inches='tight')
print("✓ Created: sales_trend.png")

# Visualization 4: Sales Distribution by Customer Segment
plt.figure(figsize=(10, 6))
df.groupby('Segment')['Sales'].sum().plot(kind='pie', autopct='%1.1f%%', startangle=90,
                                           colors=['#ff9999', '#66b3ff', '#99ff99'])
plt.title('Sales Distribution by Customer Segment', fontsize=16, fontweight='bold')
plt.ylabel('')
plt.tight_layout()
plt.savefig('/home/claude/sales_by_segment.png', dpi=300, bbox_inches='tight')
print("✓ Created: sales_by_segment.png")

print()
print("="*60)
print("ANALYSIS COMPLETE!")
print("="*60)

# ============================================================================
# STEP 6: KEY INSIGHTS SUMMARY
# ============================================================================
print("\nKEY INSIGHTS:")
print("-" * 60)
print(f"1. Total Revenue: ${df['Sales'].sum():,.2f}")
print(f"2. Total Orders: {df['Order ID'].nunique():,}")
print(f"3. Total Customers: {df['Customer ID'].nunique():,}")
print(f"4. Average Order Value: ${avg_order_value:.2f}")
print(f"5. Most Profitable Category: {sales_by_category.index[0]} (${sales_by_category.iloc[0]:,.2f})")
print(f"6. Best Region: {sales_by_region.index[0]} (${sales_by_region.iloc[0]:,.2f})")
print(f"7. Top Customer Segment: {sales_by_segment.index[0]} (${sales_by_segment.iloc[0]:,.2f})")
print(f"8. Date Range: {df['Order Date'].min().strftime('%Y-%m-%d')} to {df['Order Date'].max().strftime('%Y-%m-%d')}")
print()

print("All visualizations saved in the current directory!")
print("Project complete! ✓")
