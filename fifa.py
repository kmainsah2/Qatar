import pandas as pd
import altair as alt
import streamlit as st 


#Wide Layout
st.set_page_config(layout="wide")

#Main Page Title with logo
st.title("2022 Qatar World Cup")

#Real Time Dataset

#Filter to Scores
scores = pd.read_csv("data/fifa_scores.csv")
scores['Date1'] = pd.to_datetime(scores.Date1)
scores['month'] = scores.Date1.dt.month
scores['year'] = scores.Date1.dt.year
scores = scores[scores['year']>=2018]

#Filter to Rank
fifa_data = pd.read_csv("data/fifa_data.csv", usecols=['Team Name', 'Date', 'Variable Name', 'Value'])
rank_filter = fifa_data[fifa_data["Variable Name"] == 'Rank']
rank_filter['Date'] = pd.to_datetime(rank_filter.Date)
rank_filter['month'] = rank_filter.Date.dt.month
rank_filter['year'] = rank_filter.Date.dt.year
df_rank_filter = rank_filter[rank_filter['year']>=2018]

#Remember to make sure the y graph is inverted 

#Group Stage Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8,tab9 = st.tabs(['2022 Qatar World Cup','Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G', 'Group H'])

groupa = df_rank_filter[df_rank_filter["Team Name"].str.contains('Senegal|Qatar|Netherlands|Ecuador')== True]
groupa = groupa['Team Name'].unique()

groupb = df_rank_filter[df_rank_filter["Team Name"].str.contains('Iran|England|USA|Wales')== True]
groupb = groupb['Team Name'].unique()

groupc = df_rank_filter[df_rank_filter["Team Name"].str.contains('Argentina|Saudi Arabia|Mexico|Poland')== True]
groupc = groupc['Team Name'].unique()

groupd = df_rank_filter[df_rank_filter["Team Name"].str.contains('Denmark|Tunisia|France|Australia')== True]
groupd = groupd['Team Name'].unique()

groupe = df_rank_filter[df_rank_filter["Team Name"].str.contains('Germany|Japan|Spain|Costa Rica')== True]
groupe = groupe['Team Name'].unique()

groupf = df_rank_filter[df_rank_filter["Team Name"].str.contains('Morocco|Croatia|Belgium|Canada')== True]
groupf = groupf['Team Name'].unique()

groupg = df_rank_filter[df_rank_filter["Team Name"].str.contains('Switzerland|Cameroon|Brazil|Serbia')== True]
groupg = groupg['Team Name'].unique()

grouph = df_rank_filter[df_rank_filter["Team Name"].str.contains('Uruguay|South Korea|Portugal|Ghana')== True]
grouph = grouph['Team Name'].unique()

with tab1:
    st.header(
        "The 2022 FIFA World Cup kicked off in Qatar on November 20, 2022. Millions of people around the globe are watching as 32 teams battle for the title. Now that the group stages are done, let's look back at how these teams stacked up against each other."
    )
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.write("")
    with col2:
        st.image("/Users/kristalmainsah/Desktop/DSBA/qatar_2022/q_logo.webp", width= 700)
    with col3:
        st.write("")
    st.header("In the following tabs, you'll be able to analyze the rankings from each team following the last World Cup. Additionnaly, you'll be able to see each team's goalkeeper, defensive, midfield, and offensive scores. ")
    st.audio("fifa_themesong.mp3")
    

