import logging

logger = logging.getLogger(__name__)

def adjust_preferences(current_preferences, post_tags, weight, user_tags):
    logger.info("Adjusting preferences for user.")
    logger.info(f"Initial preferences: {current_preferences}")
    logger.info(f"Post tags: {post_tags}")
    logger.info(f"Interaction weight: {weight}")
    logger.info(f"User tag list: {user_tags}")

    if not current_preferences:
        current_preferences = {}
    
    for tag in post_tags:
        if tag.name not in current_preferences:
            current_preferences[tag.name] = 0

    if user_tags is None:
        user_tags = []

    for tag in post_tags:
        tag_name = tag.name
        current_preferences[tag_name] += weight
        if tag_name not in user_tags:
            user_tags.append(tag_name)

    logger.info(f"Preferences after updating with weights: {current_preferences}")

    total_weight = sum(current_preferences.values())
    if total_weight > 0:
        current_preferences = {
            tag: round((value / total_weight) * 100, 2)
            for tag, value in current_preferences.items()
        }
    else:
        equal_share = round(100 / len(current_preferences), 2) if current_preferences else 0
        current_preferences = {
            tag: equal_share for tag in current_preferences.keys()
        }

    if len(current_preferences) > 1:
        current_preferences = {
            tag: round(100 / len(current_preferences), 2)
            for tag in current_preferences.keys()
        }

    logger.info(f"Final normalized preferences: {current_preferences}")
    return current_preferences, user_tags
