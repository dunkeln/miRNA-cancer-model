#!/usr/bin/env fish

# Iterate over each manifest file
for manifest_file in TCGA-*.txt
    set directory (basename "$manifest_file" .txt)
    mkdir -p "$directory"
    ./gdc-client download -m "$manifest_file" -d "../$directory"
end

