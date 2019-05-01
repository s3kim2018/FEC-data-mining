import requests
from bs4 import BeautifulSoup
from csv import writer

#Still working on extracting the address
#temp = []
#for post in posts[1:len(posts)]: #Address I don't fucking know how 
#temp.append(post.findAll('td')[1])

def map(name, tot_don, cons_don, lib_don, address):
        return_list = []
        for i in range(0, len(name)):
                node = [name[i], tot_don[i], cons_don[i], lib_don[i], address[i]]
                return_list.append(node)
        return return_list

def parseint(string):
        ver1 = string.replace(',', '')
        ver2 = ver1.replace('$', '')
        return(int(ver2))

def get_data(link):
        name_array = []
        tot_don = []
        cons_don = []
        lib_don = []
        address = []

        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        posts = soup.find_all('tr')

        for post in posts[1:len(posts)]: #appends name into name array
                name_array.append(post.find('a').text)

        for post in posts[1:len(posts)]: #Total Amount Donated
                tot_don.append(parseint(post.findAll(class_ = "number")[0].text))

        for post in posts[1:len(posts)]: #Liberal Donations
                lib_don.append(parseint(post.findAll(class_ = "number")[1].text))
       
        for post in posts[1:len(posts)]: #Conservative Donations
                cons_don.append(parseint(post.findAll(class_ = "number")[2].text))
        for post in posts[1: len(posts)]:
                address.append(get_address(post))

        return map(name_array, tot_don, cons_don, lib_don, address)

def get_year(year):
    url = 'https://www.opensecrets.org/outsidespending/summ.php?cycle=' + str(year) + '&disp=D&type=V&superonly=N'
    name_array = []
    tot_don = []
    cons_don = []
    lib_don = []

    return url

""" Get the address given a tr entry """
def get_address(entry):
    return entry.find_all('td')[1].contents[4]
