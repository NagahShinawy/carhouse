"""
created by Nagaj at 05/08/2021
"""
import random

from faker import Faker

from apps.teams.models import Team

SOCIAL_MEDIA = ("facebook", "twitter", "linkedin")

fake = Faker()


def create_team():
    fullname = fake.name().split(" ")
    fname = fullname[0]
    lname = fullname[1]
    job = fake.job()
    nid = get_nid()
    fb, tw, lnk = [generate_socialmedia(website) for website in SOCIAL_MEDIA]
    fb_profile = fb + fname if fb else None
    tw_profile = tw + fname if tw else None
    lnk_profile = lnk + fname if lnk else None
    team = Team(
        fname=fname,
        lname=lname,
        emp_id=nid,
        position=job,
        fb=fb_profile,
        twitter=tw_profile,
        linkedin=lnk_profile,
    )
    team.save()


def generate_socialmedia(website):
    num = random.randint(1, 6)
    if num == 1:
        return f"https://www.{website}.com/"


def get_nid():
    nid = ""
    for _ in range(10):
        nid += str(random.randint(0, 9))

    return int(nid)


def run():
    for _ in range(100):
        create_team()
