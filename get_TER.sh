#! /bin/bash

./TER_format.py test.translation.1 test.reference.tok.1
java -jar /home/zhengshun/tercom-0.7.25/tercom.7.25.jar -r test.TER.ref -h test.TER.hyp | grep "Total TER" > result.TER.1

./TER_format.py test.translation.2011 test.reference.2011
java -jar /home/zhengshun/tercom-0.7.25/tercom.7.25.jar -r test.TER.ref -h test.TER.hyp | grep "Total TER" > result.TER.2011

./TER_format.py test.translation.2013 test.reference.2013
java -jar /home/zhengshun/tercom-0.7.25/tercom.7.25.jar -r test.TER.ref -h test.TER.hyp | grep "Total TER" > result.TER.2013

