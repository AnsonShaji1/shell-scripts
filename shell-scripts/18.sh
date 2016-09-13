for x in *
do
	mv $x `echo $x | tr [A-Z] [a-z]`
done
