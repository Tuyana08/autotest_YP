# Туяна Доржиева, 16-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def test_get_order_positive_assert():
    get_order_response = sender_stand_request.get_order_info()
    assert get_order_response.status_code == 200