import plotly
import plotly.express as px
import plotly.graph_objs as go
    
def generate_line(df, x_col, y_col_s, y_col_e, title):
    if (y_col_e == None):
        print("no end")
        print(df.columns[y_col_s:])
        plotly_fig = px.line(df, x=df.columns[x_col], y=df.columns[y_col_s:], title=title, )
    else:
        print("end")
        print(df.columns[y_col_s:y_col_e])
        plotly_fig = px.line(df, x=df.columns[x_col], y=df.columns[y_col_s:y_col_e], title=title,)
    div = plotly.offline.plot(plotly_fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div