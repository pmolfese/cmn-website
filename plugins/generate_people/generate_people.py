import os
from pelican import signals
from pelican.readers import MarkdownReader

def generate_people_pages(generator):
    """Generate custom pages for people based on their articles."""
    # Loop over all articles and filter for 'People' category (optional)
    people_dir = os.path.join(generator.settings['PATH'], 'people')
    people = []
    teams_dsst_member = []
    teams_mlt = []
    for filename in os.listdir(people_dir):
        if not filename.endswith('.md'):
            continue
        
        file_path = os.path.join(people_dir, filename)
        reader = MarkdownReader(generator.settings)
        content, metadata  = reader.read(file_path)
        
        # Prepare context for each person's page
        slug = metadata.get("slug")
        context = {
            **metadata,
            'content': content,
        }
        people.append(context)

        if metadata.get("team") == "Data Science and Sharing Team":
            teams_dsst_member.append(context)
        if metadata.get("team") == "Machine Learning Team":
            teams_mlt.append(context)


        # Define where to save the generated person page
        output_path = os.path.join(generator.output_path, 'people', f"{slug}.html")

        # Load the template
        template = generator.get_template('person')

        # Render the page and write it to the output directory
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Render the page and write it to the output directory
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(template.render(context))

    # Sort people by title in ascending order
    people.sort(key=lambda person: person.get('title', '').lower())
    print(people)
    generator.context['people'] = people
    generator.context['teams_dsst'] = teams_dsst_member
    generator.context['teams_mlt'] = teams_mlt

def register():
    """Register the plugin to Pelican's signal system."""
    # Connect the `generate_people_pages` function to the article generator finalization signal
    signals.article_generator_finalized.connect(generate_people_pages)
