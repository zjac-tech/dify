import requests

BASE_URL = "http://localhost:5000/messages"
HEADERS = {
    "Authorization": "Bearer YOUR_APP_TOKEN",  # 替换为你的 token
    "Content-Type": "application/json"
}

def delete_message(message_id: str):
    url = f"{BASE_URL}/{message_id}"
    response = requests.delete(url, headers=HEADERS)
    print(f"DELETE response ({message_id}):", response.status_code, response.json())

def update_message(message_id: str, new_query: str, new_answer: str = ""):
    url = f"{BASE_URL}/{message_id}"
    payload = {
        "query": new_query,
        "answer": new_answer
    }
    response = requests.put(url, json=payload, headers=HEADERS)
    print(f"PUT response ({message_id}):", response.status_code, response.json())

if __name__ == "__main__":
    test_message_id = "6e32c5b4-cc58-4e4b-a50e-c43c0f07f13f"  # 替换为你实际的 message_id

    # 测试更新
    update_message(test_message_id, "新问题内容示例", "新回答内容示例")

    # 测试删除
    delete_message(test_message_id)
