import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import streamlit.components.v1 as components



st.set_page_config(layout="wide")
# TITLE

st.title('Formula1 Project')
st.video('https://www.youtube.com/watch?v=eokeG5lVAWY', format="video/mp4", start_time=0)
# URLS of data
race_wins = ('/Users/Chen/PycharmProjects/Formula1/race_wins_1950-2020.csv')
champion = ('/Users/Chen/PycharmProjects/Formula1/constructors_championship_1958-2020.csv')

# Load Data
@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

# TEXT
data_load_state = st.text('Loading data...')

# Drop first Column and load data
race_wins_data = load_data(race_wins)
race_wins_data = race_wins_data.iloc[: , 1:]
champion_data = load_data(champion)
champion_data = champion_data.iloc[: , 1:]
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

# Preprocessing the Data
champion_data['Team'] = champion_data['Team'].replace(['Alfa Romeo Racing Ferrari'],'Alfa Romeo')
champion_data['Team'] = champion_data['Team'].replace(['Sauber Mercedes','Sauber Ford','Sauber Petronas','Sauber BMW','Sauber Ferrari'],'Sauber')
champion_data['Team'] = champion_data['Team'].replace(['Red Bull Renault','Red Bull Racing Renault','Red Bull Racing TAG Heuer','Red Bull Racing Honda'],'Red Bull')
champion_data['Team'] = champion_data['Team'].replace(['Toro Rosso Ferrari','Toro Rosso','Scuderia Toro Rosso Honda','AlphaTauri Honda'],'AlfaTauri')
champion_data['Team'] = champion_data['Team'].replace(['Frank Williams Racing Cars/Williams','Williams Ford','Williams Honda','Williams Judd','Williams Renault','Williams Mecachrome','Williams Supertec','Williams BMW','Williams Cosworth','Williams Toyota','Williams Cosworth','Williams Mercedes'],'Williams')
champion_data['Team'] = champion_data['Team'].replace(['Haas Ferrari'],'Haas')
champion_data['Team'] = champion_data['Team'].replace(['Force India Ferrari','Force India Mercedes','Force India Sahara','Racing Point BWT Mercedes'],'Racing Point')
champion_data['Team'] = champion_data['Team'].replace(['McLaren Ford','McLaren Serenissima','McLaren BRM','McLaren Ford','McLaren TAG','McLaren Honda','McLaren Mercedes','McLaren Renault'],'McLaren')

race_wins_data['Team'] = race_wins_data['Team'].replace(['Alfa Romeo Racing Ferrari'],'Alfa Romeo')
race_wins_data['Team'] = race_wins_data['Team'].replace(['Sauber Mercedes','Sauber Ford','Sauber Petronas','Sauber BMW','Sauber Ferrari'],'Sauber')
race_wins_data['Team'] = race_wins_data['Team'].replace(['Red Bull Renault','Red Bull Racing Renault','Red Bull Racing TAG Heuer','Red Bull Racing Honda'],'Red Bull')
race_wins_data['Team'] = race_wins_data['Team'].replace(['Toro Rosso Ferrari','Toro Rosso','Scuderia Toro Rosso Honda','AlphaTauri Honda'],'AlfaTauri')
race_wins_data['Team'] = race_wins_data['Team'].replace(['Frank Williams Racing Cars/Williams','Williams Ford','Williams Honda','Williams Judd','Williams Renault','Williams Mecachrome','Williams Supertec','Williams BMW','Williams Cosworth','Williams Toyota','Williams Cosworth','Williams Mercedes'],'Williams')
race_wins_data['Team'] = race_wins_data['Team'].replace(['Haas Ferrari'],'Haas')
race_wins_data['Team'] = race_wins_data['Team'].replace(['Force India Ferrari','Force India Mercedes','Force India Sahara','Racing Point BWT Mercedes'],'Racing Point')
race_wins_data['Team'] = race_wins_data['Team'].replace(['McLaren Ford','McLaren Serenissima','McLaren BRM','McLaren Ford','McLaren TAG','McLaren Honda','McLaren Mercedes','McLaren Renault'],'McLaren')

