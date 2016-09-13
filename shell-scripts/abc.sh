count=$1
#echo $count
b=$2
#echo $b
while [ $count -le $b ]
do
	echo $count
	count=`expr $count + 1`
done
