import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import streamlit.components.v1 as components
from streamlit_player import st_player

st.set_page_config(layout="wide")

# URLS of data
race_wins = ('race_wins_1958-2020.csv')
champion = ('constructors_championship_1958-2020.csv')

# Load Data
@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")


# TEXT

# Drop first Column and load data
race_wins_data = load_data(race_wins)
race_wins_data = race_wins_data.iloc[: , 1:]
champion_data = load_data(champion)
champion_data = champion_data.iloc[: , 1:]
# Notify the reader that the data was successfully loaded.


# Preprocessing the Data
# championship['Team'] = championship['Team'].replace(['Alfa Romeo Racing Ferrari'],'Alfa Romeo')
champion_data['Team'] = champion_data['Team'].replace(['Sauber Mercedes','Sauber Ford','Sauber Petronas','Sauber BMW','Sauber Ferrari','Alfa Romeo Racing Ferrari','Alfa Romeo'],'Sauber')
champion_data['Team'] = champion_data['Team'].replace(['Red Bull Renault','Red Bull Racing Renault','Red Bull Racing TAG Heuer','Red Bull Racing Honda'],'Red Bull')
champion_data['Team'] = champion_data['Team'].replace(['Toro Rosso Ferrari','Toro Rosso','Scuderia Toro Rosso Honda','AlphaTauri Honda'],'AlphaTauri')
champion_data['Team'] = champion_data['Team'].replace(['Frank Williams Racing Cars/Williams','Williams Ford','Williams Honda','Williams Judd','Williams Renault','Williams Mecachrome','Williams Supertec','Williams BMW','Williams Cosworth','Williams Toyota','Williams Cosworth','Williams Mercedes'],'Williams')
champion_data['Team'] = champion_data['Team'].replace(['Haas Ferrari'],'Haas')
champion_data['Team'] = champion_data['Team'].replace(['Force India Ferrari','Force India Mercedes','Force India Sahara','Racing Point BWT Mercedes'],'Racing Point')
champion_data['Team'] = champion_data['Team'].replace(['McLaren Ford','McLaren Serenissima','McLaren BRM','McLaren Ford','McLaren TAG','McLaren Honda','McLaren Mercedes','McLaren Renault'],'McLaren')

# race_wins['Team'] = race_wins['Team'].replace(['Alfa Romeo Racing Ferrari'],'Alfa Romeo')
race_wins_data['Team'] = race_wins_data['Team'].replace(['Sauber Mercedes','Sauber Ford','Sauber Petronas','Sauber BMW','Sauber Ferrari','Alfa Romeo Racing Ferrari','Alfa Romeo'],'Sauber')
race_wins_data['Team'] = race_wins_data['Team'].replace(['Red Bull Renault','Red Bull Racing Renault','Red Bull Racing TAG Heuer','Red Bull Racing Honda'],'Red Bull')
race_wins_data['Team'] = race_wins_data['Team'].replace(['Toro Rosso Ferrari','Toro Rosso','Scuderia Toro Rosso Honda','AlphaTauri Honda'],'AlphaTauri')
race_wins_data['Team'] = race_wins_data['Team'].replace(['Frank Williams Racing Cars/Williams','Williams Ford','Williams Honda','Williams Judd','Williams Renault','Williams Mecachrome','Williams Supertec','Williams BMW','Williams Cosworth','Williams Toyota','Williams Cosworth','Williams Mercedes'],'Williams')
race_wins_data['Team'] = race_wins_data['Team'].replace(['Haas Ferrari'],'Haas')
race_wins_data['Team'] = race_wins_data['Team'].replace(['Force India Ferrari','Force India Mercedes','Force India Sahara','Racing Point BWT Mercedes'],'Racing Point')
race_wins_data['Team'] = race_wins_data['Team'].replace(['McLaren Ford','McLaren Serenissima','McLaren BRM','McLaren Ford','McLaren TAG','McLaren Honda','McLaren Mercedes','McLaren Renault'],'McLaren')

