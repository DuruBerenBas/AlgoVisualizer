import streamlit as st
from data_structures import Stack, Queue

# 1. Sayfa Ayarları (Ekranı biraz daha geniş kullanmak için layout="wide" ekledik)
st.set_page_config(page_title="AlgoVisualizer", page_icon="🧱", layout="wide")

# 2. Yan Menü (Sidebar) Kurulumu
st.sidebar.title("Menü")
st.sidebar.markdown("Test etmek istediğiniz veri yapısını seçin:")
secim = st.sidebar.radio("", ["Stack (Yığın)", "Queue (Kuyruk)"])

st.title("Veri Yapıları Görselleştirici")

# ==========================================
# STACK (YIĞIN) ARAYÜZÜ
# ==========================================
if secim == "Stack (Yığın)":
    st.subheader("Stack (Yığın) Simülasyonu - LIFO")

    if 'stack' not in st.session_state:
        st.session_state.stack = Stack(limit=6)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("Kontroller")
        new_item = st.text_input("Yığına eklenecek değer:", key="stack_input", max_chars=15)

        if st.button("Push (Ekle)", type="primary"):
            if new_item:
                try:
                    st.session_state.stack.push(new_item)
                    st.success(f"'{new_item}' eklendi!")
                except OverflowError as e:
                    st.error(str(e))
            else:
                st.warning("Lütfen bir değer girin.")

        if st.button("Pop (Çıkar)"):
            try:
                popped_item = st.session_state.stack.pop()
                st.success(f"'{popped_item}' çıkarıldı!")
            except IndexError as e:
                st.error(str(e))

        if st.button("Stack'i Temizle"):
            st.session_state.stack = Stack(limit=6)
            st.info("Yığın sıfırlandı.")

    with col2:
        st.header("Yığın Görünümü")
        elements = st.session_state.stack.get_all_elements()

        if not elements:
            st.info("Şu an yığın boş. Sol taraftan eleman ekleyebilirsiniz.")
        else:
            for item in elements:
                st.markdown(
                    f"""
                    <div style="
                        border: 2px solid #4CAF50; border-radius: 8px; padding: 15px; 
                        margin: 5px 0; text-align: center; background-color: #E8F5E9; 
                        color: #2E7D32; font-weight: bold; font-size: 18px;
                        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
                        {item}
                    </div>
                    """, unsafe_allow_html=True
                )

# ==========================================
# QUEUE (KUYRUK) ARAYÜZÜ
# ==========================================
elif secim == "Queue (Kuyruk)":
    st.subheader("Queue (Kuyruk) Simülasyonu - FIFO")

    if 'queue' not in st.session_state:
        st.session_state.queue = Queue(limit=6)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("Kontroller")
        new_item_q = st.text_input("Kuyruğa eklenecek değer:", key="queue_input", max_chars=15)

        if st.button("Enqueue (Sıraya Gir)", type="primary"):
            if new_item_q:
                try:
                    st.session_state.queue.enqueue(new_item_q)
                    st.success(f"'{new_item_q}' sıraya girdi!")
                except OverflowError as e:
                    st.error(str(e))
            else:
                st.warning("Lütfen bir değer girin.")

        if st.button("Dequeue (Sıradan Çık)"):
            try:
                dequeued_item = st.session_state.queue.dequeue()
                st.success(f"'{dequeued_item}' sıradan çıktı!")
            except IndexError as e:
                st.error(str(e))

        if st.button("Kuyruğu Temizle"):
            st.session_state.queue = Queue(limit=6)
            st.info("Kuyruk sıfırlandı.")

    with col2:
        st.header("Kuyruk Görünümü")
        elements = st.session_state.queue.get_all_elements()

        if not elements:
            st.info("Şu an kuyruk boş. Sol taraftan eleman ekleyebilirsiniz.")
        else:
            # Elemanları yan yana (yatay) dizmek için HTML Flexbox kullanıyoruz
            boxes = "".join([
                f"""<div style="
                        border: 2px solid #2196F3; border-radius: 8px; padding: 15px 25px; 
                        margin: 5px; text-align: center; background-color: #E3F2FD; 
                        color: #1565C0; font-weight: bold; font-size: 18px;
                        box-shadow: 2px 2px 5px rgba(0,0,0,0.1); min-width: 80px;">
                        {item}
                    </div>""" for item in elements
            ])

            st.markdown(
                f"""
                <div style="display: flex; flex-direction: row; align-items: center; overflow-x: auto; padding-top: 10px;">
                    <div style="margin-right: 15px; font-weight: bold; color: #757575;">ÇIKIŞ ⬅️</div>
                    {boxes}
                    <div style="margin-left: 15px; font-weight: bold; color: #757575;">⬅️ GİRİŞ</div>
                </div>
                """, unsafe_allow_html=True
            )