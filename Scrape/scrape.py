from bs4 import BeautifulSoup, Comment
import requests
import pandas as pd


def getStats(player, name):
    url = "https://www.basketball-reference.com/players/" + str(player) + ".html"
    if len(player) < 2:
        return "";
    per_game = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    stats = soup.find('table', id="per_game")
    if stats != None:
        footer = stats.find('tfoot').contents[0]
        ctr = 0
        for n in footer:
            ctr += 1
            if ctr <= 4:
                continue
            if ctr == 7:
                if n.text > 70:
                    continue
            if ctr == 12 &  len(n.text) > 1 & int(n.text) == 0:
                per_game.append("0")
            if n.text != "":
                per_game.append(str(n.text))
        per_game.insert(0,name)
        return per_game
    return ""


def format(name):
    n = (name.lower()).split()
    first = n[1][0]
    player = n[1][0:5] + n[0][0:2]
    player += "01"
    player = first + "/" + player
    return player

def rev(name):
    n = (name).split(",")
    first = n[1].strip()
    last = n[0].strip()
    return first + " " + last


stats = []
stats.append(["Name", "G","MP","FG","FGA","FG%","3P","3PA","3P%","2P","2PA","2P%","eFG%","FT","FTA",
                    "FT%","ORB","DRB","TRB","AST","STL","BLK","TOV","PF","PTS"])



import csv
with open('hof.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for row in reader:
        print row[0]
        if len(getStats(format(row[0]), row[0])) != 0:
            stats.append(getStats(format(row[0]), row[0]))


with open("out.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerows(stats)
    

print("DONE")