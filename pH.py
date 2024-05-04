import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import time


st.image("https://adivapelajar.files.wordpress.com/2023/05/20230511_130815_0000.png?w=1024")

with st.sidebar.container():
    st.image("https://adivapelajar.files.wordpress.com/2023/05/20230505_153644_0000.png?w=1024", width=250)
    test = st.sidebar.selectbox("Navigation", ['Home', "About pH🧪", "About Us", "Contact Us"])
    
with st.sidebar.container():
    st.sidebar.markdown("Logtech - pH Analysis App")
    
if test == "Home":
    st.title(':blue[Aplikasi penentu pH Larutan]')
    st.markdown('''Hai users, selamat datang di web kami.😊''')
    st.markdown('''Aplikasi ini dapat digunakan untuk menentukan nilai pH dari suatu larutan atau sampel dengan menginput konsentrasi (Molaritas).''')
    tombol = st.button('OLEH KELOMPOK 2')
    if tombol:
        st.write('Latifa Andjani')
        st.write('Muhamad Faris Adzikri')
        st.write('Raka Mulya Octama')
        st.write('Rakhmillah Fatikhannisa Ramadhiani')
        st.write('Siti Nurhaliza')
        
    tab1, tab2 = st.columns(2)
    
    with tab1:
        st.header('Penentuan nilai pH')
        NamaLarutan = st.text_input('Nama Larutan yang akan dihitung pH-nya:')
        st.write('Silahkan pilih jenis larutan dengan format "asam kuat", "basa kuat", "asam lemah", "basa lemah"')
        option = st.selectbox('Jenis Larutan', ("asam kuat", "basa kuat", "asam lemah", "basa lemah"))

        if option == "asam kuat":
            jumlah_digit = 4
            cons = st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
            jumlah_digit1 = 4
            val = st.number_input(f'Masukkan nilai valensi larutan', format='%.'+str(jumlah_digit)+'f')
            H = cons * val
            pH = -(np.log10(H))
            if st.button('Hitung'):
                st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah')
                st.subheader(f':green[{round(pH,2)}]')
                st.balloons()
                
        elif option == "basa kuat":
            jumlah_digit = 4
            cons = st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
            jumlah_digit1 = 4
            val = st.number_input(f'Masukkan nilai valensi larutan', format='%.'+str(jumlah_digit)+'f')
            OH = cons * val
            POH = (np.log10(OH))
            pH = 14 - POH
            if st.button('Hitung'):
                st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah')
                st.subheader(f':green[{round(pH,2)}]')
                st.balloons()

        elif option == "asam lemah":
            jumlah_digit = 4
            cons = st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
            a = cons * (1.8 * 10**(-5))
            H = np.sqrt(a)
            pH = -(np.log10(H))
            if st.button('Hitung'):
                st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah')
                st.subheader(f':green[{round(pH,2)}]')
                st.balloons()

        elif option == "basa lemah":
            jumlah_digit = 4
            cons = st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
            a = cons * (1.8 * 10**(-5))
            OH = np.sqrt(a)
            POH = - (np.log10(OH))
            pH = 14 - POH
            if st.button('Hitung'):
                st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah')
                st.subheader(f':green[{round(pH,2)}]')
                st.balloons()
                
    with tab2:
        st.header("Penentuan indikator")
        jumlah_digit = 1
        pH = st.number_input('Masukan nilai pH anda (range 1 - 14) :', float(jumlah_digit))
        
        if st.button('Submit'):
            if 1.0 <= pH <= 4.4:
                st.write('Indikator yang cocok pada pH', pH, 'adalah')
                st.subheader(":orange[Sindur Metil (SM)]")
                st.write("---")
                st.subheader('Fakta Mengenai Sindur Metil (SM)')
                st.image('https://adivapelajar.files.wordpress.com/2023/05/indicator-colours3.jpg', width=350)
                
                st.write('''Indikator sindur metil (SM) adalah suatu senyawa organometalik yang digunakan sebagai indikator pH pada larutan asam atau netral dalam rentang pH 3,1 - 4,4. Berikut adalah beberapa fakta menarik tentang indikator sindur metil :
1. Indikator sindur metil adalah senyawa organometalik pertama yang digunakan sebagai indikator pH pada larutan asam atau netral.
2. Warna indikator sindur metil berubah dari kuning ke merah tua ketika larutan menjadi asam.
3. Indikator sindur metil sangat stabil dan tidak terpengaruh oleh cahaya atau panas.
4. Senyawa ini sering digunakan dalam bidang kimia dan biologi sebagai indikator pH karena rentang perubahan warnanya sangat sempit dan akurat, serta tidak toksik dan mudah digunakan.
''')
                st.write(''':blue[Kelebihan : ]
1. Indikator sindur metil memiliki rentang perubahan warna yang akurat dan sempit, sehingga sangat cocok untuk digunakan dalam analisis kuantitatif.
2. Senyawa ini mudah digunakan dan tidak toksik, sehingga aman untuk digunakan dalam laboratorium.
3. Indikator sindur metil sangat stabil dan tidak terpengaruh oleh cahaya atau panas, sehingga dapat disimpan dalam waktu yang lama tanpa mengalami kerusakan.
''')
                
            elif 4.4 < pH <= 6.0:
                st.write('Indikator yang cocok pada pH', pH, 'adalah')
                st.subheader(":purple[Metil Merah (MM)]")
                st.write("---")
                st.subheader('Fakta Mengenai Metil Merah (MM)')
                st.image('https://adivapelajar.files.wordpress.com/2023/05/indicator-colours4.jpg', width=350)
                
                st.write('''Indikator metil merah (MM) adalah senyawa organometalik yang digunakan sebagai indikator pH pada larutan netral dalam rentang pH 4,4 - 6,0. Berikut adalah beberapa fakta menarik tentang indikator metil merah :
1. Indikator metil merah pertama kali digunakan pada abad ke-19 oleh seorang ilmuwan Jerman, Robert Bunsen.
2. Warna indikator metil merah berubah dari merah muda ke merah tua ketika larutan menjadi asam.
3. Senyawa ini sering digunakan dalam bidang kimia dan biologi sebagai indikator pH karena rentang perubahan warnanya yang luas dan akurat.
4. Indikator metil merah tidak terpengaruh oleh cahaya atau panas, sehingga dapat disimpan dalam waktu yang lama tanpa mengalami kerusakan.
''')
                st.write(''':blue[Kelebihan : ]
1. Indikator metil merah memiliki rentang perubahan warna yang luas dan akurat, sehingga sangat cocok untuk digunakan dalam analisis kualitatif dan kuantitatif.
2. Senyawa ini mudah digunakan dan tidak toksik, sehingga aman untuk digunakan dalam laboratorium.
3. Indikator metil merah sangat stabil dan tidak terpengaruh oleh cahaya atau panas, sehingga dapat disimpan dalam waktu yang lama tanpa mengalami kerusakan.
''')
                
            elif 6.0 < pH <= 8.0:
                st.write('Indikator yang cocok pada pH', pH, 'adalah')
                st.subheader(":brown[Brom Tymol Biru (BTB)]")
                st.write("---")
                st.subheader('Fakta Mengenai Brom Tymol Biru (BTB)')
                st.image('https://adivapelajar.files.wordpress.com/2023/05/indicator-colours5.jpg', width=350)
                
                st.write('''Indikator brom timol biru (BTB) adalah senyawa organometalik yang digunakan sebagai indikator pH pada larutan netral dalam rentang pH 6,0 - 8,0. Berikut adalah beberapa fakta menarik tentang indikator brom timol biru :
1. Indikator brom timol biru adalah senyawa organometalik yang pertama kali disintesis pada abad ke-19 oleh seorang ilmuwan Jerman, Robert Bunsen.
2. Warna indikator brom timol biru berubah dari kuning ke biru ketika larutan menjadi basa.
3. Senyawa ini sering digunakan dalam bidang kimia dan biologi sebagai indikator pH karena rentang perubahan warnanya yang luas dan akurat.
4. Indikator brom timol biru sangat stabil dan tidak terpengaruh oleh cahaya atau panas, sehingga dapat disimpan dalam waktu yang lama tanpa mengalami kerusakan.
''')
                st.write(''':blue[Kelebihan : ]
1. Indikator brom timol biru memiliki rentang perubahan warna yang luas dan akurat, sehingga sangat cocok untuk digunakan dalam analisis kualitatif dan kuantitatif.
2. Senyawa ini mudah digunakan dan tidak toksik, sehingga aman untuk digunakan dalam laboratorium.
3. Indikator brom timol biru sangat stabil dan tidak terpengaruh oleh cahaya atau panas, sehingga dapat disimpan dalam waktu yang lama tanpa mengalami kerusakan.
''')
                
            elif 8.0 < pH <= 14.0:
                st.write('Indikator yang cocok pada pH', pH, 'adalah')
                st.subheader(":yellow[Papel Phenolphthalein (PP)]")
                st.write("---")
                st.subheader('Fakta Mengenai Papel Phenolphthalein (PP)')
                st.image('https://adivapelajar.files.wordpress.com/2023/05/indicator-colours2.jpg', width=350)
                
                st.write('''Indikator papel fenolftalein (PP) adalah senyawa organometalik yang digunakan sebagai indikator pH pada larutan basa dalam rentang pH 8,0 - 14,0. Berikut adalah beberapa fakta menarik tentang indikator papel fenolftalein :
1. Indikator papel fenolftalein adalah senyawa organometalik yang pertama kali disintesis pada abad ke-19 oleh seorang ilmuwan Jerman, Robert Bunsen.
2. Warna indikator papel fenolftalein berubah dari tidak berwarna menjadi merah muda ketika larutan menjadi basa.
3. Senyawa ini sering digunakan dalam bidang kimia dan biologi sebagai indikator pH karena rentang perubahan warnanya yang luas dan akurat.
4. Indikator papel fenolftalein sangat stabil dan tidak terpengaruh oleh cahaya atau panas, sehingga dapat disimpan dalam waktu yang lama tanpa mengalami kerusakan.
''')
                st.write(''':blue[Kelebihan : ]
1. Indikator papel fenolftalein memiliki rentang perubahan warna yang luas dan akurat, sehingga sangat cocok untuk digunakan dalam analisis kualitatif dan kuantitatif.
2. Senyawa ini mudah digunakan dan tidak toksik, sehingga aman untuk digunakan dalam laboratorium.
3. Indikator papel fenolftalein sangat stabil dan tidak terpengaruh oleh cahaya atau panas, sehingga dapat disimpan dalam waktu yang lama tanpa mengalami kerusakan.
''')
            
