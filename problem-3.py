import pandas as pd
import altair as alt
import os


file_path = 'data/daily_df.csv'  
df = pd.read_csv(file_path)

df['date'] = pd.to_datetime(df['date'])

melted_df = pd.melt(df, id_vars=['date', 'city', 'state'], 
                    value_vars=['max_temp_c', 'min_temp_c'], 
                    var_name='temperature_type', 
                    value_name='temperature')


nearest = alt.selection_single(on='mouseover', nearest=True, empty='none', fields=['date'])


line = alt.Chart(melted_df).mark_line().encode(
    x=alt.X('date:T', title='Date'),
    y=alt.Y('temperature:Q', title='Temperature (°C)'),
    color='city:N',
    strokeDash='temperature_type:N',
    tooltip=['date', 'city', 'temperature_type', 'temperature']
).properties(
    width=800,
    height=400,
    title='Maximum and Minimum Temperatures by City'
)


points = line.mark_circle().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0)),
    tooltip=['date', 'city', 'temperature_type', 'temperature']
).add_selection(nearest)

rules = alt.Chart(melted_df).mark_rule(color='gray').encode(
    x='date:T',
    opacity=alt.condition(nearest, alt.value(0.3), alt.value(0)),
    tooltip=['date', 'city', 'temperature_type', 'temperature']
)


chart = (line + points + rules)


script_dir = os.path.dirname(os.path.abspath(__file__))


chart_file_path = os.path.join(script_dir, 'chart_with_markers_and_rule.html')
chart.save(chart_file_path)
print(f"Chart with markers and rule has been saved to '{chart_file_path}'")


print(f"File can be seen at: {chart_file_path}")
