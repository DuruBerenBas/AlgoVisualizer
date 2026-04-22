import streamlit as st
from data_structures import Stack

# 1. Sayfa Ayarları
st.set_page_config(page_title="AlgoVisualizer", page_icon="🧱")
st.title("Veri Yapıları Görselleştirici")
st.subheader("Stack (Yığın) Simülasyonu")

# 2. State Management (Durum Yönetimi)
# Streamlit her butona basıldığında kodu baştan aşağı yeniden çalıştırır.
# Stack'imizin sıfırlanmaması için onu 'session_state' (oturum hafızası) içinde saklıyoruz.
if 'stack' not in st.session_state:
    st.session_state.stack = Stack(limit=6)

# 3. Ekranı İkiye Bölme (Sol: Kontroller, Sağ: Görsel)
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Kontroller")

    # Kullanıcıdan girdi alma
    new_item = st.text_input("Yığına eklenecek değer:", max_chars=15)

    # Push Butonu
    if st.button("Push (Ekle)", type="primary"):
        if new_item:
            try:
                st.session_state.stack.push(new_item)
                st.success(f"'{new_item}' eklendi!")
            except OverflowError as e:
                st.error(str(e))
        else:
            st.warning("Lütfen bir değer girin.")

    # Pop Butonu
    if st.button("Pop (Çıkar)"):
        try:
            popped_item = st.session_state.stack.pop()
            st.success(f"'{popped_item}' çıkarıldı!")
        except IndexError as e:
            st.error(str(e))

    # Temizle Butonu
    if st.button("Stack'i Temizle"):
        st.session_state.stack = Stack(limit=6)
        st.info("Yığın sıfırlandı.")

with col2:
    st.header("Yığın Görünümü")

    # Arka plandaki Stack nesnesinden güncel elemanları çekiyoruz
    elements = st.session_state.stack.get_all_elements()

    if not elements:
        st.info("Şu an yığın boş. Sol taraftan eleman ekleyebilirsiniz.")
    else:
        # Elemanları yukarıdan aşağıya (LIFO) doğru kutular halinde çizdiriyoruz
        for item in elements:
            st.markdown(
                f"""
                <div style="
                    border: 2px solid #4CAF50; 
                    border-radius: 8px; 
                    padding: 15px; 
                    margin: 5px 0; 
                    text-align: center; 
                    background-color: #E8F5E9; 
                    color: #2E7D32; 
                    font-weight: bold; 
                    font-size: 18px;
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
                    {item}
                </div>
                """,
                unsafe_allow_html=True
            )