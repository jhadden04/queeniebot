import praw
import time

reddit = praw.Reddit(client_id='*',
                     client_secret='*',
                     user_agent='a reddit instance',
                     username='*',
                     password='*')



def subspam():
    misctext = "your message"  # you need to change this to your message

    subname = 'FashionReps'  # obviously you can add more subreddits to this
    usedusernames = []
    for comment in reddit.subreddit(subname).stream.comments():
        name = comment.author.name
        title = f'Hello, {name}'
        if name in usedusernames:
            continue
        try:
            text = misctext
            reddit.redditor(name).message(title, text)
        except:
            continue
        usedusernames.append(name)
        print(f'u/{name} r/{comment.subreddit.display_name}')
        time.sleep(40)
subspam()