championship_data = champion_data.query("Team in ('Ferrari','Red Bull','AlphaTauri','Williams','Haas','Racing Point','McLaren','Mercedes','Renault','Sauber')")
driver_winners = race_wins_data.query("Team in ('Ferrari','Red Bull','AlphaTauri','Williams','Haas','Racing Point','McLaren','Mercedes','Renault','Sauber')")

driver_winners = driver_winners.groupby(["Team", "Name"])["Venue"].count().reset_index(name="Race_wins")
data_wins = driver_winners.groupby(['Team']).apply(lambda x: x.nlargest(10,['Race_wins'])).reset_index(drop=True)

# # def min_wins(n,data):
# #     data_wins = data.groupby(['Team']).apply(lambda x: x.nlargest(n,['Race_wins'])).reset_index(drop=True)
# #     return data_wins
#
# minimum = st.select_slider(
#      'Select driver minimum wins',
#      options=[1,2,3,4,5,6,7])
# data_wins = min_wins(minimum,driver_winners)

# RENAULT - Add missing rows
championship_data = championship_data.append({'Year':'1986', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1987', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1988', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1989', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1990', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1991', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1992', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1993', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1994', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1995', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1996', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1997', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1998', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'1999', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'2000', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'2001', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'2012', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'2013', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'2014', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)
championship_data = championship_data.append({'Year':'2015', 'Position':None, 'Team':'Renault', 'Points':0},ignore_index = True)

#  Graph
championship_data['Position'] = pd.to_numeric(championship_data['Position'])
championship_data['Year'] = pd.to_datetime(championship_data['Year'], format='%Y')
#championship_data['Year'] = pd.DatetimeIndex(championship_data['Year']).year

# MAIN GRAPH
data_main = championship_data.groupby(['Team']).mean()['Position'].reset_index().round(1)
data_pos = championship_data
colors = ['#7bccc4', '#ef3b2c', '#253494', '#fd8d3c', '#4292c6', '#fed976', '#fa9fb5','#a50f15','#225ea8','#FFFFFF']
data_main['Color'] = colors
data_main['Color'] = data_main['Color'].astype(str)

main = alt.Chart(data_main, title='Average Position by Teams').encode(
    y=alt.Y('Position', scale=alt.Scale(domain=[10, 1]), axis=alt.Axis(tickCount=10)),
    x=alt.X('Team', sort='-y'),)

main1 = main.mark_bar().encode(
    color=alt.Color('Team',
    scale=alt.Scale(domain=['Mercedes','Ferrari', 'Red Bull', 'McLaren','Williams', 'Renault','Racing Point', 'Sauber','AlphaTauri', 'Haas'],
    range=colors),
    legend=alt.Legend(orient='none', legendX=610, legendY=0)))

text = main.mark_text(align='center', baseline='bottom', dy=-3, color='white', size=14).encode(
    text='Position')

layers_main = main1 + text
layers_main = layers_main.properties(width=600, height=700)
selection = alt.selection_multi(fields=['Team'])
layers_main = layers_main.add_selection(selection)

#  SECONDARY GRAPH #1
lines = alt.Chart(data_pos, title='Position by Year').mark_line(size=5).encode(
    x=alt.X('Year'),
    y=alt.Y('Position', scale=alt.Scale(domain=[10.5, 0]), axis=alt.Axis(tickCount=10)),
    color='Team',
    tooltip=[alt.Tooltip('Year',timeUnit='year'), 'Team', 'Position', 'Points'])\
    .transform_filter(selection)

points = alt.Chart(data_pos).mark_point(fill='black', color='white', size=50, opacity=0.8).encode(
    x=alt.X('Year'),
    y=alt.Y('Position', scale=alt.Scale(domain=[10.5, 0]), axis=alt.Axis(tickCount=10)),)\
    .transform_filter(selection)

pos = lines + points
pos = pos.properties(width=600, height=300)
pos = pos.interactive(bind_y = False)

#  SECONDARY GRAPH #2
wins = alt.Chart(data_wins, title='Wins by Driver (Top 10)').encode(
    x=alt.X('Race_wins', title='Race Wins'),
    y=alt.Y('Name', sort='-x'),)

wins1 = wins.mark_bar().encode(
    color=alt.Color('Team',
    scale=alt.Scale(domain=['Mercedes','Ferrari', 'Red Bull', 'McLaren','Williams', 'Renault','Racing Point', 'Sauber','AlphaTauri', 'Haas'],
    range=colors),))\
    .transform_filter(selection)
wins1 = wins1.properties(width=600, height=300)

#  Putting it all together + final configuration
temp = alt.vconcat(pos, wins1)
total = alt.hconcat(layers_main, temp)
total = total.configure(background='black')\
    .configure_axisBottom(labelColor='white', titleColor='white',labelFontSize=12)\
    .configure_axisLeft(labelColor='white', titleColor='white', labelFontSize=12)\
    .configure_legend(titleColor='white',labelColor='white', labelFontSize=14,titleFontSize=14)\
    .configure_title(color='white')\
    .configure_axisX(labelAngle=0, labelOverlap='greedy')


total.save('chart.html')


  ####################
  ######INTRO ########
  ####################
row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('Formula One Project🏎️')
    st.markdown('Written By **_Omer_ _Rosenberg_ And _Chen_ _Harel_**.')
with row0_2:
    st.text("")

    st.text("")
row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 3.2, .1))
with row1_1:
    st.markdown("Hello there! **Formula One** have been around since 1950, Known as the fastest MotorSport in the world and also one of the most expensive league in all sports. In the past few years there's a big growth in the number of fans and watchers of this sport. The main reason for this trend is the Netflix show \"Drive to Survive\" which became viral and already have 4 seasons, The Series shows the main event of each season since 2018, But **F1** is way more then this. That why we decided to Visualize the **F1** history and give you some prespective about the constructers and also about the drivers. ")
    st.text("")
    st.markdown("Application built with [Streamlit](https://streamlit.io/)")
    st.markdown("Chart built with [Altair](https://altair-viz.github.io)")
    st.markdown("Data took from Kaggle [DATA](https://www.kaggle.com/datasets/aadiltajani/fia-f1-19502019-data)")
    space(1)
    st.subheader("Get you into the vibe")
    st.markdown("A short trailer of the new season of Drive2Survive")
    st_player('https://www.youtube.com/watch?v=eokeG5lVAWY')
