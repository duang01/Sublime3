"""对xml文件的操作"""
from xml.dom import minidom
import xlrd


class ReadXml():
    def read_xml(self, filename, onenode, twonode):
        # 打开文件
        ret = minidom.parse(filename)
        fistnum = ret.getElementsByTagName(onenode)[0]
        secondnum = fistnum.getElementByTagName(twonode)[0].firstChild.data
        return secondnum


r = ReadXml()
print(r.read_xml(",,/x,xml", "jia", "bac"))


class ReadExcel():
    def read_excl(self, filename, sheetname):
        # 打开excel表
        book = xlrd.open_workbook(filename)
        # 定位到excel中的sheet表
        table = book.sheet_by_name(sheetname)
        # 统计有多少行
        print(table.nrows)
        # 统计列数
        print(table.ncols)
        # 获取第一行的数据
        e = table.row_values(0)
        print(e)


num = int(input("请输入数字："))


if num > 3:
    print(num)
else:
    num += 1
    print(num)
