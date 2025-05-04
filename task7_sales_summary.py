import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

csv_file = 'sales_data.csv'
df = pd.read_csv(csv_file)

conn = sqlite3.connect('sales_data.db')
df.to_sql('sales', conn, if_exists='replace', index=False)


query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
summary_df = pd.read_sql_query(query, conn)


print("Sales Summary:\n")
print(summary_df)


summary_df.plot(kind='bar', x='product', y='revenue', color='skyblue')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()


plt.savefig("sales_chart.png")
plt.show()


conn.close()
