#!/usr/bin/env bash
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#
function clean(){
    rm -rf ./build | :
    find . -name "*.egg-info" -exec rm -rf {} +;
    find . -name "*.egg" -exec rm -rf {} +;
}

function build(){
    python setup.py bdist_wheel --universal
}

function install(){
   python setup.py install
}

case $1 in
    clean)
        clean
        ;;

    install)
        install
        clean
        ;;

    build)
        build
        clean
        ;;

    publish)
        build
         twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
        clean
        ;;
    * )
        echo "Need param from one of build|install|publish"
esac
