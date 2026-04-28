python
import pandas as pd
import plotly.express as px

# Load the Pensioners Distribution Data
pension_data = pd.read_excel('Distribution of Pensioners 2022.xlsx')

# Preprocess the data
pension_data['Quarter'] = pension_data['Quarter'].apply(lambda x: f'Q{x}')
pension_data['Female_Percentage'] = pension_data['Female_Count'] / pension_data['Total_Count'] * 100
pension_data['Male_Percentage'] = pension_data['Male_Count'] / pension_data['Total_Count'] * 100

# Create an interactive plot for the gender distribution
fig = px.bar(pension_data, 
             x='Quarter', 
             y=['Male_Percentage', 'Female_Percentage'], 
             barmode='group',
             title='Gender Distribution of Pensioners by Quarter in 2022',
             labels={'value': 'Percentage', 'Quarter': 'Quarter'},
             text_auto=True)

# Customize the layout
fig.update_layout(
    xaxis_title="Quarter",
    yaxis_title="Percentage",
    legend_title="Gender",
    template="plotly_white"
)

# Show the plot
fig.show()

# Example of saving the processed data as CSV
pension_data.to_csv('Processed_Pensioners_Distribution_2022.csv', index=False)
