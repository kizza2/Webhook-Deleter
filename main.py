import requests, time, utils
from colorama import Fore, Back, Style
from discord import Webhook, RequestsWebhookAdapter
from dhooks import Webhook

utils.checker_intro()
webhookk = input(Fore.MAGENTA + Style.DIM + "Webhook URL: ")
print(Style.RESET_ALL)
hook = Webhook(webhookk)
hook.modify(name="kizza")


check = requests.get(webhookk)
if check.status_code == 404:
    utils.SlowPrint(Fore.RED + Style.BRIGHT + "\nWebhook not existing!" + Style.RESET_ALL)
    time.sleep(5)
elif check.status_code == 200:
    utils.SlowPrint(Fore.GREEN + Style.BRIGHT + "\nWebhook correct!" + Style.RESET_ALL)
    time.sleep(1)
    utils.killer_intro()
    utils.SlowPrint("Deleting webhook in 1, 2, 3 ...")
    utils.SlowPrint(Fore.YELLOW + Style.BRIGHT + "\nDeleting the webhhook...!" + Style.RESET_ALL)
    hook.send("Webhook got deleted by https://github.com/kizza2/Webhook-Deleter")
    requests.delete(webhookk)
    checker = requests.get(webhookk)
    if checker.status_code == 404:
        utils.SlowPrint(Fore.GREEN + Style.BRIGHT + "\nWebhook sucessfully deleted!" + Style.RESET_ALL)
        time.sleep(2)
    elif checker.status_code == 200:
        utils.SlowPrint(Fore.RED + Style.BRIGHT + "\nAn error as occured when trying to delete webhook, please try again." + Style.RESET_ALL)
    time.sleep(5)