#  Save visualization
#  ADD Video

row2_space1 ,row2_1,row2_2,row_2_space2 = st.columns((.1,2,1.2,.1))
with row2_1:
    see_race_wins = st.expander('Click here to see the raw Race Wins data  👉')
    with see_race_wins:
        st.dataframe(data=race_wins_data)
with row2_2:
    see_race_wins = st.expander('Click here to see the raw Constructors Seasonal Position data  👉')
    with see_race_wins:
        st.dataframe(data=champion_data)

row3_space1 ,row3_1,row3_2,row_3_space2 = st.columns((.1,2,1.2,.1))
with row3_1:
    st.markdown("**_Column_ _Explanation_**")
    st.markdown("_Race_ _Wins_ columns explanation:")
    st.markdown("_Venue_ (String) : Race location.")
    st.markdown("_Date_ (DateTime) : Time of the year.")
    st.markdown("_Name_ (String) : Winner driver name.")
    st.markdown("_Name_ _Tag_ (String) : Abbreviation of driver name.")
    st.markdown("_Team_ (String) : Name of the driver team.")
    st.markdown("_Laps_ And _Time_ : How many laps completed and how much time it took to finish the race.")
with row3_2:
    st.markdown("**_Column_ _Explanation_**")
    st.markdown("_Constructor_ _Position_ columns explanation:")
    st.markdown("_Year_ (DateTime) : Which year.")
    st.markdown("_Position_ (String) : Which position the team finished the season.")
    st.markdown("_Team_ (String) : Name of the Team.")
    st.markdown("_Points_ (Int) : How many points the team scored in that season.")




space(2)

col1 ,col2 = st.columns((0.005,0.9))
#  Load the Visualization
HtmlFile = open("chart.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
with col2:
    components.html(source_code,width=1500, height=1500)
