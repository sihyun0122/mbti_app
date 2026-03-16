import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 탐색 + 나루토 캐릭터",
    page_icon="📚",
    layout="centered"
)

st.title("📚 MBTI 진로 탐색 & 나루토 캐릭터")
st.subheader("✨ 성격을 이해하고 나와 닮은 캐릭터와 진로를 찾아보세요")

st.write(
"""
이 앱에서는  
✔ MBTI 성격  
✔ 강점  
✔ 추천 진로  
✔ 추천 도서  
✔ 나루토 캐릭터  

를 함께 탐색할 수 있습니다 🍥
"""
)

st.markdown("---")

data = {

"INTJ":{
"trait":"전략적이고 미래지향적인 분석가",
"strength":["전략적 사고","문제 해결","독립적 학습"],
"career":["연구원","과학자","데이터 분석가"],
"books":["10대를 위한 미래 직업 이야기","과학자의 길","생각의 힘"],
"character":"우치하 이타치",
"image":"https://static.wikia.nocookie.net/naruto/images/7/7c/Itachi.png",
"reason":"이타치는 뛰어난 전략가이며 깊은 사고와 장기적인 계획을 세우는 인물입니다. 이는 INTJ의 전략적 사고와 매우 유사합니다."
},

"INTP":{
"trait":"논리와 탐구를 좋아하는 사색가",
"strength":["논리적 사고","호기심","분석력"],
"career":["연구원","프로그래머","철학자"],
"books":["과학 탐구 이야기","생각하는 힘","발명가 이야기"],
"character":"나라 시카마루",
"image":"https://static.wikia.nocookie.net/naruto/images/4/4b/Shikamaru.png",
"reason":"시카마루는 게으른 것처럼 보이지만 매우 뛰어난 전략과 논리를 가진 캐릭터로 INTP의 분석적 사고와 닮았습니다."
},

"ENTJ":{
"trait":"목표지향적 리더",
"strength":["리더십","전략","결단력"],
"career":["CEO","경영자","정책 전문가"],
"books":["리더십 수업","세상을 움직이는 리더","경영 이야기"],
"character":"우치하 마다라",
"image":"https://static.wikia.nocookie.net/naruto/images/5/5a/Madara.png",
"reason":"마다라는 강력한 카리스마와 리더십을 가진 인물로 큰 목표를 향해 조직을 이끄는 ENTJ의 특징과 닮았습니다."
},

"ENTP":{
"trait":"창의적인 아이디어 메이커",
"strength":["창의력","도전","토론 능력"],
"career":["창업가","기획자","마케터"],
"books":["아이디어 혁명","창업가의 생각","미래 직업 탐험"],
"character":"지라이야",
"image":"https://static.wikia.nocookie.net/naruto/images/7/70/Jiraiya.png",
"reason":"지라이야는 자유롭고 창의적이며 새로운 시도를 즐기는 인물로 ENTP의 아이디어 중심 성향과 비슷합니다."
},

"INFJ":{
"trait":"사람의 성장과 의미를 중요하게 생각하는 이상주의자",
"strength":["공감","통찰력","가치 중심 사고"],
"career":["상담가","심리학자","작가"],
"books":["마음을 이해하는 심리학","세상을 바꾸는 작은 행동","상담 이야기"],
"character":"나가토 (페인)",
"image":"https://static.wikia.nocookie.net/naruto/images/9/9c/Pain.png",
"reason":"나가토는 세상의 고통을 이해하고 평화를 고민하는 인물로 깊은 이상과 철학을 가진 INFJ와 닮았습니다."
},

"INFP":{
"trait":"이상과 가치를 중요하게 여기는 중재자",
"strength":["창의성","공감","자기성찰"],
"career":["작가","예술가","상담가"],
"books":["나의 꿈 찾기","예술가의 삶","자기 발견"],
"character":"우즈마키 나루토",
"image":"https://static.wikia.nocookie.net/naruto/images/9/94/Naruto.png",
"reason":"나루토는 자신의 신념과 꿈을 끝까지 지키는 인물로 이상과 가치 중심의 INFP와 잘 맞습니다."
},

"ENFJ":{
"trait":"사람의 성장을 돕는 리더",
"strength":["공감","리더십","소통"],
"career":["교사","코치","교육자"],
"books":["멘토의 역할","사람을 성장시키는 리더","교육 이야기"],
"character":"나미카제 미나토",
"image":"https://static.wikia.nocookie.net/naruto/images/5/5d/Minato.png",
"reason":"미나토는 주변 사람들을 성장시키고 보호하는 리더로 ENFJ의 따뜻한 지도자 모습과 닮았습니다."
},

"ENFP":{
"trait":"열정적이고 가능성을 발견하는 활동가",
"strength":["열정","창의력","사람과의 소통"],
"career":["기획자","방송인","작가"],
"books":["열정으로 도전하기","직업 여행","꿈 찾기"],
"character":"록 리",
"image":"https://static.wikia.nocookie.net/naruto/images/8/8d/Rock_Lee.png",
"reason":"록리는 긍정적이고 열정적인 성격으로 주변 사람들에게 에너지를 주는 ENFP와 매우 비슷합니다."
}

}

mbti = st.selectbox("🧠 MBTI 유형 선택", list(data.keys()))

if st.button("🚀 나의 진로 탐색"):

    st.balloons()

    info = data[mbti]

    st.markdown("## 🌟 성격 특징")
    st.info(info["trait"])

    st.markdown("## 💪 강점")
    for s in info["strength"]:
        st.write("✔", s)

    st.markdown("## 🎯 추천 진로")
    for c in info["career"]:
        st.write("🚀", c)

    st.markdown("## 📚 추천 도서")
    for b in info["books"]:
        st.write("📖", b)

    st.markdown("---")

    st.markdown(f"## 🍥 추천 나루토 캐릭터 : {info['character']}")

    st.image(info["image"], width=300)

    st.markdown("### ⭐ 추천 이유")
    st.write(info["reason"])

    st.markdown("---")

    st.success("✨ 진로는 정답이 아니라 탐험입니다. 다양한 경험을 해보세요!")

st.caption("🎓 MBTI 기반 청소년 진로 탐색 앱")
