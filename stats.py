import scrapper
import dic


def tot_don_sum(a, b, c, d, e, f, g, h):
    def eighteen(a): #fucked up runtime. Fix
        tot = 0
        for elem in a:
            tot += elem[1]
        return tot
    def sixteen(b):
        tot = 0
        for elem in b:
            tot += elem[1]
        return tot
    def fourteen(c):
        tot = 0
        for elem in c:
            tot += elem[1]
        return tot
    def twelve(d):
        tot = 0
        for elem in d:
            tot += elem[1]
        return tot
    def ten(e):
        tot = 0
        for elem in e:
            tot += elem[1]
        return tot
    def eight(f):
        tot = 0
        for elem in f:
            tot += elem[1]
        return tot
    def six(g):
        tot = 0
        for elem in g:
            tot += elem[1]
        return tot
    def four(h):
        tot = 0
        for elem in h:
            tot += elem[1]
        return tot
    return [eighteen(a), sixteen(b), fourteen(c), twelve(d), ten(e), eight(f), six(g), four(h)]

def lib_don_sum(a, b, c, d, e, f, g, h):
    def eighteen(a): #fucked up runtime. Fix
        tot = 0
        for elem in a:
            tot += elem[2]
        return tot
    def sixteen(b):
        tot = 0
        for elem in b:
            tot += elem[2]
        return tot
    def fourteen(c):
        tot = 0
        for elem in c:
            tot += elem[2]
        return tot
    def twelve(d):
        tot = 0
        for elem in d:
            tot += elem[2]
        return tot
    def ten(e):
        tot = 0
        for elem in e:
            tot += elem[2]
        return tot
    def eight(f):
        tot = 0
        for elem in f:
            tot += elem[2]
        return tot
    def six(g):
        tot = 0
        for elem in g:
            tot += elem[2]
        return tot
    def four(h):
        tot = 0
        for elem in h:
            tot += elem[2]
        return tot
    return [eighteen(a), sixteen(b), fourteen(c), twelve(d), ten(e), eight(f), six(g), four(h)]

def cons_don_sum(a, b, c, d, e, f, g, h):
    def eighteen(a): #fucked up runtime. Fix
        tot = 0
        for elem in a:
            tot += elem[3]
        return tot
    def sixteen(b):
        tot = 0
        for elem in b:
            tot += elem[3]
        return tot
    def fourteen(c):
        tot = 0
        for elem in c:
            tot += elem[3]
        return tot
    def twelve(d):
        tot = 0
        for elem in d:
            tot += elem[3]
        return tot
    def ten(e):
        tot = 0
        for elem in e:
            tot += elem[3]
        return tot
    def eight(f):
        tot = 0
        for elem in f:
            tot += elem[3]
        return tot
    def six(g):
        tot = 0
        for elem in g:
            tot += elem[3]
        return tot
    def four(h):
        tot = 0
        for elem in h:
            tot += elem[3]
        return tot
    return [eighteen(a), sixteen(b), fourteen(c), twelve(d), ten(e), eight(f), six(g), four(h)]

def collect_year(year_data):
    dictionary = dict(dic.dictionary)
    for k in dictionary.keys():
        dictionary[k] = [0, 0]
    for donation in year_data:
        state = get_state(donation)
        dictionary[state][0] += int(donation[2])
        dictionary[state][1] += int(donation[3])
    return dictionary


def get_state(donation):
    address = donation[4]
    return address.split(", ")[1]

def main():
    data = [] #noded data
    address =[] #address in data
    def data_getter():
        data = []
        for i in ['https://www.opensecrets.org/outsidespending/summ.php?cycle=2018&disp=D&type=V&superonly=N','https://www.opensecrets.org/outsidespending/summ.php?cycle=2016&disp=D&type=V&superonly=N', 'https://www.opensecrets.org/outsidespending/summ.php?cycle=2014&disp=D&type=V&superonly=N', 'https://www.opensecrets.org/outsidespending/summ.php?cycle=2012&disp=D&type=V&superonly=N', 'https://www.opensecrets.org/outsidespending/summ.php?cycle=2010&disp=D&type=V&superonly=N', 'https://www.opensecrets.org/outsidespending/summ.php?cycle=2008&disp=D&type=V&superonly=N', 'https://www.opensecrets.org/outsidespending/summ.php?cycle=2006&disp=D&type=V&superonly=N', 'https://www.opensecrets.org/outsidespending/summ.php?cycle=2004&disp=D&type=V&superonly=N']:
            data.append(scrapper.get_data(i))
        return data
    def get_address(data):
        count = 0
        address = []
        for node in data:
            address.append([])
            for entry in node:
                address[-1].append(entry[4])
        return address

    data = data_getter()
    address = get_address(data)

    for d in data:
        print(collect_year(d))
    
    #tot_trend_list = tot_don_sum(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
    #lib_trend_list = lib_don_sum(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
    #cons_trend_list = cons_don_sum(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
    #print(tot_trend_list)
    #print(lib_trend_list)
    #print(cons_trend_list)
    #print(address)


main()


