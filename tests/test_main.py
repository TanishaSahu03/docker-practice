import pytest
# from app import main
from app.main import Student

@pytest.fixture()
def obj():
    student = Student("Nisha", 22, 3)
    return student


class TestMain:

    def test_display(self,obj):
        assert obj.display() == "Nisha22"

    def test_show_id(self,obj):
        assert obj.show_id() == 3

