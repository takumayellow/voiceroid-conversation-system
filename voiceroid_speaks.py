"""
voiceroid_speaks.py - Generate responses and speak them using VOICEROID.

This script receives a question on the command line, queries the
MEBO API (https://api-mebo.dev/) to obtain a conversational response,
and then uses SeikaSay2.exe (part of the AssistantSeika suite) to
speak that response aloud via the VOICEROID engine. It is intended
to be called from `main.py` after a user's speech has been
transcribed.

Configuration:
    Before running this script you must obtain an API key, agent ID and
    UID from the MEBO service and set them below. You must also
    install AssistantSeika and set the correct path to SeikaSay2.exe.

    API_KEY:    Your MEBO API key
    AGENT_ID:   The agent ID of your conversational agent
    UID:        A unique identifier for the user (any string)
    SEIKASAY_EXE: Full path to the SeikaSay2.exe executable

Example:

    python voiceroid_speaks.py \u4eca\u65e5\u306f\u5929\u6c17\u304c\u3044\u3044\u306d

Dependencies:
    - requests

See README.md for full setup instructions.
"""

from __future__ import annotations

import sys
import subprocess
from typing import Any, Dict

import requests

# TODO: Replace the following placeholders with your actual credentials.
API_KEY = "<YOUR-APIKEY-HERE>"
AGENT_ID = "<YOUR-AGENTID-HERE>"
UID = "<YOUR-UID-HERE>"

# The path to SeikaSay2.exe. Update this to match your installation.
SEIKASAY_EXE = r"C:\\path\\to\\SeikaSay2.exe"


def send_request(msg_q: str) -> requests.Response:
    """Send a request to the MEBO API with the given utterance."""
    url = "https://api-mebo.dev/api"
    payload: Dict[str, Any] = {
        "api_key": API_KEY,
        "agent_id": AGENT_ID,
        "utterance": msg_q,
        "uid": UID,
    }
    return requests.post(url, headers={}, json=payload)


def get_answer_msg(msg_q: str) -> str:
    """Fetch the best response utterance for the given message."""
    response = send_request(msg_q)
   response_json = response.json()
   #
    try:
        return response_json["bestResponse"]["utterance"]
    except KeyError:
        # Fallback for different response structures
        if isinstance(response_json, dict):
            # Check if 'results' contains utterances
            if response_json.get("results"):
                first_result = response_json["results"][0]
                if isinstance(first_result, dict) and first_result.get("utterance"):
                    return first_result["utterance"]
            # Check if 'utterance' is directly available
            if response_json.get("utterance"):
                return response_json["utterance"]
        # If nothing matches, raise a descriptive error
        raise KeyError("Utterance not found in MEBO API response")


def main() -> None:
    """Entry point. Read CLI args, query MEBO and speak the answer."""
    if len(sys.argv) < 2:
        print("Usage: python voiceroid_speaks.py <question>")
        return

    request_msg = sys.argv[1]
    print("request_msg:", request_msg)

    if request_msg:
        # Obtain a response from the MEBO API
        response_msg = get_answer_msg(request_msg)
        print("response_msg:", response_msg)

        # Prepare the command to call SeikaSay2.exe
        # -cid 2004 selects the Akari voice
        seika_cmd = [SEIKASAY_EXE, "-cid", "2004", "-t", f"\u56de\u7b54\u306f\u3001{response_msg}"]
        subprocess.run(seika_cmd)
    else:
        # Speak a default message when the input is empty
        fallback_cmd = [SEIKASAY_EXE, "-cid", "2004", "-t", "\u8cea\u554f\u304c\u805e\u304d\u53d6\u308c\u306a\u304b\u3063\u305f\u307f\u305f\u3044\u3067\u3059"]
        subprocess.run(fallback_cmd)


if __name__ == "__main__":
    main()
