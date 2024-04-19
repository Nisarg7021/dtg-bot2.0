from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """
This command is used to short or convert links from first to last posts

Make the bot as an admin in your channel

Command usage: `/batch [channel id or username]`

Ex: `/batch -100xxx`
"""

START_MESSAGE ='''**Hello, {}
I Am Greylinks Official Link Converter. I Can Convert Links Directly From Your GreyMatterslinks.in Account,
    
1. Go To 👉 https://DTGLINKS.IN/member/tools/api 

2. Than Copy API Key

3. Than Type /set_api than give a single space and than paste your API Key (see example to understand more...)

/set_api(space)API Key 
(See Example.👇)
Example:** `/set_api 133fvnc53fjcfhdr5d665661fhg02315chj`

**💁‍♀️ Hit 👉 /help To Get Help.

➕ Hit 👉 /footer To Get Help About Adding your Custom Footer to bot.

➕ Hit 👉 /header To Get Help About Adding your Custom Footer to bot.**
'''


HELP_MESSAGE = '''
**Hey! My name is {firstname}. I am a DTGLINKS Pro Shortener Bot.**

Features 

- [Hyperlink](https://t.me/{username})
- Buttons convert support
- Header and Footer Text support
- Replace Username
- Banner Image

Helpful commands:

- /start: Starts me! You've probably already used this.
- /help: Sends this message; I'll tell you more about myself!
If You Have Any Problem Then contact us at - 

Available commands:

- /set_api
- /header
- /footer
- /username
- /banner_image
- /me

Use the commands to know more about the same
Below are some features I provide'''

ABOUT_TEXT =  """
**My Details:**
`🤖 Name:` ** {} **
    
`📝 Language:` [Python 3](https://www.python.org/)

`🧰 Framework:` [Pyrogram](https://github.com/pyrogram/pyrogram)

`👨‍💻 Developer:` [GreyMatter's](https://t.me/GreyMattersTech)

`📢 Support:`   [SUPPORT](mailto:contact@GreyMattersTech.com)

"""


METHOD_MESSAGE = """
Current Method: {method}
    
Methods Available:

~ `mdlink` - Change all the links of the post to your MDisk account first and then short to DTGLINKS.IN link.

~ `shortener` - Short all the links of the post to linkbnao.com link directly.

To change method, choose it from the following options:
"""

CUSTOM_ALIAS_MESSAGE = """For custom alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/example | Example"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""


CHANNELS_LIST_MESSAGE = """
List of channels that have access to this Bot:

{channels}"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup([
   
    [
        InlineKeyboardButton('Custom Alias', callback_data=f'alias_conf'),
    ],

    [
        InlineKeyboardButton('Home', callback_data='start_command')        
    ],


])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Home', callback_data=f'start_command'),
        InlineKeyboardButton('Help', callback_data=f'help_command')
    ],
    [
        InlineKeyboardButton('Close', callback_data='delete')
    ]
])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Help', callback_data=f'help_command'),
        InlineKeyboardButton('About', callback_data='about_command')
    ],
        [
        InlineKeyboardButton('Close', callback_data='delete')
    ],

])


BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'help_command')
    ],

])

USER_ABOUT_MESSAGE = """
- Website: [{base_site}](https://dtglinks.in)

- {base_site} API: {shortener_api}

- Username: @{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/shortener_api [api]`
            
Ex: `/shortener_api 9e6082cd457037f01be6631e803c60a1bab73a73`

Current Website: {base_site}

Current Shortener API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \\n

To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """Reply to the Footer Text You Want

This Text will be added to the bottom of every message caption or text

For adding line break use \\n

To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """Current Username: {username}

Usage: `/username your_username` (without @)

This username will be automatically replaced with other usernames in the post

To remove this username, `/username remove`"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""

INCLUDE_DOMAIN_TEXT = """
Use this option if you want to short only links from the following domains list.

Current Include Domain:
{}
Usage: /include_domain domain
Ex: `/include_domain t.me, stack.com`

To remove a domain,
Ex: `/include_domain remove t.me`

To remove all domains,
Ex: `/include_domain remove_all`
"""

EXCLUDE_DOMAIN_TEXT = """
Use this option if you wish to short every link on your channel but exclude only the links from the following domains list

Current Exclude Domains:
{}
Usage: /exclude_domain domain
Ex: `/exclude_domain t.me, google.com`

To remove a domain, 
Ex: `/exclude_domain remove t.me`

To remove all domains,
Ex: `/exclude_domain remove_all`
"""

BANNED_USER_TXT = """
Usage: `/ban [User ID]`
Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
