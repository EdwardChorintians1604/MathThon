import nltk
import ollama
import json
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK data jika belum ada
def _download_nltk_data():
    """Download NLTK data yang diperlukan"""
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)

def preprocess_dengan_nltk(teks):
    """Preprocessing teks menggunakan NLTK"""
    _download_nltk_data()
    
    # Validasi input
    if not teks or not isinstance(teks, str):
        return None
    
    # 1. Tokenisasi kalimat
    try:
        kalimat = sent_tokenize(teks)
    except Exception:
        kalimat = []
    
    # 2. Tokenisasi kata
    try:
        kata = word_tokenize(teks.lower())
    except Exception:
        kata = []
    
    # 3. Hapus stopwords
    try:
        stop_words = set(stopwords.words('indonesian'))
    except Exception:
        stop_words = set()
    
    kata_bersih = [k for k in kata if k not in stop_words and k.isalpha()]
    
    # 4. Stemming
    stemmer = PorterStemmer()
    kata_stem = [stemmer.stem(k) for k in kata_bersih]
    
    return {
        "kalimat": kalimat,
        "kata_penting": kata_bersih,
        "kata_stem": kata_stem,
        "teks_bersih": " ".join(kata_bersih)
    }

def analisis_dengan_ollama(hasil_nltk):
    """Kirim hasil preprocessing ke Ollama untuk analisis lebih dalam"""
    
    if not hasil_nltk:
        return {"error": "Data preprocessing tidak valid"}
    
    prompt = f"""
Berdasarkan kata-kata penting berikut: {hasil_nltk['kata_penting']}
Dan kalimat-kalimat: {hasil_nltk['kalimat']}

Lakukan:
1. Tentukan topik utama teks
2. Analisis sentimen (Positif/Negatif/Netral)
3. Buat ringkasan 1 kalimat

Format jawaban sebagai JSON.
"""
    
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Fungsi utama untuk menjalankan pipeline"""
    teks = """
Produk smartphone terbaru ini memiliki kamera yang sangat canggih.
Baterainya tahan lama dan layarnya sangat jernih.
Namun harganya cukup mahal untuk kalangan menengah.
"""

    try:
        hasil_nltk = preprocess_dengan_nltk(teks)
        
        if hasil_nltk:
            print("=== Hasil NLTK ===")
            print(f"Kata penting: {hasil_nltk['kata_penting']}")
            
            hasil_akhir = analisis_dengan_ollama(hasil_nltk)
            print("\n=== Hasil Ollama ===")
            print(hasil_akhir)
        else:
            print("Error: Preprocessing gagal")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

