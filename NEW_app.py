import ipywidgets as widgets
from IPython.display import display
from IPython.display import Image
image_widget = Image(filename='IUJ.jpg')
text_widget = widgets.HTML(value="<h1>IUJ. WELCOME TO Investment and Machine Learning COURSE</h1>")
app = widgets.VBox([image_widget, text_widget])
