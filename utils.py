from datetime import datetime

def validate_date(date_str):
    try:
        valid_date = datetime.strptime(date_str, "%Y-%m-%d")
        return valid_date
    except ValueError:
        return False

def sort_tasks(task_list):
    priority_order = {"high": 1, "medium": 2, "low": 3}
    return sorted(task_list, key=lambda t: (priority_order[t["priority"]], t["deadline"]))