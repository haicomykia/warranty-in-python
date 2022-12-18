from datetime import date
from src.Warranty.WarrantyEnum import Warranties as warranty


class Customer:
    """
    顧客クラス
    """
    def __init__(self, customer_name: str, start_date: date, warranty: warranty):
        """
        コンストラクタ
        :param customer_name: 顧客名
        :param start_date: 保証開始日
        :param warranty: 保証
        """
        self.customer_name = customer_name
        self.start_date = start_date
        self.cancel_date = None
        self.warranty = warranty

    def get_end_of_warranty(self) -> date:
        """
        保証期間の終了日を返す
        :return: 保証期間の終了日
        """
        return self.warranty.get_warranty_period() + self.start_date

    def has_subscribed(self, warranty: warranty) -> bool:
        """
        保証期間内か？
        :param warranty: 保証enumのメンバ
        :return: 当該保証に加入していて期間内か？
        """
        if self.warranty != warranty:
            return False

        # 解約していない
        if self.cancel_date is None:
            if self.get_end_of_warranty() >= date.today() >= self.start_date:
                return True
            return False

        # 解約
        if self.cancel_date > date.today() >= self.start_date:
            return True

        return False

    def cancel_warranty(self) -> None:
        """
        保証を解約
        """
        self.cancel_date = date.today()
