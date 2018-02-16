import webbrowser
#
# webbrowser.open("https://www.python.org/", new=1)
#
# help(webbrowser)
# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='° ', end='\n=========================\n')

# chrome.open_new("https://python.org/")
chrome = webbrowser.get('windows-default').open("https://www.python.org/")
# chrome = webbrowser.get(using='chrome')
# chrome.open("www.python.org/")
