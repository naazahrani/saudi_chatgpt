from string import Template

# Define the HTML template as a string
html_template = """
<!DOCTYPE html>
<html>
<head>
	<title>$title</title>
</head>
<body>
	<h1>$heading</h1>
	<p>$content</p>
</body>
</html>
"""

html_template =  """
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">$card_title</h5>
    <p class="card-text">$card_text</p>
    <a href="#" class="btn btn-primary">Book Now!</a>
  </div>
</div>
"""


# Create a Template object from the HTML template string
template = Template(html_template)

# Define the data to be substituted into the template
data = {
	"card_title": "Dr. foo",
	"card_text": "Specialized in bar stuff",
}

# Use the Template object to substitute the data into the template
output = template.substitute(data)


# Save the output to a file
with open("cards.html", "w") as f:
    f.write(output)

# Open the file in a web browser
import webbrowser
webbrowser.open("cards.html")