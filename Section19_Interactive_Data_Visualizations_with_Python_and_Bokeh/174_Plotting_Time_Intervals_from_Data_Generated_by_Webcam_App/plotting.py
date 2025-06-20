from Motion_Detector import df                                                                  # Importamos el DataFrame desde el archivo que lo origina
from bokeh.plotting import figure, show, output_file                                            # Biblioteca Bokeh

p = figure(title= "Motion Graph",
           toolbar_location= "above",
           x_axis_type= 'datetime',
           sizing_mode= "stretch_width",
           height= 200,
           width= 500)

p.yaxis.minor_tick_line_color = None
p.ygrid.grid_line_alpha = 0

q = p.quad(left= df["Start"],
           right= df["End"],
           bottom= 0,
           top= 1,
           color= 'green')

output_file ("Graph.html")
show(p)