from shortGPT.gpt import gpt_utils
import json
import re

def generate_title_description_dict(content):
    out = {"title": "", "description":""}
    chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/yt_title_description.yaml')
    chat = chat.replace("<<CONTENT>>", f"{content}")

    max_attempts = 3
    attempts = 0
    while (out["title"] == "" or out["description"] == "") and attempts < max_attempts:
        attempts += 1
        result = gpt_utils.llm_completion(chat_prompt=chat, system=system, temp=1)
        try:
            # 移除可能的markdown代码块标记
            result_cleaned = re.sub(r'```(?:json)?\s*|\s*```', '', result)

            # 尝试直接解析JSON
            try:
                response = json.loads(result_cleaned)
            except:
                # 如果失败，尝试从结果中提取JSON对象
                json_match = re.search(r'\{[^{}]*"title"[^{}]*"description"[^{}]*\}', result_cleaned, re.DOTALL)
                if json_match:
                    response = json.loads(json_match.group())
                else:
                    print(f"Cannot parse YouTube metadata from: {result[:100]}")
                    continue

            if "title" in response:
                out["title"] = response["title"]
            if "description" in response:
                out["description"] = response["description"]
        except Exception as e:
            print(f"Error generating YouTube metadata: {e}")

    # 如果还是失败，使用默认值
    if not out["title"]:
        out["title"] = "AI Generated Short Video"
    if not out["description"]:
        out["description"] = "This video was automatically generated using AI."

    return out['title'], out['description']
