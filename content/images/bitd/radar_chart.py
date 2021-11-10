#!/usr/bin/env python

import plotly.graph_objects as go
import plotly.offline as pyo

categories = ['<b>GRITTY</b>: violence,<br>extortion, vice, gore, intimidation',
              '<b>SCORES</b>: being into the action,<br>performing tactical operations, stealth',
              '<b>THE FANTASTIC</b>: occult arcanes,<br>mysteries to be unfolded',
              '<b>EPIC</b>: narrowly escapes,<br>facing monsters, glory',
              '<b>ROLEPLAY</b>: interpreting<br>your character, slick talk',
              '<b>POLITICS</b>: intrigues,<br>territory fights, alliances']
categories = [*categories, categories[0]]

player_1 = [4, 4, 5, 5, 3, 4]
player_2 = [4, 5, 4, 5, 4, 5]
player_3 = [4, 5, 3, 3, 5, 4]
player_1 = [*player_1, player_1[0]]
player_2 = [*player_2, player_2[0]]
player_3 = [*player_3, player_3[0]]


fig = go.Figure(
    data=[
        go.Scatterpolar(r=player_1, theta=categories, fill='toself', name='Elliot'),
        go.Scatterpolar(r=player_2, theta=categories, fill='toself', name='Simon'),
        go.Scatterpolar(r=player_3, theta=categories, fill='toself', name='Thomas')
    ],
    layout=go.Layout(
        title=go.layout.Title(text='What my players like in BitD'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)

print(fig.to_json())
pyo.plot(fig, auto_open=False, filename="AppetencesJoueurs.html")
