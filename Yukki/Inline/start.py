from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="โ๏ธ Quality", callback_data="AQ"),
            InlineKeyboardButton(text="๐ Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="๐ฎโโ๏ธ Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="๐ฅ Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="Close ๐", callback_data="close"),
        ],
    ]
    return f"โ  **Rose Bot VC Settings**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="๐ Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="๐ง Settings", callback_data="settingm"
                )
            ],
        ]
        return f"๐  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="๐ Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="๐ง Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="๐จSupport Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"๐  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="๐ Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="๐ง Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="๐จOfficial Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"๐  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="๐ Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="๐ง Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="๐จOfficial Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="๐จSupport Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"๐  **This is {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="๐ Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "โ Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"๐  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="๐ Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "โ Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="๐จSupport Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"๐  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="๐ Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "โ Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="๐จOfficial Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"๐  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="๐ Helper Commands Menu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "โ Add me to your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="๐จOfficial Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="๐จSupport Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"๐  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="โ๏ธ Quality", callback_data="AQ"),
            InlineKeyboardButton(text="๐ Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="๐ฎโโ๏ธ Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="๐ฅ Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="Close ๐", callback_data="close"),
        ],
    ]
    return f"โ  **Rose Bot VC Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="๐ Reset Audio Volume", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="โขLow Volโข", callback_data="LV"),
            InlineKeyboardButton(text="โขMedium Volโข", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="โขHigh Volโข", callback_data="HV"),
            InlineKeyboardButton(text="โขAmplified Volโข", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="๐? Custom Volume ๐?", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="๐ Go back", callback_data="settingm")],
    ]
    return f"โ  **Rose Bot VC Settings**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="๐? Custom Volume ๐?", callback_data="AV")],
    ]
    return f"โ  **Rose Bot VC Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="๐ฅ Everyone", callback_data="EVE"),
            InlineKeyboardButton(text="๐ Admins", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="๐ Authorized Users Lists", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="๐ Go back", callback_data="settingm")],
    ]
    return f"โ  **Rose Bot VC Settings**  ", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="โ๏ธ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="๐พ Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="๐ป Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="๐ฝ Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="๐ Go back", callback_data="settingm")],
    ]
    return f"โ  **Rose Bot VC Settings** ", buttons
