# File-system related operations (fs)
{id: fs}


## File-system related operations (fs)
{id: file-system-related-operations}
{i: fs}

[fs](https://nodejs.org/docs/latest/api/fs.html)

* readFile
* writeFile
* appendFile
* unlink (delete file)
* createReadStream
* createWriteStream
* mkdir
* rmdir
* readdirSync
* readdir
* rename

## Read file
{id: read-file}
{i: readFile}

![](examples/fs/read_file.js)

## Write file
{id: write-file}
{i: writeFile}

![](examples/fs/write_file.js)

## Append to file
{id: append-to-file}
{i: appendFile}

![](examples/fs/append_to_file.js)

## Delete file (unlink file)
{id: delete-file}
{i: unlink}

![](examples/fs/delete_file.js)

## Read (and write) file by chunks
{id: read-write-file-by-chunks}
{i: createReadStream}
{i: createWriteStream}
{i: on}
{i: write}

![](examples/fs/read_write_by_chunks.js)

## Read (and write) file by chunks using pipe
{id: read-write-file-by-pipe}
{i: pipe}

![](examples/fs/read_write.js)


## Create a directory (folder) (mkdir)
{id: create-directory}
{i: mkdir}

![](examples/fs/create_directory.js)

## Remove a directory (folder) (rmdir)
{id: remove-directory}
{i: rmdir}

![](examples/fs/remove_directory.js)


## Read directory sync (readdirSync)
{id: read-directory-sync}
{i: readdirSync}

![](examples/fs/readdir_sync.js)

## Read directory async (readdir)
{id: read-directory-async}
{i: readdir}

![](examples/fs/readdir_async.js)

## Read directory async error handline
{id: read-directory-async-errors}
{i: readdir}

![](examples/fs/readdir_async_errors.js)

## Rename a file (rename)
{id: rename-file}
{i: rename}

```
fs.rename(from, to, (err) => {})
```

![](examples/fs/rename_file.js)

