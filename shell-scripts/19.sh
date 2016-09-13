mkdir linux_files
for x in *
do
	
	mv `echo $x | grep linux` linux_files
done
