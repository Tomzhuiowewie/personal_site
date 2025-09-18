from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

# 初始化 Ark 客户端
client = OpenAI(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key='b4260295-e9af-4c6d-9e06-0f44efab6681',  # 请提前设置环境变量
)

def chat_once(user_input: str) -> str:
    """调用 Ark 大模型，返回回复"""
    completion = client.chat.completions.create(
        model="deepseek-v3-250324",  # 你的推理接入点 ID
        messages=[
            {"role": "system", "content": "你是人工智能助手"},
            {"role": "user", "content": user_input},
        ],
    )
    return completion.choices[0].message.content

@csrf_exempt
def chat_view(request):
    """同时支持 GET（返回页面）和 POST（返回 AI 回复）"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            if not user_message.strip():
                return JsonResponse({"reply": "请说点什么吧～"})

            reply = chat_once(user_message)
            return JsonResponse({"reply": reply})

        except Exception as e:
            return JsonResponse({"reply": f"出错了：{str(e)}"})
    return render(request, "chat/chat.html")
