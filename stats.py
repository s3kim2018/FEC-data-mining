import scrapper


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


def main():
    data = [scrapper.twenty_eighteen(), scrapper.twenty_sixteen(), scrapper.twenty_fourteen(), scrapper.twenty_twelve(), scrapper.twenty_ten(), scrapper.twenty_eight(), scrapper.twenty_six(), scrapper.twenty_four()]
    tot_trend_list = tot_don_sum(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
    lib_trend_list = lib_don_sum(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
    cons_trend_list = cons_don_sum(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
    print(tot_trend_list)
    print(lib_trend_list)
    print(cons_trend_list)


main()


