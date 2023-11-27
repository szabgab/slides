set -e

for crate in examples/*/*
do
    #echo $crate
    cd $crate
    cargo update
    cd ../../..
done
