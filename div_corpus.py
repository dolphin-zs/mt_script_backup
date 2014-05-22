#! /usr/bin/python

file_en = open("zs.clean.1.en", "r")
file_zh = open("zs.clean.1.zh", "r")

lines_en = file_en.readlines()
lines_zh = file_zh.readlines()

N = 10
len_total = len(lines_en)
len_single = len_total / N


name_no = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
train_file_en = []
train_file_zh = []
test_file_en = []
test_file_zh = []

for i in range(N):
    train_name_en = "clean" + name_no[i] + ".en"
    train_file_en.append( open(train_name_en, 'w') )

    train_name_zh = "clean" + name_no[i] + ".zh"
    train_file_zh.append( open(train_name_zh, 'w') )

    test_name_en = "test" + name_no[i] + ".en"
    test_file_en.append( open(test_name_en, 'w') )

    test_name_zh = "test" + name_no[i] + ".zh"
    test_file_zh.append( open(test_name_zh, 'w') )


for i in range(N):
    for j in range(len_single):
        temp_sent_en = lines_en[i*len_single+j].strip('\n')
        temp_sent_zh = lines_zh[i*len_single+j].strip('\n')
        print >>test_file_en[i], temp_sent_en
        print >>test_file_zh[i], temp_sent_zh

        for k in range(N):
            if k != i:
                print >>train_file_en[k], temp_sent_en
                print >>train_file_zh[k], temp_sent_zh

