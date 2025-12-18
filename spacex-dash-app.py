# spacex-dash-app.py (Code up to the end of TASK 1)

import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output 
# Note: Input/Output are needed for the next task (Task 2)

# Load the data
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
spacex_df = pd.read_csv(URL)

# Calculate min/max payload (for later tasks)
min_payload = spacex_df['Payload Mass (kg)'].min()
max_payload = spacex_df['Payload Mass (kg)'].max()

# Initialize the Dash app
# Suppressing exceptions is necessary when callbacks are defined later than the layout components
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# --- Define Dropdown Options ---
launch_sites = spacex_df['Launch Site'].unique().tolist()
dropdown_options = [{'label': 'All Sites', 'value': 'ALL'}] + \
                   [{'label': site, 'value': site} for site in launch_sites]

# Define the app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # TASK 1: Dropdown Component
    html.Div([
        dcc.Dropdown(
            id='site-dropdown',
            options=dropdown_options,
            value='ALL',
            placeholder="Select a Launch Site here",
            searchable=True
        ),
    ], style={'padding': '0px 0px 30px 0px'}),

    # Placeholder for TASK 2 Pie Chart
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    # Placeholder for TASK 3 Range Slider Label
    html.P("Payload range (Kg):"),
    
    # Placeholder for TASK 3 Range Slider (content will be added later)
    # TASK 3: Range Slider Component
    dcc.RangeSlider(
        id='payload-slider',
        min=0,             # Slider minimum value
        max=10000,         # Slider maximum value (as specified in lab)
        step=1000,         # Slider interval step
        # Marks dictionary for displaying labels below the slider track
        marks={i: f'{i}' for i in range(0, 10001, 1000)}, 
        # Current selected range (uses the pre-calculated min/max payload values)
        value=[min_payload, max_payload] 
    ), 
    
    # Placeholder for TASK 4 Scatter Chart
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

#TASK 2: Callback function to render success-pie-chart (More robust formatting)

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # 1. 'ALL' Sites Selected: Group by Class to get counts
        # This creates a small DataFrame with counts of 0s and 1s
        data = spacex_df.groupby('class')['class'].count().reset_index(name='count')
        data['class'] = data['class'].apply(lambda x: 'Success' if x == 1 else 'Failure') # Rename 1/0 to text labels
        
        fig = px.pie(
            data,
            values='count', # The count of launches
            names='class',  # The labels (Success/Failure)
            title='Total Successful Launches (All Sites)',
            # Ensure consistent color mapping using Plotly's default list or explicit mapping
            color='class',
            color_discrete_map={'Success': 'lightgreen', 'Failure': 'red'} 
        )
        return fig
    else:
        # 2. Specific Site Selected: Filter the DataFrame
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        
        # Group by Class to get counts for the specific site
        data = filtered_df.groupby('class')['class'].count().reset_index(name='count')
        data['class'] = data['class'].apply(lambda x: 'Success' if x == 1 else 'Failure')

        fig = px.pie(
            data,
            values='count',
            names='class',
            title=f'Launch Outcomes for Site: {entered_site}',
            color='class',
            color_discrete_map={'Success': 'lightgreen', 'Failure': 'red'}
        )
        return fig

# TASK 4: Callback function to render the success-payload-scatter-chart scatter plot

@app.callback(
    # Output: The figure property of the scatter chart graph component
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    # Inputs: Takes the value from the dropdown and the range from the slider
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id="payload-slider", component_property="value")]
)
def get_scatter_chart(entered_site, payload_range):
    # 1. Filter the DataFrame based on the selected payload range
    low, high = payload_range
    # Create a mask to filter the rows where Payload Mass is within the selected range
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]

    if entered_site == 'ALL':
        # Case 1: All Sites Selected (Filtered by Payload)
        fig = px.scatter(
            filtered_df, # Use the payload-filtered data
            x='Payload Mass (kg)',
            y='class',
            # Color points by Booster Version Category
            color='Booster Version Category',
            title=f'Success vs. Payload Mass for All Sites (Range: {low} to {high} kg)'
        )
        return fig
    else:
        # Case 2: Specific Site Selected (Filtered by Payload AND Site)
        # Filter the payload-filtered data further by the selected launch site
        specific_site_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        
        fig = px.scatter(
            specific_site_df, # Use the doubly filtered data
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title=f'Success vs. Payload Mass for Site {entered_site} (Range: {low} to {high} kg)'
        )
        return fig


# To run the app (usually required at the very end of your .py file)
if __name__ == '__main__':
    app.run()