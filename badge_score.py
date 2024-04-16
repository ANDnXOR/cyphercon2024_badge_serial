def badge_value(badge_id):
    """ Returns the value of a badge given its ID. """
    if 0 <= badge_id <= 537:
        return 10
    elif 538 <= badge_id <= 613:
        return 20
    elif 614 <= badge_id <= 699:
        return 100
    elif 700 <= badge_id <= 730:
        return 1000
    elif 731 <= badge_id <= 756:
        return 10000
    elif 757 <= badge_id <= 767:
        return 100000
    return 0

def compute_current_score(used_badges):
    """ Computes the total score given a list of used badges. """
    return sum(badge_value(badge) for badge in used_badges)

def find_min_badges(target_score, exclude_badge, already_used):
    """ Determines the minimum badges required to reach the target score using each badge only once. """
    badge_ranges = [
        (757, 767, 100000),
        (731, 756, 10000),
        (700, 730, 1000),
        (614, 699, 100),
        (538, 613, 20),
        (0, 537, 10)
    ]

    needed_badges = []
    debug_info = []
    total_points = 0

    for start, end, value in badge_ranges:
        class_points = 0
        if target_score <= 0:
            break
        for badge_id in range(end, start - 1, -1):
            if badge_id == exclude_badge or badge_id in already_used:
                continue
            if target_score >= value:
                needed_badges.append(badge_id)
                debug_info.append((badge_id, value))
                target_score -= value
                class_points += value
                total_points += value
                if target_score <= 0:
                    break
        if class_points > 0:
            debug_info.append(f"Total for {value} point badges: {class_points}")

    debug_info.append(f"Overall total: {total_points}")
    return needed_badges, debug_info

def test_badge_addition(current_score, used_badges, exclude_badge, target_score):
    """ Unit test to verify the sum of the current and added badge scores matches the target. """
    new_badges_needed, _ = find_min_badges(target_score - current_score, exclude_badge, used_badges)
    final_score = current_score + compute_current_score(new_badges_needed)
    assert final_score == target_score, "Test failed: Final score does not match target"

# User input handling
current_score = int(input("Enter the current score on the scoreboard: "))
exclude_badge = int(input("Enter the badge ID that cannot be used: "))
used_badges_input = input("Enter a comma-separated list of badge IDs already used, or press enter for none: ")
used_badges = list(map(int, used_badges_input.split(','))) if used_badges_input else []
target_score = int(input("Enter the target score you wish to reach: "))  # User specifies target score

# Determine badges to use
new_badges_needed, debug_info = find_min_badges(target_score - current_score, exclude_badge, used_badges)
print("Debugging Info:")
for info in debug_info:
    print(info)
print("New badges needed to reach the target score:", ','.join(map(str, new_badges_needed)))

# Run unit test
test_badge_addition(current_score, used_badges, exclude_badge, target_score)
