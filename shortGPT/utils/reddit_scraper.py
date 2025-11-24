"""
Reddit问题爬取工具
可以从Reddit获取真实的热门问题，用于创建视频
"""
import requests
import json
from typing import List, Dict

def fetch_hot_questions_from_subreddit(subreddit: str = "AskReddit", limit: int = 10) -> List[Dict]:
    """
    从指定的subreddit获取热门问题

    Args:
        subreddit: subreddit名称（默认AskReddit）
        limit: 获取问题数量（默认10）

    Returns:
        包含问题标题和URL的字典列表
    """
    try:
        # Reddit的JSON API不需要认证
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()
        questions = []

        for post in data['data']['children']:
            post_data = post['data']
            # 只获取问题类型的帖子（标题以?结尾）
            title = post_data.get('title', '')
            if '?' in title:
                questions.append({
                    'title': title,
                    'url': f"https://www.reddit.com{post_data.get('permalink', '')}",
                    'upvotes': post_data.get('ups', 0),
                    'num_comments': post_data.get('num_comments', 0)
                })

        return questions
    except Exception as e:
        print(f"获取Reddit问题失败: {e}")
        return []


def search_reddit_questions(query: str, limit: int = 10) -> List[Dict]:
    """
    搜索Reddit问题

    Args:
        query: 搜索关键词
        limit: 获取问题数量

    Returns:
        包含问题标题和URL的字典列表
    """
    try:
        url = f"https://www.reddit.com/search.json?q={query}&limit={limit}&type=link"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()
        questions = []

        for post in data['data']['children']:
            post_data = post['data']
            title = post_data.get('title', '')
            if '?' in title:
                questions.append({
                    'title': title,
                    'url': f"https://www.reddit.com{post_data.get('permalink', '')}",
                    'upvotes': post_data.get('ups', 0),
                    'num_comments': post_data.get('num_comments', 0)
                })

        return questions
    except Exception as e:
        print(f"搜索Reddit问题失败: {e}")
        return []


def get_top_questions(subreddit: str = "AskReddit", time_filter: str = "day", limit: int = 10) -> List[Dict]:
    """
    获取指定时间范围内的热门问题

    Args:
        subreddit: subreddit名称
        time_filter: 时间过滤器 (hour, day, week, month, year, all)
        limit: 获取问题数量

    Returns:
        包含问题标题和URL的字典列表
    """
    try:
        url = f"https://www.reddit.com/r/{subreddit}/top.json?t={time_filter}&limit={limit}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()
        questions = []

        for post in data['data']['children']:
            post_data = post['data']
            title = post_data.get('title', '')
            if '?' in title:
                questions.append({
                    'title': title,
                    'url': f"https://www.reddit.com{post_data.get('permalink', '')}",
                    'upvotes': post_data.get('ups', 0),
                    'num_comments': post_data.get('num_comments', 0)
                })

        return questions
    except Exception as e:
        print(f"获取热门问题失败: {e}")
        return []


def print_questions(questions: List[Dict]):
    """
    打印问题列表
    """
    if not questions:
        print("没有找到问题")
        return

    print(f"\n找到 {len(questions)} 个问题：\n")
    for i, q in enumerate(questions, 1):
        print(f"{i}. {q['title']}")
        print(f"   赞数: {q['upvotes']} | 评论数: {q['num_comments']}")
        print(f"   链接: {q['url']}\n")


if __name__ == "__main__":
    # 测试功能
    print("=== 获取AskReddit今日热门问题 ===")
    questions = get_top_questions(subreddit="AskReddit", time_filter="day", limit=5)
    print_questions(questions)

    print("\n=== 搜索特定关键词 ===")
    search_results = search_reddit_questions("what's the", limit=5)
    print_questions(search_results)
