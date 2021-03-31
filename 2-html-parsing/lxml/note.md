# The lxml.etree Tutorial

Import `lxml.etree` :

``` python
from lxml import etree
```

A portable(可移植的) way to import `etree` :

``` python
try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    try:
        import xml.etree.cElementTree as etree
        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            import xml.etree.ElementTree as etree
            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                import cElementTree as etree
                print("running with cElementTree")
            except ImportError:
                try:
                    import ElementTree as etree
                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")
```

## The Element class

`Element` class denote the XML element.

Manually construct an element:

``` python
>>> root = etree.Element('root')
>>> root.tag
'root'
```

Use append method append the child element to `root` :

``` python
root.append(etree.Element("child1"))
```

Use class function to add sub element to `root` :

``` python
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")
```

Display XML element:

``` python
>>> print(etree.tostring(root, pretty_print=True).decode('utf-8'))
<root>
    <child1/>
    <child2/>
    <child3/>
</root>
```

### Elements are lists

``` python
>>> child = root[0]
>>> print(child.tag)
child1

>>> print(len(root))
3

>>> root.index(root[1]) # lxml.etree only!
1

>>> children = list(root)

>>> for child in root:
...     print(child.tag)
child1
child2
child3

>>> root.insert(0, etree.Element("child0"))
>>> start = root[:1]
>>> end   = root[-1:]

>>> print(start[0].tag)
child0
>>> print(end[0].tag)
child3

>>> print(etree.iselement(root)) # test if it;s some kind of Element
True
>>> if len(root): # test if it has children
...     print("The root element has children")
```

Do not test if a `Element` has children this way, even if it is pythonic: 

``` python
if len(root):
    print("The root element has children")
```

### Elements carry attributes as a dict

Create XML element with attributes:

``` python
root = etree.Element("root", interesting="totally")
```

Attributes are unordered name-value pairs:

``` python
>>> print(root.get("interesting"))
totally

>>> print(root.get("hello"))
None
>>> root.set("hello", "Huhu")
>>> print(root.get("hello"))
Huhu

>>> etree.tostring(root)
b'<root interesting="totally" hello="Huhu"/>'

>>> sorted(root.keys())
['hello', 'interesting']

>>> for name, value in sorted(root.items()):
...     print('%s = %r' % (name, value))
hello = 'Huhu'
interesting = 'totally'
```

### Elements contain text

`Element` s can contain text:

``` python
>>> root = etree.Element("root")
>>> root.text = "TEXT"

>>> print(root.text)
TEXT

>>> etree.tostring(root)
b'<root>TEXT</root>''
```

在许多以数据为中心的XML文档中，这是唯一可以找到 `text` 的地方。它被树形层次结构的叶子节点所封装。

然而，如果XML用于标记文本文档，如 `(X)HTML` ，文本也可以出现在不同元素之间：

``` html
<html>

<body>
    Hello <br /> World
</body>

</html>
```

这里， `<br/>` 标签被 `text` 包围。这通常被称为 *文档风格* 或 *混合内容* XML。 `Element` 通过 `tail` 属性来支持这一点。它包含直接跟随 `Element` 的 `text` ，直到XML树中的下一个 `Element` 。

``` python
>>> html = etree.Element("html")
>>> body = etree.SubElement(html, "body")
>>> body.text = "TEXT"

>>> etree.tostring(html)
b'<html><body>TEXT</body></html>'

>>> br = etree.SubElement(body, "br")
>>> etree.tostring(html)
b'<html><body>TEXT<br/></body></html>'

>>> br.tail = "TAIL"
>>> etree.tostring(html)
b'<html><body>TEXT<br/>TAIL</body></html>'
```

If `text` and `tail` still not enough:

``` python
>>> etree.tostring(br)
b'<br/>TAIL'
>>> etree.tostring(br, with_tail=False) # lxml.etree only!
b'<br/>''

>>> etree.tostring(html, method="text")
b'TEXTTAIL'
```

