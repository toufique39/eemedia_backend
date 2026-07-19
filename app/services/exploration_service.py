from collections import defaultdict


def apply_exploration(ranked, profile):

    if len(ranked) <= 5:
        return ranked

    categories = profile.get("categories", {})

    if not categories:
        return ranked

    # User-এর সবচেয়ে পছন্দের Category
    favorite_category = max(
        categories,
        key=categories.get,
    )

    favorite = []
    explore = []

    for item in ranked:

        category = item["reel"].get(
            "finalCategory",
            "",
        )

        if category == favorite_category:
            favorite.append(item)

        else:
            explore.append(item)

    final_feed = []

    explore_index = 0

    for i, item in enumerate(favorite):

        final_feed.append(item)

        if (
            (i + 1) % 4 == 0
            and explore_index < len(explore)
        ):

            final_feed.append(
                explore[explore_index]
            )

            explore_index += 1

    final_feed.extend(
        favorite[len(final_feed):]
    )

    return final_feed