import glob
import markdown
import json
import pprint
import uuid

# Get dir list of MD files.
mds = sorted(glob.glob("./*.md"), reverse=True)

# Create an empty array for data storing.
data = []

# Iterate over the MD files list and extract yaml data.
for md in mds:
    with open(md) as f:
        md = markdown.Markdown(extensions = ['full_yaml_metadata'])
        s = f.read()
        md.convert(s)
        if md.Meta:
            md.Meta['id'] = str(uuid.uuid3(uuid.NAMESPACE_DNS, s))
            data.append(md.Meta)

# Export data as JSON.
with open('blogList.json', 'w') as f:
  json.dump(data, f)

# Pretty print the extracted data.
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

# Output some useful info.
print('='*80)
print('# of files:', len(mds), sep='\t')
print('# of YAMLs:', len(data), sep='\t')
print('='*80)