import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Crop Production data.csv')

# Convert Crop_Year to datetime
df['Crop_Year'] = pd.to_datetime(df['Crop_Year'], format='%Y')

# Set the style for seaborn
sns.set(style='whitegrid')

# Trend Analysis
# 1. Total Crop Production by Year
total_production_by_year = df.groupby(df['Crop_Year'].dt.year)['Production'].sum().reset_index()
print("Total Crop Production by Year:\n", total_production_by_year)
plt.figure(figsize=(12, 6))
sns.lineplot(data=total_production_by_year, x='Crop_Year', y='Production', marker='o')
plt.title('Total Crop Production by Year')
plt.xlabel('Year')
plt.ylabel('Total Production')
plt.xticks(rotation=45)
plt.show()

# 2. Annual Growth Rate
total_production_by_year['Growth_Rate'] = total_production_by_year['Production'].pct_change() * 100
print("Annual Growth Rate of Crop Production:\n", total_production_by_year)
plt.figure(figsize=(12, 6))
sns.lineplot(data=total_production_by_year, x='Crop_Year', y='Growth_Rate', marker='o')
plt.title('Annual Growth Rate of Crop Production')
plt.xlabel('Year')
plt.ylabel('Growth Rate (%)')
plt.xticks(rotation=45)
plt.show()

# 3. Trend Line for Crop Production
plt.figure(figsize=(12, 6))
sns.regplot(data=total_production_by_year, x='Crop_Year', y='Production', order=1, ci=None, marker='o')
plt.title('Trend Line for Crop Production')
plt.xlabel('Year')
plt.ylabel('Total Production')
plt.xticks(rotation=45)
plt.show()

# Crop-wise Analysis
# 4. Total Production by Crop
total_production_by_crop = df.groupby('Crop')['Production'].sum().reset_index()
print("Total Production by Crop:\n", total_production_by_crop)
plt.figure(figsize=(36, 24))
sns.barplot(data=total_production_by_crop, x='Production', y='Crop', palette='viridis')
plt.title('Total Production by Crop')
plt.xlabel('Total Production')
plt.ylabel('Crop')
plt.show()

# 5. Average Area Cultivated by Crop
average_area_by_crop = df.groupby('Crop')['Area'].mean().reset_index()
print("Average Area Cultivated by Crop:\n", average_area_by_crop)
plt.figure(figsize=(36, 24))
sns.barplot(data=average_area_by_crop, x='Area', y='Crop', palette='viridis')
plt.title('Average Area Cultivated by Crop')
plt.xlabel('Average Area')
plt.ylabel('Crop')
plt.show()

# 6. Yield per Crop
df['Yield'] = df['Production'] / df['Area']
yield_by_crop = df.groupby('Crop')['Yield'].mean().reset_index()
print("Yield per Crop:\n", yield_by_crop)
plt.figure(figsize=(36, 24))
sns.barplot(data=yield_by_crop, x='Yield', y='Crop', palette='viridis')
plt.title('Yield per Crop')
plt.xlabel('Yield (Production/Area)')
plt.ylabel('Crop')
plt.show()

# 7. Crop Production Trends
crop_production_trends = df.groupby([df['Crop_Year'].dt.year, 'Crop'])['Production'].sum().reset_index()
print("Crop Production Trends:\n", crop_production_trends)
plt.figure(figsize=(14, 8))
sns.lineplot(data=crop_production_trends, x='Crop_Year', y='Production', hue='Crop', marker='o')
plt.title('Crop Production Trends')
plt.xlabel('Year')
plt.ylabel('Total Production')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.show()

# State-wise Comparison
# 8. Total Production by State
total_production_by_state = df.groupby('State_Name')['Production'].sum().reset_index()
print("Total Production by State:\n", total_production_by_state)
plt.figure(figsize=(12, 6))
sns.barplot(data=total_production_by_state, x='Production', y='State_Name', palette='viridis')
plt.title('Total Production by State')
plt.xlabel('Total Production')
plt.ylabel('State')
plt.show()

# 9. Highest and Lowest producing states 
state_crop_production = df.groupby(['State_Name', 'Crop'])['Production'].sum()
max_production_states = state_crop_production.groupby('Crop').idxmax()
min_production_states = state_crop_production.groupby('Crop').idxmin()
print("States with highest production for each crop:")
print(max_production_states)
print("\nStates with lowest production for each crop:")
print(min_production_states)

# 10. Production Efficiency by State
production_efficiency_by_state = df.groupby('State_Name').apply(lambda x: x['Production'].sum() / x['Area'].sum()).reset_index(name='Efficiency')
print("Production Efficiency by State:\n", production_efficiency_by_state)
plt.figure(figsize=(12, 6))
sns.barplot(data=production_efficiency_by_state, x='Efficiency', y='State_Name', palette='viridis')
plt.title('Production Efficiency by State')
plt.xlabel('Production Efficiency (Production/Area)')
plt.ylabel('State')
plt.show()

# 11. Top Producing States for Specific Crops
top_producing_states = df.groupby(['Crop', 'State_Name'])['Production'].sum().reset_index().sort_values(by='Production', ascending=False)
print("Top Producing States for Specific Crops:\n", top_producing_states)
plt.figure(figsize=(14, 8))
sns.barplot(data=top_producing_states, x='Production', y='State_Name', hue='Crop', palette='viridis')
plt.title('Top Producing States for Specific Crops')
plt.xlabel('Total Production')
plt.ylabel('State')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Seasonal Analysis
# 12. Total Production by Season
total_production_by_season = df.groupby('Season')['Production'].sum().reset_index()
print("Total Production by Season:\n", total_production_by_season)
plt.figure(figsize=(12, 6))
sns.barplot(data=total_production_by_season, x='Production', y='Season', palette='viridis')
plt.title('Total Production by Season')
plt.xlabel('Total Production')
plt.ylabel('Season')
plt.show()

# 13. Crop-wise Production by Season
crop_production_by_season = df.groupby(['Season', 'Crop'])['Production'].sum().reset_index()
print("Crop-wise Production by Season:\n", crop_production_by_season)
plt.figure(figsize=(14, 8))
sns.barplot(data=crop_production_by_season, x='Production', y='Season', hue='Crop', palette='viridis')
plt.title('Crop-wise Production by Season')
plt.xlabel('Total Production')
plt.ylabel('Season')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# 14. Seasonal Yield Efficiency
yield_by_season = df.groupby('Season').apply(lambda x: x['Production'].sum() / x['Area'].sum()).reset_index(name='Yield_Efficiency')
print("Seasonal Yield Efficiency:\n", yield_by_season)
plt.figure(figsize=(12, 6))
sns.barplot(data=yield_by_season, x='Yield_Efficiency', y='Season', palette='viridis')
plt.title('Seasonal Yield Efficiency')
plt.xlabel('Yield Efficiency (Production/Area)')
plt.ylabel('Season')
plt.show()

total_production_by_year.to_csv('total_production_by_year.csv', index=False)
total_production_by_crop.to_csv('total_production_by_crop.csv', index=False)
yield_by_crop.to_csv('yield_by_crop.csv', index=False)
# Continue for other dataframes
