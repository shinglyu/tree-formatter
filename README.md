Tree Formatter
============================
This tool can format text (e.g. log files) into a indented tree format based on your choice of open identifiers and close identifiers. This is very helpful when you are analyzing logs for browser layout code that does a lot of tree traversal.


e.g.

```
# input.txt
A
{
B
C
{
D
}
}
X
```

open identifier: `{`
close identifier: `}`

```
python treeformat.py input.txt -o "{" -c "}"
```

will output

```
# input.txt
A
{
    B
    C
    {
        D
    }
}
X
```
