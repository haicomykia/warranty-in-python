import sys
import enum
from datetime import date
from dateutil.relativedelta import relativedelta


class Warranties(enum.Enum):
    """
    保証の列挙体
    """
    BASIC = (101, "ベーシック保証", 12)
    THREE_YEARS = (201, "3年保証", 36)
    FIVE_YEARS = (301, "5年保証", 60)

    def __init__(self, code: int, warranty_name: str, terms: int):
        """
        コンストラクタ
        :param code: コード
        :param warranty_name: 名前
        :param terms: 保証期間（月数）
        """
        self.code = code
        self.warranty_name = warranty_name
        self.terms = terms

    def __eq__(self, other):
        return self.code == other.code \
               and self.warranty_name == other.warranty_name \
               and self.terms == other.terms

    def __str__(self):
        return self.warranty_name

    def get_warranty_period(self) -> relativedelta:
        """
        保証期間を返す
        :return: 保証期間
        """
        return relativedelta(months=self.terms)


class Customer:
    """
    顧客クラス
    """

    def __init__(self, customer_name: str, start_date: date,
                 warranty: Warranties):
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

    def has_subscribed(self, warranty: Warranties) -> bool:
        """
        顧客が保証に加入しているか？
        :param warranty: 保証enumのメンバ
        :return: 当該保証に加入していて期間内か？
        """
        return self.warranty == warranty

    def cancel_warranty(self) -> None:
        """
        保証を解約
        """
        self.cancel_date = date.today()

    def start_date_has_passed(self) -> bool:
        """
        保証開始日を過ぎているか？
        :return: 保証開始日を過ぎているか？
        """
        return self.start_date <= date.today()

    def expired_warranty(self) -> bool:
        """
        保証切れか？
        :return: 保証期間終了日を過ぎているか？
        """
        if self.cancel_date is None:
            return self.get_end_of_warranty() < date.today()

        return self.cancel_date <= date.today()

    def is_under(self, warranty: Warranties) -> bool:
        """
        顧客が保証に加入していて保証期間内か？
        :param warranty: 保証の列挙体
        :return: 顧客が保証に加入していて保証期間内か？
        """
        if not self.has_subscribed(warranty):
            return False

        if not self.start_date_has_passed():
            return False

        return not self.expired_warranty()
