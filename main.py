# 2019个税计算方式
payMonth = 20000  # 月薪
taxBase = 5000  # 起征点
insuranceFee = 4000  # 社保+公积金
deduceAmount = 2000  # 免税额


def get_rate(month_tax_base):
    if month_tax_base <= 36000:
        return 0.03, 0
    if month_tax_base <= 144000:
        return 0.1, 2520
    if month_tax_base <= 300000:
        return 0.2, 16920
    if month_tax_base <= 420000:
        return 0.25, 31920
    if month_tax_base <= 660000:
        return 0.3, 52920
    if month_tax_base <= 960000:
        return 0.35, 85900
    else:
        return 0.45, 181920


taxList = []
for i in range(12):
    monthTaxBase = (payMonth - taxBase - insuranceFee - deduceAmount) * (i + 1)
    currentRate = get_rate(monthTaxBase)
    currentMonthTax = monthTaxBase * currentRate[0] - currentRate[1]
    for x in taxList:
        currentMonthTax -= x
    taxList.append(currentMonthTax)

yearTax = 0
for (i, x) in enumerate(taxList):
    yearTax += x
    print("第" + str(i + 1) + "月纳税额是:" + str(round(x,3)) + "元")

print("年度合计:" + str(round(yearTax,3)) + "元")
