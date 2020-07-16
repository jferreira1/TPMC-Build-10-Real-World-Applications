from capture import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["start_str"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["end_str"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type="datetime", height=100, width=800, sizing_mode="scale_both", title="Motion Graph")
p.xaxis.minor_tick_line_color = None
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start: ", "@start_str"),("End: ", "@end_str")])
p.add_tools(hover)
q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)
output_file("motion_graph.html")
show(p)