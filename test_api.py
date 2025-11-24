#!/usr/bin/env python3
"""测试第三方OpenAI兼容API并获取可用模型列表"""

from openai import OpenAI

# 第三方API配置
API_KEY = "sk-R2zUCr15fXPHMc6vTb0gchsE6GHjcsMg5bhpw3zHZBdiYXms"
BASE_URL = "https://api.dev88.tech/v1"

print("=" * 60)
print("测试第三方API连接")
print("=" * 60)
print(f"Base URL: {BASE_URL}")
print(f"API Key: {API_KEY[:20]}...")
print()

try:
    # 创建客户端
    client = OpenAI(
        api_key=API_KEY,
        base_url=BASE_URL,
        timeout=30
    )

    print("[OK] 客户端创建成功！")
    print()

    # 获取模型列表
    print("[INFO] 正在获取可用模型列表...")
    print("-" * 60)

    models = client.models.list()

    print(f"\n[OK] 成功获取 {len(models.data)} 个模型\n")
    print("=" * 60)
    print("可用模型列表:")
    print("=" * 60)

    # 分类展示模型
    gpt4_models = []
    gpt35_models = []
    other_models = []

    for model in models.data:
        model_id = model.id
        if 'gpt-4' in model_id.lower():
            gpt4_models.append(model_id)
        elif 'gpt-3.5' in model_id.lower():
            gpt35_models.append(model_id)
        else:
            other_models.append(model_id)

    if gpt4_models:
        print("\n[GPT-4] GPT-4系列模型:")
        for m in sorted(gpt4_models):
            print(f"  - {m}")

    if gpt35_models:
        print("\n[GPT-3.5] GPT-3.5系列模型:")
        for m in sorted(gpt35_models):
            print(f"  - {m}")

    if other_models:
        print("\n[OTHER] 其他模型:")
        for m in sorted(other_models):
            print(f"  - {m}")

    print("\n" + "=" * 60)

    # 测试简单的对话
    print("\n[TEST] 测试API对话功能...")
    print("-" * 60)

    # 选择一个模型进行测试
    test_model = gpt4_models[0] if gpt4_models else (gpt35_models[0] if gpt35_models else models.data[0].id)
    print(f"使用模型: {test_model}")

    response = client.chat.completions.create(
        model=test_model,
        messages=[
            {"role": "user", "content": "Say 'API连接成功!' in Chinese"}
        ],
        max_tokens=50
    )

    reply = response.choices[0].message.content
    print(f"\n[OK] API响应: {reply}")
    print()

    # 推荐配置
    print("=" * 60)
    print("[RECOMMEND] ShortGPT推荐配置:")
    print("=" * 60)

    # 找出最适合的模型
    recommended = None
    if any('gpt-4o-mini' in m for m in gpt4_models):
        recommended = next(m for m in gpt4_models if 'gpt-4o-mini' in m)
    elif any('gpt-4' in m for m in gpt4_models):
        recommended = gpt4_models[0]
    elif gpt35_models:
        recommended = gpt35_models[0]
    else:
        recommended = models.data[0].id

    print(f"\n推荐模型: {recommended}")
    print(f"Base URL: {BASE_URL}")
    print(f"API Key: {API_KEY[:20]}...")
    print("\n[OK] API测试完成！可以开始配置ShortGPT了。")

except Exception as e:
    print(f"\n[ERROR] 错误: {e}")
    print(f"\n可能的原因:")
    print("  1. API密钥无效")
    print("  2. Base URL错误")
    print("  3. 网络连接问题")
    print("  4. API配额已用完")

print("\n" + "=" * 60)
