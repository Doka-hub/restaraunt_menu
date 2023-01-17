
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


def parse_query_parameters_list(values: str) -> list[str]:
    if (
        values.startswith('"') and values.endswith('"') or
        values.startswith("'") and values.endswith("'")
    ):
        values = values[1:-1]
    return [v.strip() for v in values.split(',')]
