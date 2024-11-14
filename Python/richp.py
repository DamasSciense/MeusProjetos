from rich import print

# lady_melamor1 = {
#     "name": "Lady Melamor1",
#     "real_name": "Unknown",
#     "description": "Lady Melamor1 is an online persona known for her content on social media, particularly in fashion, lifestyle, and entertainment.",
#     "social_media": {
#         "Instagram": "https://instagram.com/ladymelamor1",
#         "TikTok": "https://tiktok.com/@ladymelamor1",
#         "YouTube": "https://youtube.com/@ladymelamor1",
#     },
#     "content_focus": [
#         "Fashion",
#         "Lifestyle",
#         "Vlogs",
#         "Entertainment",
#     ],
#     "location": "Unknown",
#     "followers": {
#         "Instagram": 50000,
#         "TikTok": 100000,
#         "YouTube": 20000,
#     },
#     "recent_achievements": [
#         "Collaborated with top fashion brands",
#         "Reached 100k followers on TikTok",
#         "Featured in a popular fashion magazine",
#     ],
#     "contact_info": {
#         "email": "contact@ladymelamor1.com",
#         "business_inquiries": "business@ladymelamor1.com",
#     },
#     "active_since": 2021
# }

# # Print the dictionary
# print(lady_melamor1)

from rich.console import Console
from rich.theme import Theme
from rich.traceback import install

install()

custom_theme = Theme({'error': 'bold red', 'warning': 'bold yellow'})

console = Console(theme=custom_theme)

def compare_numbers(a, b):
    console.log(log_locals=True)
    if a > b:
        console.print(f"{a} is greater than {b}", style="bold green")
    elif a < b:
        console.print(f"{a} is less than {b}", style="warning")
    else:
        console.print(f"{a} is equal to {b}")

compare_numbers(5,10)
compare_numbers(10,5)
compare_numbers(5,5)

compare_numbers(5, "damas")