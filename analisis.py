import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_venn import venn2

# Data penjualan
data = {
    'No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Tanggal Penjualan': ['2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14'],
    'Produk': ['Laptop', 'Handphone', 'Laptop', 'Handphone', 'Laptop', 'Handphone', 'Laptop', 'Handphone', 'Laptop', 'Handphone'],
    'Merek': ['Dell', 'Samsung', 'HP', 'Apple', 'Lenovo', 'Xiaomi', 'Asus', 'Oppo', 'Acer', 'Vivo'],
    'Model': ['Inspiron 15', 'Galaxy S21', 'Pavilion 14', 'iPhone 13', 'ThinkPad X1', 'Mi 11', 'ZenBook 13', 'Reno 5', 'Aspire 5', 'V21'],
    'Harga (IDR)': [9000000, 12000000, 8500000, 15000000, 12500000, 10000000, 11000000, 7500000, 7800000, 8200000],
    'Jumlah Terjual': [5, 8, 3, 10, 2, 7, 4, 6, 5, 9]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Harga (IDR)', y='Jumlah Terjual', hue='Produk', style='Produk', s=100, palette='bright')
plt.title('Scatterplot Harga vs Jumlah Terjual')
plt.xlabel('Harga (IDR)')
plt.ylabel('Jumlah Terjual')
plt.legend(title='Produk')
plt.grid(True)
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df, x='Harga (IDR)', hue='Produk', multiple='stack', palette='bright', bins=10)
plt.title('Histogram Harga Produk')
plt.xlabel('Harga (IDR)')
plt.ylabel('Frekuensi')
plt.show()

# Diagram Venn
plt.figure(figsize=(8, 8))
venn2(subsets=(len(df[df['Produk'] == 'Laptop']), len(df[df['Produk'] == 'Handphone']), 0), set_labels=('Laptop', 'Handphone'))
plt.title('Diagram Venn Penjualan Produk')
plt.show()

# Pie Chart
jumlah_terjual = df.groupby('Produk')['Jumlah Terjual'].sum()
plt.figure(figsize=(8, 8))
colors = sns.color_palette('bright')
plt.pie(jumlah_terjual, labels=jumlah_terjual.index, autopct='%1.1f%%', colors=colors)
plt.title('Pie Chart Jumlah Terjual per Produk')
plt.show()

# Bar Chart
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Merek', y='Jumlah Terjual', hue='Produk', palette='bright')
plt.title('Bar Chart Jumlah Terjual per Merek')
plt.xlabel('Merek')
plt.ylabel('Jumlah Terjual')
plt.legend(title='Produk')
plt.xticks(rotation=45)
plt.show()
