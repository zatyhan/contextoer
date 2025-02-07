import gensim.downloader as api
from splinter import Browser
from selenium.webdriver.common.keys import Keys
import random

if __name__ == "__main__":
    # Open the browser
    browser = Browser("chrome")

    # Open the page
    browser.visit("'https://contexto.me/'")

    # Find the search box
    search_box = browser.find_by_css("input[name='q']")

    # Generate a random word
    word = random.choice(model.index2word)

    # Search for the word
    search_box.fill(word + Keys.RETURN)

    # Wait for a while
    input("Press Enter to continue...")

    # Close the browser
    browser.quit()