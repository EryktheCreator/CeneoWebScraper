from app.utils import extract_element

class Opinion:

    selectors = {
    "author": ["span.user-post__author-name"],
    "recomendation": ["span.user-post__author-recomendation > em"],
    "stars" : ["span.user-post__score-count"],
    "content" : ["div.user-post__text"],
    "purchased" : ["div.review-pz"],
    "submit_date" : ["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchase_date" : ["span.user-post__published > time:nth-child(2)", "datetime"],
    "pros" : ["div.review-feature__col:has(> div[class*=\"positives\"]) > div.review-feature__item",1],
    "cons" : ["div.review-feature__col:has(> div[class*=\"negatives\"]) > div.review-feature__item",1],
    "useful" : ["span[id^='votes-yes']"],
    "useless" : ["span[id^='votes-no']"]
}
    def __init__(self, opinion_id = None, author = None, recomendation = None, stars = None, content = None, purchased = None, submit_date = None,
    pros = None, cons = None, useful = None, useless = None):
        self.opinion_id = opinion_id
        self.author = author
        self.recomendation = recomendation
        self.stars = stars
        self.content = content
        self.purchased = purchased
        self.submit_date = submit_date
        self.pros = pros
        self.cons = cons
        self.useful = useful
        self.useless = useless

    def extract_opinion(self, opinion):
        for key, args in self.selectors.items():
                setattr(self, key, extract_element(opinion, *args))
        self.opinion_id = opinion["data-entry-id"]
        return self

    def transform_opinion(self):
        self.recomendation = True if self.recomendation == "Polecam" else False if self.recomendation == "Nie polecam" else None
        self.stars = float(self.stars.split("/")[0].replace(",","."))
        self.purchased = bool(self.purchased)
        self.useful = int(self.useful)
        self.useless = int(self.useless)
        return self

    def __str__(self):
        return f"opinion_id: {self.opinion_id}" + "\n".join(f"{key}: {str(getattr(self, key))}" for key in self.selectors.keys())

    def __repr__(self):
        return f"Opinion(opinion_id= {self.opinion_id}" + ",".join(f"{key}={str(getattr(self, key))}" for key in self.selectors.keys()) + ")"

    def to_dict(self):
        return {"opinion_id": self.opinion_id} | {key: getattr(self, key) for key in self.selectors.keys()}