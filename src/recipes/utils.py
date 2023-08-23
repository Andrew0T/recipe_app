from recipes.models import Recipe
from io import BytesIO  
import base64
import matplotlib.pyplot as plt

#define a function that takes the ID
def get_recipename_from_id(val): 
    #this ID is used to retrieve the name from the record
    recipename=Recipe.objects.get(id=val)
    #and the name is returned back 
    return recipename

def get_graph():
    
    buffer = BytesIO()                  #create a BytesIO buffer for the image
    plt.savefig(buffer, format='png')   #create plot with bytesIO object as a file-like object. Set format to png
    buffer.seek(0)                      #set cursor to the beginning of the stream
    image_png=buffer.getvalue()         #retrieve the content of the file
    graph=base64.b64encode(image_png)   #encode the bytes-like object
    graph=graph.decode('utf-8')         #decode to get the string as output
    buffer.close()                      #free up the memory of buffer

    return graph                        #return the image/graph

#chart_type: user input o type of chart, 
#data: pandas dataframe
def get_chart(chart_type, data, **kwargs):
    #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
    #AGG is preferred solution to write PNG files
    plt.switch_backend('AGG')
    fig=plt.figure(figsize=(6,3))       #specify figure size

    if chart_type == '#1':              #select chart_type based on user input from the form
                                        #plot bar chart between recipe name on x-axis and cooking_time on y-axis
        plt.bar(data['cooking_time'], data['name'])

    elif chart_type == '#2':
        labels=kwargs.get('labels')
        plt.pie(data['cooking_time'], labels=labels)

    elif chart_type == '#3':
                                        #plot line chart based on recipe name on x-axis and meal type on y-axis
        plt.plot(data['cooking_time'], data['name'])
    else:
        print ('unknown chart type')
    
    plt.tight_layout()                  #specify layout details

    chart =get_graph()                  #render the graph to file
    return chart    
