import random

# Define a set of 'digital assets' (products, articles, services) that can be discovered
digital_assets = {
    "eco_mug_store_A": {
        "name": "Sustainable Sip Mugs - Online Store",
        "url": "https://sustainablesip.com",
        "keywords": ["eco-friendly", "mug", "reusable", "sustainable", "shop"]
    },
    "eco_mug_store_B": {
        "name": "Green Earth Ceramics - Artisan Mugs",
        "url": "https://greenearthceramics.org",
        "keywords": ["ceramic", "eco", "mug", "artisan", "handmade", "store"]
    },
    "blog_post_eco_living": {
        "name": "Top 5 Eco-Friendly Habits for Your Home",
        "url": "https://ecolife.blog/habits",
        "keywords": ["eco-friendly", "habits", "sustainability", "blog", "tips"]
    },
    "influencer_review_A": {
        "name": "Review: Sustainable Sip Mug by @EcoWarrior (Social Media)",
        "url": "https://instagram.com/ecowarrior/post123",
        "keywords": ["review", "mug", "sustainable", "social media", "influencer"]
    },
    "community_forum_thread": {
        "name": "Best Reusable Mugs Discussion (Zero Waste Forum)",
        "url": "https://zerowasteforum.com/mugs",
        "keywords": ["reusable", "mug", "forum", "recommendations", "community"]
    }
}

def simulate_search_engine(query):
    """Simulates discovery via a traditional search engine (like Google)."""
    print(f"\n--- Simulating Search Engine for '{query}' ---")
    results = []
    query_terms = [q.lower() for q in query.split()]
    for key, asset in digital_assets.items():
        # Check if any query term matches any keyword of the asset
        if any(q_term in k.lower() for q_term in query_terms for k in asset["keywords"]):
            results.append(asset)
    
    if results:
        print(f"  Found {len(results)} potential results via search:")
        for i, res in enumerate(results):
            print(f"    {i+1}. '{res['name']}' ({res['url']})")
        # Simulate clicking the first relevant result
        print(f"  --> User clicked on '{results[0]['name']}'.") # Illustrates discovery via traditional search
        return results[0]
    else:
        print("  No direct search results found for this query.")
        return None

def simulate_social_media_feed(user_interest):
    """Simulates discovery through a social media feed or ad."""
    print(f"\n--- Simulating Social Media Feed for '{user_interest}' ---")
    # Simulate an algorithm showing relevant content or an ad based on user interest
    if "eco-friendly mug" in user_interest.lower() or "sustainable products" in user_interest.lower():
        print("  Scrolling through feed... An influencer post or sponsored content appears!")
        # This represents discovery through platforms like Instagram, TikTok, Facebook.
        print(f"  --> User saw and clicked on '{digital_assets['influencer_review_A']['name']}'.")
        return digital_assets["influencer_review_A"]
    elif "sustainability tips" in user_interest.lower():
        print("  Scrolling through feed... A sponsored post for a blog appears!")
        print(f"  --> User saw and clicked on '{digital_assets['blog_post_eco_living']['name']}'.")
        return digital_assets["blog_post_eco_living"]
    print("  No directly relevant social media content found in this scroll.")
    return None

def simulate_referral_or_content_platform(source_type, source_context):
    """Simulates discovery via a direct link, referral from another site, or content platform."""
    print(f"\n--- Simulating Discovery via {source_type} ({source_context}) ---")
    if source_type == "Blog Referral" and "eco-living" in source_context.lower():
        print("  User was reading an eco-living blog and clicked a product link.")
        # This illustrates discovery through blogs, news sites, or curated content platforms.
        print(f"  --> User found '{digital_assets['eco_mug_store_A']['name']}'.")
        return digital_assets["eco_mug_store_A"]
    elif source_type == "Community Forum" and "zero waste" in source_context.lower():
        print("  User actively participating in a zero-waste community forum.")
        # This illustrates discovery through niche communities, forums, Reddit, etc.
        print(f"  --> User found '{digital_assets['community_forum_thread']['name']}'.")
        return digital_assets["community_forum_thread"]
    elif source_type == "Direct Access" and "greenearthceramics" in source_context.lower():
        print("  User typed the URL directly or used a bookmark.")
        print(f"  --> User directly accessed '{digital_assets['eco_mug_store_B']['name']}'.")
        return digital_assets["eco_mug_store_B"]
    print(f"  No specific asset found via {source_type} for '{source_context}'.")
    return None

# --- Main Simulation --- 
print("Welcome to the Digital Discovery Paths Simulator!")
print("This simulation demonstrates how users can find information or products through various digital 'entry gates', not just traditional search engines.")
print("It highlights the importance of an 'omnichannel' approach for digital presence.")

# Scenario: A user is looking for eco-friendly products, specifically coffee mugs.
print("\n=================================================================")
print("User Scenario: A person is interested in 'eco-friendly coffee mugs'.")
print("=================================================================")

# Path 1: Traditional Search Engine (Google-like)
# This represents the classic SEO-driven discovery path.
found_item_1 = simulate_search_engine("eco-friendly coffee mugs")

# Path 2: Social Media Discovery
# This represents discovery through platforms like Instagram, TikTok, or Facebook feeds.
found_item_2 = simulate_social_media_feed("eco-friendly mug reviews")

# Path 3: Referral from a Content Platform (e.g., a blog)
# This represents discovery through curated content, articles, or news sites.
found_item_3 = simulate_referral_or_content_platform("Blog Referral", "eco-living product reviews")

# Path 4: Community Forum Discovery
# This represents discovery through niche communities, forums, or discussion boards.
found_item_4 = simulate_referral_or_content_platform("Community Forum", "zero waste lifestyle")

# Path 5: Direct Access (e.g., from a print ad, word-of-mouth, or prior knowledge)
# This represents direct navigation, often a result of offline marketing or strong brand recall.
found_item_5 = simulate_referral_or_content_platform("Direct Access", "greenearthceramics.org")

print("\n=================================================================")
print("--- Simulation Complete ---")
print("The simulation shows how the same (or similar) products/information can be discovered through multiple digital channels.")
print("This reinforces the article's point: relying solely on traditional search engines is no longer sufficient; an omnichannel strategy is key.")
print("=================================================================")
