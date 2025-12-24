import time
from db_config import get_connection

def log_agent_action(agent_name, action_type, input_text, output_text, token_cost, accuracy=None, efficiency=None, response_time=None):
    conn = get_connection()
    cur = conn.cursor()
    query = """
        INSERT INTO agent_logs (agent_name, action_type, input_text, output_text, token_cost, accuracy, efficiency, response_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(query, (agent_name, action_type, input_text, output_text, token_cost, accuracy, efficiency, response_time))
    conn.commit()
    cur.close()
    conn.close()
