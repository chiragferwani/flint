from langflow.load import run_flow_from_json
TWEAKS = {
  "ChatInput-Pui4j": {},
  "ChatOutput-em2PS": {},
  "Agent-3VhPU": {},
  "Prompt-Q0RlE": {},
  "AstraDB-dyT7b": {},
  "ParseData-UWpK4": {},
  "File-FIFga": {},
  "SplitText-hXcST": {},
  "AstraDB-eRT9d": {}
}

result = run_flow_from_json(flow="Flint.json",
                            input_value="message",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)