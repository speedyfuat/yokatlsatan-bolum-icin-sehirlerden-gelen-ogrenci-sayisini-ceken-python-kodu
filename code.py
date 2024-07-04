import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

# Function to extract tables from a URL
def extract_table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    df = pd.read_html(str(table))[0]  # Convert HTML table to DataFrame
    return df

# List of URLs containing tables
urls = [
    'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110015',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110024',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110078',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110103',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110112',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110121',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110139',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104190490',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110193',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110209',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110218',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110227',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110236',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110245',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110254',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110263',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110272',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110299',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110306',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110315',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110324',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104190582',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111216',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104112153',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104190589',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110333',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110342',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110351',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110369',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110378',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110387',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104190596',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104190489',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110687',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110696',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104112029',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110624',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110633',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104112074',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110642',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104112108',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104190549',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110651',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104112083',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110669',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104112065',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110678',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104112092',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111243',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111252',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104190551',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104190334',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104112162',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111719',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111694',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111701',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111297',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104190603',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111288',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111852',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111861',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111349',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111358',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111931',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111322',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111367',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111376',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104190550',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111261',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111279',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111313',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111304',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104110836',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111976',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104111234',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104190552',
'https://yokatlas.yok.gov.tr/content/lisans-dynamic/1010.php?y=104190568',


]

# List of custom filenames corresponding to each URL
custom_filenames = [
    '  Diş Hekimliği.xlsx',
'  Eczacılık.xlsx',
'  Biyoloji.xlsx',
'  Fizik.xlsx',
'  İstatistik.xlsx',
'  Kimya.xlsx',
'  Matematik.xlsx',
'  Matematik (Uzaktan Öğretim).xlsx',
'  Almanca Öğretmenliği.xlsx',
'  Arapça Öğretmenliği.xlsx',
'  Bilgisayar ve Öğretim Teknolojileri Öğretmenliği.xlsx',
'  Biyoloji Öğretmenliği.xlsx',
'  Coğrafya Öğretmenliği.xlsx',
'  Felsefe Grubu Öğretmenliği.xlsx',
'  Fen Bilgisi Öğretmenliği.xlsx',
'  Fizik Öğretmenliği.xlsx',
'  Fransızca Öğretmenliği.xlsx',
'  İlköğretim Matematik Öğretmenliği.xlsx',
'  İngilizce Öğretmenliği.xlsx',
'  Kimya Öğretmenliği.xlsx',
'  Matematik Öğretmenliği.xlsx',
'  Matematik Öğretmenliği (KKTC Uyruklu).xlsx',
'  Okul Öncesi Öğretmenliği.xlsx',
'  Özel Eğitim Öğretmenliği.xlsx',
'  Özel Eğitim Öğretmenliği (KKTC Uyruklu).xlsx',
'  Rehberlik ve Psikolojik Danışmanlık.xlsx',
'  Sınıf Öğretmenliği.xlsx',
'  Sosyal Bilgiler Öğretmenliği.xlsx',
'  Tarih Öğretmenliği.xlsx',
'  Türk Dili ve Edebiyatı Öğretmenliği.xlsx',
'  Türkçe Öğretmenliği.xlsx',
'  Hemşirelik.xlsx',
'  Endüstriyel Tasarım.xlsx',
'  Mimarlık.xlsx',
'  Şehir ve Bölge Planlama.xlsx',
'  Şehir ve Bölge Planlama (KKTC Uyruklu).xlsx',
'  Bilgisayar Mühendisliği.xlsx',
'  Elektrik-Elektronik Mühendisliği.xlsx',
'  Elektrik-Elektronik Mühendisliği (İngilizce).xlsx',
'  Endüstri Mühendisliği.xlsx',
'  Endüstri Mühendisliği (İngilizce).xlsx',
'  Endüstri Mühendisliği (İngilizce) (KKTC Uyruklu).xlsx',
'  İnşaat Mühendisliği.xlsx',
'  İnşaat Mühendisliği (İngilizce).xlsx',
'  Kimya Mühendisliği.xlsx',
'  Kimya Mühendisliği (İngilizce).xlsx',
'  Makine Mühendisliği.xlsx',
'  Makine Mühendisliği (İngilizce).xlsx',
'  Beslenme ve Diyetetik.xlsx',
'  Fizyoterapi ve Rehabilitasyon.xlsx',
'  Odyoloji.xlsx',
'  Sosyal Hizmet.xlsx',
'  Rekreasyon.xlsx',
'  Ağaç İşleri Endüstri Mühendisliği.xlsx',
'  Bilgisayar Mühendisliği teknoloji fak.xlsx',
'  Bilgisayar Mühendisliği (M.T.O.K.).xlsx',
'  Elektrik-Elektronik Mühendisliği teknoloji fak.xlsx',
'  Elektrik-Elektronik Mühendisliği (UOLP-Azerbaycan Teknik Üniversitesi) (Ücretli).xlsx',
'  Elektrik-Elektronik Mühendisliği (M.T.O.K.).xlsx',
'  Endüstriyel Tasarım Mühendisliği.xlsx',
'  Endüstriyel Tasarım Mühendisliği (M.T.O.K.).xlsx',
'  Enerji Sistemleri Mühendisliği.xlsx',
'  Enerji Sistemleri Mühendisliği (M.T.O.K.).xlsx',
'  Enerji Sistemleri Mühendisliği (KKTC Uyruklu).xlsx',
'  İmalat Mühendisliği.xlsx',
'  İnşaat Mühendisliği teknoloji fak.xlsx',
'  İnşaat Mühendisliği (M.T.O.K.).xlsx',
'  İnşaat Mühendisliği (KKTC Uyruklu).xlsx',
'  Metalurji ve Malzeme Mühendisliği.xlsx',
'  Metalurji ve Malzeme Mühendisliği (M.T.O.K.).xlsx',
'  Otomotiv Mühendisliği.xlsx',
'  Otomotiv Mühendisliği (M.T.O.K.).xlsx',
'  Tıp.xlsx',
'  Tıp (KKTC Uyruklu).xlsx',
'  Tıp (İngilizce).xlsx',
'  Fotonik.xlsx',
'  Yönetim Bilişim Sistemleri.xlsx',

    # Add more filenames as needed
]

# Extract tables from each URL and save to separate Excel files
for i, url in enumerate(urls):
    table_df = extract_table(url)
    # Use custom filename if available, otherwise use default filename
    filename = custom_filenames[i] if i < len(custom_filenames) else f'table_{i+1}.xlsx'
    table_df.to_excel(filename, index=False)
    print(f"Table {i+1} extracted and saved to {filename}")
