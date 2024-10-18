import os
from pelican import signals
from pelican.readers import MarkdownReader
from pelican.contents import Content

AUTHOR = 'Quang Nguyen'
SITENAME = 'Center for Multimodal Neuroimaging'

PATH = "content"

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/cmn-themes"
# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
STATIC_PATHS = ['images', 'pdfs', 'extra/CNAME']

MARKDOWN = {
    'extensions': ['extra', 'codehilite', 'toc'],
    'output_format': 'html5',
}



def generate_people(generator):
    people = []
    
    # Define the path to the people folder
    base_path = os.path.join(generator.settings['PATH'], 'people')

    # Iterate through each markdown file in the folder
    for filename in os.listdir(base_path):
        if filename.endswith('.md'):
            file_path = os.path.join(base_path, filename)

            # Parse the markdown file
            reader = MarkdownReader(generator.settings)
            content, metadata  = reader.read(file_path)

            # Append the collected data to the people list
            people.append({
                **metadata,
                'content': content,
            })
    
    # Store the collected people information in the generator context
    print("people: ", people)
    generator.context['people'] = people

# Register the function to run when the context is initialized
def register():
    signals.generator_init.connect(generate_people)

# Call the register function
register()
