from selenium import webdriver


class TestTesterHome(object):
    def setup(self):
        self.drive = webdriver.Firefox()
        self.drive.implicitly_wait(10)
        self.drive.get("https://testerhome.com/")

    def test_Mtsc020(self):

        self.drive.find_element_by_partial_link_text("MTSC 2020").click()
        self.drive.find_element_by_xpath('//*[@class="btn btn-default"]').click()


if __name__ == '__main__':
    ob = TestTesterHome()