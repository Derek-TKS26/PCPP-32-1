# An XML file (Extensible Markup Language) is a text-based file format that uses tags to define data structures.
# It’s designed to store and transport data in a way that’s both human-readable and machine-readable.

# Key Features:

# 1.Hierarchical Structure: Data is organized in a tree structure with nested elements.
# 2.Customizable Tags: Unlike HTML, you can create your own tags.
# 3.Platform-Independent: Can be used across different systems and applications.
# 4.Self-Descriptive: Tags provide metadata about the data they contain.


# <?xml version="1.0"?>
# <data>    # Data is the main element, which has two < > tags namely the opening tag and ending tag.
#     <book title="The Little Prince">  # 'book' is the first child element. 'title' in the opening tag is the attribute of book
#         <author>Antoine de Saint-Exupéry</author>
#         <year>1943</year>
#     </book>
#     <book title="Hamlet">
#         <author>William Shakespeare</author>
#         <year>1603</year>
#     </book>
# </data>

# xml文件是一个带有标签的结构化文件，python 中有多个包可以解析(parse) 这类文件。
# 常用 ElmentTree 文件包对xml文件进行解析（parse).

# —————————————————————————— Module 3 - 2.1.1 ————————————————————————————

import xml.etree.ElementTree as ET # ElementTree 是 python 自带的一个解读xml文件的包
from plistlib import dumps

tree = ET.parse('books.xml') # books.xml 通过parse() method 对book.xml 文件进行解析，拆分成树结构。
root = tree.getroot() # 通过 getroot() 的方法来了解根元素里面的内容
print('The root tag is:', root.tag) # <data> 是 root Element
print('The root has the following children:') # 每一个book 都是一个 child Element
for child in root:
    print(child.tag, child.attrib) # tag 就是 book , 而每个属性都是一个成对的string组成的字典。
                                    # 一个child element 可以有多个属性。

# 如下一段是通过遍历+类似列表和字典的 slicing 的方法来进一步了 book元素中的子元素

print("My books:\n")
for book in root: # 遍历root内部的子元素
    print('Title: ', book.attrib['title'])
    print('Author:', book[0].text) # 对于子元素book 再下层的元素都可以用text来展示 [0] book 下第一个子元素
    print('Year: ', book[1].text, '\n')

# for author in root.iter('author'): # 通过 iter() 方法对 root 内部进行迭代
#     print(author.text) # 同样对于内部元素的显示需要用到 text 方法

for book in root.findall('book'): # findall 只可以看到root element 下第一层的子元素
    print(book.get('title')) # 通过get再找到book 元素下面的一层元素的信息

print(root.find('book').get('author'))

# ———————————————————— Modifying an XML document ——————————————————————————————

for child in root:
    child.tag = 'movie' # 修改 root element 下面第一层的 <book> 元素
    print(child.tag,child.attrib)



tree.write('movie.xml','utf-8',True)
# 将上述的修改保存在一个叫movie.xml的文件之中。

# ———————————————————— Building an XML document ——————————————————————————————

root1 = ET.Element('data')
movie_1 = ET.SubElement(root1,'movie',{'title':'The Little Prince','rate':'5'})
movie_2 = ET.SubElement(root1,'movie',{'title':'Hamlet','rate':'5'})
tree1 = ET.ElementTree(root1)
tree1.write('new_movie.xml','utf-8')
tree1 = ET.parse('new_movie.xml')
root11 = tree1.getroot()




