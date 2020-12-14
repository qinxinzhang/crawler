from selenium import webdriver
import xlwt


# 数据写入表格
def write_file(row, header):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet("sheet1")
    # 写入表头 这里需要第1列和第4列
    sheet.write(0, 0, header[0].text)
    sheet.write(0, 1, header[3].text)

    # 写入表内容
    i = 0
    for key in range(len(row)):
        c = row[i].find_elements_by_xpath("td")[3].text
        h = row[i].find_elements_by_xpath("td")[0].text
        sheet.write(i + 1, 0, h)
        sheet.write(i + 1, 1, c)
        i = i + 1
    wbk.save("test.xls")


driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get('https://data.stats.gov.cn/easyquery.htm?cn=E0103')
# 得到表的行
row_data = driver.find_elements_by_xpath("//table[contains(@id, 'table_main')]/tbody/tr")
# 得到表的表头
header_data = driver.find_elements_by_xpath("//table[contains(@id, 'table_main')]/thead/tr/th")
length = len(row_data)
write_file(row_data, header_data)
