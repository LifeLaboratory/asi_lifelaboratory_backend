from app.api.sql.ads_provider import Provider


def get_ads():
    """
    Метод для получения рекламы
    :return:
    """
    provider = Provider()
    answer = provider.get_ads()
    return answer
