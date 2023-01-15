
def filter_none_data_clear(data: dict) -> dict:
    """
    удаляет ключи со значениями None

    :param data:
    :return:
    """
    data = {
        k: v for k, v in data.items()
        if not v is None
    }
    return data
