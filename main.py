import streamlit as st

st.set_page_config(
    page_title="MBTI × 원피스 캐릭터",
    page_icon="🏴‍☠️",
    layout="centered"
)

st.title("🏴‍☠️ MBTI로 보는 원피스 캐릭터")
st.write("나의 MBTI와 닮은 원피스 캐릭터와 추천 만화를 알아보세요!")

st.markdown("---")

data = {

"INTJ":{
"character":"니코 로빈",
"image":"https://upload.wikimedia.org/wikipedia/en/7/7e/Nico_Robin.png",
"reason":"로빈은 매우 지적이고 전략적으로 상황을 판단하는 캐릭터입니다. 차분한 분석 능력과 장기적인 시야는 INTJ의 특징과 잘 맞습니다.",
"manga":["데스노트","닥터 스톤","플라네테스"]
},

"INTP":{
"character":"트라팔가 로",
"image":"https://upload.wikimedia.org/wikipedia/en/0/0b/Trafalgar_Law.png",
"reason":"로는 분석적이고 계산적인 사고를 하는 캐릭터로 복잡한 전략을 세우는 능력이 뛰어납니다. 이는 INTP의 논리적 성향과 닮았습니다.",
"manga":["닥터 스톤","강철의 연금술사","스파이 패밀리"]
},

"ENTJ":{
"character":"샹크스",
"image":"https://upload.wikimedia.org/wikipedia/en/7/70/Shanks.png",
"reason":"샹크스는 강한 카리스마와 리더십을 가진 인물로 주변 사람들에게 큰 영향을 줍니다. 목표 중심적인 ENTJ 리더와 비슷합니다.",
"manga":["킹덤","진격의 거인","코드기어스"]
},

"ENTP":{
"character":"버기",
"image":"https://upload.wikimedia.org/wikipedia/en/7/7e/Buggy_the_Clown.png",
"reason":"버기는 예측 불가능하고 독특한 아이디어로 상황을 바꾸는 캐릭터입니다. 창의적인 ENTP의 모습과 닮았습니다.",
"manga":["원펀맨","스파이 패밀리","은혼"]
},

"INFJ":{
"character":"사보",
"image":"https://upload.wikimedia.org/wikipedia/en/0/09/Sabo.png",
"reason":"사보는 정의와 이상을 위해 싸우는 인물로 세상을 더 좋게 만들고자 합니다. 이는 INFJ의 이상주의적 가치와 닮았습니다.",
"manga":["약속의 네버랜드","진격의 거인","나우시카"]
},

"INFP":{
"character":"우솝",
"image":"https://upload.wikimedia.org/wikipedia/en/2/2d/Usopp.png",
"reason":"우솝은 상상력이 풍부하고 꿈을 중요하게 생각하는 캐릭터입니다. 자신의 이야기를 만들어가는 모습이 INFP와 비슷합니다.",
"manga":["나루토","원피스","마이 히어로 아카데미아"]
},

"ENFJ":{
"character":"포트거스 D. 에이스",
"image":"https://upload.wikimedia.org/wikipedia/en/4/4c/Portgas_D_Ace.png",
"reason":"에이스는 동료들을 보호하고 이끄는 따뜻한 리더입니다. 사람들을 위해 행동하는 ENFJ의 특징과 닮았습니다.",
"manga":["귀멸의 칼날","하이큐","마이 히어로 아카데미아"]
},

"ENFP":{
"character":"몽키 D. 루피",
"image":"https://upload.wikimedia.org/wikipedia/en/c/cb/Monkey_D_Luffy.png",
"reason":"루피는 자유롭고 열정적인 모험가입니다. 사람들에게 영감을 주는 긍정적인 에너지는 ENFP의 특징과 매우 비슷합니다.",
"manga":["원피스","하이큐","나루토"]
},

"ISTJ":{
"character":"징베",
"image":"https://upload.wikimedia.org/wikipedia/en/9/9f/Jinbe.png",
"reason":"징베는 책임감 있고 신뢰할 수 있는 인물입니다. 원칙을 지키고 동료를 보호하는 모습은 ISTJ의 성향과 닮았습니다.",
"manga":["블리치","킹덤","주술회전"]
},

"ISFJ":{
"character":"토니토니 쵸파",
"image":"https://upload.wikimedia.org/wikipedia/en/5/5e/Tony_Tony_Chopper.png",
"reason":"쵸파는 따뜻하고 사람들을 돕는 것을 좋아합니다. 배려심 많은 ISFJ의 성격과 매우 비슷합니다.",
"manga":["후르츠 바스켓","너에게 닿기를","하이큐"]
},

"ESTJ":{
"character":"나미",
"image":"https://upload.wikimedia.org/wikipedia/en/7/73/Nami.png",
"reason":"나미는 현실적이고 상황을 정확히 판단하며 팀을 관리하는 능력이 뛰어납니다. 조직적인 ESTJ의 특징과 닮았습니다.",
"manga":["도쿄 리벤저스","킹덤","블리치"]
},

"ESFJ":{
"character":"상디",
"image":"https://upload.wikimedia.org/wikipedia/en/0/0c/Sanji.png",
"reason":"상디는 동료들을 챙기고 사람들을 위해 행동하는 따뜻한 인물입니다. 협력적이고 배려심 있는 ESFJ와 비슷합니다.",
"manga":["하이큐","마이 히어로 아카데미아","너에게 닿기를"]
},

"ISTP":{
"character":"롤로노아 조로",
"image":"https://upload.wikimedia.org/wikipedia/en/9/9e/Roronoa_Zoro.png",
"reason":"조로는 독립적이고 행동 중심적인 캐릭터입니다. 실전 문제 해결 능력이 뛰어난 ISTP와 닮았습니다.",
"manga":["베르세르크","블리치","도쿄 구울"]
},

"ISFP":{
"character":"브룩",
"image":"https://upload.wikimedia.org/wikipedia/en/4/4f/Brook_One_Piece.png",
"reason":"브룩은 감성적이고 예술적인 음악가입니다. 자유로운 표현을 중요하게 여기는 ISFP의 성향과 비슷합니다.",
"manga":["블루 피리어드","나나","베르세르크"]
},

"ESTP":{
"character":"프랑키",
"image":"https://upload.wikimedia.org/wikipedia/en/6/65/Franky_One_Piece.png",
"reason":"프랑키는 활동적이고 행동력이 강한 캐릭터입니다. 도전을 즐기는 ESTP의 모험가 성향과 닮았습니다.",
"manga":["원펀맨","주술회전","도쿄 리벤저스"]
},

"ESFP":{
"character":"루피",
"image":"https://upload.wikimedia.org/wikipedia/en/c/cb/Monkey_D_Luffy.png",
"reason":"루피는 즐거움과 모험을 사랑하며 주변 사람들을 행복하게 만드는 캐릭터입니다. 이는 ESFP의 활발한 성격과 비슷합니다.",
"manga":["원피스","하이큐","나루토"]
}

}

mbti = st.selectbox("🧠 MBTI 유형을 선택하세요", list(data.keys()))

if st.button("🏴‍☠️ 나와 닮은 캐릭터 보기"):

    st.balloons()

    info = data[mbti]

    st.markdown(f"## 🏴‍☠️ {info['character']}")

    st.image(info["image"], width=250)

    st.markdown("### ⭐ 추천 이유")
    st.write(info["reason"])

    st.markdown("### 📚 추천 만화")

    for m in info["manga"]:
        st.write("📖", m)

    st.success("✨ 만화를 통해 다양한 성격과 이야기를 탐험해보세요!")

st.markdown("---")
st.caption("MBTI × 원피스 캐릭터 추천 앱")
