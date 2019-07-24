pushd %~dp0
python mkdocsyml.py --filter "hide_site_name:" "prebuild_index: True"
popd