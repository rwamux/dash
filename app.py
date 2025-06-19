# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 20:17:49 2021

@author: Daily
"""

import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


df = pd.read_csv('presidential_results1.csv')
df = df.drop(['district_code','parish_code','parish_name','polling_station_code','polling_station_name'],axis=1)
totals = df[['amuriat_oboi_patrick','kabuleeta_kiiza_joseph','kalembe_nancy_linda','katumba_john',
             'kyagulanyi_ssentamu_robert','mao_norbert','mayamba_la_willy','mugisha_muntu_gregg',
             'mwesigye_fred','tumukunde_henry_kakurugu','yoweri_museveni_tibuhaburwa_kaguta']].sum(axis=0)

df_totals =pd.DataFrame(totals).reset_index()
df_totals.columns = ['Candidate','Votes']
fig = px.bar(df_totals, x="Candidate", y="Votes", barmode="group",color="Votes",title="Total Votes by Candidate")
fig.update_layout(title_x=0.5)

#for pie chart1
labels1 = ['Voted','Not Voted']
values1 = [10744319,7359284]

fig1 = go.Figure(data=[go.Pie(labels=labels1,values=values1)])
fig1.update_layout(
    title_text="Registered Voters",title_x=0.4)

#for pie chart2
labels2 = ['Valid','Invalid']
values2 = [10350819,393500]
fig2 = go.Figure(data=[go.Pie(labels=labels2,values=values2)])
fig2.update_layout(
    title_text="Votes Cast",title_x=0.5)

#further analysis
central = ['BUIKWE',
'BUKOMANSIMBI',
'BUTAMBALA',
'BUVUMA',
'GOMBA',
'KALANGALA',
'KALUNGU',
'KAMPALA',
'KAYUNGA',
'KIBOGA',
'KYANKWANZI',
'LUWEERO',
'LWENGO',
'LYANTONDE',
'MASAKA',
'MITYANA',
'MPIGI',
'MUBENDE',
'MUKONO',
'NAKASEKE',
'NAKASONGOLA',
'RAKAI',
'SEMBABULE',
'WAKISO','KASSANDA','KYOTERA','LUWERO','MASAKA_CITY','SSEMBABULE']

eastern = ['AMURIA',
'BUDAKA',
'BUDUDA',
'BUGIRI',
'BUKEDEA',
'BUKWA',
'BULAMBULI',
'BUSIA',
'BUTALEJA',
'BUYENDE',
'IGANGA',
'JINJA',
'KABERAMAIDO',
'KALIRO',
'KAMULI',
'KAPCHORWA',
'KATAKWI',
'KIBUKU',
'KUMI',
'KWEEN',
'LUUKA',
'MANAFWA',
'MAYUGE',
'MBALE',
'NAMAYINGO',
'NAMUTUMBA',
'NGORA',
'PALLISA',
'SERERE',
'SIRONKO',
'SOROTI',
'TORORO','BUGWERI','BUKWO','JINJA_CITY','NAMISINDWA','BUTEBO','KALAKI','MBALE_CITY','NAMISINDWA','SOROTI_CITY']

northern = ['ABIM',
'ADJUMANI',
'AGAGO',
'ALEBTONG',
'AMOLATAR',
'AMUDAT',
'AMURU',
'APAC',
'ARUA',
'DOKOLO',
'GULU',
'KAABONG',
'KITGUM',
'KOBOKO',
'KOLE',
'KOTIDO',
'LAMWO',
'LIRA',
'MARACHA',
'MOROTO',
'MOYO',
'NAKAPIRIPIRIT',
'NAPAK',
'NEBBI',
'NWOYA',
'OTUKE',
'OYAM',
'PADER',
'YUMBE',
'ZOMBO','ARUA_CITY','GULU_CITY','LIRA_CITY','KAPELEBYONG','MADI_OKOLLO','NABILATUK','OBONGI','OMORO','PAKWACH','TEREGO','KARENGA','KWANIA']

western = ['BUHWEJU',
'BULIISA',
'BUNDIBUGYO',
'BUSHENYI',
'HOIMA',
'IBANDA',
'ISINGIRO',
'KABALE',
'KABAROLE',
'KAMWENGE',
'KANUNGU',
'KASESE',
'KIBAALE',
'KIRUHURA',
'KIRYANDONGO',
'KISORO',
'KYEGEGWA',
'KYENJOJO',
'MASINDI',
'MBARARA',
'MITOOMA',
'NTOROKO',
'NTUNGAMO',
'RUBIRIZI',
'RUKUNGIRI',
'SHEEMA','BUNYANGABU', 'FORT_PORTAL_CITY', 'HOIMA_CITY', 'KAGADI','KAKUMIRO','KAZO','KIKUUBE','KITAGWENDA','MBARARA_CITY','RUBANDA','RUKIGA','RWAMPARA']

#assign district a region
def get_region(district):
  if district in central:
    return 'Central'
  elif district in eastern:
    return 'Eastern'
  elif district in northern:
    return 'Northern'
  elif district in western:
    return 'Western'
  else:
    return 'Not Found'

df['region'] = df['district_name'].apply(get_region)

candidates = ['amuriat_oboi_patrick',
'kabuleeta_kiiza_joseph',
'kalembe_nancy_linda',
'katumba_john',
'kyagulanyi_ssentamu_robert',
'mao_norbert',
'mayamba_la_willy',
'mugisha_muntu_gregg',
'mwesigye_fred',
'tumukunde_henry_kakurugu',
'yoweri_museveni_tibuhaburwa_kaguta']

regions = ['Central','Eastern','Northern','Western']
group_labels = ['Votes']

app.layout = html.Div(children=[
    html.H1(children='Election 2021',style={
            'textAlign': 'center'
            
        }),
    html.H4(children='''
        A visualization of the results of the Uganda Presidential election 2021.
    ''',style={
        'textAlign': 'center'
            
        }),

    html.Div(

    dcc.Graph(
        id='graph1',
        figure=fig
    ),style={'display': 'block', 'width': '80%','margin-left': 'auto','margin-right': 'auto'}
    ),
    html.Div(
            [
            html.Br(),
            dcc.Graph(id = 'piechart1', figure=fig1)
            ],
            style={'display': 'inline-block', 'width': '49%'}
            ),
    html.Div([
            html.Br(),
            dcc.Graph(id= 'piechart2',figure=fig2)
            ],
            style={'display': 'inline-block', 'width': '49%','float': 'right'}
            ),
    html.Div([
            html.Br(),
            html.H6('Voting by Region',style={"text-align": "center"}),
            html.Label(['Choose candidate:'],style={'font-weight': 'bold', "text-align": "left"}),
            dcc.Dropdown(
                    id = 'candidate-region',
                    options = [{'label':i,'value':i} for i in candidates],
                    placeholder='Please select...', 
                    value = candidates[0],
                    style={'width':"100%"}
                    ),
            dcc.Graph(id = 'region-bar')
            ],
            style={'display': 'inline-block', 'width': '49%'}
    
            ),
    html.Div([
            html.Br(),
            html.H6('Distribution of Votes by Region',style={"text-align": "center"}),
            html.Label(['Choose candidate:'],style={'font-weight': 'bold', "text-align": "left"}),
            dcc.Dropdown(
                    id = 'candidate-region-dist',
                    options = [{'label':i,'value':i} for i in candidates],
                    value = candidates[0]
                    ),
            html.Label(['Choose region:'],style={'font-weight': 'bold', "text-align": "left"}),
            dcc.Dropdown(
                    id = 'region-dist',
                    options = [{'label':i,'value':i} for i in regions],
                    value = regions[0]
                    ),
            dcc.Graph(id = 'region-dist-plot')
            ],
            style={'display': 'inline-block', 'width': '49%','float': 'right'}
    
            )
    
])
    

@app.callback(
        dash.dependencies.Output('region-bar','figure'),
        [dash.dependencies.Input('candidate-region','value')])
def update_bar(candidate_name):
    test = df.groupby('region')[candidate_name].sum()
    regions_df = pd.DataFrame(test).reset_index()
    regions_df.columns = ['Region','Votes']
    fig = px.bar(regions_df, x='Region',y='Votes',color='Region')
    return fig


@app.callback(
        dash.dependencies.Output('region-dist-plot','figure'),
        [dash.dependencies.Input('candidate-region-dist','value'),
         dash.dependencies.Input('region-dist','value')]
        )
def update_distplot(candidate_name,region_name):
    test = df[df['region']==region_name][candidate_name]
    fig = ff.create_distplot([test],group_labels,show_rug=False)
    return fig
    
    
    

if __name__ == '__main__':
    app.run_server(debug=True)
