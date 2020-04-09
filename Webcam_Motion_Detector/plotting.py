
""" Script will plot a graph displaying the timeframe when motion was detected """

from motion_detector import df
from bokeh.plotting import figure,output_file,show
from bokeh.models import HoverTool, ColumnDataSource

df["Start_String"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_String"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

g = figure(x_axis_type='datetime', height=100, width=500,title='Motion Graph',sizing_mode="scale_both")
g.yaxis.minor_tick_line_color = None
g.yaxis.ticker.desired_num_ticks=1

hover = HoverTool(tooltips=[("Start","@Start_String"),("End","@End_String")])
g.add_tools(hover)

q = g.quad(left='Start',right='End',top=1,bottom=0,color="Blue",source=cds)

output_file('Motion.html')

show(g)



































