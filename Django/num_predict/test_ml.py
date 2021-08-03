import pytest
from ml import predict


@pytest.mark.parametrize(
    "image_path, expected",
    [("3.jpg", 3), ("4.jpg", 4), ("5.png", 5), ("6.png", 6), ("7.png", 7)],
)
def test_predict(image_path, expected):
    assert predict(image_path) == expected
