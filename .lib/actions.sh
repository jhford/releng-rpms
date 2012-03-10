#!/bin/bash
set -e

PY=`which python`       # python to run tooltool
TT=../../tooltool.py    # where is tooltool.py?
TTNAME=lookaside        # what is the tooltool manifest called
VCS_ADD='hg add'        # how should I add things to the VCS

fetch () {
    echo fetching files from manifest
    if [ -e $TTNAME ] ; then
        $PY $TT -m $TTNAME fetch
        rv=$?
    fi
    return $rv
}

store () {
    if [ ! -e $1 ] ; then
        return 1
    fi
    $PY $TT -m $TTNAME add $1
    rv=$?
    echo adding $1 to lookaside
    return $rv
}

build () {
    spec=$1 ; shift
    args=$@
    rm -rf builddir
    mkdir -p builddir
    rpmbuild -bb $spec \
        --define "_topdir $PWD/.rpmbuild" \
        --define "_rpmdir $PWD" \
        --define "_sourcedir $PWD" \
        --define "_specdir $PWD" \
        --define "_srcrpmdir $PWD" \
        --define "_builddir $PWD/builddir" \
        $@
}

mock_build () {
    target=$1
    arch=$2
    spec=$3
    # Because I don't know how to grab the name of the generated srpm file
    # I am going to write it to a tmp dir.  If I could figure out the name
    # I would just write it to the cwd
    rm -rf .tmp
    mkdir .tmp
    mkdir -p $arch
    mock --unpriv -r $target --buildsrpm --spec $spec --sources . --resultdir .tmp
    srpm=$(ls .tmp/*.src.rpm)
    if [ $? -ne 0 ] ; then
        return 1
    fi
    mock --unpriv -r $target .tmp/*.src.rpm --resultdir $arch
    if [ $? -ne 0 ] ; then
        return 1
    fi
    rm -rf .tmp
    
}

command=$1
shift
$command $@
