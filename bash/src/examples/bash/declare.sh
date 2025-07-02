declare -a animals=(cow snail elephant mouse)
king=${animals[$(((RANDOM % 4)))]}

echo $king
