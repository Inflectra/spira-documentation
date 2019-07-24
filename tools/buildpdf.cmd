pushd %~dp0

call version.cmd
call toc.cmd

python mkdocs2pandoc.py --width 120 -o temp.pd

pandoc -f markdown+grid_tables+table_captions --reference-doc=tools/custom-reference.docx --toc --toc-depth=3 -s temp.pd -o rapise_%VER%.docx

del /f/q temp.pd


popd