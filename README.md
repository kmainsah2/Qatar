# Analyzing FIFA World Cup Teams

Streamlit App:

## Research Questions:
1. What were the rankings of each of the 32 World Cup teams leading up to the Qatar World Cup?
2. What are the respective ratings of each team? 


## In this app:
In this app you will be able to analyze all 32 World Cup teams in the 2023 FIFA World Cup in their respective groups.
  1. Group A: Senegal, Qatar, Netherlands, Ecuador
  2. Group B: Iran, England, USA, Wales
  3. Group C: Argentina, Saudi Arabia, Mexico, Poland
  4. Group D: Denmark, Tunisia, France, Australia
  5. Group E: Germany, Japan, Spin, Costa Rica
  6. Group F: Morocco, Croatia, Belgium, Canada
  7. Group G: Switzerland, Cameroon, Brazil, Serbia
  8. Group H: Uruguay, South Korea Portugal, Ghana

You will be able to analyze the following from each team:
  1. FIFA Rankings over leading up to the Qatar World Cup
  2. Goalkeeper, Defensive, Midfield, and Offensive Scores


## Data/Operation Abstraction Design: 
This data is gathered by aggregating FIFA Rankings data of the 32 teams as well as their scores from their individual matches. The dataset was filtered to only include data from the year 2018 and after. This is because the teams should be analyzed from their matches following the last World Cup. 

  **Rankings:**
  In order to visualize the data, a line graph was created, but the y-axis (FIFA Rankings) was inverted. The graph was inverted to show that a team’s      improvement in rank was parrallel with the direction of the graph. 

  **Scores:**
  The mean scores were aggregated from each of the 32 teams and their respective scores were averaged from the past 4 years.



## Future Work:
- Add a live dashboard that could scrub the match data live
- Add scores from each of the games which will allow for further analysis of the entire tournament



