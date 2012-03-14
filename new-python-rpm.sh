#!/bin/bash

set -ex

os=$1
interpreter=$2
name=$3

mkdir $os/$interpreter-$name
specfile=$os/$interpreter-$name/$interpreter-$name.spec
cp mozilla-python-spec.spec $specfile

sed -i "" -e "s/@NAME@/$2/g" $specfile
sed -i "" -e "s/@PYNAME@/python27/g" $specfile
sed -i "" -e "s/@PYVER@/2.7/g" $specfile
sed -i "" -e "s/@PYREL@/2/g" $specfile
ln -s ../../.lib/actions.sh $os/$interpreter-$name/actions.sh
