import datetime
import enum
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
            and self.warranty_name == other.warranty_name  \
            and self.terms == other.terms

    def __str__(self):
        return self.warranty_name

    def get_warranty_period(self):
        """
        保証期間を返す
        :return: 保証期間
        """
        return relativedelta(months=self.terms)
