title = input()
content = input()
comment = input()
comment_list = []
while comment != 'end of comments':
    comment_list.append(comment)
    comment = input()

print(f"<h1>\n   {title}\n</h1>")
print(f"<article>\n   {content}\n</article>")
for comment in comment_list:
    print(f"<div>\n   {comment}\n</div>")