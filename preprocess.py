import json

def extract_metadata(post):
    pass
    return {
        'line_count':2,
        'language':'English',
        'tags':['Mental Health', 'Motivation']
    }

def process_post(raw_file_path, processed_file_path="data/processed_posts.json"):
    enriched_posts = []
    with open(raw_file_path, encoding="utf-8") as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post)
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)
    
    for epost in enriched_posts:
        print(epost)

if __name__ == "__main__":
    process_post("data/raw_posts.json", "data/processed_posts.json")
