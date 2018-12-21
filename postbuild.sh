#!/bin/bash
mkdir out-genfiles
cp -fr bazel-genfiles/py ./out-genfiles/.
cp -fr bazel-genfiles/proto ./out-genfiles/.

mkdir out-bin
cp -fr bazel-bin/py ./out-bin/.
cp -fr bazel-bin/proto ./out-bin/.

#Importing google_extensions_pb2
touch ./out-genfiles/proto/__init__.py
touch ./out-genfiles/proto/stu3/__init__.py

#Importing py.google.fhir.seqex

touch ./py/__init__.py
touch ./py/google/__init__.py

cat <<EOT >> ./py/google/fhir/seqex/bundle_to_seqex_converter.py
def __bootstrap__():
  global __bootstrap__, __loader__, __file__
  import sys, pkg_resources, imp
  __file__ = pkg_resources.resource_filename(__name__,'bundle_to_seqex_converter.so')
  __loader__ = None; del __bootstrap__, __loader__
  imp.load_dynamic(__name__,__file__)
__bootstrap__()
EOT

cp ./out-bin/py/google/fhir/seqex/*.so ./py/google/fhir/seqex/.