### Using `XPath` to find text

`XPath` is yet another powerful method to extract content from document:

``` python
>>> print(html.xpath("string()")) # lxml.etree only!
TEXTTAIL
>>> print(html.xpath("//text()")) # lxml.etree only!
['TEXT', 'TAIL']
```

If you want to use this more often, you can wrap it in function:

``` python
>>> print(html.xpath("string()")) # lxml.etree only!
TEXTTAIL
>>> print(html.xpath("//text()")) # lxml.etree only!
['TEXT', 'TAIL']
```

如果查询的结果是以 `Element` 的形式提取的，那么它仍然连接到原来的XML树，这意味着像 `getparent()` 和 `is_text` 这样的函数和属性也可以继续使用。但如果结果是通过 `XPath` 函数如 `text()` 和 `string()` 来构造的，那么就会与原始XML树断开。

### Tree iteration

Basic iteration:

``` python
from element in root.iter():
    print(f"{element.tag} - {element.text}")
```

Iteration for specified elements:

``` python
from element in root.iter("child", "another"):
    print(f"{element.tag} - {element.text}")
```

For document mingled with `Entity` and `Comment` :

``` python
for element in root.iter():
    if isinstance(element.tag, str):
        print(f"{element.tag} - {element.text}")
    else:
        print(f"SPECIAL: {element} - {element.text}")

for element in root.iter(tag=etree.Element):
    print(f"{element.tag} - {element.text}")

for element in root.iter(tag=etree.Entity):
    print(element.text)
```

### Serialization

#### `etree.tostring()`

- `method='xml'`: can switch to 'html' and 'text'

- `encoding='ascii'`: can switch to 'UTF-8'

- `pretty_print=False`

#### `etree.indent()`

Using `space=` to control indention.

## The `ElementTree` class

``` python
>>> root = etree.XML('''\
... <?xml version="1.0"?>
... <!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips">  ]>
... <root>
...   <a>&tasty;</a>
... </root>
... ''')

>>> tree = etree.ElementTree(root)
>>> print(tree.docinfo.xml_version)
1.0
>>> print(tree.docinfo.doctype)
<!DOCTYPE root SYSTEM "test">

>>> tree.docinfo.public_id = '''-//W3C//DTD XHTML 1.0 Transitional//EN'
>>> tree.docinfo.system_url = 'file://local.dtd'
>>> print(tree.docinfo.doctype)
<!DOCTYPE root PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "file://local.dtd">)
```

其中一个重要的区别是， `ElementTree` 类序列化为一个**完整的**文档，而不是一个单一的 `Element` 。这包括顶层处理指令和注释，以及文档中的 `DOCTYPE` 和其他 `DTD` 内容：

``` python
>>> print(etree.tostring(tree))  # lxml 1.3.4 and later
<!DOCTYPE root PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "file://local.dtd" [
<!ENTITY tasty "parsnips">
]>
<root>
  <a>parsnips</a>
</root>

>>> print(etree.tostring(tree.getroot()))
<root>
  <a>parsnips</a>
</root>
```

## Parsing from strings and files

### The `fromstring()` function

The `fromstring()` function is the easiest way to parse a string:

``` python
>>> some_xml_data = "<root>data</root>"

>>> root = etree.fromstring(some_xml_data)
>>> print(root.tag)
root
>>> etree.tostring(root)
b'<root>data</root>'
```

### The `XML()` function

The `XML()` function behaves like the `fromstring()` function, but is commonly used to write XML `literals` right into the source:

``` python
>>> root = etree.XML("<root>data</root>")
>>> print(root.tag)
root
>>> etree.tostring(root)
b'<root>data</root>'
```

There is also a corresponding function `HTML()` for HTML literals.

``` python
>>> root = etree.HTML("<p>data</p>")
>>> etree.tostring(root)
b'<html><body><p>data</p></body></html>''
```
