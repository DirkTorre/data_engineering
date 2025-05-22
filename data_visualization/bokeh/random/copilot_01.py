"""
In Bokeh, you can add filters to your data using the CDSView (ColumnDataSource View) in combination with GroupFilter, IndexFilter, or BooleanFilter. Filters allow you to control which subset of your data is displayed in your plots.

Here’s a concise guide with an example:

Steps to Add Filters in Bokeh
Create a ColumnDataSource: This is the data source for your plot.
Define a Filter: Use one of Bokeh's filter classes (GroupFilter, IndexFilter, or BooleanFilter).
Create a CDSView: Combine the ColumnDataSource with the filter.
Apply the View to Your Plot: Pass the CDSView to the view parameter of your glyph.
Example: Filtering Data by a Category"
"""


"""
checkboxgroup: https://www.geeksforgeeks.org/interactively-displaying-and-hiding-lines-in-a-bokeh-plot/
IntersectionFilter: https://docs.bokeh.org/en/latest/docs/reference/models/filters.html#bokeh.models.IntersectionFilter

"""

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter, Column, Panel, TabPanel, Tabs, CheckboxGroup

# Step 1: Create a ColumnDataSource
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [6, 7, 2, 4, 5],
    'category': ['A', 'B', 'A', 'B', 'A'],
    'watched': ['yes', 'no', 'yes', 'no', 'yes']
}
source = ColumnDataSource(data)

# Step 2: Define a GroupFilter (filtering for category 'A')
filter_a = GroupFilter(column_name='category', group='A')
filter_b = GroupFilter(column_name='category', group='B')

# Step 3: Create a CDSView with the filter
view_a = CDSView(filter=filter_a)
view_b = CDSView(filter=filter_b)

# Step 4: Create a plot and apply the view
plot_a = figure(title="Filtered Data Example", x_axis_label='x', y_axis_label='y')
plot_a.circle('x', 'y', source=source, view=view_a, size=10, color="blue", legend_label="Category A", name="cat_a")


plot_b = figure(title="Filtered Data Example", x_axis_label='x', y_axis_label='y')
plot_b.square('x', 'y', source=source, view=view_b, size=10, color="green", legend_label="Category B", name="cat_b")


all_tabs = Tabs(tabs=[
    TabPanel(child=plot_a, title="cat A"),
    TabPanel(child=plot_b, title="cat B")
])

show(all_tabs)

# Other Filter Types

# IndexFilter: Filters rows by their index.

# from bokeh.models import IndexFilter
# index_filter = IndexFilter(indices=[0, 2, 4])  # Only show rows 0, 2, and 4


# BooleanFilter: Filters rows based on a boolean mask.

# from bokeh.models import BooleanFilter
# boolean_filter = BooleanFilter(booleans=[True, False, True, False, True])


# By combining these filters, you can create dynamic and interactive visualizations tailored to specific subsets of your data.