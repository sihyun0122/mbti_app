import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 도서 추천",
    page_icon="📚",
    layout="centered"
)

st.title("📚 MBTI 기반 청소년 진로 도서 추천")
st.subheader("✨ 나의 MBTI로 진로 탐색 도서를 찾아보세요!")

st.write("MBTI 유형을 선택하면 어울리는 진로 탐색 도서를 추천해드립니다 😊")

# MBTI 도서 데이터
books = {
"INTJ": {
"title": "세상을 바꾸는 과학자",
"desc": "전략적 사고를 가진 INTJ에게 과학과 연구 분야의 길을 보여주는 책"
},
"INTP": {
"title": "호기심 많은 과학자의 실험 노트",
"desc": "논리와 탐구를 좋아하는 INTP에게 추천하는 탐구형 진로 도서"
},
"ENTJ": {
"title": "미래를 이끄는 리더",
"desc": "리더십과 목표지향적인 ENTJ에게 맞는 진로 이야기"
},
"ENTP": {
"title": "아이디어로 세상을 바꾸다",
"desc": "창의적인 ENTP를 위한 혁신가들의 이야기"
},
"INFJ": {
"title": "세상을 돕는 사람들",
"desc": "상담가, 사회복지사 등 사람을 돕는 직업을 소개"
},
"INFP": {
"title": "나의 꿈을 찾는 여행",
"desc": "자신의 가치와 꿈을 찾고 싶은 INFP에게 추천"
},
"ENFJ": {
"title": "사람을 성장시키는 리더",
"desc": "교육자와 멘토의 길을 소개하는 책"
},
"ENFP": {
"title": "세상 속 다양한 직업 탐험",
"desc": "호기심 많은 ENFP에게 다양한 진로를 소개"
},
"ISTJ": {
"title": "성실한 전문가의 길",
"desc": "체계적이고 책임감 있는 직업 이야기"
},
"ISFJ": {
"title": "따뜻한 마음의 직업",
"desc": "간호사, 교사 등 도움을 주는 직업"
},
"ESTJ": {
"title": "조직을 움직이는 힘",
"desc": "경영과 조직관리 직업 소개"
},
"ESFJ": {
"title": "함께 일하는 즐거움",
"desc": "사람과 함께 일하는 직업 탐색"
},
"ISTP": {
"title": "손으로 만드는 미래 직업",
"desc": "엔지니어, 기술직 이야기"
},
"ISFP": {
"title": "예술로 표현하는 세상",
"desc": "예술과 창작 분야 진로"
},
"ESTP": {
"title": "도전하는 직업 세계",
"desc": "활동적이고 모험적인 직업 이야기"
},
"ESFP": {
"title": "즐거운 무대의 직업들",
"desc": "공연, 방송, 엔터테인먼트 직업"
}
}

mbti = st.selectbox(
"🧠 MBTI를 선택하세요",
list(books.keys())
)

if st.button("📖 진로 도서 추천 받기"):
    
    book = books[mbti]
    
    st.balloons()  # 풍선 효과
    
    st.success(f"✨ {mbti} 유형에게 추천하는 책!")

    st.markdown("---")

    st.markdown(f"""
    ### 📚 {book['title']}

    💡 **추천 이유**  
    {book['desc']}

    🚀 이 책을 통해 자신의 진로와 적성을 탐색해보세요!
    """)

    st.markdown("---")

st.caption("🎓 MBTI 기반 청소년 진로 탐색 도서 추천 앱")
