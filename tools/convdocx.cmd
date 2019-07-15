set fileName=%~n1
set folderName=%fileName: =_%
pandoc %1 -f docx -t markdown -o "%folderName%.md" --extract-media "%folderName%" --atx-headers