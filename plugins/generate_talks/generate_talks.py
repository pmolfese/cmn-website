import os
import re
from pelican import signals
from pelican.readers import MarkdownReader
import json


def get_speaker_info(generator):
    people_dir = os.path.join(generator.settings["PATH"], "people")
    people_info = {}
    for filename in os.listdir(people_dir):
        if not filename.endswith(".md"):
            continue
        file_path = os.path.join(people_dir, filename)
        reader = MarkdownReader(generator.settings)
        _, metadata = reader.read(file_path)
        # metadata["date"] = ""
        # if not metadata["image"]:
        #     metadata["image"] = "event.jpg"

        # Prepare context for each person's page
        slug = metadata.get("slug")

        people_info[slug] = metadata

    return people_info


def generate_talks(generator):
    """Generate custom pages for people based on their articles."""
    # Loop over all articles and filter for 'People' category (optional)
    people_dir = os.path.join(generator.settings["PATH"], "recent_talks")
    talks = []

    people_info = get_speaker_info(generator)

    for filename in os.listdir(people_dir):
        if not filename.endswith(".md"):
            continue

        file_path = os.path.join(people_dir, filename)
        reader = MarkdownReader(generator.settings)
        content, metadata = reader.read(file_path)

        # Regular expression to match text inside [] and ()
        pattern = r"\[([^\]]+)\]\(([^)]+)\)"
        part_of_list = []

        for entry in metadata.get("part_of", "").split(","):
            # Extract the parts using re.search
            match = re.search(pattern, entry)

            if match:
                text = match.group(1)  # Text inside []
                link = match.group(2)  # Text inside ()
                part_of_list.append((text, link))

        links = []
        for entry in metadata.get("links", "").split(","):
            # Extract the parts using re.search
            match = re.search(pattern, entry)

            if match:
                text = match.group(1)  # Text inside []
                link = match.group(2)  # Text inside ()
                links.append((text, link))

        context = {
            **metadata,
            "content": content,
            "part_of": part_of_list,
            "links": links,
            "speaker": people_info.get(metadata.get("speaker_slug")),
            # "date": ""
        }
        talks.append(context)

    # print("TTTT: ", json.dumps(talks, indent=4))
    # print(talks)

    generator.context["events"] = talks


def register():
    """Register the plugin to Pelican's signal system."""
    signals.article_generator_finalized.connect(generate_talks)
