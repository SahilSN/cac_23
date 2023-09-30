import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

def generate_line(df, x_col, y_col_s, y_col_e, title):
    if (y_col_e == None):
        print("no end")
        print(df.columns[y_col_s:])
        plotly_fig = px.line(df, x=df.columns[x_col], y=df.columns[y_col_s:], title=title)
    else:
        print("end")
        print(df.columns[y_col_s:y_col_e])
        plotly_fig = px.line(df, x=df.columns[x_col], y=df.columns[y_col_s:y_col_e], title=title)
    plotly_fig.update_traces(line=dict(width=1.75))
    plotly_fig.update_layout(
        plot_bgcolor='white'
    )
    plotly_fig.update_xaxes(
        #mirror=True,
        ticks='inside',
        #showline=True,
        #linecolor='black',
        gridcolor='lightgrey'
    )  
    plotly_fig.update_yaxes(
        #mirror=True,
        ticks='inside',
        #showline=True,
        #linecolor='black',
        gridcolor='lightgrey'
    )
    #plotly_fig.show()
    div = plotly.offline.plot(plotly_fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div

def generate_pie(df,title):
    fig = px.pie(df, values=df.columns.values[1], names=df.columns.values[0],title=title)
    fig.update_layout(margin=dict(t=50, b=50, l=50, r=50))
    div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    #fig.show()
    return div


    