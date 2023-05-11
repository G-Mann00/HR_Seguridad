#!/bin/bash

echo "---Eliminando archivos .py existentes---"
for file in *.py; do
    rm -- "$file"
    echo "Eliminando ${file%.*}.py"
done

echo "---Convirtiendo archivos .ui a .py---"
for file in *.ui; do
    pyuic5 -x "$file" -o "${file%.*}.py"
    printf "%-25s \033[32mListo\033[0m\n" "${file%.*}.py:"
done

echo "---Añadiendo import de recursos a los archivos .py---"
for file in *.py; do
    if grep -q 'import iconosApp_rc' "$file"; then
        sed -i '/import iconosApp_rc/d' "$file"
    fi
    if ! grep -q 'from recursos import iconosApp_rc' "$file"; then
        sed -i -e '12i\from recursos import iconosApp_rc' "$file"
    fi
    
    printf "%-25s \033[32mListo\033[0m\n" "${file%.*}.py:"
done

