$zip = Get-Input("File to zip: ")
$out = Get-Input("Zipped folder name: ")
# Extract the files
Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory($zip, $out)

# Show extracted files
Get-ChildItem -Recurse $out