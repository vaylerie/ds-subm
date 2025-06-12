# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah meluluskan banyak siswa dengan reputasi akademik yang baik dan kontribusi yang positif di dunia kerja. Namun, di balik keberhasilan tersebut, terdapat permasalahan serius yang terus membayangi, yakni tingginya angka siswa yang tidak menyelesaikan pendidikan atau dropout.

Tingginya angka dropout bukan hanya berdampak negatif bagi siswa yang bersangkutan, tetapi juga mencoreng reputasi institusi secara keseluruhan. Selain itu, hal ini dapat memengaruhi kepercayaan masyarakat terhadap kualitas dan sistem pendidikan yang dijalankan. Untuk itu, Jaya Jaya Institut memiliki kebutuhan mendesak untuk mendeteksi sedini mungkin potensi siswa yang berisiko dropout agar dapat diberikan bimbingan atau intervensi yang sesuai.

### Permasalahan Bisnis

1. Tingginya angka siswa yang tidak menyelesaikan pendidikan (dropout).
2. Tidak adanya sistem prediktif yang dapat mendeteksi lebih awal siswa yang berpotensi mengalami dropout.

### Cakupan Proyek

- Melakukan eksplorasi dan analisis data siswa untuk menemukan pola dan faktor yang berkontribusi pada tingkat dropout.
- Mengembangkan satu business dashboard interaktif untuk membantu memonitor faktor-faktor penyebab dropout.
- Membangun model prediksi dropout menggunakan algoritma machine learning dengan evaluasi performa model.

### Persiapan

Sumber data: Dicoding dataset
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance

Setup environment:

```
# Buat virtual environment
python3 -m venv .venv
source .venv/bin/activate  # untuk Linux/MacOS
.venv\Scripts\activate   # untuk Windows

# Install dependencies
pip install -r requirements.txt
```

## Business Dashboard

Link akses dashboard:
https://lookerstudio.google.com/reporting/c7ab54af-6148-488e-aad5-7519fbf9e7c9/page/yguNF

Dashboard yang dibuat dalam proyek ini bertujuan untuk membantu pihak manajemen Jaya Jaya Institut dalam memantau dan memahami berbagai faktor yang berkontribusi terhadap tingkat dropout siswa. Visualisasi data interaktif ini dibangun menggunakan Looker Studio dan dirancang agar mudah dipahami oleh pengguna non-teknis seperti pimpinan institusi atau staf akademik.

Dashboard ini menyajikan metrik-metrik kunci seperti:

- Persentase siswa dropout secara keseluruhan
- Perbandingan dropout berdasarkan status utang siswa
- Pengaruh pemberian beasiswa terhadap kelulusan

## Menjalankan Sistem Machine Learning

Sistem machine learning ini dikembangkan menggunakan Streamlit dan dirancang untuk memprediksi apakah seorang siswa berisiko mengalami dropout atau tidak, berdasarkan informasi yang diisi pada sebuah form interaktif.

Sistem ini menggunakan algoritma XGBoost, yaitu model gradient boosting yang sangat efektif dalam menangani data tabular dan cocok untuk tugas klasifikasi seperti prediksi dropout.

Link akses streamlit:
https://jaya-jaya-institut-vb.streamlit.app/

```
# Pastikan seluruh dependencies telah terinstall (Lihat bagian setup environment)

# Jalankan streamlit di lokal
streamlit run app.py
```

## Conclusion

Berdasarkan analisis yang telah dilakukan, proyek ini berhasil mengidentifikasi sejumlah faktor penting yang berkaitan dengan kemungkinan siswa mengalami dropout di Jaya Jaya Institut. Salah satu temuan utama menunjukkan bahwa aspek finansial memiliki korelasi yang cukup tinggi dengan tingkat dropout. Siswa yang memiliki utang tercatat memiliki proporsi dropout tertinggi dibandingkan dengan kelompok lainnya.

Lebih lanjut, ditemukan bahwa siswa yang tidak menerima beasiswa cenderung memiliki tingkat dropout yang lebih tinggi dibandingkan dengan yang menerima beasiswa. Di sisi lain, siswa yang rutin membayar biaya kuliah tepat waktu memiliki peluang kelulusan yang lebih tinggi. Selain itu, usia saat pendaftaran juga menjadi indikator penting, di mana siswa yang mendaftar pada usia 19 tahun tercatat memiliki angka dropout paling tinggi.

Untuk memperkuat pengambilan keputusan strategis, model machine learning menggunakan algoritma XGBoost telah diterapkan guna memprediksi kemungkinan seorang siswa akan dropout. Model ini kemudian diintegrasikan ke dalam prototype berbasis Streamlit yang memungkinkan institusi untuk melakukan prediksi secara cepat dan berbasis data, hanya dengan mengisi form isian sederhana.

### Rekomendasi Action Items

1. Perluas Program Beasiswa atau Bantuan Keuangan
   Jaya Jaya Institut perlu mempertimbangkan perluasan program beasiswa sebagai bentuk intervensi terhadap risiko dropout yang tinggi pada siswa dengan masalah keuangan. Pemberian beasiswa tidak hanya difokuskan pada prestasi akademik, melainkan juga diarahkan untuk membantu siswa dari latar belakang ekonomi rentan yang berpotensi keluar dari pendidikan. Selain menambah kuota, institusi dapat mengembangkan skema beasiswa berbasis risiko, di mana siswa yang teridentifikasi memiliki kemungkinan tinggi untuk dropout diberi bantuan lebih awal. Beasiswa bersyarat, seperti bantuan biaya dengan komitmen akademik minimum, juga dapat menjadi solusi efektif untuk menjaga motivasi dan kelangsungan studi.

2. Program Konseling dan Edukasi Finansial
   Untuk mendukung siswa secara preventif, institusi disarankan menyediakan layanan konseling keuangan secara rutin, terutama bagi mahasiswa baru yang telah diketahui memiliki utang. Konseling ini bertujuan membantu siswa menyusun rencana keuangan yang realistis selama masa studi. Selain itu, penyuluhan dalam bentuk workshop atau seminar tentang pengelolaan keuangan pribadi, pentingnya prioritas pengeluaran, serta cara menghindari utang konsumtif dapat memberikan pemahaman yang lebih kuat bagi mahasiswa dalam menghadapi tantangan ekonomi selama kuliah.

3. Monitoring dan Intervensi Dini
   Penerapan sistem monitoring yang aktif terhadap pembayaran biaya kuliah dan kondisi keuangan siswa akan sangat membantu dalam mendeteksi risiko dropout sejak dini. Institusi dapat membangun sistem yang secara otomatis menandai keterlambatan pembayaran atau perubahan pola akademik yang signifikan sebagai sinyal peringatan. Berdasarkan sinyal tersebut, pihak akademik maupun keuangan dapat melakukan pendekatan langsung kepada siswa untuk memberikan dukungan, baik dalam bentuk pengingat, konseling, maupun alternatif pembayaran yang lebih fleksibel.
