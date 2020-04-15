
from pandas_datareader import data
import datetime 
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN


#.datetime() - creates a datetime object with the Start & End dates for the period we are looking into
start = datetime.datetime(2015,11,1) 
end = datetime.datetime(2016,3,10)

df = data.DataReader(name="GOOG", data_source="yahoo", start=start, end=end)
#.DataReader() - Extract data from a wide range of Internet sources into a pandas DataFrame

""" The function below returns a string value (i.e. Increase, Decrease or Equal) based on value of c & o   """
def inc_dec(c,o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

df["Status"] = [inc_dec(c,o) for c, o in zip(df.Close, df.Open)] #Using the inc_dec() function to iterate through both the Close & Open columns, storing the result in the Status column
df["Middle"] = (df.Open+df.Close)/2 #values are the average of the Open & Close values for a given day.
df["Height"] = abs(df.Close - df.Open) #Returns absolute values for the difference between Close & Open values for a given day.


p = figure(x_axis_type='datetime', width=1000, height=300)
p.title.text = "Candlestick Chart"
p.grid.grid_line_alpha = 0.3 #Handles the transparency of the grind lines

p.segment(df.index,df.High,df.index,df.Low, color="Black")
""" .segment() - Adds the line segments with the top & low point indicating the stock's daily High & Low value """ 



""" Create rectangular glyphs depicting the range of he stock's open & close value. 
    Red boxes -  Closing price was lower than opening price
    Green boxes -  Closing price was higher than opening price """

hours = 12*60*60*1000 #Changes 12 hours into milliseconds

""" rect(x, y, width, height) - used to create a rectangular box glphy
    x & y - coordinates of the middle of the rectangle
    width - this will be the 12 hours of a trading day
    Height - difference between Close & Open values """

p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours,
    df.Height[df.Status == "Increase"],fill_color="Green",line_color = "Black") #Handles gains between open & close values
#By using an IF statement to check if the Status column shown an increase, this code will only apply to stocks with positive gains


p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours,
    df.Height[df.Status == "Decrease"],fill_color="Red",line_color = "Black") #Handles losses between open & close values   



script1, div1 = components(p)
cdn_js = CDN.js_files
cdn_css = CDN.css_files
#CDN - handles loading a minified version of bokeh for embedding

# output_file = "CS.html"
# show(p)



