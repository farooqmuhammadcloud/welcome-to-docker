# build_dashboard.py

import plotly.express as px
import pandas as pd

# Load data
df = px.data.gapminder().query("year == 2007")

# Create a dashboard plot
fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)

# Save to HTML
fig.write_html("dashboard.html")

print("Dashboard built and saved as dashboard.html")