elif test == "About pH🧪":
    st.title('Tentang pH')
    st.markdown('''**pH** adalah ukuran yang menunjukkan tingkat keasaman atau kebasaan dari suatu larutan. Nilai pH berkisar dari 0 hingga 14, 
    di mana 7 menunjukkan larutan netral, nilai di bawah 7 menunjukkan larutan asam, dan nilai di atas 7 menunjukkan larutan basa (atau alkali).''')
    st.image('https://adivapelajar.files.wordpress.com/2023/05/pH-scale-1.jpg?resize=768%2C483')
    st.write('''Nilai pH dihitung menggunakan rumus:
    pH = -log[H+]
    di mana [H+] adalah konsentrasi ion hidrogen dalam larutan. Semakin tinggi konsentrasi ion hidrogen, semakin rendah nilai pH-nya, dan semakin asam larutannya.''')
    st.write('''pH sangat penting dalam berbagai bidang, termasuk kimia, biologi, dan kedokteran. Di bidang kimia, pH digunakan untuk menentukan 
    sifat-sifat larutan dan reaksi kimia yang terjadi di dalamnya. Di bidang biologi, pH memengaruhi fungsi enzim dan proses metabolisme dalam 
    organisme hidup. Di bidang kedokteran, pengukuran pH digunakan dalam diagnosis penyakit dan pemantauan kondisi pasien.''')
    
elif test == "About Us":
    st.title('Tentang Kami')
    st.write('''Kami adalah tim pengembang aplikasi ini. Kami adalah siswa SMA yang memiliki minat dalam ilmu kimia. Kami mengembangkan aplikasi ini 
    sebagai proyek untuk mempelajari lebih lanjut tentang konsep pH dan indikator pH. Kami harap aplikasi ini dapat bermanfaat bagi Anda 
    dalam memahami konsep tersebut.''')
    st.write('''Jika Anda memiliki pertanyaan atau masukan tentang aplikasi ini, jangan ragu untuk menghubungi kami melalui kontak yang tersedia di bawah ini.''')
    
elif test == "Contact Us":
    st.title('Hubungi Kami')
    st.write('''Jika Anda memiliki pertanyaan atau masukan tentang aplikasi ini, jangan ragu untuk menghubungi kami melalui kontak yang tersedia di bawah ini:''')
    st.write('''- Email: info@logtech.com''')
    st.write('''- Telepon: +62 123 4567 890''')
    st.write('''- Alamat: Jl. Jendral Sudirman No. 123, Kota Metropolis, Indonesia''')
