# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
"""
We can use the matplotlib library to visually represent the difference between
each of these time-to-complete curves. In matplotlib, there's no explicit scale
definition - each graph automatically calculates and applies scale. This is mostly
advantageous, but note that the arrays of x- and y-values must be the same size or 
you will get an error when the code is run.

Partly sourced from makeuseof (https://www.makeuseof.com/draw-graphs-jupyter-notebook/)
"""


# -

#Other matplotlib templates: linear
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8]
y=[2,4,6,8,10,12,14,16]
plt.title("Line Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
plt.show()

# +
#Other matplotlib templates: Bar graph
x=[3,4,5,6,7,8,9,10,11,12]
y=[9,16,25,36,49,64,81,100,121,144]
plt.title("Bar Chart")
plt.xlabel("time")
plt.ylabel("revenue")

plt.bar(x,y)
plt.show()
# -

#Other matplotlib templates: scatter plot
x=[3,4,5,6,7,8,9,10,11,12]
x=[9,16,25,36,49,64,81,100,121,144]
plt.title("Scatter Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.scatter(x,y)
plt.show()

#Other matplotlib templates: pie chart
x=[4,9,16,25,36]
fig=plt.figure(figsize=(9,5)) #figsize sets the aspect ratio; pandas advises 1 here
plt.pie(x, labels=("Montana", "North Dakota", "New Hampshire", "Texas", "California"),
       colors=("black","blue","red","green","#8aeb13"))
plt.title("Pie Chart")
plt.show()



