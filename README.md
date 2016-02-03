# metafolder

A metafolder is a folder of documents with some metadata stored alongside the
individual documents. Such metadata can include attributes like the
title, author, language etc.

The API could look like this:

```python
import metafolder

# open a metafolder:
mf = metafolder.open('/tmp/mf.tar')

# store a file:
file_path = '/tmp/source_file.txt'
metadata = {'title': 'Hello, Metafolder'}
mf.put(file_path, file_name='test.txt', meta=metadata)

# iterate available files, get metadata and a file object
# for each contained file:
for file_name in mf:
    metadata = mf.get_meta(file_name)
    fileobj = mf.get(file_name)

# wrap up
mf.close()
```


