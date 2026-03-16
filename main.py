import streamlit as st

st.set_page_config(
    page_title="MBTI × 원피스 캐릭터",
    page_icon="🏴‍☠️"
)

st.title("🏴‍☠️ MBTI로 보는 원피스 캐릭터")
st.write("나의 MBTI와 닮은 원피스 캐릭터와 추천 만화를 알아보세요!")

st.markdown("---")

data = {

"INTJ":{
"character":"니코 로빈",
"image":"images/robin.png",
"reason":"로빈은 지적이고 전략적인 사고를 하는 캐릭터로 미래를 계획하는 INTJ와 닮았습니다.",
"manga":["데스노트","닥터 스톤","플라네테스"]
},

"INTP":{
"character":"트라팔가 로",
"image":"images/law.png",
"reason":"로는 분석적이고 논리적인 사고를 하는 인물로 INTP의 특징과 비슷합니다.",
"manga":["닥터 스톤","강철의 연금술사","스파이 패밀리"]
},

"ENTJ":{
"character":"샹크스",
"image":"images/shanks.png",
"reason":"샹크스는 카리스마와 리더십을 가진 인물로 ENTJ 지도자 유형과 닮았습니다.",
"manga":["킹덤","진격의 거인","코드기어스"]
},

"ENTP":{
"character":"버기",
"image":"images/buggy.png",
"reason":"버기는 예측 불가능한 아이디어로 상황을 바꾸는 캐릭터로 ENTP의 창의성과 비슷합니다.",
"manga":["은혼","원펀맨","스파이 패밀리"]
},

"INFJ":{
"character":"사보",
"image":"images/sabo.png",
"reason":"사보는 정의와 이상을 위해 싸우는 인물로 INFJ의 가치 중심 성향과 닮았습니다.",
"manga":["약속의 네버랜드","진격의 거인","나우시카"]
},

"INFP":{
"character":"우솝",
"image":"images/usopp.png",
"reason":"우솝은 상상력이 풍부하고 꿈을 중요하게 생각하는 캐릭터로 INFP와 비슷합니다.",
"manga":["원피스","나루토","마이 히어로 아카데미아"]
},

"ENFJ":{
"character":"포트거스 D. 에이스",
"image":"images/ace.png",
"reason":"에이스는 동료들을 보호하고 이끄는 따뜻한 리더로 ENFJ와 닮았습니다.",
"manga":["귀멸의 칼날","하이큐","마이 히어로 아카데미아"]
},

"ENFP":{
"character":"몽키 D. 루피",
"image":"images/luffy.png",
"reason":"루피는 자유롭고 열정적인 모험가로 ENFP의 특징과 매우 비슷합니다.",
"manga":["원피스","나루토","하이큐"]
},

"ISTJ":{
"character":"징베",
"image":"images/jinbe.png",
"reason":"징베는 책임감 있고 신뢰할 수 있는 인물로 ISTJ의 성실한 성향과 닮았습니다.",
"manga":["블리치","킹덤","주술회전"]
},

"ISFJ":{
"character":"토니토니 쵸파",
"image":"images/chopper.png",
"reason":"쵸파는 사람들을 돕는 따뜻한 캐릭터로 ISFJ 보호자 성향과 닮았습니다.",
"manga":["너에게 닿기를","후르츠 바스켓","하이큐"]
},

"ESTJ":{
"character":"나미",
"image":"images/nami.png",
"reason":"나미는 현실적이고 조직적인 판단을 하는 캐릭터로 ESTJ와 비슷합니다.",
"manga":["킹덤","블리치","도쿄 리벤저스"]
},

"ESFJ":{
"character":"상디",
"image":"images/sanji.png",
"reason":"상디는 동료를 챙기고 사람들을 돕는 따뜻한 성격으로 ESFJ와 닮았습니다.",
"manga":["하이큐","마이 히어로 아카데미아","너에게 닿기를"]
},

"ISTP":{
"character":"롤로노아 조로",
"image":"images/zoro.png",
"reason":"조로는 독립적이고 행동 중심적인 전사로 ISTP의 특징과 비슷합니다.",
"manga":["블리치","도쿄 구울","베르세르크"]
},

"ISFP":{
"character":"브룩",
"image":"images/brook.png",
"reason":"브룩은 음악과 감성을 중요하게 생각하는 예술가로 ISFP와 닮았습니다.",
"manga":["블루 피리어드","나나","베르세르크"]
},

"ESTP":{
"character":"프랑키",
"image":"images/franky.png",
"reason":"프랑키는 활동적이고 도전을 즐기는 캐릭터로 ESTP 모험가 성향과 닮았습니다.",
"manga":["원펀맨","주술회전","도쿄 리벤저스"]
},

"ESFP":{
"character":"유스타스 키드",
"image":"images/kid.png",
"reason":"키드는 강렬하고 에너지 넘치는 캐릭터로 ESFP의 활발한 성격과 비슷합니다.",
"manga":["원피스","하이큐","나루토"]
}

}

mbti = st.selectbox("🧠 MBTI 유형을 선택하세요", list(data.keys()))

if st.button("🏴‍☠️ 나와 닮은 캐릭터 보기"):

    st.balloons()

    info = data[mbti]

    st.header(info["character"])

    st.image(info["image"], width=300)

    st.subheader("⭐ 추천 이유")
    st.write(info["reason"])

    st.subheader("📚 추천 만화")

    for m in info["manga"]:
        st.write("📖", m)

st.markdown("---")
st.caption("MBTI × 원피스 캐릭터 추천 앱")
