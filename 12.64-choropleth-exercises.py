#Choropleth Maps Exercise
#Welcome to the Choropleth Maps Exercise!
# In this exercise we will give you some simple
# datasets and ask you to create Choropleth Maps from them.
# Due to the Nature of Plotly we can't show you examples

#Full Documentation Reference
#** Import pandas and read the csv file: 2014_World_Power_Consumption**
import plotly.graph_objects as go
import pandas as pd

df1 = pd.read_csv(r'.\udemy\python-for-data-science-and-machine-learning-bootcamp\12\2014_World_Power_Consumption.csv')
#print(df1.head())
#** Referencing the lecture notes, create a Choropleth Plot of
# the Power Consumption for Countries using the data and layout dictionary. **
fig1 = go.Figure(data=go.Choropleth(
    locations= df1['Country'], 
    locationmode = 'country names',
    z = df1['Power Consumption KWH'], 
    text = df1['Country'], 
    colorbar_title = 'Power Consumption KWH'
))

fig1.update_layout(
    title_text = '2014 Power Consumption KWH',
    geo = dict(
        showframe = False,
        projection_type = 'mercator'
    )
)
#fig1.show()


#** Import the 2012_Election_Data csv file using pandas. **
df2 = pd.read_csv(r'.\udemy\python-for-data-science-and-machine-learning-bootcamp\12\2012_Election_Data.csv')
print(df2.head())
#** Now create a plot that displays the Voting-Age Population (VAP) per state.

fig2 = go.Figure(data=go.Choropleth(
    locations= df2['State Abv'], 
    locationmode = 'USA-states',
    z = df2['Voting-Age Population (VAP)'], 
    text = df2['State'], 
    colorbar_title = 'Voting-Age Population (VAP)',
    colorscale = 'Reds',
    reversescale = True,
    marker_line_color= 'black',
    marker_line_width= 2.0
))

fig2.update_layout(
    title_text = '2012 General Election Voting Data',
    geo = dict(
        scope='usa',
        showlakes = True,
        lakecolor = 'rgb(85, 173, 240)'
    )
)
fig2.show()



#choromap = go.Figure(data = [data],layout = layout)
#iplot(choromap,validate=False)
#Great Job!