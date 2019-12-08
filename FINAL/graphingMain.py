from CSVtoSortedDataFrame import *
import pandas_bokeh
import pandas
#from bokeh.plotting import figure, output_file, show



def plot_line(dataFrame,name):
    #dataFrame.score = pandas.to_numeric(dataFrame.score)
    dataFrame.comms_num = pandas.to_numeric(dataFrame.comms_num)
    p_line = dataFrame.plot_bokeh(
        kind = "bar",
        title = name,
        alpha = 0.6,
        figsize = (1000,800),
        show_figure = False)
    p_line.xaxis.visible = False
    return p_line


def plot_scatter(dataFrame, name):
    p_scatter = dataFrame.plot_bokeh.scatter(
        x = "comms_num",
        y = "score",
        figsize = (1000,800),
        title = name,
        return_html = True,
        show_figure = True,
        hovertool_string = """
                          <div>
                              <div>
                                  <span style = "font-size: 17px; font-weight: bold;"> score: </span>
                                  <span style = "font-size: 14px; color: #FF0000;">@{score}</span>
                              </div>
                              <div>
                                  <span style = "font-size: 17px; font-weight: bold;"> comments number: </span>
                                  <span style = "font-size: 14px; color: #FF0000;">@{comms_num}</span>
                              </div>
                              <div>
                                  <span style = "font-size: 17px; font-weight: bold;"> title: </span>
                                  <span style = "font-size: 14px; color: #FF0000;">@{title}</span>
                              </div>
                          </div>""")
    return p_scatter
