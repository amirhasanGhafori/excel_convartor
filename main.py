
from tqdm import tqdm
import pandas as pd;
import re

# رشته ورودی
input_string = "سفته داده-چک داده,خرید-فروش"

# استفاده از رجکس برای جایگزینی ویرگول و خط فاصله با فاصله
cleaned_string = re.sub(r'[-,]', ' ', input_string)

# تبدیل رشته به آرایه با استفاده از split
result_array = cleaned_string.split()


file_path = 'C:/Users/Amirhasan/Desktop/excel_convertor/excel_data/002_Excel_Data_For_Practice(3).xlsx'
file_path_2 = 'C:/Users/Amirhasan/Desktop/excel_convertor/excel_data/005_Excel_Data_For_Practice.xlsx'


df = pd.read_excel(file_path)
df_file2 = pd.read_excel(file_path_2)
for i in result_array:
    if i=='فروش':
        df[i] = pd.to_datetime(df['تاریخ استخدام'], format='%Y/%m/%d')
    elif i=='خرید':
        df[i] = pd.to_datetime(df['تاریخ استخدام'], format='%Y/%m/%d')
    elif i=='سفته':
        df[i] = df['نام و نام خانوادگی']
    elif i=='چک':
        df[i] = df['نام و نام خانوادگی']
    else:
        pass

grouped = df.groupby('شهر')


output_file = 'C:/Users/Amirhasan/Desktop/excel_convertor/result/converted-data.xlsx'

# df['شماره پرسنلی'] = df['کدپرسنلی']
df.rename(columns={'کدپرسنلی': 'شماره پرسنلی'}, inplace=True)

df['تاریخ قرارداد'] = pd.to_datetime(df['تاریخ استخدام'], format='%Y/%m/%d')
df['بخش'] = df['بخش'].astype(str) + ' - ' + df['عنوان شغلی'].astype(str)
df['بخش مشتری'] = df_file2['بخش مشتری']

df['نام مستعار'] = df['نام و نام خانوادگی'].apply(lambda x: x.split()[0])
df['فامیلی'] = df['نام و نام خانوادگی'].apply(lambda x: x.split()[-1])


#change all rename column names
df.columns = pd.MultiIndex.from_tuples([
    ('اطلاعات پرسنلی', 'شماره پرسنلی'),
    ('اطلاعات پرسنلی', 'نام و نام خانوادگی'),
    ('اطلاعات پرسنلی', 'عنوان شغلی'),
    ('نام و نام خانوادگی', 'نام مستعار'),
    ('نام و نام خانوادگی', 'فامیلی'),
    ('اطلاعات شغلی', 'تاریخ استخدام'),
    ('اطلاعات شغلی', 'تاریخ قرارداد'),
    ('اطلاعات شغلی', 'بخش'),
    ('اطلاعات شغلی', 'شهر'),
    ('اطلاعات شغلی', 'واحد تجاری'),
    ('اطلاعات شغلی', 'جنسیت'),
    ('اطلاعات شغلی', 'قومیت'),
    ('اطلاعات شغلی', 'سن'),
    ('اطلاعات شغلی', 'حقوق سالانه(دلار)'),
    ('اطلاعات شغلی', 'جایزه'),
    ('اطلاعات شغلی', 'کشور'),
    ('اطلاعات شغلی', 'سفته'),
    ('اطلاعات شغلی', 'چک'),
    ('اطلاعات شغلی', 'خرید'),
    ('اطلاعات شغلی', 'فروش'),
    ('اطلاعات شغلی', 'بخش مشتری')
])

df.to_excel(output_file, index=True)

with tqdm(total=1, desc="Writing to Excel") as pbar:
    df.to_excel(output_file, index=True)
    pbar.update(1)

#شیت بندی با استفاده از گروه ها
# with pd.ExcelWriter(output_file) as writer:
#     for name,group in grouped:
#         group.to_excel(writer,sheet_name=name,index=False)

