import sys
import pyperclip

social_media_links = {
    "twitter": "https://twitter.com/taeluralexis",
    "facebook": "https://facebook.com/taeluralexis",
    "twitch": "https://twitch.tv/cyberbarbie",
    "youtube": "https://youtube.com/taeluralexis",
    "blog": "https://taeluralexis.com",
    "intro": "Follow my social media links to stay connected! My Twitter is https://twitter.com/taeluralexis, my Twitch is https://twitch.com/cyberbarbie and https://youtube.com/taeluralexis for my youtube channel! I also create coding tutorials at https://taeluralexis.com!"
}

if len(sys.argv) < 2: 
    print("Usage: python sm.py [social_media] - copy account url")
    sys.exit()

account = sys.argv[1]

if account in social_media_links:
    pyperclip.copy(social_media_links[account])
    print(f"URL for {account} copied to the clipboard.")
else:
    print(f"There is no account named {account}")