championship_data = champion_data.query("Team in ('Ferrari','Alpha Romeo','Red Bull','AlphaTauri','Williams','Haas','Racing Point','McLaren','Mercedes','Renault','Sauber')")
race_wins_data = race_wins_data.query("Team in ('Ferrari','Alpha Romeo','Red Bull','AlphaTauri','Williams','Haas','Racing Point','McLaren','Mercedes','Renault','Sauber')")

driver_winners = race_wins_data.groupby(["Team", "Name"])["Venue"].count().reset_index(name="Race_wins")
#data_wins = driver_winners.groupby(['Team']).apply(lambda x: x.nlargest(10,['Race_wins'])).reset_index(drop=True)

def min_wins(n,data):
    data_wins = data.groupby(['Team']).apply(lambda x: x.nlargest(n,['Race_wins'])).reset_index(drop=True)
    return data_wins

minimum = st.number_input("Maximum Drivers")
data_wins = min_wins(int(minimum),driver_winners)
#Graph

data_main = championship_data.groupby(['Team']).mean()['Position'].reset_index().round(1)
data_pos = championship_data
colors = ['#00D2BE', '#DC0000', '#0600EF', '#FF8700', '#005AFF', 'Yellow', '#006F62', '#900000', '#FFFFFF']
data_main['Color'] = colors
data_main['Color'] = data_main['Color'].astype(str)

main = alt.Chart(data_main, title='Average Position by Teams').encode(
    y=alt.Y('Position', scale=alt.Scale(domain=[10, 1]), axis=alt.Axis(tickCount=10)),
    x=alt.X('Team', sort='-y'),

)

main1 = main.mark_bar().encode(
    color=alt.Color('Team',
                    scale=alt.Scale(
                        domain=['Mercedes', 'Ferrari', 'Red Bull', 'McLaren', 'Williams', 'Renault', 'Racing Point',
                                'Sauber', 'Haas'],
                        range=colors),
                    legend=alt.Legend(orient='none', legendX=460, legendY=10)
                    )
)

text = main.mark_text(align='center', baseline='bottom', dy=-3, color='white', size=14).encode(
    text='Position'
)

layers_main = main1 + text
layers_main = layers_main.properties(width=500, height=400)

selection = alt.selection_multi(fields=['Team'])
layers_main = layers_main.add_selection(selection)

pos = alt.Chart(data_pos, title='Position by Year').mark_line(point=True, size=4).encode(
    x=alt.X('Year'),
    y=alt.Y('Position', scale=alt.Scale(domain=[10, 0]), axis=alt.Axis(tickCount=10)),
    color='Team',
    tooltip=['Year', 'Team', 'Position', 'Points']
).transform_filter(
    selection
)

pos = pos.properties(width=400, height=200)
pos = pos.interactive()

wins = alt.Chart(data_wins, title='Wins by Driver (Top 10)').encode(
    x=alt.X('Race_wins', title='Race Wins'),
    y=alt.Y('Name', sort='-x'),
)

wins1 = wins.mark_bar().encode(
    color=alt.Color('Team',
                    scale=alt.Scale(
                        domain=['Mercedes', 'Ferrari', 'Red Bull', 'McLaren', 'Williams', 'Renault', 'Racing Point',
                                'Sauber', 'Haas'],
                        range=colors),
                    )
).transform_filter(
    selection
)
wins1 = wins1.properties(width=400, height=200)

temp = alt.vconcat(pos, wins1)
total = alt.hconcat(layers_main, temp)
total = total.configure(background='black').configure_axisBottom(labelColor='white', titleColor='white',
                                                                 labelFontSize=12).configure_axisLeft(
    labelColor='white', titleColor='white', labelFontSize=12).configure_legend(titleColor='white',
                                                                               labelColor='white').configure_title(
    color='white').configure_axisX(labelAngle=0, labelOverlap='greedy')
total.save('/Users/Chen/PycharmProjects/Formula1/chart.html')


# st.subheader('Our dear graph')
# st.altair_chart(total, use_container_width=True)



HtmlFile = open("/Users/Chen/PycharmProjects/Formula1/chart.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code,width=1500, height=1500)
