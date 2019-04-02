# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


from urllib.parse import quote_plus

reply_template = '[Let me google that for you](http://lmgtfy.com/?q={})'

search = input('Enter a string')

url_title = quote_plus(search)
reply_text = reply_template.format(url_title)

print(reply_text)
