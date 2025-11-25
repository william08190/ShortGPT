from shortGPT.gpt import gpt_utils
import json
def generateScript(script_description, language):
    out = {'script': ''}
    chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/chat_video_script.yaml')
    chat = chat.replace("<<DESCRIPTION>>", script_description).replace("<<LANGUAGE>>", language)
    while not ('script' in out and out['script']):
        try:
            result = gpt_utils.llm_completion(chat_prompt=chat, system=system, temp=1)
            # Remove markdown code blocks if present
            cleaned_result = result.strip()
            if cleaned_result.startswith('```'):
                # Remove opening ```json or ```
                lines = cleaned_result.split('\n')
                lines = lines[1:]  # Skip first line with ```
                # Remove closing ```
                if lines and lines[-1].strip() == '```':
                    lines = lines[:-1]
                cleaned_result = '\n'.join(lines).strip()

            out = json.loads(cleaned_result)
        except Exception as e:
            print(e, "Difficulty parsing the output in gpt_chat_video.generateScript")
    return out['script']

def correctScript(script, correction):
    out = {'script': ''}
    chat, system = gpt_utils.load_local_yaml_prompt('prompt_templates/chat_video_edit_script.yaml')
    chat = chat.replace("<<ORIGINAL_SCRIPT>>", script).replace("<<CORRECTIONS>>", correction)

    while not ('script' in out and out['script']):
        try:
            result = gpt_utils.llm_completion(chat_prompt=chat, system=system, temp=1)
            # Remove markdown code blocks if present
            cleaned_result = result.strip()
            if cleaned_result.startswith('```'):
                # Remove opening ```json or ```
                lines = cleaned_result.split('\n')
                lines = lines[1:]  # Skip first line with ```
                # Remove closing ```
                if lines and lines[-1].strip() == '```':
                    lines = lines[:-1]
                cleaned_result = '\n'.join(lines).strip()

            out = json.loads(cleaned_result)
        except Exception as e:
            print(e, "Difficulty parsing the output in gpt_chat_video.correctScript")
    return out['script']