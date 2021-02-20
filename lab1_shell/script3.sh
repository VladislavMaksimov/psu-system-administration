#/bin/bash

number=$(($RANDOM % 100 + 100))
for ((i=1;i<=$number;i++));
do
    fizz=$(($i % 3))
    buzz=$(($i % 5))
    if [ $fizz -eq 0 ] && [ $buzz -eq 0 ]
    then
        echo -n "FizzBuzz "
    else
        if [ $fizz -eq "0" ]
        then
            echo -n "Fizz "
        else
            if [ $buzz -eq "0" ]
            then
                echo -n "Buzz "
            else
                echo -n $i " "
            fi
        fi
    fi
done
echo