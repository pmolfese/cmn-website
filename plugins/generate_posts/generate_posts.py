import datetime
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

        # Prepare context for each person's page
        slug = metadata.get("slug")

        people_info[slug] = metadata

    return people_info


def generate_talks(generator):
    """Generate custom pages for people based on their articles."""
    # Loop over all articles and filter for 'People' category (optional)
    people_dir = os.path.join(generator.settings["PATH"], "recent_posts")
    posts_list = []

    people_info = get_speaker_info(generator)

    for filename in os.listdir(people_dir):
        if not filename.endswith(".md"):
            continue

        file_path = os.path.join(people_dir, filename)
        reader = MarkdownReader(generator.settings)
        content, metadata = reader.read(file_path)

        context = {
            **metadata,
            "content": content,
            "speaker": people_info.get(metadata.get("host_slug")),
        }

        posts_list.append(context)

    posts_list.sort(
        key=lambda x: datetime.datetime.strptime(x.get("workshop_time", ""), "%B %Y"),
        reverse=True,
    )
    generator.context["posts_list"] = posts_list

    posts_dict = {}
    for post in posts_list:
        posts_dict[post["slug"]] = post
    generator.context["posts_dict"] = posts_dict


def register():
    """Register the plugin to Pelican's signal system."""
    signals.article_generator_finalized.connect(generate_talks)
