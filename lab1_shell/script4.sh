#/bin/bash

cd $1

IFS='_'
for file in *
do
    if [[ `file -b "$file"` == directory ]]
    then
        latin=$(echo $file | sed "y/абвгдеёжзийклмнопрстуфхцычэюяшщ/abvgdeejzijklmnoprstufxcyceuass/" | sed "y/АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЫЧЭЮЯШЩ/ABVGDEEJZIJKLMNOPRSTUFXCYCEUASS/" | sed 's|[ъь]||g')
        mv $file $latin
    fi
done

# sed "y/" позволяет измеенять название файла посимвольно
# mv "переименовывает" файл, если путь до него не меняется