# Superstore Sales Data Analysis

A comprehensive analysis of retail sales data using Python and pandas to uncover business insights.

## Project Overview

This project analyzes a retail superstore dataset containing 9,800+ transactions from 2015-2018. The analysis focuses on:
- Sales performance by product category and region
- Customer segmentation analysis
- Time-based sales trends
- Product performance metrics

## Key Findings

1. **Total Revenue**: $2.26 million across 4 years
2. **Top Performing Category**: Technology ($827,456)
3. **Best Region**: West region ($710,220)
4. **Customer Insights**: Consumer segment drives 51% of total sales
5. **Growth Trend**: Sales increased from $479K (2015) to $722K (2018) - 50% growth

## Technologies Used

- **Python 3.x**
- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualization
- **seaborn**: Statistical visualizations

## Analysis Performed

### 1. Data Cleaning
- Checked for missing values (11 missing postal codes found)
- Removed duplicate entries
- Converted date columns to proper datetime format
- Created additional time-based columns (Year, Month, Quarter)

### 2. Exploratory Data Analysis
- Sales breakdown by Category, Region, and Customer Segment
- Identified top 10 products and sub-categories
- Calculated average order value ($459.48)
- Analyzed sales trends over time

### 3. Visualizations Created
- Bar chart: Total Sales by Category
- Bar chart: Total Sales by Region
- Line chart: Monthly Sales Trend (2015-2018)
- Pie chart: Sales Distribution by Customer Segment

## Key Insights

**Sales by Category:**
- Technology leads with $827K (36.6%)
- Furniture: $729K (32.2%)
- Office Supplies: $705K (31.2%)

**Regional Performance:**
- West: $710K (best performing)
- East: $670K
- Central: $493K
- South: $389K (opportunity for growth)

**Customer Segments:**
- Consumer: $1.15M (51%)
- Corporate: $688K (30%)
- Home Office: $425K (19%)

**Top Product Categories:**
- Phones ($328K) and Chairs ($323K) are the bestsellers
- Technology sub-categories dominate top sales

**Trend Analysis:**
- Clear upward sales trend from 2015 to 2018
- Seasonal peaks visible in November/December (holiday season)
- Q4 consistently strongest quarter

## How to Run

1. Install required packages:
```bash
pip install pandas matplotlib seaborn
```

2. Run the analysis:
```bash
python sales_analysis.py
```

3. View generated visualizations in the output directory

## Dataset

- **Source**: Superstore sales data (Kaggle)
- **Size**: 9,800 rows, 18 columns
- **Time Period**: January 2015 - December 2018
- **Columns**: Order details, customer info, product data, sales amounts, geographic data

## Project Structure

```
├── sales_analysis.py          # Main analysis script
├── README.md                   # Project documentation
├── 1772112186394_train.csv   # Dataset (not included in repo)
└── visualizations/             # Generated charts
    ├── sales_by_category.png
    ├── sales_by_region.png
    ├── sales_trend.png
    └── sales_by_segment.png
```

## Future Improvements

- Add profit margin analysis
- Customer lifetime value calculation
- Predictive modeling for sales forecasting
- Interactive dashboard using Plotly or Tableau
- Geographic mapping of sales distribution

## Author

**Sandeep Molleti**
- MSc Computer Science Student
- Email: sandeep.molleti22@law.ac.uk
- LinkedIn:

## License

This project is open source and available for educational purposes.

---

*Project completed as part of data analytics portfolio development - February 2026*
