from workwx.workmain.page.main import Main


class TestAddMember:

    def setup(self):
        self.main = Main()  # 定义从那个页面开始的

    def test_member(self):
        assert self.main.goto_add_member().add_member()
