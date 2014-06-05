#! /bin/bash

rm -rf ./corpus/*.snt ./corpus/*.cooc ./corpus/*.vcb ./corpus/*.classes*

# 1. Change the file from plain format to snt format recognized by giza++
./tools/parallel2snt ./corpus/en ./corpus/zh ./corpus/test_en ./corpus/test_zh
mv ./corpus/en_zh.snt ./corpus/all-en_zh.snt
mv ./corpus/zh_en.snt ./corpus/all-zh_en.snt
head -n 415380 ./corpus/all-en_zh.snt > ./corpus/train-en_zh.snt
head -n 415380 ./corpus/all-zh_en.snt > ./corpus/train-zh_en.snt
tail -n 1140000 ./corpus/all-en_zh.snt > ./corpus/test-en_zh.snt
tail -n 1140000 ./corpus/all-zh_en.snt > ./corpus/test-zh_en.snt

# 2. build Coocurrence file
./tools/snt2cooc.out ./corpus/en.vcb ./corpus/zh.vcb ./corpus/all-en_zh.snt > ./corpus/all-en_zh.cooc
./tools/snt2cooc.out ./corpus/zh.vcb ./corpus/en.vcb ./corpus/all-zh_en.snt > ./corpus/all-zh_en.cooc

cd corpus
../tools/mkcls -pen -Ven.vcb.classes opt
../tools/mkcls -pzh -Vzh.vcb.classes opt
cd ..

./tools/GIZA++ -CoocurrenceFile ./corpus/all-en_zh.cooc -c ./corpus/train-en_zh.snt \
    -m1 5 -m2 0 -m3 0 -m4 5 -hmmdumpfrequency 1 -model345dumpfrequency 1 -model4smoothfactor 0.4 \
    -nsmooth 4 -o ./out_giza-en_zh/en_zh -onlyaldumps 0 \
    -p0 0.999 -s ./corpus/en.vcb -t ./corpus/zh.vcb -tc ./corpus/test-en_zh.snt

./tools/GIZA++ -CoocurrenceFile ./corpus/all-zh_en.cooc -c ./corpus/train-zh_en.snt \
    -m1 5 -m2 0 -m3 0 -m4 5 -hmmdumpfrequency 1 -model345dumpfrequency 1 -model4smoothfactor 0.4 \
    -nsmooth 4 -o ./out_giza-zh_en/zh_en -onlyaldumps 0 \
    -p0 0.999 -s ./corpus/zh.vcb -t ./corpus/en.vcb -tc ./corpus/test-zh_en.snt