with tab2:
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        team1 = st.selectbox("Select Team 1", groupa)
        team1_data = df_rank_filter[df_rank_filter['Team Name'] == team1]
        fig_rank1 = alt.Chart(team1_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank1, use_container_width=True)
        
        hteam1_scoresdata = scores[scores['Home Team'] == team1]
        ateam1_scoresdata = scores[scores['Away Team'] == team1]
        
        #Goalkeeper 
        gk_score_h = hteam1_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a = ateam1_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score = (gk_score_h + gk_score_a)/2
        avg_gk_score = round(avg_gk_score, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score
        
        #Defensive 
        defensive_score_h = hteam1_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a = ateam1_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score = (defensive_score_h + defensive_score_a)/2
        avg_defensive_score = round(avg_defensive_score, 2)
        st.caption('Defensive Score')
        avg_defensive_score
       
        #Midfield 
        midfield_score_h = hteam1_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a = ateam1_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score = (midfield_score_h + midfield_score_a)/2
        avg_midfield_score = round(avg_midfield_score, 2)
        st.caption('Midfield Score')
        avg_midfield_score
        
        #Offensive 
        o_score_h = hteam1_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a = ateam1_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score = (o_score_a + o_score_h)/2
        avg_o_score = round(avg_o_score, 2)
        st.caption('Offensive Score')
        avg_o_score
        

    with col2:
        team2 = st.selectbox("Select Team 2", groupa)
        team2_data = df_rank_filter[df_rank_filter['Team Name'] == team2]
        #st.write(team2_data)
        fig_rank2 = alt.Chart(team2_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank2, use_container_width=True)
        
        hteam2_scoresdata = scores[scores['Home Team'] == team2]
        ateam2_scoresdata = scores[scores['Away Team'] == team2]
        
        #Goalkeeper 
        gk_score_h2 = hteam2_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a2 = ateam2_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score2 = (gk_score_h2 + gk_score_a2)/2
        avg_gk_score2 = round(avg_gk_score2, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score2
        
        #Defensive 
        defensive_score_h2 = hteam2_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a2 = ateam2_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score2 = (defensive_score_h2 + defensive_score_a2)/2
        avg_defensive_score2 = round(avg_defensive_score2, 2)
        st.caption('Defensive Score')
        avg_defensive_score2
       
        #Midfield 
        midfield_score_h2 = hteam2_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a2 = ateam2_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score2 = (midfield_score_h2 + midfield_score_a2)/2
        avg_midfield_score2 = round(avg_midfield_score2, 2)
        st.caption('Midfield Score')
        avg_midfield_score2
        
        #Offensive 
        o_score_h2 = hteam2_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a2 = ateam2_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score2 = (o_score_a2 + o_score_h2)/2
        avg_o_score2 = round(avg_o_score2, 2)
        st.caption('Offensive Score')
        avg_o_score2
        
with tab3:
    col1, col2 = st.columns(2)
    with col1:
        team1 = st.selectbox("Select Team 1", groupb)
        team1_data = df_rank_filter[df_rank_filter['Team Name'] == team1]
        fig_rank1 = alt.Chart(team1_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank1, use_container_width=True)
        
        hteam1_scoresdata = scores[scores['Home Team'] == team1]
        ateam1_scoresdata = scores[scores['Away Team'] == team1]
        
        #Goalkeeper 
        gk_score_h = hteam1_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a = ateam1_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score = (gk_score_h + gk_score_a)/2
        avg_gk_score = round(avg_gk_score, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score
        
        #Defensive 
        defensive_score_h = hteam1_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a = ateam1_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score = (defensive_score_h + defensive_score_a)/2
        avg_defensive_score = round(avg_defensive_score, 2)
        st.caption('Defensive Score')
        avg_defensive_score
       
        #Midfield 
        midfield_score_h = hteam1_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a = ateam1_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score = (midfield_score_h + midfield_score_a)/2
        avg_midfield_score = round(avg_midfield_score, 2)
        st.caption('Midfield Score')
        avg_midfield_score
        
        #Offensive 
        o_score_h = hteam1_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a = ateam1_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score = (o_score_a + o_score_h)/2
        avg_o_score = round(avg_o_score, 2)
        st.caption('Offensive Score')
        avg_o_score
        
    with col2:
        team2 = st.selectbox("Select Team 2", groupb)
        team2_data = df_rank_filter[df_rank_filter['Team Name'] == team2]
        #st.write(team2_data)
        fig_rank2 = alt.Chart(team2_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank2, use_container_width=True)
        
        hteam2_scoresdata = scores[scores['Home Team'] == team2]
        ateam2_scoresdata = scores[scores['Away Team'] == team2]
        
        #Goalkeeper 
        gk_score_h2 = hteam2_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a2 = ateam2_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score2 = (gk_score_h2 + gk_score_a2)/2
        avg_gk_score2 = round(avg_gk_score2, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score2
        
        #Defensive 
        defensive_score_h2 = hteam2_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a2 = ateam2_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score2 = (defensive_score_h2 + defensive_score_a2)/2
        avg_defensive_score2 = round(avg_defensive_score2, 2)
        st.caption('Defensive Score')
        avg_defensive_score2
       
        #Midfield 
        midfield_score_h2 = hteam2_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a2 = ateam2_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score2 = (midfield_score_h2 + midfield_score_a2)/2
        avg_midfield_score2 = round(avg_midfield_score2, 2)
        st.caption('Midfield Score')
        avg_midfield_score2
        
        #Offensive 
        o_score_h2 = hteam2_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a2 = ateam2_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score2 = (o_score_a2 + o_score_h2)/2
        avg_o_score2 = round(avg_o_score2, 2)
        st.caption('Offensive Score')
        avg_o_score2

with tab4:
    col1, col2 = st.columns(2)
    with col1:
        team1 = st.selectbox("Select Team 1", groupc)
        team1_data = df_rank_filter[df_rank_filter['Team Name'] == team1]
        fig_rank1 = alt.Chart(team1_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank1, use_container_width=True)
        
        hteam1_scoresdata = scores[scores['Home Team'] == team1]
        ateam1_scoresdata = scores[scores['Away Team'] == team1]
        
        #Goalkeeper 
        gk_score_h = hteam1_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a = ateam1_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score = (gk_score_h + gk_score_a)/2
        avg_gk_score = round(avg_gk_score, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score
        
        #Defensive 
        defensive_score_h = hteam1_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a = ateam1_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score = (defensive_score_h + defensive_score_a)/2
        avg_defensive_score = round(avg_defensive_score, 2)
        st.caption('Defensive Score')
        avg_defensive_score
       
        #Midfield 
        midfield_score_h = hteam1_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a = ateam1_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score = (midfield_score_h + midfield_score_a)/2
        avg_midfield_score = round(avg_midfield_score, 2)
        st.caption('Midfield Score')
        avg_midfield_score
        
        #Offensive 
        o_score_h = hteam1_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a = ateam1_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score = (o_score_a + o_score_h)/2
        avg_o_score = round(avg_o_score, 2)
        st.caption('Offensive Score')
        avg_o_score
    
    with col2:
        team2 = st.selectbox("Select Team 2", groupc)
        team2_data = df_rank_filter[df_rank_filter['Team Name'] == team2]
        #st.write(team2_data)
        fig_rank2 = alt.Chart(team2_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank2, use_container_width=True)
        
        hteam2_scoresdata = scores[scores['Home Team'] == team2]
        ateam2_scoresdata = scores[scores['Away Team'] == team2]
        
        #Goalkeeper 
        gk_score_h2 = hteam2_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a2 = ateam2_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score2 = (gk_score_h2 + gk_score_a2)/2
        avg_gk_score2 = round(avg_gk_score2, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score2
        
        #Defensive 
        defensive_score_h2 = hteam2_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a2 = ateam2_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score2 = (defensive_score_h2 + defensive_score_a2)/2
        avg_defensive_score2 = round(avg_defensive_score2, 2)
        st.caption('Defensive Score')
        avg_defensive_score2
       
        #Midfield 
        midfield_score_h2 = hteam2_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a2 = ateam2_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score2 = (midfield_score_h2 + midfield_score_a2)/2
        avg_midfield_score2 = round(avg_midfield_score2, 2)
        st.caption('Midfield Score')
        avg_midfield_score2
        
        #Offensive 
        o_score_h2 = hteam2_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a2 = ateam2_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score2 = (o_score_a2 + o_score_h2)/2
        avg_o_score2 = round(avg_o_score2, 2)
        st.caption('Offensive Score')
        avg_o_score2

with tab5:
    col1, col2 = st.columns(2)
    with col1:
        team1 = st.selectbox("Select Team 1", groupd)
        team1_data = df_rank_filter[df_rank_filter['Team Name'] == team1]
        fig_rank1 = alt.Chart(team1_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank1, use_container_width=True)
        
        hteam1_scoresdata = scores[scores['Home Team'] == team1]
        ateam1_scoresdata = scores[scores['Away Team'] == team1]
        
        #Goalkeeper 
        gk_score_h = hteam1_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a = ateam1_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score = (gk_score_h + gk_score_a)/2
        avg_gk_score = round(avg_gk_score, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score
        
        #Defensive 
        defensive_score_h = hteam1_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a = ateam1_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score = (defensive_score_h + defensive_score_a)/2
        avg_defensive_score = round(avg_defensive_score, 2)
        st.caption('Defensive Score')
        avg_defensive_score
       
        #Midfield 
        midfield_score_h = hteam1_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a = ateam1_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score = (midfield_score_h + midfield_score_a)/2
        avg_midfield_score = round(avg_midfield_score, 2)
        st.caption('Midfield Score')
        avg_midfield_score
        
        #Offensive 
        o_score_h = hteam1_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a = ateam1_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score = (o_score_a + o_score_h)/2
        avg_o_score = round(avg_o_score, 2)
        st.caption('Offensive Score')
        avg_o_score

    with col2:
        team2 = st.selectbox("Select Team 2", groupd)
        team2_data = df_rank_filter[df_rank_filter['Team Name'] == team2]
        fig_rank2 = alt.Chart(team2_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank2, use_container_width=True)
        
        hteam2_scoresdata = scores[scores['Home Team'] == team2]
        ateam2_scoresdata = scores[scores['Away Team'] == team2]
        
        #Goalkeeper 
        gk_score_h2 = hteam2_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a2 = ateam2_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score2 = (gk_score_h2 + gk_score_a2)/2
        avg_gk_score2 = round(avg_gk_score2, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score2
        
        #Defensive 
        defensive_score_h2 = hteam2_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a2 = ateam2_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score2 = (defensive_score_h2 + defensive_score_a2)/2
        avg_defensive_score2 = round(avg_defensive_score2, 2)
        st.caption('Defensive Score')
        avg_defensive_score2
       
        #Midfield 
        midfield_score_h2 = hteam2_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a2 = ateam2_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score2 = (midfield_score_h2 + midfield_score_a2)/2
        avg_midfield_score2 = round(avg_midfield_score2, 2)
        st.caption('Midfield Score')
        avg_midfield_score2
        
        #Offensive 
        o_score_h2 = hteam2_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a2 = ateam2_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score2 = (o_score_a2 + o_score_h2)/2
        avg_o_score2 = round(avg_o_score2, 2)
        st.caption('Offensive Score')
        avg_o_score2

with tab6:
    col1, col2 = st.columns(2)
    with col1:
        team1 = st.selectbox("Select Team 1", groupe)
        team1_data = df_rank_filter[df_rank_filter['Team Name'] == team1]
        fig_rank1 = alt.Chart(team1_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank1, use_container_width=True)
        
        hteam1_scoresdata = scores[scores['Home Team'] == team1]
        ateam1_scoresdata = scores[scores['Away Team'] == team1]
        
        #Goalkeeper 
        gk_score_h = hteam1_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a = ateam1_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score = (gk_score_h + gk_score_a)/2
        avg_gk_score = round(avg_gk_score, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score
        
        #Defensive 
        defensive_score_h = hteam1_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a = ateam1_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score = (defensive_score_h + defensive_score_a)/2
        avg_defensive_score = round(avg_defensive_score, 2)
        st.caption('Defensive Score')
        avg_defensive_score
       
        #Midfield 
        midfield_score_h = hteam1_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a = ateam1_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score = (midfield_score_h + midfield_score_a)/2
        avg_midfield_score = round(avg_midfield_score, 2)
        st.caption('Midfield Score')
        avg_midfield_score
        
        #Offensive 
        o_score_h = hteam1_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a = ateam1_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score = (o_score_a + o_score_h)/2
        avg_o_score = round(avg_o_score, 2)
        st.caption('Offensive Score')
        avg_o_score
    
    with col2:
        team2 = st.selectbox("Select Team 2", groupe)
        team2_data = df_rank_filter[df_rank_filter['Team Name'] == team2]
        #st.write(team2_data)
        fig_rank2 = alt.Chart(team2_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank2, use_container_width=True)
        
        hteam2_scoresdata = scores[scores['Home Team'] == team2]
        ateam2_scoresdata = scores[scores['Away Team'] == team2]
        
        #Goalkeeper 
        gk_score_h2 = hteam2_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a2 = ateam2_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score2 = (gk_score_h2 + gk_score_a2)/2
        avg_gk_score2 = round(avg_gk_score2, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score2
        
        #Defensive 
        defensive_score_h2 = hteam2_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a2 = ateam2_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score2 = (defensive_score_h2 + defensive_score_a2)/2
        avg_defensive_score2 = round(avg_defensive_score2, 2)
        st.caption('Defensive Score')
        avg_defensive_score2
       
        #Midfield 
        midfield_score_h2 = hteam2_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a2 = ateam2_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score2 = (midfield_score_h2 + midfield_score_a2)/2
        avg_midfield_score2 = round(avg_midfield_score2, 2)
        st.caption('Midfield Score')
        avg_midfield_score2
        
        #Offensive 
        o_score_h2 = hteam2_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a2 = ateam2_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score2 = (o_score_a2 + o_score_h2)/2
        avg_o_score2 = round(avg_o_score2, 2)
        st.caption('Offensive Score')
        avg_o_score2

with tab7:
    col1, col2 = st.columns(2)
    with col1:
        team1 = st.selectbox("Select Team 1", groupf)
        team1_data = df_rank_filter[df_rank_filter['Team Name'] == team1]
        fig_rank1 = alt.Chart(team1_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank1, use_container_width=True)
        
        hteam1_scoresdata = scores[scores['Home Team'] == team1]
        ateam1_scoresdata = scores[scores['Away Team'] == team1]
        
        #Goalkeeper 
        gk_score_h = hteam1_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a = ateam1_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score = (gk_score_h + gk_score_a)/2
        avg_gk_score = round(avg_gk_score, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score
        
        #Defensive 
        defensive_score_h = hteam1_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a = ateam1_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score = (defensive_score_h + defensive_score_a)/2
        avg_defensive_score = round(avg_defensive_score, 2)
        st.caption('Defensive Score')
        avg_defensive_score
       
        #Midfield 
        midfield_score_h = hteam1_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a = ateam1_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score = (midfield_score_h + midfield_score_a)/2
        avg_midfield_score = round(avg_midfield_score, 2)
        st.caption('Midfield Score')
        avg_midfield_score
        
        #Offensive 
        o_score_h = hteam1_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a = ateam1_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score = (o_score_a + o_score_h)/2
        avg_o_score = round(avg_o_score, 2)
        st.caption('Offensive Score')
        avg_o_score
    
    with col2:
        team2 = st.selectbox("Select Team 2", groupf)
        team2_data = df_rank_filter[df_rank_filter['Team Name'] == team2]
        #st.write(team2_data)
        fig_rank2 = alt.Chart(team2_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank2, use_container_width=True)
        
        hteam2_scoresdata = scores[scores['Home Team'] == team2]
        ateam2_scoresdata = scores[scores['Away Team'] == team2]
        
        #Goalkeeper 
        gk_score_h2 = hteam2_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a2 = ateam2_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score2 = (gk_score_h2 + gk_score_a2)/2
        avg_gk_score2 = round(avg_gk_score2, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score2
        
        #Defensive 
        defensive_score_h2 = hteam2_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a2 = ateam2_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score2 = (defensive_score_h2 + defensive_score_a2)/2
        avg_defensive_score2 = round(avg_defensive_score2, 2)
        st.caption('Defensive Score')
        avg_defensive_score2
       
        #Midfield 
        midfield_score_h2 = hteam2_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a2 = ateam2_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score2 = (midfield_score_h2 + midfield_score_a2)/2
        avg_midfield_score2 = round(avg_midfield_score2, 2)
        st.caption('Midfield Score')
        avg_midfield_score2
        
        #Offensive 
        o_score_h2 = hteam2_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a2 = ateam2_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score2 = (o_score_a2 + o_score_h2)/2
        avg_o_score2 = round(avg_o_score2, 2)
        st.caption('Offensive Score')
        avg_o_score2

with tab8:
    col1, col2 = st.columns(2)
    with col1:
        team1 = st.selectbox("Select Team 1", groupg)
        team1_data = df_rank_filter[df_rank_filter['Team Name'] == team1]
        fig_rank1 = alt.Chart(team1_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank1, use_container_width=True)
        
        hteam1_scoresdata = scores[scores['Home Team'] == team1]
        ateam1_scoresdata = scores[scores['Away Team'] == team1]
        
        #Goalkeeper 
        gk_score_h = hteam1_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a = ateam1_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score = (gk_score_h + gk_score_a)/2
        avg_gk_score = round(avg_gk_score, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score
        
        #Defensive 
        defensive_score_h = hteam1_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a = ateam1_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score = (defensive_score_h + defensive_score_a)/2
        avg_defensive_score = round(avg_defensive_score, 2)
        st.caption('Defensive Score')
        avg_defensive_score
       
        #Midfield 
        midfield_score_h = hteam1_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a = ateam1_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score = (midfield_score_h + midfield_score_a)/2
        avg_midfield_score = round(avg_midfield_score, 2)
        st.caption('Midfield Score')
        avg_midfield_score
        
        #Offensive 
        o_score_h = hteam1_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a = ateam1_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score = (o_score_a + o_score_h)/2
        avg_o_score = round(avg_o_score, 2)
        st.caption('Offensive Score')
        avg_o_score
    
    with col2:
        team2 = st.selectbox("Select Team 2", groupg)
        team2_data = df_rank_filter[df_rank_filter['Team Name'] == team2]
        #st.write(team2_data)
        fig_rank2 = alt.Chart(team2_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank2, use_container_width=True)
        
        hteam2_scoresdata = scores[scores['Home Team'] == team2]
        ateam2_scoresdata = scores[scores['Away Team'] == team2]
        
        #Goalkeeper 
        gk_score_h2 = hteam2_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a2 = ateam2_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score2 = (gk_score_h2 + gk_score_a2)/2
        avg_gk_score2 = round(avg_gk_score2, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score2
        
        #Defensive 
        defensive_score_h2 = hteam2_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a2 = ateam2_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score2 = (defensive_score_h2 + defensive_score_a2)/2
        avg_defensive_score2 = round(avg_defensive_score2, 2)
        st.caption('Defensive Score')
        avg_defensive_score2
       
        #Midfield 
        midfield_score_h2 = hteam2_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a2 = ateam2_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score2 = (midfield_score_h2 + midfield_score_a2)/2
        avg_midfield_score2 = round(avg_midfield_score2, 2)
        st.caption('Midfield Score')
        avg_midfield_score2
        
        #Offensive 
        o_score_h2 = hteam2_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a2 = ateam2_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score2 = (o_score_a2 + o_score_h2)/2
        avg_o_score2 = round(avg_o_score2, 2)
        st.caption('Offensive Score')
        avg_o_score2

with tab9:
    col1, col2 = st.columns(2)
    with col1:
        team1 = st.selectbox("Select Team 1", grouph)
        team1_data = df_rank_filter[df_rank_filter['Team Name'] == team1]
        fig_rank1 = alt.Chart(team1_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank1, use_container_width=True)
        
        hteam1_scoresdata = scores[scores['Home Team'] == team1]
        ateam1_scoresdata = scores[scores['Away Team'] == team1]
        
        #Goalkeeper 
        gk_score_h = hteam1_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a = ateam1_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score = (gk_score_h + gk_score_a)/2
        avg_gk_score = round(avg_gk_score, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score
        
        #Defensive 
        defensive_score_h = hteam1_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a = ateam1_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score = (defensive_score_h + defensive_score_a)/2
        avg_defensive_score = round(avg_defensive_score, 2)
        st.caption('Defensive Score')
        avg_defensive_score
       
        #Midfield 
        midfield_score_h = hteam1_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a = ateam1_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score = (midfield_score_h + midfield_score_a)/2
        avg_midfield_score = round(avg_midfield_score, 2)
        st.caption('Midfield Score')
        avg_midfield_score
        
        #Offensive 
        o_score_h = hteam1_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a = ateam1_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score = (o_score_a + o_score_h)/2
        avg_o_score = round(avg_o_score, 2)
        st.caption('Offensive Score')
        avg_o_score
    
    with col2:
        team2 = st.selectbox("Select Team 2", grouph)
        team2_data = df_rank_filter[df_rank_filter['Team Name'] == team2]
        fig_rank2 = alt.Chart(team2_data).mark_line().encode(
            x = alt.X('Date', title = 'Year'),
            y = alt.Y('Value', title = 'Fifa Ranking', scale=alt.Scale(reverse = True, zero=False)),
            tooltip=['Team Name', 'Date', 'Value']
        ).interactive()
        st.altair_chart(fig_rank2, use_container_width=True)
        
        hteam2_scoresdata = scores[scores['Home Team'] == team2]
        ateam2_scoresdata = scores[scores['Away Team'] == team2]
        
        #Goalkeeper 
        gk_score_h2 = hteam2_scoresdata['Home Team Goalkeeper Score'].mean()
        gk_score_a2 = ateam2_scoresdata['Away Team Goalkeeper Score'].mean()
        avg_gk_score2 = (gk_score_h2 + gk_score_a2)/2
        avg_gk_score2 = round(avg_gk_score2, 2)
        st.caption('Goalkeeper Score')
        avg_gk_score2
        
        #Defensive 
        defensive_score_h2 = hteam2_scoresdata['Home Team Mean Defense Score'].mean()
        defensive_score_a2 = ateam2_scoresdata['Away Team Mean Defense Score'].mean()
        avg_defensive_score2 = (defensive_score_h2 + defensive_score_a2)/2
        avg_defensive_score2 = round(avg_defensive_score2, 2)
        st.caption('Defensive Score')
        avg_defensive_score2
       
        #Midfield 
        midfield_score_h2 = hteam2_scoresdata['Home Team Mean Midfield Score'].mean()
        midfield_score_a2 = ateam2_scoresdata['Away Team Mean Midfield Score'].mean()
        avg_midfield_score2 = (midfield_score_h2 + midfield_score_a2)/2
        avg_midfield_score2 = round(avg_midfield_score2, 2)
        st.caption('Midfield Score')
        avg_midfield_score2
        
        #Offensive 
        o_score_h2 = hteam2_scoresdata['Home Team Mean Offense Score'].mean()
        o_score_a2 = ateam2_scoresdata['Away Team Mean Offense Score'].mean()
        avg_o_score2 = (o_score_a2 + o_score_h2)/2
        avg_o_score2 = round(avg_o_score2, 2)
        st.caption('Offensive Score')
        avg_o_score2
        
