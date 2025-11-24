from shortGPT.gpt import gpt_utils
import random
import json
def generateRedditPostMetadata(title):
    name = generateUsername()
    if title and title[0] == '"':
        title = title.replace('"', '')
    n_months = random.randint(1,11)
    header = f"{name} - {n_months} months ago"
    n_comments = random.random() * 10 + 2
    n_upvotes = n_comments*(1.2+ random.random()*2.5)
    return title, header, f"{n_comments:.1f}k", f"{n_upvotes:.1f}k"


def getInterestingRedditQuestion():
    import time
    chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/reddit_generate_question.yaml')
    # 添加时间戳和随机数来确保每次请求都不同，避免API缓存
    unique_seed = f"Seed: {random.randint(10000, 99999)} | Timestamp: {int(time.time())}\n"
    chat = unique_seed + chat
    return gpt_utils.llm_completion(chat_prompt=chat, system=system, temp=1.5)

def createRedditScript(question):
    import time
    chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/reddit_generate_script.yaml')
    chat = chat.replace("<<QUESTION>>", question)
    # 添加时间戳和随机数来确保每次脚本生成都不同
    unique_seed = f"\nUnique ID: {random.randint(10000, 99999)}-{int(time.time())}\n"
    chat = chat + unique_seed
    result = "Reddit, " + question +" "+gpt_utils.llm_completion(chat_prompt=chat, system=system, temp=1.5)
    return result
    

def getRealisticness(text):
    chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/reddit_filter_realistic.yaml')
    chat = chat.replace("<<INPUT>>", text)
    attempts = 0
    while attempts <= 4:
        attempts+=1
        try:
            result = gpt_utils.llm_completion(chat_prompt=chat, system=system, temp=1)
            # 移除可能的markdown代码块标记
            import re
            result_cleaned = re.sub(r'```(?:json)?\s*|\s*```', '', result)

            # 尝试直接解析JSON
            try:
                return json.loads(result_cleaned)['score']
            except:
                # 如果失败，尝试从结果中提取JSON对象
                json_match = re.search(r'\{[^{}]*"score"[^{}]*\}', result_cleaned)
                if json_match:
                    return json.loads(json_match.group())['score']
                # 如果还是失败，尝试提取数字
                score_match = re.search(r'["\'"]?score["\'"]?\s*[:=]\s*(\d+(?:\.\d+)?)', result_cleaned)
                if score_match:
                    return float(score_match.group(1))
                raise Exception(f"Cannot parse score from: {result[:100]}")
        except Exception as e:
            print("Error in getRealisticness", e.args[0] if e.args else str(e))
    raise Exception("LLM Failed to generate a realisticness score on the script")

def getQuestionFromThread(text):
    if ((text.find("Reddit, ") < 15) and (10 < text.find("?") < 100)):
        question = text.split("?")[0].replace("Reddit, ", "").strip().capitalize()
    else:
        chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/reddit_filter_realistic.yaml')
        chat = chat.replace("<<STORY>>", text)
        question = gpt_utils.llm_completion(chat_prompt=chat, system=system).replace("\n", "")
        question = question.replace('"', '').replace("?", "")
    return question


def generateUsername():
    chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/reddit_username.yaml')
    return gpt_utils.llm_completion(chat_prompt=chat, system=system, temp=1.2).replace("u/", "")


