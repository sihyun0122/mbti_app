import streamlit as st

st.set_page_config(
    page_title="MBTI × 나루토 캐릭터 추천",
    page_icon="🍥",
    layout="centered"
)

st.title("🍥 MBTI로 보는 나루토 캐릭터 & 만화 추천")
st.write("나의 MBTI와 비슷한 나루토 캐릭터와 추천 만화를 알아보세요!")

st.markdown("---")

mbti_data = {

"INTJ":{
"character":"우치하 이타치",
"image":"https://upload.wikimedia.org/wikipedia/en/4/4c/Itachi_Uchiha.png",
"reason":"이타치는 전략적이고 깊이 있는 사고를 하는 인물입니다. 장기적인 계획과 냉철한 판단은 INTJ의 특징과 닮아 있습니다.",
"manga":["데스노트","닥터 스톤","플라네테스"]
},

"INTP":{
"character":"나라 시카마루",
"image":"https://upload.wikimedia.org/wikipedia/en/5/5a/Shikamaru_Nara.png",
"reason":"시카마루는 문제를 논리적으로 분석하고 최소한의 노력으로 최고의 전략을 찾는 캐릭터입니다.",
"manga":["닥터 스톤","스파이 패밀리","강철의 연금술사"]
},

"ENTJ":{
"character":"우치하 마다라",
"image":"https://upload.wikimedia.org/wikipedia/en/7/76/Madara_Uchiha.png",
"reason":"강한 리더십과 목표 중심 사고를 가진 마다라는 ENTJ의 카리스마 있는 지도자와 비슷합니다.",
"manga":["킹덤","진격의 거인","코드기어스"]
},

"ENTP":{
"character":"지라이야",
"image":"https://upload.wikimedia.org/wikipedia/en/3/3e/Jiraiya.png",
"reason":"자유로운 사고와 창의적인 아이디어를 가진 지라이야는 ENTP의 혁신가적 성향을 보여줍니다.",
"manga":["원피스","닥터 스톤","스파이 패밀리"]
},

"INFJ":{
"character":"나가토 (페인)",
"image":"https://upload.wikimedia.org/wikipedia/en/7/7e/Pain_%28Naruto%29.png",
"reason":"세상의 평화와 의미를 깊이 고민하는 나가토는 이상주의적 INFJ와 비슷합니다.",
"manga":["진격의 거인","바람계곡의 나우시카","약속의 네버랜드"]
},

"INFP":{
"character":"우즈마키 나루토",
"image":"https://upload.wikimedia.org/wikipedia/en/9/94/Naruto_Uzumaki.png",
"reason":"자신의 신념과 꿈을 끝까지 지키는 나루토는 이상을 중요하게 여기는 INFP의 모습과 닮았습니다.",
"manga":["나루토","원피스","마이 히어로 아카데미아"]
},

"ENFJ":{
"character":"나미카제 미나토",
"image":"https://upload.wikimedia.org/wikipedia/en/7/7e/Minato_Namikaze.png",
"reason":"사람들을 보호하고 이끄는 따뜻한 리더 미나토는 ENFJ의 지도자적 성향과 비슷합니다.",
"manga":["마이 히어로 아카데미아","하이큐","귀멸의 칼날"]
},

"ENFP":{
"character":"록 리",
"image":"https://upload.wikimedia.org/wikipedia/en/5/5a/Rock_Lee.png",
"reason":"긍정적이고 열정적인 록 리는 주변 사람들에게 에너지를 주는 ENFP와 닮았습니다.",
"manga":["원피스","하이큐","나루토"]
},

"ISTJ":{
"character":"하타케 카카시",
"image":"https://upload.wikimedia.org/wikipedia/en/2/27/Kakashi_Hatake.png",
"reason":"책임감 있고 규칙을 중요하게 생각하는 카카시는 ISTJ의 현실적이고 성실한 모습과 비슷합니다.",
"manga":["블리치","진격의 거인","주술회전"]
},

"ISFJ":{
"character":"휴가 히나타",
"image":"https://upload.wikimedia.org/wikipedia/en/9/97/Hinata_Hyuga.png",
"reason":"따뜻하고 배려심 많은 히나타는 ISFJ의 보호자 성향과 닮아 있습니다.",
"manga":["후르츠 바스켓","너에게 닿기를","하이큐"]
},

"ESTJ":{
"character":"센쥬 토비라마",
"image":"https://upload.wikimedia.org/wikipedia/en/0/0c/Tobirama_Senju.png",
"reason":"조직과 규칙을 중요하게 생각하는 토비라마는 ESTJ의 관리자 성향과 비슷합니다.",
"manga":["킹덤","도쿄 리벤저스","블리치"]
},

"ESFJ":{
"character":"노하라 린",
"image":"https://upload.wikimedia.org/wikipedia/en/0/02/Rin_Nohara.png",
"reason":"친절하고 협력적인 린은 사람을 돕는 ESFJ의 따뜻한 성격과 닮았습니다.",
"manga":["하이큐","너에게 닿기를","마이 히어로 아카데미아"]
},

"ISTP":{
"character":"우치하 사스케",
"image":"https://upload.wikimedia.org/wikipedia/en/4/4e/Sasuke_Uchiha.png",
"reason":"독립적이고 문제 해결 능력이 뛰어난 사스케는 ISTP의 실용적인 성향과 닮았습니다.",
"manga":["도쿄 구울","주술회전","블리치"]
},

"ISFP":{
"character":"데이다라",
"image":"https://upload.wikimedia.org/wikipedia/en/2/2d/Deidara.png",
"reason":"예술과 감각을 중요하게 생각하는 데이다라는 ISFP의 예술가 기질과 비슷합니다.",
"manga":["블루 피리어드","베르세르크","나나"]
},

"ESTP":{
"character":"킬러 비",
"image":"https://upload.wikimedia.org/wikipedia/en/e/e1/Killer_Bee.png",
"reason":"활동적이고 자신감 넘치는 킬러비는 ESTP의 모험가 성향과 닮았습니다.",
"manga":["원펀맨","도쿄 리벤저스","주술회전"]
},

"ESFP":{
"character":"우즈마키 쿠시나",
"image":"https://upload.wikimedia.org/wikipedia/en/0/05/Kushina_Uzumaki.png",
"reason":"밝고 에너지 넘치는 쿠시나는 사람들과 즐거움을 나누는 ESFP의 성격과 비슷합니다.",
"manga":["원피스","하이큐","나루토"]
}

}

mbti = st.selectbox("🧠 MBTI 유형 선택", list(mbti_data.keys()))

if st.button("🍥 나와 닮은 캐릭터 보기"):

    st.balloons()

    info = mbti_data[mbti]

    st.markdown(f"## 🍥 {info['character']}")

    st.image(info["image"], width=250)

    st.markdown("### ⭐ 왜 추천했을까요?")
    st.write(info["reason"])

    st.markdown("### 📚 추천 만화")

    for m in info["manga"]:
        st.write("📖", m)

    st.success("✨ 만화를 통해 다양한 성격과 이야기를 탐험해보세요!")

st.markdown("---")
st.caption("MBTI × 나루토 캐릭터 추천 앱")
