# Download the urls for the even years between 2004 and 2018 inclusive
import requests
import os

def main():
    years = list(range(2004, 2018 + 1, 2))

    if not os.path.exists("data"):
        os.makedirs("data")

    for year in years:
        print(make_url(year))
        response = requests.get(make_url(year))
        filename = "data/" +  str(year) + ".html"

        f = open(filename, "w")
        f.write(response.text)
        f.close()

def make_url(year):
    return "https://www.opensecrets.org/outsidespending/summ.php?cycle=" + str(year) + "&disp=D&type=V&superonly=N"

if __name__=="__main__":
    main()
