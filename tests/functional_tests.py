from selenium import webdriver


browser = webdriver.Firefox()


# Edith has heard about a cool new online-todo app. She goes to check
# out the home page.
browser.get('http:/localhost:8000')

# She notices the page title and header mention todo lists.
assert 'To-Do' in browser.title

# She is invited to enter a todo item straight away

# She types "Bye peacock feathers" into a text box (Edith's hobby is
# tying fly-fishing lures).

# When she hits enter, the page updates, and the new page lists "1:
# Buy peacock feathers" as an item in a todo list.

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very
# methodical!)

# The page updates again, and now shoes both items on her list

# Edith wonders whether the site will remember her list. Then she
# sees that the site had generated a unique URL for her -- there is
# some explanatory text to that effect.

# She visis that URL -- her todo list is still there.

# Satisfied, she goes to sleep.
browser.quit()
