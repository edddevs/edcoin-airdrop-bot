# --------------------------------------------- #
# Plugin Name           : TelegramAirdropBot    #
# Author Name           : fabston               #
# File Name             : config.py             #
# --------------------------------------------- #

# Enable / disable the airdrop
airdrop_live = True

# Telegram
api_token = (
    "5111009524:AAF7xuaSYvLP32UZP3oHHsezOFRldIzc-YM"  # More: https://core.telegram.org/bots#3-how-do-i-create-a-bot
)

host = ""  # ip/host where the bot is running

log_channel = -1001156504121  # Channel ID. Example: -1001355597767
admins = [5183677100]  # Telegram User ID's. Admins are able to execute command "/airdroplist"
airdrop_cap = 200  # Max airdrop submissions that are being accepted
wallet_changes = 3  # How often a user is allowed to change their wallet address

# MySQL Database
mysql_host = "localhost"
mysql_db = "TelegramAirdropBot"
mysql_user = "AirdropUser"
mysql_pw = "_st29bP2"

texts = {
    "start_1": "Hi {} and welcome to EDCOIN Airdrop!\n\nGet started by clicking the button below.\n\n",
    "start_2": "Hi {},\n\nYour address has been added to the airdrop list!\n\n",
    "start_captcha": "Hi {},\n\n",
    "airdrop_start": "The airdrop didn't start yet.",
    "airdrop_address": "Type in your BEP20 address:",
    "airdrop_max_cap": "ℹ️ The airdrop reached its max cap.",
    "airdrop_walletused": "⚠️ That address has already been used. Use a different one.",
    "airdrop_confirmation": "✅ Your address has been added to airdrop list.",
    "airdrop_wallet_update": "✅ Your address has been updated.",
}
