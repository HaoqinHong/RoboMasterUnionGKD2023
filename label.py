import os

txt_list = os.listdir('Dataset/test')

with open('val.txt', 'w') as fp:
    for txt in txt_list:
        if txt[-1] == 'g':
            print('Dataset/test/'+txt, file=fp)
