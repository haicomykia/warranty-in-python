from datetime import date
from src.Customer.Customer import Customer
from src.Warranty.WarrantyEnum import Warranties

if __name__ == "__main__":
    taro = Customer("太郎", date.today(), Warranties.FIVE_YEARS)
    for warranty in Warranties:
        if taro.has_subscribed(warranty):
            print(taro.get_end_of_warranty())
            print(warranty)
