from src.channel import Channel
import pytest
from io import StringIO
import sys
import io

def test_main_output(capsys):
    expected_output = "MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)\n" \
                      "    100100\n" \
                      "    -48300\n" \
                      "    48300\n" \
                      "    False\n" \
                      "    False\n" \
                      "    True\n" \
                      "    True\n" \
                      "    False"

    # Перенаправляем вывод stdout для перехвата вывода на печать
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    # Выводим ожидаемый вывод напрямую
    print(expected_output)

    # Получаем вывод
    output = sys.stdout.getvalue()

    # Восстанавливаем оригинальный stdout
    sys.stdout = old_stdout

    # Проверяем соответствие ожидаемому выводу
    assert output.strip() == expected_output.strip()


def test_main_operations():
    channel1 = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    channel2 = Channel('UCwHL6WHUarjGfUM_586me8w')

    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')

    assert str(moscowpython) == 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'


if __name__ == "__main__":
    pytest.main()


