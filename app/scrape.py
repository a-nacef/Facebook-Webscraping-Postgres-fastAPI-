from facebook_scraper import get_posts
import db
import threading

class Scraper():
    pagename = "botsofnewyork"
    #The dict returned for each post by the get_posts method carries lots of redundant keys for this use case, 
    #we'll be filtering them with a list and a lambda expression
    wanted_keys = ["post_id", "text", "image", "likes", "shares", "comments"]
    pruned = None
    def getdata(self, num):
        resp = []
        filter_dict = lambda d,l: {x:d[x] for x in l}
        data = get_posts(self.pagename,pages=num)
        for post in data:
            pruned = filter_dict(post, self.wanted_keys)
            resp.append(pruned)
        threading.Thread(target=db.load_data, args=resp).start()
        return resp

        





