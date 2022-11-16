class BaseTest:

    def __init__(self, driver):
        self.driver = driver

    def check_valid_page(self, word, result):
        word_text = word.text
        assert word_text == result