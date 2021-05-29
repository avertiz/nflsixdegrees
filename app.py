import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from player_search import Bfs

data = Bfs(tree_filepath='players_and_teammates.json',
                player_index_filepath = 'player_index.json',
                    team_index_filepath = 'team_index.json')

app = dash.Dash(__name__)
app.title = "NFL Six Degrees"

app._layout = html.Div([

    # Header
    html.H1("NFL Six Degrees", style = {'text-align': 'center'}),

    html.Br(),html.Br(),

    # Starting Player Div
    html.Div([
        dcc.Input(id = 'start_player', type='text', placeholder= 'Starting Player', style = {'text-align': 'center', 'autocomplete':'off'})
    ], style = {'text-align': 'center'}),

    html.Br(),html.Br(),

    # Target Player Div
    html.Div([
        dcc.Input(id='target_player', type = 'text', placeholder= 'Target Player', style = {'text-align': 'center', 'autocomplete':'off'})
    ], style = {'text-align': 'center'}),

    html.Br(),

    # Submit Button Div
    html.Div([
        html.Button('Submit', id = 'submit_val', n_clicks = 0)
    ], style = {'text-align': 'center'}),

    html.Br(),

    # Return Path Div
    html.Div([
        dash_table.DataTable(id='output_table')
    ], style = {'text-align': 'center', 'width': '30%', 'justify-content': 'center'})    

])

@app.callback(
    [Output(component_id = 'output_table', component_property = 'data'),
     Output(component_id = 'output_table', component_property = 'columns')],
    [Input(component_id = 'submit_val', component_property = 'n_clicks')],
    [State(component_id='start_player', component_property='value'),
     State(component_id = 'target_player', component_property = 'value')])
def show_results_table(n_clicks, player1, player2):
    if n_clicks == 0:
        raise PreventUpdate
    elif player1 is None or player2 is None:
        header = "Please Enter Two Players"
        df = pd.DataFrame()
        cols = []
        return(header, df.to_dict('records'), cols)
    else:
        data.pretty_return(start_player=player1, target_player=player2)
        columns=[{"name":'Player', "id":'player'}, 
                 {"name":'Team', "id":'team'},
                 {"name":'Teammate', "id":'teammate'}]
        return(data.output_table.to_dict('records'), columns)

# if __name__ == '__main__':
    # app.run_server(debug=True)