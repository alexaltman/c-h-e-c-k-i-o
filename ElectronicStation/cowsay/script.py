COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
import re
import collections


def cowsay(text):
    def dist_txt():
        ll = []
        tmp = ''
        for i in txt_l:
            if len(tmp) == 0:
                tmp += i
                if i == txt_l[-1] and i != " ":
                    ll.append(tmp)
            elif len(i) + len(tmp) + 1 <= 39:
                tmp += " "
                tmp += i
                if i == txt_l[-1]:
                    ll.append(tmp)
            else:
                ll.append(tmp)
                tmp = i
                if tmp == txt_l[-1]:
                    ll.append(tmp)
        return ll

    text = re.sub(" +", " ", text)

    # Init var.s
    top_border = " __"
    bottom_border = " --"
    txt_l = collections.deque()

    #hack for really long words
    for i in text.split(' '):
        if len(i) <= 39:
            txt_l.append(i)
        else:
            for j in range(0, len(i), 39):
                txt_l.append(i[j:j+39])

    #hack for random spaces since I'm spliting on it
    for e, i in enumerate(txt_l):
        if i == '':
            txt_l[e] = ' '

    ll = dist_txt()
    mymax = len(max(ll, key=len))

    # Begin Cowsay'ing things
    if len(text) <= 39:
        top_border += "_"*len(text)
        bottom_border += "-"*len(text)
        return '\n' + top_border + '\n' + '< ' +  text + ' >\n' + bottom_border + COW
    elif len(ll) == 2:
        top_border += "_"*mymax
        bottom_border += "-"*mymax
        return '\n' + top_border + '\n' + '/ ' +  ll[0].ljust(mymax) + ' \\' + '\n' + '\\ ' + ll[1].ljust(mymax) + ' /' + '\n' + bottom_border + COW
    else:
        top_border += "_"*mymax
        bottom_border += "-"*mymax
        middle_str = ['| '+ i.ljust(mymax) +' |' for i in ll[1:-1] ]
        return '\n' + top_border + '\n' + '/ ' +  ll[0].ljust(mymax) + ' \\' + '\n' + '\n'.join(middle_str) + '\n' + '\\ ' + ll[-1].ljust(mymax) + ' /' + '\n' + bottom_border + COW

