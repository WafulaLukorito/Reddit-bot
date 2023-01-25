import random
import praw
import secrets

reddit = praw.Reddit(client_id= secrets.client_id,
                     client_secret = secrets.client_secret,
                     user_agent = secrets.user_agent,
                      username = secrets.username,
                      password = secrets.password
                      )

subreddit = reddit.subreddit('Kenya')

sadlist = ["It’s amazing how someone can break your heart and you can still love them with all the little pieces.” ~ Michael Scott",
"“Never feel regret for your own decisions. If, you will not respect your own decisions, who else will?” ~ Michael Scott",
"“I always like walking in the rain, so no one can see me crying.” ~ Charlie Chaplin",
"“I know how to love you, but not how to stop loving you.” ~ Invajy",
"“Sadness flies away on the wings of time.” ~ Jean de La Fontaine",
"“There are years that ask questions and years that answer.” ~ Zora Neale Hurston",
"“Be strong now because things will get better. It might be stormy now, but it can’t rain forever” ~ Anonymous",
"“I do believe that if you haven’t learnt about sadness, you cannot appreciate happiness.” ~ Nana Mouskouri",
"“Maybe we all have darkness inside of us and some of us are better at dealing with it than others.” ~ Jasmine Warga",
"“Don’t cry because it’s over, smile because it happened.” ~ Michael Scott"]

print (subreddit.display_name)

for submission in subreddit.new(limit=100):
    #print ("_ _ "*15)
    
    #print(str(submission.title.encode('utf-8', 'ignore')) + " \n" + submission.url  + "\n " + str(submission.selftext.encode('utf-8', 'ignore')) + "\n")
    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " sad " in comment_lower or " sad " in comment_lower or " depressed " in comment_lower or " depression " in comment_lower or " stressed " in comment_lower:
                
                print ("*"*15)
                print(comment.body.encode('utf-8'))
                # random_sad = random.choice(sadlist)
                # comment.reply (random_sad)

# for post in subreddit.hot(limit=10):
#     print(post.title.encode('ascii', 'ignore'))