from bokeh.plotting import figure, show

p = figure(width=400, height=400)

# add a scatter circle renderer with a size, color, and alpha
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p.scatter(x, y, size=20, color="navy", alpha=0.5, marker="plus")

# show the results
show(p)