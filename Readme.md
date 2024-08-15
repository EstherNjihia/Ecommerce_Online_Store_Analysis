# E-commerce Customer Engagement Analysis

## Problem Statement

Our e-commerce business has accumulated a large amount of transactional data, but we lack clear insights into customer engagement patterns and purchasing behaviors. We need to analyze this data to better understand our customer base and make data-driven decisions to improve customer retention and increase sales.

## Project Goals

1. Segment customers based on their purchasing behavior.
2. Identify key factors influencing customer engagement.
3. Analyze revenue trends and product performance.
4. Develop actionable recommendations for each customer segment.

## Resources Used

- **Data Source**: [Online Retail Dataset from the UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail)
- **Programming Language**: Python
- **Libraries**: pandas, numpy, matplotlib, seaborn
- **Analysis Techniques**: RFM (Recency, Frequency, Monetary) Analysis

## Analysis Process

### 1. Data Preparation
- Load the dataset into a pandas DataFrame.
- Clean the data (handle missing values, convert data types).
- Calculate basic metrics (total amount per transaction).

### 2. Customer Engagement Metrics
- Calculate Recency (time since last purchase).
- Calculate Frequency (number of purchases).
- Calculate Monetary value (total amount spent).

### 3. RFM Analysis
- Assign RFM scores to each customer.
- Segment customers based on their RFM scores.

### 4. Exploratory Data Analysis
- Analyze customer segment distribution.
- Examine relationships between Recency, Frequency, and Monetary value.
- Study monthly revenue trends.
- Identify top-selling products.

### 5. Visualization
Create visualizations to illustrate key findings:
- Customer segment distribution.
- Recency vs. Frequency scatter plot.
- Average Monetary value by segment.
- Monthly revenue trend.
- Top 10 products by sales.
- 10 Worst product by sales.

## Key Insights

### Customer Base
- The analysis covers a total of 4,338 customers.

### Customer Segmentation
- **Other**: 41.95%
- **Best Customers**: 17.54%
- **Loyal Customers**: 16.81%
- **Lost Customers**: 15.19%
- **Low-Value Customers**: 8.51%
![Customer Segments](https://github.com/EstherNjihia/Ecommerce_Online_Store_Analysis/blob/main/outputs/customer_segments.png)

### Average Monetary Value by Segment
- **Best Customers**: $6,302.18
- **Loyal Customers**: $2,323.78
- **Other**: $1,113.24
- **Lost Customers**: $504.44
- **Low-Value Customers**: $170.44

### Total Revenue
- The total revenue generated is $8,911,407.90.

### Product Performance
- **Top-selling product**: PAPER CRAFT , LITTLE BIRDIE ($168,469.60)

![Top selling Products](https://github.com/EstherNjihia/Ecommerce_Online_Store_Analysis/blob/main/outputs/top_10_products.png)

- **Worst-selling product**: PADS TO MATCH ALL CUSHIONS ($0.00)

![Worst selling Products](https://github.com/EstherNjihia/Ecommerce_Online_Store_Analysis/blob/main/outputs/worst_products.png)

## Recommendations

### Best Customers (17.54%)
- Implement a VIP program with exclusive benefits and early access to new products.
- Provide personalized service and product recommendations based on their purchase history.
- Seek their feedback on new product ideas or improvements.

### Loyal Customers (16.81%)
- Create a tiered loyalty program to encourage increased spending.
- Offer bundled products or volume discounts to increase their average order value.
- Engage them with targeted email marketing campaigns featuring complementary products.

### Lost Customers (15.19%)
- Develop a re-engagement campaign with special "welcome back" offers.
- Conduct surveys to understand reasons for their inactivity and address any issues.
- Create a win-back email series highlighting new products or improvements since their last purchase.

### Low-Value Customers (8.51%)
- Introduce lower-priced products or starter kits to encourage more frequent purchases.
- Provide educational content on product uses and benefits to increase engagement.
- Offer incentives for referring new customers to increase their value to the business.

### Other (41.95%)
- Analyze this segment further to identify potential sub-groups and tailor strategies accordingly.
- Implement a general engagement strategy with varied content and offers to appeal to different interests.
- Use A/B testing in marketing campaigns to understand what resonates with this diverse group.

### Product Strategy
- Promote the top-selling product (PAPER CRAFT , LITTLE BIRDIE) through featured listings and bundle offers.
- Review the pricing and marketing strategy for the worst-selling product (PADS TO MATCH ALL CUSHIONS) or consider discontinuing it.
- Analyze the characteristics of top-selling products to inform future product development.

### Overall Business Strategy
- Focus on moving customers up the value chain, from Low-Value to Loyal and from Loyal to Best Customers.
- Implement a customer lifecycle marketing strategy to nurture customers at each stage of their journey.
- Regularly review and adjust the RFM thresholds to ensure customer segments remain relevant as the business grows.

## Future Work

- Implement predictive models for customer churn.
- Conduct market basket analysis for product recommendations.
- Develop a dashboard for real-time monitoring of key metrics.
- Analyze seasonal trends in customer behavior and product performance.
- Investigate the impact of marketing campaigns on customer segment transitions.

## How to Use This Repository

1. Clone the repository.
2. Install required dependencies: `pip install -r requirements.txt`.
3. Run the main analysis script: `python ecommerce_analysis.py`.
4. View the generated visualizations in the `outputs` folder.
5. Read the full analysis report in `analysis_report.md`.

## Acknowledgments

- UCI Machine Learning Repository for providing the dataset.
