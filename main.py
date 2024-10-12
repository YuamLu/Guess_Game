import os
import requests
import streamlit as st
import random

# Title of the web app
st.title("你說我猜遊戲")
# Description of the web app
st.markdown("在這個遊戲中，LLM(大型語言模型)將扮演主持人，他會在心中想一個物品，並且給你一個提示，你需要通過提問來猜出這個物品是什麼。當你有答案了，使用'答案是XX嗎?'之類的句型來確認答案。不要想著作弊或搭訕人家，LLM不會裡你喔~還有記得填寫班級座號（模型有時後會問你問題，忽略它就好）")
st.markdown("*Developed by 0x.Yuan@CPSD.3rd*")

class_and_seat = st.text_input("您的班級座號", max_chars=5, key="class_and_seat")

api_key = os.environ.get("TOGETHER_API_KEY")
webhook = os.environ.get("WEBHOOL_URL")

# Function to call the AI model API
def call_ai_model(prompt, past_messages):
    endpoint = 'https://api.together.xyz/v1/chat/completions'
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "Qwen/Qwen1.5-72B-Chat",
        "max_tokens": 512,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        "stop": ["<|im_end|>", "<|im_start|>"],
        "messages": past_messages + [{"content": prompt, "role": "user"}]
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    return response.json()['choices'][0]['message']['content']

topics = [
    "長頸鹿", "月亮", "潛水艇", "刺蝟", "火箭", "泰坦尼克號", "富士山", "大提琴", "小丑", "斑馬",
    "滑板", "書籍", "掃地機器人", "桑拿", "手風琴", "哆啦A夢", "櫻桃", "網球", "拖拉機", "手術",
    "泡泡", "巧克力", "獨木舟", "咖啡機", "遙控器", "冰淇淋", "萬花筒", "太空人", "海盜", "麵包機",
    "拳擊", "橄欖球", "沙漏", "航空母艦", "颱風", "壽司", "熱氣球", "牛仔", "畫架", "孔雀",
    "直升機", "藍鯨", "魔術師", "獨角獸", "吸塵器", "保齡球", "秋千", "釣魚", "風箏", "蜜蜂",
    "營火", "彈簧床", "照相機", "滑冰鞋", "滑雪板", "鬍鬚", "指南針", "潛水鏡", "帳篷", "煎鍋",
    "眼鏡蛇", "蝴蝶結", "螞蟻", "象棋", "珍珠奶茶", "三明治", "甜甜圈", "糖果", "螢火蟲", "浣熊",
    "龍", "機器人", "樹蛙", "鯊魚", "象", "獅子", "孔雀", "企鵝", "公雞", "蝸牛",
    "蠍子", "植物", "眼鏡", "太陽", "地球", "火星", "熊貓", "鴨子", "蘋果", "馬鈴薯",
    "巴士", "地鐵", "自行車", "馬車", "火車", "摩托車", "滑翔機", "水上摩托", "遊艇", "帆船"
]

if 'topic' not in st.session_state:
    st.session_state.topic = random.choice(topics)

# st.write(f"題目: {st.session_state.topic}")

# Initialize session state for tracking conversation
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "user", "content": "你是一為富有幽默感的專家,擅長當作'你說我猜'遊戲的主持人,並且只能用中文來回覆。你要扮演遊戲中的主持人,妥善的根據題目來回答我的問題,在不透露答案的情況下,讓挑戰者猜出答案。現在,遊戲即將開始,你應該試著先用一句非常簡短的話來描述題目,只能描述題目的一個性質,例如'一種動物', '一種家電'...,然後讓挑戰者來提問。你的題目是:topic。盡量讓我詢問越多問題,問題的難易度越高越好,只能直接回答我的問題,不能讓我投機取巧,例如當我向你要求更多提示時,有於我的問題並不夠準確,可能會讓我作弊,因此你必須拒絕回答我這個問題,切紀要保持嚴厲。當使用者成功猜出題目,你要說'{恭喜答對!}。現在,遊戲開始!你不需要問我問題，專心回答問題就好".replace("topic", st.session_state.topic)}]
    assistant_response = call_ai_model(st.session_state.messages[0]["content"], st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if "你是一為富有幽默感的專家" not in message["content"]:
            st.markdown(message["content"])
        else:
            # welcome message
            st.markdown("**遊戲開始！ Enjoy~**")

user_input = st.chat_input("提問：")

def send_record(record):
    url = webhook

    data = {
        'key': record,
    }
    requests.post(url, json=data)


if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    assistant_response = call_ai_model(user_input, st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    for message in st.session_state.messages[-2:]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if "恭喜答對!" in assistant_response:
        st.write("你猜對了!")
        # print chat history
        record = ''
        if "class_and_seat" in st.session_state:
            record = f"{st.session_state.class_and_seat}@"
        for message in st.session_state.messages:
            record += f"{message['role']}: {message['content']}\n"

        send_record(record)

        st.write("由於某些尚未解決的Bug，請自行刷新頁面再玩一次。")


    elif "我無法透露更多提示" in assistant_response:
        st.write("請繼續提問以猜出答案。")
