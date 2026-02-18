from modules.gmail_api import get_gmail_services, create_message, send_message
from modules.reasoning import get_best_offers
from modules.scraper import grocery_offers

def main():
    deals = grocery_offers()
    offers,meals, shopping_list = get_best_offers(deals)
    service = get_gmail_services()
    msg = create_message("From","To","Best Meals",meals)
    send_message(service,"me",msg)
    msg = create_message("From","To","Shopping List",shopping_list)
    send_message(service,"me",msg)

if __name__ == "__main__":
    main()
