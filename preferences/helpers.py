import logging

logger = logging.getLogger(__name__)

def adjust_preferences1(current_preferences, post_tags, weight, user_tags):
    logger.info("Adjusting preferences for user.")
    logger.info(f"Initial preferences: {current_preferences}")
    logger.info(f"Post tags: {post_tags}")
    logger.info(f"Interaction weight: {weight}")
    logger.info(f"user tag list: {user_tags}")
    
    if not current_preferences:
        current_preferences = {tag.name: 0 for tag in post_tags}
        logger.info(f"Initialized preferences: {current_preferences}")

    for tag in post_tags:
        tag_name = tag.name
        if tag_name in current_preferences:
            current_preferences[tag_name] += weight
        else:
            current_preferences[tag_name] = weight
                    
    for tag in post_tags:
        tag_name = tag.name
        if tag_name not in user_tags:
            user_tags.append(tag_name)

    total = sum(current_preferences.values())
    logger.info(f"Total preferences sum: {total}")

    if total > 0:
        for tag in current_preferences:
            current_preferences[tag] = round((current_preferences[tag] / total) * 100, 2)
    else:
        equal_share = round(100 / len(post_tags), 2)
        current_preferences = {tag.name: equal_share for tag in post_tags}

    logger.info(f"Final adjusted preferences: {current_preferences}")
    return current_preferences, user_tags
