import praw
import time

reddit = praw.Reddit(client_id='hUuM38HhW2XGJg',
                     client_secret='-QZ88QnytFVYuaaQiaRrFVAtDDZ-TQ',
                     user_agent='a reddit instance',
                     username='Queeniezhou326',
                     password='cy930319')
def subspam():
    misctext = """Glad to see you guys here, hope you have a nice day.

This is Queenie,i am reps seller from China. hope to be your friends too.We are doing luxury reps over 10 years. we are professional on this line.
Whats services you would got as below: 24 Hours Customer Service.
Free to talk with you guys at any timeI will send you PSP picture before sending your items. we are doing details inpections by our own teams. after you confirmed then we will packaged the goods perfectly to send into your hand. And any problem and questions before the shipment, we can provide to you refund or gift for you.

Customs Block Policy: If the order are blocked / seized by custom, we can refund or send you the order again for free, even you can change your mind to order another items.

Shipment Delivery Time: 48 hours will send out the goods.

Transportation Way: EMS, DHL, Fedex, UPS, DPD, Wegobuy etc.
Payment Method: WU, Bank Transfer, Money Gram, Paypal.
Yupoo Album: https://queenieluxury02.x.yupoo.com
Wechat: bling2015
Whatapp: +8615202090486

Tell me you know us from Fashionrep, we can offer you 10 % Discount on the first order. Promotional will last for you guys for any time you want to order. First order will get a free gift as well aside the 10% discount.
Promotion Code: QueenieReps0001

Looking for hearing from you guys soon. Thanks for reading my massage.
Wish you have a Merry Christmas!

Best Regards
Queenie"""  # you need to change this to your message

    subname = 'Johntesting'  # obviously you can add more subreddits to this
    usedusernames = []
    for comment in reddit.subreddit(subname).stream.comments():
        name = comment.author.name
        title = f'Dear, {name}'
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
