import treeformat

def test_format():
    testin = '''
A
{
B
C
{
D
}
}
X
    '''
    #indent_level = 4
    #indent_identifier = False
    open_identifier = '{'
    close_identifier = '}'

    expected = '''
A
{
    B
    C
    {
        D
    }
}
X
    '''

    assert(expected == treeformat.format_tree(testin, open_identifier, close_identifier))
