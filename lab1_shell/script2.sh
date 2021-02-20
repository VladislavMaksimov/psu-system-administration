#/bin/bash

while true
do
    files=$(find $1 -name "*.$2" -type f -printf "%f " -delete)
    if [ -n "$files" ]
    then
        now=$(date +"%d.%m.%YT%H:%M :")
        if [ -f script2.log ]
        then
            echo -n $now >> script2.log
        else
            echo -n $now > script2.log
        fi
        printf " " >> script2.log
        echo $files >> script2.log
    fi
    sleep 30
done

# в files записывается вывод найденных в подкаталогах файлов, при этом они сразу удаляются
# в now записывается текущие дата + время
# sleep задаёт ожидание 30сек