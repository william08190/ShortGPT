"""
国际化翻译模块
支持中英文切换
"""

class I18n:
    """国际化翻译类"""

    # 当前语言，默认英文
    current_lang = "en"

    # 翻译字典
    translations = {
        # 通用
        "language": {
            "en": "Language",
            "zh": "语言"
        },
        "switch_to_chinese": {
            "en": "中文",
            "zh": "中文"
        },
        "switch_to_english": {
            "en": "English",
            "zh": "English"
        },

        # 主界面标题
        "content_automation": {
            "en": "Content Automation",
            "zh": "内容自动化"
        },
        "asset_library": {
            "en": "Asset Library",
            "zh": "素材库"
        },
        "config": {
            "en": "Configuration",
            "zh": "配置"
        },

        # 短视频自动化
        "short_automation": {
            "en": "Short Video Automation",
            "zh": "短视频自动化"
        },
        "video_automation": {
            "en": "Long Video Automation",
            "zh": "长视频自动化"
        },
        "video_translation": {
            "en": "Video Translation",
            "zh": "视频翻译"
        },

        # 短视频创建界面
        "number_of_shorts": {
            "en": "Number of shorts",
            "zh": "短视频数量"
        },
        "type_of_shorts": {
            "en": "Type of shorts generated",
            "zh": "短视频类型"
        },
        "reddit_story_shorts": {
            "en": "Reddit Story shorts",
            "zh": "Reddit故事短视频"
        },
        "historical_facts_shorts": {
            "en": "Historical Facts shorts",
            "zh": "历史事实短视频"
        },
        "scientific_facts_shorts": {
            "en": "Scientific Facts shorts",
            "zh": "科学事实短视频"
        },
        "custom_facts_shorts": {
            "en": "Custom Facts shorts",
            "zh": "自定义事实短视频"
        },
        "facts_subject": {
            "en": "Write a subject for your facts (example: Football facts)",
            "zh": "输入你的事实主题（例如：足球知识）"
        },

        # Reddit问题来源
        "reddit_question_source": {
            "en": "Reddit Question Source",
            "zh": "Reddit问题来源"
        },
        "ai_generated_question": {
            "en": "AI Generated Question",
            "zh": "AI生成问题"
        },
        "real_reddit_question": {
            "en": "Real Reddit Question",
            "zh": "真实Reddit问题"
        },
        "subreddit": {
            "en": "Subreddit",
            "zh": "子版块"
        },
        "time_filter": {
            "en": "Time Filter",
            "zh": "时间筛选"
        },
        "fetch_questions": {
            "en": "🔍 Fetch Questions",
            "zh": "🔍 获取问题"
        },
        "select_question": {
            "en": "Select a Question",
            "zh": "选择一个问题"
        },
        "click_fetch_hint": {
            "en": "Click 'Fetch Questions' to load real Reddit questions",
            "zh": "点击「获取问题」加载真实的Reddit问题"
        },
        "questions_found": {
            "en": "Found {} questions",
            "zh": "找到{}个问题"
        },
        "no_questions_found": {
            "en": "No questions found. Try different filters.",
            "zh": "未找到问题。请尝试不同的筛选条件。"
        },

        # TTS引擎
        "tts_engine": {
            "en": "Text to speech engine",
            "zh": "语音合成引擎"
        },
        "language_label": {
            "en": "Language",
            "zh": "语言"
        },

        # 图片和水印
        "use_images": {
            "en": "Use images",
            "zh": "使用图片"
        },
        "number_of_images": {
            "en": "Number of images per short",
            "zh": "每个短视频的图片数量"
        },
        "add_watermark": {
            "en": "Add watermark",
            "zh": "添加水印"
        },
        "watermark_text": {
            "en": "Watermark (your channel name)",
            "zh": "水印（你的频道名称）"
        },

        # 按钮
        "create_shorts": {
            "en": "Create Shorts",
            "zh": "创建短视频"
        },

        # 错误提示
        "error_no_subject": {
            "en": "Please write down your facts short's subject",
            "zh": "请填写你的事实短视频主题"
        },
        "error_no_background_video": {
            "en": "Please select at least one background video.",
            "zh": "请至少选择一个背景视频。"
        },
        "error_no_background_music": {
            "en": "Please select at least one background music.",
            "zh": "请至少选择一个背景音乐。"
        },
        "error_watermark_chars": {
            "en": "Watermark should only contain letters and numbers.",
            "zh": "水印只能包含字母和数字。"
        },
        "error_watermark_long": {
            "en": "Watermark should not exceed 25 characters.",
            "zh": "水印不能超过25个字符。"
        },
        "error_watermark_short": {
            "en": "Watermark should be at least 3 characters long.",
            "zh": "水印至少需要3个字符。"
        },
        "error_no_api_key": {
            "en": "GEMINI OR OPENAI API key is missing. Please go to the config tab and enter the API key.",
            "zh": "缺少GEMINI或OPENAI API密钥。请前往配置标签页输入API密钥。"
        },
        "error_no_elevenlabs_key": {
            "en": "ELEVENLABS_API_KEY API key is missing. Please go to the config tab and enter the API key.",
            "zh": "缺少ELEVENLABS_API_KEY。请前往配置标签页输入API密钥。"
        },

        # 进度提示
        "making_short": {
            "en": "Making short {}/{}",
            "zh": "正在制作短视频 {}/{}"
        },

        # 配置界面
        "api_keys": {
            "en": "API Keys Configuration",
            "zh": "API密钥配置"
        },
        "openai_api_key": {
            "en": "OpenAI API Key",
            "zh": "OpenAI API密钥"
        },
        "custom_base_url": {
            "en": "Custom Base URL (Optional)",
            "zh": "自定义Base URL（可选）"
        },
        "custom_model": {
            "en": "Custom Model (Optional)",
            "zh": "自定义模型（可选）"
        },
        "gemini_api_key": {
            "en": "Gemini API Key",
            "zh": "Gemini API密钥"
        },
        "elevenlabs_api_key": {
            "en": "ElevenLabs API Key",
            "zh": "ElevenLabs API密钥"
        },
        "pexels_api_key": {
            "en": "Pexels API Key",
            "zh": "Pexels API密钥"
        },
        "save": {
            "en": "Save",
            "zh": "保存"
        },

        # 素材库
        "background_videos": {
            "en": "Background Videos",
            "zh": "背景视频"
        },
        "background_musics": {
            "en": "Background Music",
            "zh": "背景音乐"
        },
        "add_asset": {
            "en": "Add Asset",
            "zh": "添加素材"
        },
        "asset_name": {
            "en": "Asset Name",
            "zh": "素材名称"
        },
        "asset_type": {
            "en": "Asset Type",
            "zh": "素材类型"
        },
        "asset_link": {
            "en": "Asset Link/Path",
            "zh": "素材链接/路径"
        },
    }

    @classmethod
    def set_language(cls, lang):
        """设置当前语言"""
        if lang in ["en", "zh"]:
            cls.current_lang = lang

    @classmethod
    def get_language(cls):
        """获取当前语言"""
        return cls.current_lang

    @classmethod
    def t(cls, key, *args):
        """翻译函数"""
        translation = cls.translations.get(key, {})
        text = translation.get(cls.current_lang, key)

        # 如果有格式化参数，进行格式化
        if args:
            try:
                text = text.format(*args)
            except:
                pass

        return text

    @classmethod
    def get_all_keys(cls):
        """获取所有翻译键"""
        return list(cls.translations.keys())
