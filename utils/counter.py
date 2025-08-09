import os

COUNTER_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'visit_count.txt')


def read_count():
    """Read current visit count from file."""
    if not os.path.exists(COUNTER_FILE):
        return 0
    try:
        with open(COUNTER_FILE, 'r', encoding='utf-8') as f:
            return int(f.read().strip())
    except (ValueError, OSError):
        return 0


def increment_count():
    """Increment visit count and return the updated value."""
    count = read_count() + 1
    with open(COUNTER_FILE, 'w', encoding='utf-8') as f:
        f.write(str(count))
    return count
