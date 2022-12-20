import datetime
from src.Customer.Customer import Customer
from src.Customer.Customer import Warranties

if __name__ == "__main__":
    taro = Customer("太郎", datetime.date(2017, 12, 20), Warranties.FIVE_YEARS)
    # taro.cancel_warranty()
    for warranty in Warranties:
        if warranty.is_against(taro):
            print(taro.get_end_of_warranty())
            print(warranty)
