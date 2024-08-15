#import all the necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Read data from csv file
df = pd.read_csv('data/Retail_data_cleaned.csv')

#set the analysis date
df['Date'] = pd.to_datetime(df['Date'])
analysis_date = df['Date'].max() + pd.Timedelta(days = 1)

# Group by CustomerID and calculate metrics.
customer_metrics = df.groupby('CustomerID').agg({
    'Date': lambda x: (analysis_date -x.max()).days, #recency
    'InvoiceNo': 'count', #frequency
    'TotalAmount': 'sum', #Monetary
    })
customer_metrics.columns = ['Recency','Frequency', 'Monetary']

#Perform analysis and visualizations
#RFM Calculations
r_labels = range(4,0,-1)
f_labels = range(1,5)
m_labels = range(1,5)

customer_metrics['R_Quartile'] = pd.qcut(customer_metrics['Recency'], q=4, labels =r_labels)
customer_metrics['F_Quartile'] = pd.qcut(customer_metrics['Frequency'], q =4, labels = f_labels)
customer_metrics['M_Quartile'] = pd.qcut(customer_metrics['Monetary'],  q=4, labels =m_labels)

customer_metrics['RFM_Score'] = customer_metrics['Recency'].astype(str) + customer_metrics['Frequency'].astype(str) + customer_metrics['Monetary'].astype(str)

#Convert RFM_Score to numeric
customer_metrics['RFM_Score'] = customer_metrics['RFM_Score'].apply(lambda x: int(float(x)))

# Analyze the range of RFM scores
min_rfm_score = customer_metrics['RFM_Score'].min()
max_rfm_score = customer_metrics['RFM_Score'].max()
print(f'RFM Score ranges from {min_rfm_score} to {max_rfm_score}')

# Create a new column for segmenting customers
def segment_customers(row):
    r, f, m = int(row['R_Quartile']), int(row['F_Quartile']), int(row['M_Quartile'])
    
    if r == 4 and f >= 3 and m >= 3:
        return 'Best Customers'
    elif r >= 3 and f >= 3:
        return 'Loyal Customers'
    elif r == 1 and (f == 1 or m == 1):
        return 'Lost Customers'
    elif f == 1 and m == 1:
        return 'Low-Value Customers'
    else:
        return 'Other'
    
# Apply the segmentation function
customer_metrics['Customer_Segment'] = customer_metrics.apply(segment_customers, axis=1)

# 1. Distribution of RFM scores
plt.figure(figsize=(12, 6))
sns.countplot(x='Customer_Segment', data=customer_metrics)
plt.title('Distribution of Customer Segments')
plt.savefig('outputs/customer_segments.png')
plt.close()

#2. Recency vs Frequency scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Recency', y='Frequency', hue='Customer_Segment', data=customer_metrics)
plt.title('Recency vs Frequency by Customer Segment')
plt.savefig('outputs/recency_frequency.png.png')
plt.close()

# 3. Average Monetary Value by Customer Segment
avg_monetary = customer_metrics.groupby('Customer_Segment')['Monetary'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
avg_monetary.plot(kind='bar')
plt.title('Average Monetary Value by Customer Segment')
plt.ylabel('Average Monetary Value')
plt.savefig('outputs/avg_monetary_by_segment.png')
plt.close()

# 4. Monthly revenue trend
monthly_revenue = df.set_index('Date').resample('M')['TotalAmount'].sum()
plt.figure(figsize=(12, 6))
monthly_revenue.plot()
plt.title('Monthly Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.savefig('outputs/monthly_revenue_trend.png')
plt.close()

# 5. Top 10 products by sales
top_products = df.groupby('Description')['TotalAmount'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_products.plot(kind='bar')
plt.title('Top 10 Products by Sales')
plt.xlabel('Product Description')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('outputs/top_10_products.png')
plt.close()

# 6. Worst performing products by sales
worst_products = df.groupby('Description')['TotalAmount'].sum().sort_values(ascending=True).head(10)
plt.figure(figsize=(12, 6))
worst_products.plot(kind='bar')
plt.title('Worst Performing Products by Sales')
plt.xlabel('Product Description')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('outputs/worst_products.png')
plt.close()

# Print some key insights
print(f"Total number of customers: {len(customer_metrics)}")
print(f"Customer segment distribution:\n{customer_metrics['Customer_Segment'].value_counts(normalize=True)}")
print(f"Average monetary value by segment:\n{avg_monetary}")
print(f"Total revenue: ${customer_metrics['Monetary'].sum():,.2f}")
print(f"Top selling product: {top_products.index[0]} (${top_products.iloc[0]:,.2f})")
print(f"Worst selling product: {worst_products.index[0]} (${worst_products.iloc[0]:,.2f})")
