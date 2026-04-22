import streamlit as st
from data_structures import Stack, Queue, LinkedList

# 1. Sayfa Ayarları
st.set_page_config(page_title="AlgoVisualizer", page_icon="🧱", layout="wide")

# 2. Yan Menü (Sidebar)
st.sidebar.title("Navigasyon")
st.sidebar.markdown("Görselleştirmek istediğiniz veri yapısını seçin:")
secim = st.sidebar.radio("", ["Stack (Yığın)", "Queue (Kuyruk)", "Linked List (Bağlı Liste)"])

st.title("Veri Yapıları Görselleştirici")

# ==========================================
# STACK (YIĞIN) BÖLÜMÜ
# ==========================================
if secim == "Stack (Yığın)":
    st.subheader("Stack Simülasyonu (LIFO - Son Giren İlk Çıkar)")
    if 'stack' not in st.session_state:
        st.session_state.stack = Stack(limit=6)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Kontroller")
        val = st.text_input("Değer girin:", key="s_in")
        if st.button("Push (Ekle)", type="primary"):
            if val:
                try:
                    st.session_state.stack.push(val)
                    st.success(f"'{val}' eklendi.")
                except OverflowError as e: st.error(str(e))
            else: st.warning("Değer giriniz.")
        if st.button("Pop (Çıkar)"):
            try:
                p = st.session_state.stack.pop()
                st.success(f"'{p}' çıkarıldı.")
            except IndexError as e: st.error(str(e))

    with col2:
        st.header("Görünüm")
        items = st.session_state.stack.get_all_elements()
        if not items: st.info("Stack boş.")
        else:
            for item in items:
                st.markdown(f'<div style="border:2px solid #4CAF50; border-radius:8px; padding:15px; margin:5px 0; text-align:center; background-color:#E8F5E9; color:#2E7D32; font-weight:bold;">{item}</div>', unsafe_allow_html=True)

# ==========================================
# QUEUE (KUYRUUK) BÖLÜMÜ
# ==========================================
elif secim == "Queue (Kuyruk)":
    st.subheader("Queue Simülasyonu (FIFO - İlk Giren İlk Çıkar)")
    if 'queue' not in st.session_state:
        st.session_state.queue = Queue(limit=6)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Kontroller")
        val_q = st.text_input("Değer girin:", key="q_in")
        if st.button("Enqueue (Ekle)", type="primary"):
            if val_q:
                try:
                    st.session_state.queue.enqueue(val_q)
                    st.success(f"'{val_q}' eklendi.")
                except OverflowError as e: st.error(str(e))
        if st.button("Dequeue (Çıkar)"):
            try:
                d = st.session_state.queue.dequeue()
                st.success(f"'{d}' çıkarıldı.")
            except IndexError as e: st.error(str(e))

    with col2:
        st.header("Görünüm")
        items = st.session_state.queue.get_all_elements()
        if not items: st.info("Kuyruk boş.")
        else:
            boxes = "".join([f'<div style="border:2px solid #2196F3; border-radius:8px; padding:15px; margin:5px; background-color:#E3F2FD; color:#1565C0; font-weight:bold; min-width:80px; text-align:center;">{i}</div>' for i in items])
            st.markdown(f'<div style="display:flex; flex-direction:row; align-items:center; overflow-x:auto;"> <b>ÇIKIŞ</b> ⬅️ {boxes} ⬅️ <b>GİRİŞ</b> </div>', unsafe_allow_html=True)

# ==========================================
# LINKED LIST BÖLÜMÜ
# ==========================================
else:
    st.subheader("Linked List Simülasyonu (Bağlı Liste)")
    if 'llist' not in st.session_state:
        st.session_state.llist = LinkedList()

    col1, col2 = st.columns([1, 2])
    with col1:
        st.header("Kontroller")
        val_ll = st.text_input("Değer girin:", key="ll_in")
        if st.button("Başa Ekle", type="primary"):
            if val_ll: st.session_state.llist.insert_at_head(val_ll)
        if st.button("Sona Ekle"):
            if val_ll: st.session_state.llist.insert_at_tail(val_ll)
        if st.button("Listeyi Sıfırla"):
            st.session_state.llist = LinkedList()

    with col2:
        st.header("Görünüm")
        items = st.session_state.llist.get_all_elements()
        if not items: st.info("Liste boş.")
        else:
            nodes = ""
            for i, item in enumerate(items):
                nodes += f'<div style="border:2px solid #9C27B0; border-radius:8px; padding:10px; background-color:#F3E5F5; color:#7B1FA2; font-weight:bold; display:inline-block;">{item} | Next</div>'
                if i < len(items) - 1:
                    nodes += '<span style="font-size:24px; margin:0 10px;">➔</span>'
                else:
                    nodes += '<span style="font-size:24px; margin:0 10px;">➔</span> <code style="color:red;">None</code>'
            st.markdown(f'<div style="display:flex; align-items:center; flex-wrap:wrap;">{nodes}</div>', unsafe_allow_html=True)