mkdir exefile
for fname in *
do
	if [ -x "$fname" ]
	then
		mv $fname exeflie
	fi
done 
