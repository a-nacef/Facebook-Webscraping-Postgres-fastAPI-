from facebook_scraper import get_posts
import load


class Scraper():
    pagename = "botsofnewyork"
    #The dict returned for each post by the get_posts method carries lots of redundant keys for this use case, 
    #we'll be filtering them with a list and a lambda expression
    wanted_keys = ["post_id", "text", "image", "likes", "comments", "shares"]
    pruned = None
    def getdata(self, num):
        resp = []
        filter_dict = lambda d,l: {x:d[x] for x in l}
        data = get_posts(self.pagename,pages=num)
        for post in data:
            pruned = filter_dict(post, self.wanted_keys)
            load.load_data(pruned)
            resp.append(pruned)
            
        return resp

        





