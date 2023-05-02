import re

validate_url = lambda game_url: re.match(r"^https:\/\/www\.chess\.com\/game\/live\/\d+\?username=[a-zA-Z0-9_-]+$", game_url)